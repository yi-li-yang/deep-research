# Field-use builds: status

Purpose: build two briefings for the user's own use with the revised skill (build-time check, source-line rule), then write up what the check step caught. Plan: see the PR description and `evals/RESULTS.md` §11. If the session was interrupted, read this file and continue from "Next".

Updated: 2026-10-07 (both research waves launched).

## Dota 2 position 3, 7000+ MMR, Europe → `briefings/dota2-position-3-7000-mmr-eu.md`

| Step | State |
|---|---|
| Prior (`evals/build/dota2-pos3/prior.md`) | done |
| Research 1, patch and changes | done: `research/1-patch.md` |
| Research 3, pro offlane play | done: `research/3-pro.md` |
| Research 2, high-MMR EU pub meta | running; notes in `research/2-pub-meta.md` |
| Research 4, offlane craft | running; notes in `research/4-craft.md` |
| Research 5, Russian and Chinese communities | running; notes in `research/5-russian-chinese.md` |
| Briefing (patch step) | not started |
| Check (2 fresh agents) | not started |

The agents' briefs are in `evals/build/dota2-pos3/briefs.md`. A stopped agent can be re-run from its section. An interrupted run loses at most the last few tool calls, because agents append to their notes files as they go.

## Sichuanese-dialect podcasts → `briefings/sichuanese-dialect-podcasts.md`

| Step | State |
|---|---|
| Prior (`evals/build/sichuanese-podcasts/prior.md`) | done |
| Research 1–4 | running (an earlier launch was stopped with no report); briefs in `evals/build/sichuanese-podcasts/briefs.md`; notes in `research/1-apps.md`, `2-video-radio.md`, `3-learning.md`, `4-abroad.md` |
| Briefing | not started |
| Check (2 fresh agents) | not started |

## Next

1. Wait for both waves; commit each agent's notes as it finishes. (The podcast wave was launched in a separate turn from the Dota wave, because each turn shares a cap of 200 web searches across its agents.)
2. Write the Dota briefing, then check it. Same for the podcasts.
3. Send both briefings to the user, then write `evals/RESULTS.md` §12 ("Field use"), update `README.md`, `conceptualisation.md`, `evals/build/cost.tsv` and the PR body.

Cost so far, in `evals/build/cost.tsv`: two finished Dota research agents (about 0.47M tokens). An earlier launch of seven more agents was stopped without reports.
