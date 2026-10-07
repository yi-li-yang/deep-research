# A/B results

**Does `/expertise` make Claude's answers better, by how much, and does it cause problems of its own?** Run on 2026-10-06, following [PROTOCOL.md](PROTOCOL.md). Every number below comes from the files in this folder and can be recomputed with `tools/score.py` and `tools/agree.py`.

## Bottom line

- **Large gain over Claude answering from memory.** Mean score went from 4.5 to 8.7 out of 10, and B scored higher on 23 of 24 questions. Confident false claims fell from 23 to 11.
- **No gain over a Claude that searched the web for every question.** B scored 8.7 against A's 9.0. The difference, −0.29, is within noise (95% CI −0.71 to +0.08; p = 0.39). Two more independent blind judgings found the same: −0.25 and −0.12.
- **The briefing alone, with no search at all, closes about two-thirds of the gap** between answering from memory and searching the web: 7.5, against 4.3 and 9.2 under the second judge. This was exploratory.
- **B made more confident errors than A in all three judgings:** 11, 7 and 8, against 5, 6 and 4. Three of B's eight losses came from trusting the briefing too far, so the skill now tells Claude to use the briefing as a prior, not a boundary. In an exploratory retest, that guidance made Claude search as much as A, but neither its score (8.9 against A's 9.0) nor its confident errors (9 against 4) improved. **Confident errors are the main open problem.**
- **The briefings are mostly right, not always.** Of 416 audited claims, 87% were correct, 3.4% wrong and 5.3% cited to the wrong source. All three examples have been corrected.
- **Building a briefing is expensive.** It took 1.1–1.7M tokens of agent work, 4.6–6.0 times what arm A spent answering all eight questions. B answered with fewer web calls than A (159 against 284) and in about a quarter less time. With the revised guidance (B1), answering cost about the same as A: 276 web calls, 7% more tokens and 7% less time.

## Setup

Three topics were chosen for the gaps the skill targets:
- **Claude Code extensibility:** a fast-moving tool.
- **League of Legends, current patch:** a sudden change.
- **Japanese hand planes (kanna):** a niche whose experts write in Japanese.

For each topic, an independent agent wrote 8 questions (current facts, recent changes, judgment, one trap) and an answer key. The questions were hidden from whoever built the briefing.

| Arm | Setup |
|---|---|
| A0 | No tools, no briefing |
| A | Web search and fetch, no briefing |
| B | The `/expertise` briefing, plus the same web tools |
| B0 | The briefing only, no tools. Exploratory |
| B1 | B with the revised guidance. Exploratory retest |

Each arm is a fresh agent answering one topic's 8 questions as one conversation. Judges saw the answers shuffled and unlabelled, checked claims against primary sources, and scored 1–10.

## 1. The pre-registered result

| Topic | A0 (no tools) | A (web search) | B (/expertise + web) | B − A |
|---|---|---|---|---|
| Claude Code | 5.1 | 9.5 | 9.5 | +0.0 |
| League of Legends | 2.9 | 8.4 | 8.4 | +0.0 |
| Kanna | 5.4 | 9.1 | 8.2 | −0.9 |
| **All 24 questions** | **4.5** | **9.0** | **8.7** | **−0.3** |

| Comparison | Mean per question | 95% CI | Wins / ties / losses | Sign test |
|---|---|---|---|---|
| B − A | −0.29 | −0.71 to +0.08 | 4 / 12 / 8 | p = 0.39 |
| B − A0 | +4.25 | +3.38 to +5.04 | 23 / 0 / 1 | p < 0.0001 |

| Arm | Confident false claims | Answers with at least one | Trap questions (mean of 3) |
|---|---|---|---|
| A0 | 23 | 15 / 24 | 6.0 |
| A | 5 | 3 / 24 | 9.7 |
| B | 11 | 7 / 24 | 9.7 |

By question type, B matched A on traps (9.7 each) and trailed slightly on current facts (9.0 against 9.2), recent changes (8.5 against 9.0) and judgment (8.0 against 8.3). Neither B nor A invented an answer to a trap; A0 fell for the League trap (2/10).

## 2. A second judge

A fresh blind judge per topic re-scored every answer, with B0 added as a fourth arm (`judge4.json`).

- Both judges scored the same 72 answers. 49 scores were identical and 71 were within one point; on average the second judge scored 0.11 higher.
- **B − A replicated:** −0.25 (95% CI −0.62 to +0.12; 5 wins, 10 ties, 9 losses; p = 0.42), against −0.29 the first time. The judges agreed on the direction (win, tie or loss) for 15 of 24 questions. Most of B's per-question differences from A are one point, which is about the judges' own noise.
- **The confident-error gap narrowed but kept its direction:** A0 21, A 6, B 7, B0 9.
- **A third judging, during the retest (§5), scored A and B again.** B − A came out at −0.12. Its scores matched the first judge's on 30 of 48 answers, and all 48 were within one point.

## 3. What the briefing alone carries (B0, exploratory)

| Topic | A0 | B0 (briefing only) | B | A |
|---|---|---|---|---|
| Claude Code | 4.8 | 8.0 | 9.8 | 9.5 |
| League of Legends | 3.0 | 6.6 | 8.6 | 8.8 |
| Kanna | 5.2 | 7.8 | 8.5 | 9.4 |
| **All** | **4.3** | **7.5** | **9.0** | **9.2** |

- B0 − A0 = +3.12 (95% CI +2.29 to +3.96). B0 beat A0 on 22 questions and tied 2.
- B0 − A = −1.75 (95% CI −2.38 to −1.17). A beat B0 on 19 questions.
- By type, B0 was strongest on recent changes (8.0) and traps (8.0), and weakest on current facts (6.8). A briefing records what changed; it can't hold every live number a question might ask for.

The briefing is real knowledge, not decoration: it lifts a Claude that doesn't search by about three points. Live search adds the rest.

## 4. Where B lost, and why

All of B's losses to A under the pre-registered judge:

| Question | A → B | What went wrong in B | Cause |
|---|---|---|---|
| Claude Code 1 | 9 → 8 | Said a subagent's `tools: Agent(...)` list limits what it may spawn; the docs say that list is ignored in subagents | B's own error; B0, with the same briefing, didn't make it |
| League 7 | 9 → 8 | Two details wrong: who Eclipse's melee/ranged split applies to; how often Lee Sin builds Sundered Sky | B's own errors |
| League 8 | 9 → 8 | "Riot hasn't published a rule" on main-role protection. Riot Support guarantees autofilled players their primary or secondary role for the next handful of games. | **Briefing silent; B read the silence as absence** |
| Kanna 1 | 9 → 7 | Said all of Hida's Funahiro planes were sold out, and that the Komori make small planes only | **Briefing's stock claim was over-scoped, and B trusted it without re-checking** |
| Kanna 2 | 9 → 8 | Dated Kawai's steel imports to Taishō instead of late Meiji, and misattributed a source | B's own errors |
| Kanna 5 | 9 → 8 | Couldn't name the fourth Miki plane smith | **Briefing gap that B didn't search to fill** |
| Kanna 6 | 9 → 6 | Recommended grinding the bevel back to fix *ura-gire*, which makes it worse | B's own reasoning error; B0 scored 9 here |
| Kanna 8 | 10 → 9 | Missed one explanation for contest results of about 20 µm | Depth |

B's four wins (Claude Code 7, League 3, League 5, Kanna 3) were by one point each, mostly from extra verified detail.

**Diagnosis.**
- Three losses came from **trusting the briefing too far**: reading its silence as absence, repeating a perishable fact without re-checking, and not filling a gap it exposed.
- The other five were ordinary answer errors of the kind A also made elsewhere. For example, A misread a stats table on League 3.
- **B also searched less.** It made 159 web calls against A's 284, with 44 searches against 98, and its instructions ("use it throughout… search, for example, where the briefing marks something as unknown") invited that.

**Fix.** SKILL.md now tells Claude to use the briefing as a prior, not a boundary:
- re-check anything time-sensitive that an answer hinges on
- never read the briefing's silence as absence
- trust a primary source over the briefing

The Patch step now records perishable facts (stock, prices, live statistics) as where to check them, with the value as of its date.

## 5. Retest with the fix (B1, exploratory)

B1 answered the same questions with the same briefings, under the revised guidance. A third blind judge per topic scored A, B and B1 together (`judge-retest.json`).

| Topic | A (web search) | B (briefing + web) | B1 (revised guidance) |
|---|---|---|---|
| Claude Code | 9.2 | 9.9 | 9.4 |
| League of Legends | 8.9 | 8.8 | 8.9 |
| Kanna | 8.8 | 7.9 | 8.4 |
| **All** | **9.0** | **8.8** | **8.9** |

| Comparison | Mean per question | 95% CI | Wins / ties / losses | Sign test |
|---|---|---|---|---|
| B1 − A | −0.08 | −0.54 to +0.42 | 6 / 9 / 9 | p = 0.61 |
| B1 − B | +0.04 | −0.42 to +0.62 | 6 / 9 / 9 | p = 0.61 |
| B − A (third judging) | −0.12 | −0.58 to +0.29 | 8 / 9 / 7 | p = 1.0 |

- **The fix changed behaviour.** B1 made 276 web calls (Claude Code 50, League 72, kanna 154), against B's 159 and A's 284. It searched as much as A.
- **It helped where it was aimed:**
  - League 8: B1 no longer claimed Riot publishes no role guarantee.
  - Kanna 1: it re-checked Hida's stock.
  - Kanna 6: B's grinding mistake didn't recur (9 against 6). B0 hadn't made it either, so it was a one-off.
  - League 3: B1 read the stats tables that A and B both misread (10 against 6).
- **New errors cancelled the gains.**
  - Re-checking live pages brought misreadings of its own. A category page with no sold-out badge led B1 to call a sold-out Hida plane available, and it misread a section of the final 26.20 notes.
  - It still repeated a narrowing taken from the briefing (the Komori make small planes only).
  - It still missed the fourth Miki smith.
- **Neither score nor errors improved.** B1 scored level with A and B, and made as many confident errors: A 4, B 8, B1 9 under this judge.

**Confident errors are the open problem.** The same B and A answers were judged three times, and each time B's held more confident false claims (11, 7 and 8) than A's (5, 6 and 4). B1's new answers repeated the pattern.
- Between a third and a half of these errors trace to the briefing: claims repeated from it or stretched beyond it.
- The rest are misreadings and reasoning slips of a kind A made less often.
- Why is unclear. Length doesn't explain it: B's answers were about as long as A's. They ran 3,507 words against 4,049 for Claude Code, 3,085 against 3,089 for League, and 2,941 against 2,761 for kanna.

Judges can disagree with sources that disagree with each other. The third kanna judge marked "the Komori brothers" false, because the guild page calls Masaki おじ（弟）, an uncle. The Gifu databook calls Hideki and Masaki 兄弟, brothers. That cost B and B1 but not A. Scores are reported as judged.

## 6. Are the briefings right?

Separate auditors checked every claim in each briefing against its cited source and other primary sources ([Claude Code](claude-code-extensibility/briefing-audit.md), [League](league-of-legends/briefing-audit.md), [kanna](kanna/briefing-audit.md)).

| Briefing | Claims | Correct | Wrong | Mis-cited (true, wrong source) | Unverifiable |
|---|---|---|---|---|---|
| Claude Code | 155 | 146 | 5 | 1 | 3 |
| League of Legends | 132 | 110 | 2 | 15 | 5 |
| Kanna | 129 | 107 | 7 | 6 | 9 |
| **All** | **416** | **363 (87%)** | **14 (3.4%)** | **22 (5.3%)** | **17 (4.1%)** |

What went wrong, and what changed:
- **Claude Code.** All five wrong claims came from compression that dropped a qualifier, the kind of edit that turns "on most events" into "always". SKILL.md now says: compress the wording, not the meaning.
- **League.** 15 claims were true but cited to the nearest source in their paragraph. SKILL.md now says: cite each claim to the source that actually states it.
- **Kanna.**
  - Some claims came from stale or undated pages: a smith's age from a page written about 2020, a dealer's wait time, and EU postal rules that changed on 1 Oct 2026.
  - Others were misreadings, and one inference went beyond its source.
  - The research habits already ask for dates checked in the primary text. The new perishable-facts rule covers the stock claim.

The corrected briefings are in [`examples/`](../examples/); each records its corrections in its Log. The versions the arms saw are archived in `build/<topic>/briefing-as-evaluated.md`.

## 7. Process checks

- **Refresh.** A fresh agent refreshed the Claude Code briefing after it was backdated to 2026-08-01, using the one-thread path that claude.ai uses.
  - It recovered 11 of 13 genuine changes since August and repaired a damaged file.
  - It grew the briefing from 25 KB to 41 KB, so SKILL.md now says to prune as you add.
- **Cold read.** A fresh agent read SKILL.md with no context and listed everything it would have to improvise:
  - where to write the prior
  - research habits missing from the agents' briefs
  - no length cap on agent reports
  - where to save briefings
  - a README promise that the next conversation "starts current"

  All were fixed before the A/B run ([cold-review.md](build/skill-review/cold-review.md)).
- **Skipped steps.** None seen.
  - The three builds were run by this session's orchestrator, following SKILL.md. Each wrote a prior first (from a fresh agent with no tools), ran 5–6 parallel research agents, and wrote the briefing.
  - The refresh agent, reading SKILL.md cold, also wrote its prior, probed, and logged its changes.

## 8. Cost

Tokens are each agent's total as reported by the harness; times are wall-clock. The orchestrator's own tokens for writing each briefing are not counted.

| | Claude Code | League | Kanna |
|---|---|---|---|
| Prior (fresh agent, no tools) | 108k | 102k | 116k |
| Research agents | 6 agents, 1,624k | 5 agents, 959k | 5 agents, 1,486k |
| **Build total** | **1,732k** | **1,061k** | **1,602k** |
| Research wave, wall-clock | 12 min | 19 min | 22 min |
| A0: 8 answers | 113k, 10 min | 111k, 11 min | 132k, 14 min |
| A: 8 answers | 337k, 17 min | 229k, 26 min | 266k, 31 min |
| B: 8 answers | 335k, 15 min | 179k, 17 min | 226k, 23 min |
| B0: 8 answers | 133k, 10 min | 120k, 10 min | 147k, 14 min |
| B1: 8 answers | 406k, 16 min | 176k, 16 min | 310k, 37 min |

- A build costs 4.6–6.0 times what A spent answering all eight questions.
- B's answers cost 11% fewer tokens than A's in total, and took 25% less time. Those savings came from searching less, which the revised guidance undoes.
- B1's answers, under the revised guidance, cost 7% more tokens than A's and took 7% less time. With the skill as shipped, the build is not paid back in tokens by later conversations. What it buys is the briefing itself and its value when Claude doesn't search (§3).

## 9. The pre-registered problems

| Problem (defined in advance) | Found? | Severity | What changed |
|---|---|---|---|
| A wrong claim in a briefing | Yes: 14 of 416 claims (3.4%), plus 22 mis-cited | Medium. None of the 14 surfaced in a judged answer, but an over-scoped stock claim did (kanna 1), and a saved briefing carries its errors into every later conversation. | Two writing rules and a perishable-facts rule in SKILL.md; examples corrected |
| B losing to A | 8 losses against 4 wins, mean −0.29, not significant; −0.25 and −0.12 under two more judges | Medium. B is no better than per-question search. | "A prior, not a boundary" guidance. In the retest, B1 searched more but scored the same (§5). |
| B with more confident errors than A, or inventing a trap answer | Yes, in all three judgings (11/5, 7/6, 8/4), and again in the retest (B1 9, A 4). No invented trap answers. | Medium, and **open** | The fix didn't reduce it. The cause is partly the briefing and partly unexplained. |
| Build cost not justified by the quality gain | Yes, against a Claude that searches every question; no, against Claude from memory | High for one-off questions | The README says when to use it and when not to |
| The skill skipping its own steps | Not seen | None | None |

## 10. What this means

**Facts:**
- With a briefing, Claude answered as well as a Claude that searched the web for each question, and not better.
- With a briefing and no search, Claude closed two-thirds of the gap between memory and search.
- Building a briefing costs about five conversations' worth of tokens.
- Answers with a briefing held more confident errors than answers from search, in every judging. Telling Claude to treat the briefing as a prior made it search more, but didn't fix this.

**Inference.** The skill's measured value is not better answers than a diligent searcher. It is two things:
- getting current knowledge into Claude without per-question search
- leaving behind a sourced, dated file that a person can read and check, and that later conversations can reuse

**Judgment.** `/expertise` should not claim to beat web search. It earns its cost when:
- a topic will be revisited across conversations
- the research itself is worth reading
- Claude would otherwise answer from memory

For a few one-off questions, asking Claude to search is enough and much cheaper. Whoever uses a briefing should check the claims an answer hinges on against their cited sources.

**What to try next.** The confident-error gap is the problem worth solving next. Two candidates, neither tested:
- Have Claude verify, at answer time, any claim it takes from the briefing that the answer hinges on, just as it re-checks perishable facts.
- Have a separate auditor check a briefing claim by claim after it's built, as the audits here did. They found and fixed 14 wrong claims.

**The hinges, where being wrong would change the conclusion:**
1. **How often everyday Claude searches.** Arm A was told the date, asked to answer as of today, and searched 11–58 times per topic. If everyday Claude searches less, the real-world gain sits between B − A (none) and B − A0 (+4.2). This was not measured.
2. **Q&A versus real work.** The test asked eight independent questions. Longer work in one domain (designing, writing code against a new API) may use a briefing differently. Not measured.
3. **How briefings age.** The arms answered on the day each briefing was built. The refresh test suggests refreshing works, but how fast a briefing's value decays wasn't measured.

See [PROTOCOL.md](PROTOCOL.md#known-limitations) for the limits of this evaluation: a small sample, the same model family judging, and an orchestrator who wasn't blind to topic 1.

## 11. Error census: where the confident errors came from

After the retest, every confident false claim from all three judgings was listed (`python3 tools/errors.py claude-code-extensibility league-of-legends kanna`) and traced by hand to its source. The same B answers were judged three times, so duplicates were merged.

| Where the error came from | B (15 distinct) | B1 (9) | A (6) |
|---|---|---|---|
| Repeated from the briefing, where it was wrong, over-scoped or contested (Mizuno "about 70"; HSS "flat back"; "Nitori"; Hida "all sold out"; "the Komori brothers") | 5 | 1 | 0 |
| Stretched beyond the briefing ("small planes *only*"; ranks reset "only in January" when the briefing gave the exception; a permission rule applied to subagent tools) | 3 | 2 | 0 |
| The briefing's silence read as absence (no role guarantee) | 1 | 0 | 0 |
| Misreading a live page (a stats table, a category tile, a section of the notes) | 4 | 4 | 4–5 |
| Own reasoning or memory | 2 | 2 | 1–2 |

- **More than half of B's distinct errors (9 of 15) came through the briefing.** A made none of that kind; its errors were misreadings and memory slips, which B and B1 made at about the same rate.
- **The audits had already caught two of them** (Mizuno's age, the "flat back"). A check step at build time would have kept those out of the briefing.
- **Answers stretched briefing claims beyond what they said.** No build-time check prevents that; only answer-time discipline does.
- **The first fix shifted errors rather than removing them.** B1 re-checked more and leaned on the briefing less, but misread the extra pages it opened.
- **Density doesn't explain the gap.** Answers carried about as many specific tokens (numbers, dates, versions, prices): A 22.3 per answer, B 24.5, B1 23.7.
- **The briefing arms made 2–3 times more claims the judges could neither confirm nor refute:** B 30, 16 and 20 against A's 10, 5 and 8. The briefing brings obscure specifics into answers without their sources.

**The second fix**, now in SKILL.md, follows the two paths:
- **At build time, the briefing is checked claim by claim against its cited sources before it is saved.** This is what the independent audits did; they found 14 wrong and 22 mis-cited claims.
- **At answer time, Claude asserts a hinge fact only after reading the line that states it, and keeps that line's scope.**

The build-time check was exercised on two new briefings (§12). **The answer-time rule has not had a controlled retest.**
