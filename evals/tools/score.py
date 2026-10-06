#!/usr/bin/env python3
"""Turn blind judgments into results: per-arm means, B-A difference with a bootstrap CI, sign test.

    python3 score.py [--prefix blind4 --judge judge4] <topic-dir> [<topic-dir> ...]

Each topic dir needs <judge>.json (scores by blind answer number) and <prefix>-key.json (number -> arm);
the defaults are judge.json and blind-key.json (the pre-registered 3-arm run).
Prints markdown tables to stdout.
"""
import json
import random
import argparse
import sys
from math import comb
from pathlib import Path
from statistics import mean

ARMS = ("A0", "A", "B")
ORDER = ("A0", "A", "B", "B0")


def load(d, prefix="blind", judge_name="judge"):
    key = json.loads((d / f"{prefix}-key.json").read_text())
    judge = json.loads((d / f"{judge_name}.json").read_text())
    rows = []
    for item in judge["questions"]:
        q = str(item["q"])
        row = {"topic": d.name, "q": int(q), "type": item.get("type", "")}
        for number, verdict in item["answers"].items():
            arm = key[q][number]
            row[arm] = verdict["score"]
            row[arm + "_errors"] = len(verdict.get("confident_false_claims", []))
        rows.append(row)
    return rows


def sign_test(wins, losses):
    n = wins + losses
    if n == 0:
        return 1.0
    k = min(wins, losses)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)


def bootstrap_ci(diffs, rounds=10000, seed=1):
    rng = random.Random(seed)
    means = sorted(mean(rng.choices(diffs, k=len(diffs))) for _ in range(rounds))
    return means[int(0.025 * rounds)], means[int(0.975 * rounds) - 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", default="blind")
    parser.add_argument("--judge", default="judge")
    parser.add_argument("dirs", nargs="+")
    args = parser.parse_args()
    global ARMS
    rows = [r for d in args.dirs for r in load(Path(d), args.prefix, args.judge)]
    ARMS = tuple(a for a in ORDER if a in rows[0])
    topics = [Path(d).name for d in args.dirs]
    names = {"A0": "A0 (no tools)", "A": "A (web search)", "B": "B (/expertise + web)", "B0": "B0 (briefing only)"}
    print("| Topic | " + " | ".join(names[a] for a in ARMS) + " | B − A |")
    print("|---" * (len(ARMS) + 2) + "|")
    for t in topics + ["All"]:
        rs = [r for r in rows if t == "All" or r["topic"] == t]
        m = {arm: mean(r[arm] for r in rs) for arm in ARMS}
        print(f"| {t} | " + " | ".join(f"{m[a]:.1f}" for a in ARMS) + f" | {m['B'] - m['A']:+.1f} |")
    diffs = [r["B"] - r["A"] for r in rows]
    lo, hi = bootstrap_ci(diffs)
    wins = sum(d > 0 for d in diffs)
    losses = sum(d < 0 for d in diffs)
    ties = sum(d == 0 for d in diffs)
    print(f"\nB − A per question: mean {mean(diffs):+.2f}, 95% bootstrap CI [{lo:+.2f}, {hi:+.2f}]")
    print(f"B vs A: {wins} wins, {ties} ties, {losses} losses; two-sided sign test p = {sign_test(wins, losses):.4f}")
    d0 = [r["B"] - r["A0"] for r in rows]
    print(f"B − A0 per question: mean {mean(d0):+.2f}")
    if "B0" in ARMS:
        for other in ("A0", "A"):
            dd = [r["B0"] - r[other] for r in rows]
            lo2, hi2 = bootstrap_ci(dd)
            w2, l2 = sum(x > 0 for x in dd), sum(x < 0 for x in dd)
            print(f"B0 − {other} per question: mean {mean(dd):+.2f}, 95% CI [{lo2:+.2f}, {hi2:+.2f}]; {w2} wins, {len(dd)-w2-l2} ties, {l2} losses; sign test p = {sign_test(w2, l2):.4f}")
    print("\n| Arm | Confident false claims (total) | Answers with at least one |")
    print("|---|---|---|")
    for arm in ARMS:
        errs = [r[arm + "_errors"] for r in rows]
        print(f"| {arm} | {sum(errs)} | {sum(e > 0 for e in errs)} / {len(errs)} |")
    print("\n| Topic | Q | Type | " + " | ".join(ARMS) + " |")
    print("|---" * (len(ARMS) + 3) + "|")
    for r in rows:
        print(f"| {r['topic']} | {r['q']} | {r['type']} | " + " | ".join(str(r[a]) for a in ARMS) + " |")


if __name__ == "__main__":
    main()
