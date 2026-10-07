# Field-use builds: status

**Paused at the user's request, 2026-10-07, about 15:55 UTC. Nothing is running.**

Purpose: build two briefings for the user's own use with the revised skill (build-time check, source-line rule), then write up what the check step caught. If this file is all you have, read "To resume".

## What exists

All seven research agents were stopped before they finished, but each had been saving notes. The notes are raw: unconsolidated, carrying each agent's own verification labels, with no final report, and none of them has been checked yet.

### Dota 2 position 3, 7000+ MMR, Europe → `briefings/dota2-position-3-7000-mmr-eu.md` (not yet written)

| Piece | State | Words |
|---|---|---|
| Prior (`evals/build/dota2-pos3/prior.md`) | done | 486 |
| 1 patch and changes (`research/1-patch.md`) | finished | 400 |
| 3 pro offlane play (`research/3-pro.md`) | finished | 444 |
| 2 EU pub meta (`research/2-pub-meta.md`) | stopped. Sections: patch window, OpenDota data limits, Immortal thresholds, sampling facts, leaderboard structure, pro comparison | 1,661 |
| 4 craft at 7k+ (`research/4-craft.md`) | stopped. Sections: patch timeline, map objects and timings, 7.41 lane changes, runes and neutrals, current item values, practitioner evidence from r/learndota2 | 8,319 |
| 5 Russian and Chinese communities (`research/5-russian-chinese.md`) | stopped. Sections: patch context, Russian findings, 7.41f hero changes, Chinese findings so far, verification of the unverified beliefs | 4,938 |

### Sichuanese-dialect podcasts → `briefings/sichuanese-dialect-podcasts.md` (not yet written)

| Piece | State | Words |
|---|---|---|
| Prior (`evals/build/sichuanese-podcasts/prior.md`) | done | 345 |
| 1 Chinese podcast apps (`research/1-apps.md`) | stopped. Sections: Apple catalogue, shows verified on primary pages and feeds, 小宇宙 pages | 2,895 |
| 2 video, radio, storytelling (`research/2-video-radio.md`) | stopped. Sections: 李伯清 and 散打评书, dialect TV, Bilibili, YouTube, streaming listings | 1,043 |
| 3 learning the dialect (`research/3-learning.md`) | stopped. Sections: phonology and tones (sources conflict), grammar and vocabulary, younger speakers, romanization, learner material | 2,670 |
| 4 listening from abroad (`research/4-abroad.md`) | stopped. Sections: Apple Podcasts, verified shows, Chinese apps from abroad, RSS | 1,443 |

The agents' briefs are in `evals/build/<topic>/briefs.md`.

## To resume

1. **Say "continue".** Then, for each topic, I write the briefing from these notes (the Patch step). A gap-filling agent is needed only where a claim in the notes can't be sourced. To resume an agent, re-run its section of `briefs.md` and tell it to read its notes file first and continue from there.
2. **Check step.** Two fresh agents per topic open every cited source and report each claim as stated, wrong, superseded or not in the source, with the line quoted. I fix, re-cite or drop what fails, and log the counts.
3. **Deliver** both briefings to the user, then write `evals/RESULTS.md` §12 ("Field use"), update `README.md`, `conceptualisation.md`, `evals/build/cost.tsv` and the PR body.

Cost: tokens for the stopped agents were not reported. `evals/build/cost.tsv` has only the two finished Dota agents (about 0.47M).
