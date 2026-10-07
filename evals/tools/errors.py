#!/usr/bin/env python3
"""List every confident false claim the judges found, per arm, across all judging runs.

    python3 errors.py <topic-dir> [<topic-dir> ...]

Reads each run's <prefix>-key.json and <judge>.json that exist in the topic dirs
(blind/judge, blind4/judge4, blind-retest/judge-retest) and prints one line per claim,
then a count per run and arm. Classifying each claim by where it came from is done by hand
in RESULTS.md ("Error census").
"""
import json
import sys
from collections import Counter
from pathlib import Path

RUNS = (("blind", "judge"), ("blind4", "judge4"), ("blind-retest", "judge-retest"))


def main():
    counts = Counter()
    for d in map(Path, sys.argv[1:]):
        for prefix, judge in RUNS:
            key_file, judge_file = d / f"{prefix}-key.json", d / f"{judge}.json"
            if not (key_file.exists() and judge_file.exists()):
                continue
            key = json.loads(key_file.read_text())
            for item in json.loads(judge_file.read_text())["questions"]:
                q = str(item["q"])
                for number, verdict in item["answers"].items():
                    arm = key[q][number]
                    for claim in verdict.get("confident_false_claims", []):
                        counts[(judge, arm)] += 1
                        print(f"{judge}\t{d.name}\tQ{q}\t{arm}\t{claim}")
    print()
    for (judge, arm), n in sorted(counts.items()):
        print(f"{judge}\t{arm}\t{n}")


if __name__ == "__main__":
    main()
