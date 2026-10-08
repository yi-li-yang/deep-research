# Pilot: Q1 on each version

Run before the rest, exactly as the protocol describes. The two answers are the subjects' verbatim output. They have **not been judged**; they count as run 1 of Q1 if the full test goes ahead.

| Run | Skill text | Tokens (harness) | Duration | Tool uses (two Reads, plus the hand-back) | Effort lines: first wave, further, checkers, claims, fetches |
|---|---|---|---|---|---|
| CUR1-Q1 | current | 99,017 | 1,156 s | 2 | 2, 2, 2, 12, 37 |
| LEAN1-Q1 | lean candidate | 136,310 | 1,390 s | 2 | 2, 3, 2, 13, 38 |

**Static cost** (`claude plugin details`, same description in both): always-on about 186 tokens in both; on invoke about 2.3k (current) against 1.9k (lean).

**Modelled cost of a real build** from each answer's Effort lines, priced with this repository's logged agents (mean research agent 252,292 tokens over 18 agents; mean check agent 322,772 over 4): CUR1-Q1 about 1.65M, LEAN1-Q1 about 1.91M (+15%).

**What this shows.** Almost all of a subject's tokens are its own deliberation (about 100,000 or more per answer), not the skill text, so the cost of the test is far above the 25,000 to 30,000 per run assumed when the 0.6M estimate was made. One pair cannot say which version deliberates more.

**Projected cost of the rest.** At the pilot mean of about 118,000 per run, 30 more runs would cost about 3.5M and the 14 more of the one-run-per-cell cut about 1.65M, plus judging.
