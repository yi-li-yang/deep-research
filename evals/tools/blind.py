#!/usr/bin/env python3
"""Shuffle the three arms' answers per question so the judge can't tell which arm wrote which.

    python3 blind.py <topic-dir> [--seed N]

Reads <topic-dir>/questions.md and answers-A0.md, answers-A.md, answers-B.md (each split by '## Q<n>'),
writes <topic-dir>/blind.md for the judge and <topic-dir>/blind-key.json (the judge never sees it).
"""
import argparse
import json
import random
import re
from pathlib import Path

ARMS = ("A0", "A", "B")


def split(text):
    parts = re.split(r"^## Q(\d+)\s*$", text, flags=re.M)
    return {int(n): body.strip() for n, body in zip(parts[1::2], parts[2::2])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_dir")
    parser.add_argument("--seed", type=int, default=20261006)
    args = parser.parse_args()
    d = Path(args.topic_dir)
    rng = random.Random(f"{args.seed}-{d.name}")
    questions = split((d / "questions.md").read_text())
    answers = {arm: split((d / f"answers-{arm}.md").read_text()) for arm in ARMS}
    out, key = [], {}
    for q in sorted(questions):
        missing = [arm for arm in ARMS if q not in answers[arm]]
        if missing:
            raise SystemExit(f"Q{q} has no answer from {missing}")
        order = list(ARMS)
        rng.shuffle(order)
        key[q] = {str(i + 1): arm for i, arm in enumerate(order)}
        out.append(f"## Q{q}\n\n**Question:** {questions[q]}\n")
        for i, arm in enumerate(order):
            out.append(f"### Answer {i + 1}\n\n{answers[arm][q]}\n")
    (d / "blind.md").write_text("\n".join(out))
    (d / "blind-key.json").write_text(json.dumps(key, indent=1))
    print(f"wrote {d / 'blind.md'} ({len(questions)} questions)")


if __name__ == "__main__":
    main()
