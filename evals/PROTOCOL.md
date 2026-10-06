# A/B evaluation protocol

**Question:** do answers from Claude *with* `/expertise` beat Claude's normal behaviour, and by how much? Does the skill introduce problems of its own?

The design was fixed before any results existed.

## Topics

Each topic is chosen to cover one kind of gap the skill targets:

| Topic | Kind of gap |
|---|---|
| `claude-code-extensibility`: Claude Code skills, plugins, hooks, subagents, MCP | a fast-moving tool |
| `league-of-legends`: the current patch and meta | a sudden change (a balance patch every two weeks) |
| `kanna`: Japanese hand planes (makers, steels, setup) | a niche with a Japanese-speaking community |

## Questions

A separate agent per topic wrote 8 realistic user questions, 24 in total. Each set contains:
- 3 about current facts
- 2 about recent changes
- 2 practical-judgment questions
- 1 trap: a confident question about something plausible that doesn't exist

The writer also produced an answer key with sources, for the judge only. The orchestrator, who built the briefings, did not open the questions or the key until every briefing was final, so no briefing could be tailored to the test.

Contamination control: this repository is public, and arm A searches the web. The questions, answer keys, briefings and answers were therefore kept out of the public repository until every arm had finished answering, so no arm could find them online.

## Arms

Each arm is one fresh agent, running the same model. It answers a topic's 8 questions in order, as one conversation.

| Arm | Setup |
|---|---|
| **A0** | Claude alone: no tools, no briefing |
| **A** | Claude with web search and fetch, no briefing. This is the realistic baseline. |
| **B** | Claude after `/expertise`: the topic's briefing in context, plus the same web search and fetch |

All arms are told:
- answer as an expert would
- cite sources where they have them
- don't describe their process, tools, briefing, or knowledge cutoff, so answers are harder to tell apart

B reads only the finished briefing. A real `/expertise` conversation also has the research agents' reports in context, so B is closest to a later conversation that loads a saved briefing.

## Blinding and judging

- `tools/blind.py` shuffles the three answers to each question with a fixed seed and labels them Answer 1, 2 and 3. The mapping is kept in `blind-key.json`, which the judge never sees.
- **One judge agent per topic** reads `blind.md`. It verifies checkable claims against primary sources on the web and the answer key. For each answer it records:
  - a score from 1 to 10
  - confident false claims
  - unsupported claims
- **Briefing claims are audited by separate agents.** Each auditor checks every claim in a briefing as *correct*, *wrong* or *unverifiable*. This is a deliberate split: a judge that had read the briefing could recognise answers that echo it, which would break the blinding.

### Scoring anchors

| Score | Meaning |
|---|---|
| 9–10 | Correct and current on every key point, specific and insightful (what an expert would add), well calibrated, no false claims |
| 7–8 | Correct and current on the key points; minor gaps or imprecision |
| 5–6 | Partly correct: misses important current facts, or mixes current and outdated information |
| 3–4 | Significant errors, or outdated information presented as current |
| 1–2 | Mostly wrong, or confidently fabricated |

Trap questions are scored differently:

| Response to the trap | Score |
|---|---|
| States the premise is false or unknowable, with evidence | 8–10 |
| Hedges without committing | 4–6 |
| Answers as if the premise were real | 1–2 |

## Metrics

`tools/score.py` reports:
- mean score per arm, per topic and overall
- B − A per question, with a 95% bootstrap confidence interval (10,000 resamples)
- B vs A wins, ties and losses, with a two-sided exact sign test
- confident false claims per arm
- trap handling per arm

Reported separately:
- briefing claim accuracy, from the auditors
- tokens and time per arm, with the cost of building each briefing spread over its questions
- a diagnosis of every question where B lost to A

## Significant problems, defined in advance

1. **A wrong claim in a briefing.** It would mislead every later conversation that loads the briefing.
2. **B losing to A.** A sign that Claude over-trusts the briefing, or stops using its tools.
3. **B with more confident errors than A, or B inventing an answer to a trap.**
4. **Build cost not justified** by the quality gain.
5. **The skill run skipping its own steps,** such as no written prior or no research agents.

## Added after the pre-registered run

These were designed after the pre-registered results were known. They help explain the main result but don't replace it.

| Arm | Setup | Why |
|---|---|---|
| **B0** | The briefing in context, no tools at all | Separates what the briefing carries from what live search adds. It is also what happens whenever Claude has the briefing but doesn't search. |
| **B1** | Same as B, but with the answer-time guidance written into SKILL.md after B's losses were diagnosed | The one fix-and-retest round the plan allowed |

- **Second blind judging, four arms.** A fresh judge per topic scored A0, A, B and B0 together (`blind4.md`, `blind4-key.json`, `judge4.json`). Because it re-scores A0, A and B, it also measures how far two independent judges agree (`tools/agree.py`).
- **Retest judging.** A third fresh judge per topic scored A, B and B1 together (`blind-retest.md`, `blind-retest-key.json`, `judge-retest.json`).
- B0 and B1 read each briefing exactly as B saw it, archived at `build/<topic>/briefing-as-evaluated.md`. The copies in `examples/` were corrected later from the audits.

B was told: "Read it first and use it throughout", and "You may use WebSearch and WebFetch as you normally would, for example where the briefing marks something as unknown or likely to have changed." That wording may itself have steered B toward the briefing and away from search. B1 was told instead, as SKILL.md now says:

> Use the briefing as a prior, not a boundary:
> - Re-check live anything time-sensitive that an answer hinges on, such as current stock, prices, live statistics, or a specific version, number or status.
> - Never read the briefing's silence as evidence that something doesn't exist.
> - Where the briefing and a primary source disagree, trust the primary source.

## Running notes

- **Search budget.** This environment caps WebSearch at 200 calls per turn, shared by every agent launched in that turn. Each arm that used the web was therefore launched in its own turn. Each recorded whether any search was refused for budget reasons; none was.
- **Timing.** A0, A and B answered on 2026-10-06 between about 17:30 and 18:20 UTC, B0 by 18:40, and B1 between about 18:55 and 19:30. League of Legends patch 26.20's notes were published at about 18:00 UTC, inside that window, so League judges were told to accept the clearly labelled preview values or the final notes.

## Known limitations

- **Small sample.** 24 questions show direction and rough size, not a precise effect.
- **Same model family.** The judge and the answerers share a model family. Blinding, checking claims against sources, and an independent answer key limit judge bias but cannot remove it.
- **Topic 1's orchestrator wasn't blind to the subject.** It had read Claude Code documentation earlier in the same session while designing the skill. Its prior came from a fresh agent with no tools, and its research came from fresh agents, but its choice of research angles may have benefited from that reading. Topics 2 and 3 had no such exposure.
- **B was built with the parallel research team (the Claude Code path).** claude.ai runs the same loop one thread at a time, and was not evaluated here.
- **The baseline searched diligently.** Arm A was told the date, asked to answer as of today, and given web tools. It made 11–58 searches and 35–76 fetches per topic. Whether Claude searches that thoroughly in everyday use was not measured; A0 is the other extreme.
- **The retest ran later and was not pre-registered.** B1 answered about an hour after A and B, and its guidance was written after seeing B's losses. Treat it as evidence about the fix, not as a fresh test of the skill.
- **Contamination, retest only.** Topic 1's questions, key and pre-registered answers were already on the public branch when B1 ran with web access. B1 was told not to open other files, and a branch pushed an hour earlier is unlikely to be in any search index, but it was possible in principle.
