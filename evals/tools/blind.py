#!/usr/bin/env python3
"""Shuffle the three arms' answers per question so the judge can't tell which arm wrote which.

    python3 blind.py <topic-dir> [--seed N] [--arms A0,A,B] [--out blind]

Reads <topic-dir>/questions.md and answers-<arm>.md for each arm (each split by '## Q<n>'),
writes <topic-dir>/<out>.md for the judge and <topic-dir>/<out>-key.json (the judge never sees it).
"""
import argparse
import json
import random
import re
from pathlib import Path



def split(text):
    parts = re.split(r"^## Q(\d+)\s*$", text, flags=re.M)
    return {int(n): body.strip() for n, body in zip(parts[1::2], parts[2::2])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_dir")
    parser.add_argument("--seed", type=int, default=20261006)
    parser.add_argument("--arms", default="A0,A,B")
    parser.add_argument("--out", default="blind")
    args = parser.parse_args()
    arms = tuple(args.arms.split(","))
    d = Path(args.topic_dir)
    rng = random.Random(f"{args.seed}-{d.name}" + ("" if args.out == "blind" else f"-{args.out}"))
    questions = split((d / "questions.md").read_text())
    answers = {arm: split((d / f"answers-{arm}.md").read_text()) for arm in arms}
    out, key = [], {}
    for q in sorted(questions):
        missing = [arm for arm in arms if q not in answers[arm]]
        if missing:
            raise SystemExit(f"Q{q} has no answer from {missing}")
        order = list(arms)
        rng.shuffle(order)
        key[q] = {str(i + 1): arm for i, arm in enumerate(order)}
        out.append(f"## Q{q}\n\n**Question:** {questions[q]}\n")
        for i, arm in enumerate(order):
            out.append(f"### Answer {i + 1}\n\n{answers[arm][q]}\n")
    (d / f"{args.out}.md").write_text("\n".join(out))
    (d / f"{args.out}-key.json").write_text(json.dumps(key, indent=1))
    print(f"wrote {d / (args.out + '.md')} ({len(questions)} questions, arms {','.join(arms)})")


if __name__ == "__main__":
    main()
