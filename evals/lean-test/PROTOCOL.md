# Lean-skill test: protocol

Fixed before any run. Anything changed afterwards goes in "Deviations" at the end, with the reason.

## Question

The maintainer wants the skill driven by a few convictions rather than a growing list of rules, and asked that performance improve before any change is made. Does a rewrite of `SKILL.md` that states the convictions (`candidate/SKILL.md`) handle a spread of situations better than the current text, and what does each cost in tokens?

## Versions

| Arm | Text | Source |
|---|---|---|
| CUR1, CUR2 | current skill, runs 1 and 2 | `skills/expertise/SKILL.md` at commit `ffdd5dc` |
| LEAN1, LEAN2 | lean candidate, runs 1 and 2 | `evals/lean-test/candidate/SKILL.md` |

Sizes: current 1,142 words in the body (109 lines); candidate 964 words (63 lines). The briefing format, the storage rules and the video section are the same in both; the judgement and loop sections went from 829 to 684 words. The candidate keeps the same mechanisms (prior, probe, patch, a fresh-agent check, the briefing file) and states the judgements as convictions.

## Scenarios and rubric

Eight situations in `questions.md`. Four re-create the failures the current rules were written for: a walled critical source (Q1), a refresh (Q2), an injected instruction (Q3), a topic Claude already knows well (Q4). Four are new to both texts: a paywalled primary source (Q5), a topic flooded with SEO pages (Q6), official sources in another language (Q7), and a user whose claim the sources contradict (Q8). `rubric.md` holds the per-scenario checklists and the pairwise criteria.

## Subjects

- Two runs per version per scenario: 32 runs. A fresh general-purpose agent for each, on the session's default model.
- Each agent may use the Read tool on exactly two files, its skill text and its scenario, and nothing else: no web, no shell, no other files. The skill text is given as `skill-1.md` (current) or `skill-2.md` (candidate), so the file name does not say which is new. A run whose tool-use count is not 2, or whose transcript shows other tools, is discarded and rerun.
- The prompt, identical for every run:

  > You are testing a skill. Read these two files and use no other tool: (1) `{skill}`, the skill instructions loaded for you in this session; (2) `{scenario}`, the situation. Follow the skill as you would in a real session. You cannot run research here, so wherever the skill would have you act, write down exactly what you would do, including the verbatim text of any brief you would send to a research agent. Treat the scenario's Event as what comes back at that point. Answer in these sections, in at most 900 words before the last one: A. Prior notes. B. Research plan and briefs (how many agents, and each brief verbatim). C. What you do after the Event. D. The briefing as you would write it: its Confidence line, its Unknown section, and the one or two most important claims with their sources. E. How you check it before saving, and what you tell the user. Last, a section "Effort" with these lines as numbers: research_agents_first_wave=, further_agents=, check_agents=, claims_checked=, searches_or_fetches_planned_in_total=.

- Two pilot runs first (Q1 on each version), to measure real cost. If the full test would cost more than about 1.2M tokens, it is cut to one run per cell (16 runs, 8 pairs) and the cut is recorded under Deviations before the rest are launched.

## Judging

- **Blinding.** `evals/tools/blind.py` shuffles the answers for each scenario and strips the labels; the key is kept out of the judges' reach.
- **Checklist.** Four judges, one per two scenarios, each reading the four shuffled answers for each of their scenarios against that scenario's checklist. Judges run on a different model from the subjects.
- **Pairwise.** For each run index, CUR_i against LEAN_i for all eight scenarios, in random order, forced choice with a one-line reason. Two independent judges per run index. A pair counts for a version only if both judges prefer it; if they disagree, or either says tie, it counts as a tie.
- Judges see the scenario, the rubric and the answers. They never see the skill texts, the arm names or this protocol.

## Gate

The lean text replaces the current one only if both hold:

1. **Better.** Over the 16 pairs, ties counting half, the lean version is preferred in at least 12 (a one-sided sign test at about 4%).
2. **Nothing lost.** Its total checklist score is at least the current version's, and no checklist item that the current version satisfies in both its runs is satisfied in neither of the lean version's runs.

If either fails, the current text stays, and the write-up says what the lean version lacked. A revised candidate is tested only on new scenario variants, never on these eight.

## Token consumption (reported beside the quality result, not part of the gate)

- **Static.** Tokens of each skill file as `claude plugin details` reports them, for a scratch plugin built from each text, plus word counts.
- **Measured.** Total tokens, tool uses and duration of every subject run, per version and per scenario. This is the cost of planning, not of research.
- **Modelled.** From each answer's Effort lines, the cost of a real build under each version, priced with the unit costs of this repository's own logged agents (`evals/build/cost.tsv`: mean tokens of a research agent and of a check agent). If the lean version's modelled cost is more than 25% higher, the write-up says so and leaves the call to the maintainer.
- The cost of a real run is measured only by a paired live refresh, which is outside this protocol.

## Also reported, not gated

Scenario-level counts (a version "wins" a scenario when it is preferred in both of its pairs, "loses" when the other is), because the two runs within a scenario are not independent. Judge agreement on the pairwise choices.

## Limits

- It measures what an agent says it would do with the skill, not what it does with tools. A plan can be sound and the execution poor.
- The judges share a model family with the subjects, although not the same model.
- The scenarios and the rubric were written by the same person who wrote the candidate, from the maintainer's stated aims. The checklists favour the behaviours the maintainer asked for.
- Eight scenarios and 32 runs can show a large difference or a vanished behaviour. They cannot show a small difference.
- Per-run variation: two runs per cell is a minimum.

## Deviations

None yet.
