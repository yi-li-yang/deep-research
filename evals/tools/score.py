#!/usr/bin/env python3
"""Turn blind judgments into results: per-arm means, B-A difference with a bootstrap CI, sign test.

    python3 score.py <topic-dir> [<topic-dir> ...]

Each topic dir needs judge.json (scores by blind answer number) and blind-key.json (number -> arm).
Prints markdown tables to stdout.
"""
import json
import random
import sys
from math import comb
from pathlib import Path
from statistics import mean

ARMS = ("A0", "A", "B")


def load(d):
    key = json.loads((d / "blind-key.json").read_text())
    judge = json.loads((d / "judge.json").read_text())
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
    rows = [r for d in sys.argv[1:] for r in load(Path(d))]
    topics = sorted({r["topic"] for r in rows}, key=lambda t: sys.argv[1:].index(next(a for a in sys.argv[1:] if Path(a).name == t)))
    print("| Topic | A0 (no tools) | A (web search) | B (/expertise) | B − A |")
    print("|---|---|---|---|---|")
    for t in topics + ["All"]:
        rs = [r for r in rows if t == "All" or r["topic"] == t]
        m = {arm: mean(r[arm] for r in rs) for arm in ARMS}
        print(f"| {t} | {m['A0']:.1f} | {m['A']:.1f} | {m['B']:.1f} | {m['B'] - m['A']:+.1f} |")
    diffs = [r["B"] - r["A"] for r in rows]
    lo, hi = bootstrap_ci(diffs)
    wins = sum(d > 0 for d in diffs)
    losses = sum(d < 0 for d in diffs)
    ties = sum(d == 0 for d in diffs)
    print(f"\nB − A per question: mean {mean(diffs):+.2f}, 95% bootstrap CI [{lo:+.2f}, {hi:+.2f}]")
    print(f"B vs A: {wins} wins, {ties} ties, {losses} losses; two-sided sign test p = {sign_test(wins, losses):.4f}")
    d0 = [r["B"] - r["A0"] for r in rows]
    print(f"B − A0 per question: mean {mean(d0):+.2f}")
    print("\n| Arm | Confident false claims (total) | Answers with at least one |")
    print("|---|---|---|")
    for arm in ARMS:
        errs = [r[arm + "_errors"] for r in rows]
        print(f"| {arm} | {sum(errs)} | {sum(e > 0 for e in errs)} / {len(errs)} |")
    print("\n| Topic | Q | Type | A0 | A | B |")
    print("|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['topic']} | {r['q']} | {r['type']} | {r['A0']} | {r['A']} | {r['B']} |")


if __name__ == "__main__":
    main()
