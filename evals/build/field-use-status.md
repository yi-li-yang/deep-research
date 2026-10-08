# Field-use builds: complete

Two briefings were built with the revised skill (build-time check, source-line rule), checked claim by claim and fixed on 2026-10-07. What the check found, and what it did not test, is written up in `evals/RESULTS.md` section 12.

| Topic | Briefing | Check brief | Check reports |
|---|---|---|---|
| Dota 2 position 3, 7000+ MMR, Europe | `briefings/dota2-position-3-7000-mmr-eu.md` | `evals/build/dota2-pos3/check/brief.md` | `check/report-1.md`, `report-2.md` |
| Sichuanese-dialect podcasts | `briefings/sichuanese-dialect-podcasts.md` | `evals/build/sichuanese-podcasts/check/brief.md` | `check/report-1.md`, `report-2.md` |

The priors are `prior.md` and the research notes are in `research/`, both in each topic's folder under `evals/build/`.

## Cost

`evals/build/cost.tsv` logs the agents that reported their tokens:

- Dota 2: 4 agents, 1.18M tokens. Two were research agents (0.47M) and two were check agents (0.71M).
- Sichuanese podcasts: 2 agents, 0.59M tokens, both check agents.
- Whole log: 57 agents, 15.3M tokens.

The other research notes (three for Dota 2, four for the podcasts) have no cost rows. Those agents were stopped by the pauses, or their tokens went unreported. So every figure above is a floor.
