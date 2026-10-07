# Field-use builds: status

**Resumed 2026-10-07 after a pause. Both briefings are written, checked and fixed. Next: deliver them and write up.**

Purpose: build two briefings for the user's own use with the revised skill (build-time check, source-line rule), then write up what the check step caught. If this file is all you have, read "To resume".

## What exists

Both briefings are written from the saved research notes and are in `briefings/`. The check step (two fresh agents per topic) follows `SKILL.md`: each agent opens every cited source and reports each claim as stated, wrong, superseded, differently scoped or not in the source.

| Topic | Briefing | Check brief | Reports |
|---|---|---|---|
| Dota 2 position 3, 7000+ MMR, Europe | `briefings/dota2-position-3-7000-mmr-eu.md` (checked and fixed; about 3,000 words) | `evals/build/dota2-pos3/check/brief.md` | `check/report-1.md`, `report-2.md` |
| Sichuanese-dialect podcasts | `briefings/sichuanese-dialect-podcasts.md` (checked and fixed; about 2,200 words) | `evals/build/sichuanese-podcasts/check/brief.md` | `check/report-1.md`, `report-2.md` |

Research notes for both topics are in `evals/build/<topic>/research/`; the priors are `prior.md` in each topic folder.

## To resume

1. If a check report is incomplete, re-run that agent from its brief and tell it to read its report file first and continue after the last row.
2. When both reports for a topic are complete: fix, re-cite or drop what failed in the briefing, add the counts to its Log, and set the Log's "check pending" line to done.
3. Send both briefings to the user. Then write `evals/RESULTS.md` §12 ("Field use"), and update `README.md`, `conceptualisation.md`, `evals/build/cost.tsv` and the PR body.

Cost: tokens for stopped agents were not reported. `evals/build/cost.tsv` has only the two finished Dota agents (about 0.47M).
