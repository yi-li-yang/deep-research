#!/usr/bin/env python3
"""How much two blind judging runs agree on the answers both scored.

    python3 agree.py <prefix1>:<judge1> <prefix2>:<judge2> <topic-dir> [<topic-dir> ...]

Example: python3 agree.py blind:judge blind4:judge4 evals/claude-code-extensibility
"""
import json
import sys
from pathlib import Path
from statistics import mean


def scores(d, run):
    prefix, judge = run.split(":")
    key = json.loads((d / f"{prefix}-key.json").read_text())
    out = {}
    for item in json.loads((d / f"{judge}.json").read_text())["questions"]:
        q = str(item["q"])
        for number, verdict in item["answers"].items():
            out[(d.name, int(q), key[q][number])] = verdict["score"]
    return out


def sign(x):
    return (x > 0) - (x < 0)


def main():
    run1, run2, *dirs = sys.argv[1:]
    s1, s2 = {}, {}
    for d in map(Path, dirs):
        s1.update(scores(d, run1))
        s2.update(scores(d, run2))
    common = [k for k in s1 if k in s2]
    diffs = [s2[k] - s1[k] for k in common]
    print(f"Answers scored by both runs: {len(common)}; same score: {sum(d == 0 for d in diffs)}; "
          f"within 1 point: {sum(abs(d) <= 1 for d in diffs)}; mean shift (run 2 − run 1): {mean(diffs):+.2f}")
    questions = sorted({(t, q) for t, q, _ in common})
    if all((t, q, arm) in s1 and (t, q, arm) in s2 for t, q in questions for arm in ("A", "B")):
        d1 = [s1[(t, q, "B")] - s1[(t, q, "A")] for t, q in questions]
        d2 = [s2[(t, q, "B")] - s2[(t, q, "A")] for t, q in questions]
        same = sum(sign(a) == sign(b) for a, b in zip(d1, d2))
        print(f"B − A: run 1 mean {mean(d1):+.2f}, run 2 mean {mean(d2):+.2f}; "
              f"same direction (win, tie or loss) on {same} of {len(questions)} questions")


if __name__ == "__main__":
    main()
