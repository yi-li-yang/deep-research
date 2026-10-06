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

## Known limitations

- **Small sample.** 24 questions show direction and rough size, not a precise effect.
- **Same model family.** The judge and the answerers share a model family. Blinding, checking claims against sources, and an independent answer key limit judge bias but cannot remove it.
- **Topic 1's orchestrator wasn't blind to the subject.** It had read Claude Code documentation earlier in the same session while designing the skill. Its prior came from a fresh agent with no tools, and its research came from fresh agents, but its choice of research angles may have benefited from that reading. Topics 2 and 3 had no such exposure.
- **B was built with the parallel research team (the Claude Code path).** claude.ai runs the same loop one thread at a time, and was not evaluated here.
