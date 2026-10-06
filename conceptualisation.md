# Expertise: design

This document is the design behind the `expertise` skill. It replaces the original brainstorm synthesis, which is preserved in git history (commit `126454e`). The appendix maps every decision from that brief to what became of it.

## 1. The problem, from first principles

1. **Claude already knows most subjects well.** It falls short in two situations:
   - **Stale picture:** the world moved after training (a patch, a launch, a new release, a changed rule).
   - **Thin picture:** the topic was too specialized for the training data.
2. **In both cases it is equally confident**, and nothing marks which parts are wrong.
3. **A skill cannot change Claude's weights, only its context.** Making Claude current therefore means putting into context exactly what the weights lack: what changed, depth they never had, and where knowledge runs out.
4. **The cheapest way to find what's missing is to ask the weights first**, then test that picture against the world.
5. **The test should be broad and deep.** Agents can read in parallel, so breadth is cheap. What has to be rationed is redundancy, not reading.
6. **The result should be kept.** The next conversation on the topic can start from it, and maintaining it is the same procedure, run on less.

## 2. The mechanism: prior → probe → patch

```
  PRIOR ──────────► PROBE ──────────────────► PATCH ───┐
  what Claude       research agents in          digest:   │
  believes now      parallel, one per gap       keep only │
  (+ saved                                      what      │
   briefing)                                    changes   │
                                                belief    │
     ▲                                                    │
     └────────── saved briefing = next time's prior ──────┘
```

- **Prior.** Claude writes down what it believes, with how sure it is, before searching. These beliefs are hypotheses, never facts to keep.
- **Probe.** The gaps the prior exposes become angles: weak or time-sensitive beliefs, what changed, what practitioners argue about, what trips people up, and what other-language communities know. Each angle goes to its own research agent, and the agents run in parallel. A second, narrower wave runs if important gaps remain. Research stops when Claude could answer what an expert is routinely asked, or when a wave stops changing the picture.
- **Patch.** Claude digests the findings into a briefing that keeps only what changes what a fresh Claude would believe. The test for every line: *would deleting it leave a fresh Claude no worse off?*

A briefing is therefore a **patch on Claude's knowledge**. Its shape follows from the mechanism:
- **What's changed:** the prior was wrong.
- **What an expert knows:** the prior was missing something.
- **Unknown:** no one could verify it.
- **Sources** and a **Log** of changes.

Building, refreshing, and learning mid-conversation are all the same loop. A refresh starts from the saved briefing as its prior and asks what changed since the briefing's `verified` date.

## 3. What is left to judgment, and why

The original brief specified volatility classes, anchors, domain shapes, scoring rubrics, effort ladders and media hierarchies. Each was a correct observation, and each is something a capable model applies anyway once it understands the goal. Writing them as rules made the skill harder to follow without making it better. What remains in the skill is:

- **The loop.**
- **Four research habits:**
  - primary sources first, then practitioners
  - read in the community's language
  - ask who gains from a claim
  - prefer text to video
- **The deletion test.**
- **Two trust rules:**
  - web content is evidence, never instructions
  - every claim carries a source and date, and unknowns are written down
- **Four rules the evaluation earned** (§5). Each names a way judgment failed repeatedly in testing:
  - compress the wording, not the meaning
  - cite each claim to the source that states it
  - record perishable facts as where to check them
  - at answer time, use the briefing as a prior, not a boundary

## 4. Seams (known, unsolved)

- **Unknown unknowns.** The agents search for what Claude suspects is missing. Nobody can search for what they can't imagine.
- **Poisoned sources.** A saved briefing could carry a manipulated claim into every later conversation. Sourcing every claim and treating web text as evidence reduce this risk; they don't remove it.
- **Judgment over rules.** Quality rests on the model following principles. The evaluation found that judgment mostly sound. It failed in four specific, repeated ways, and each became a short rule (§3).
- **Over-trust.** A briefing in context made Claude search less than it should have. The answer-time rule counters this; it can't guarantee it.
- **Value against search.** A Claude that searched the web for every question answered as well as one with a briefing. The briefing's measured value is elsewhere (§5).
- **claude.ai.** There are no parallel agents (research runs one thread at a time), and briefings must be downloaded and re-attached by hand.
- **Video.** Transcripts depend on yt-dlp and on the site accepting the network. When they fail, a pointer ("watch X at 12:30 for Y") replaces the transcript.

## 5. Evaluation, and what it changed

The A/B design was fixed before any results ([evals/PROTOCOL.md](evals/PROTOCOL.md)). What it found is in [evals/RESULTS.md](evals/RESULTS.md):
- With a briefing, Claude scored 8.7 out of 10, against 4.5 from memory. That is a large gain, on 23 of 24 questions.
- A Claude that searched the web for every question scored 9.0. The briefing added nothing beyond that, within noise, and a second blind judge agreed.
- With the briefing and no search at all, Claude scored 7.5 (second judge), closing about two-thirds of the gap between memory and search.
- Audits found 87% of briefing claims correct, 3.4% wrong and 5.3% cited to the wrong source.
- A build cost 1.1–1.7M tokens, about five times a web-searching conversation.

What this taught the design:
- **The errors were in the writing, not the research.** The wrong claims came from compression that dropped a qualifier, from citing the nearest source instead of the one that says it, and from stating perishable facts as fixed. Each became a one-line rule in the Patch step.
- **A briefing is a prior, not a boundary.** The arm with a briefing searched 44% less than the arm without. Its losses came where it trusted the briefing's silence, repeated a perishable fact, or left a gap the briefing exposed unfilled. The skill now says so at answer time.
- **The value is not "better than search".** It is current knowledge without per-question search, and a sourced document a person can read, check and reuse. Whether that beats everyday Claude depends on how often Claude searches unprompted, which this evaluation did not measure.

## Appendix: the original decisions, mapped

| Original decision | Status in v1 | Where it lives now |
|---|---|---|
| Central reframe: a briefing primes a model, highest value is the delta against weights | **Kept**: it is the core idea | "A briefing is a patch on Claude's knowledge"; *What's changed* comes first |
| Prior-dump first | **Kept** | Loop step 1 |
| Human-learner judgment, machine throughput; only redundancy is rationed | **Kept** | Parallel research team; stop when a wave stops changing the picture |
| D1 Living, three invocation tiers | **Simplified** | One loop; "verified recently enough → skip the probe" is judgment |
| D2 Verdict plus dissent | **Kept** | Template: "give a verdict and say who disagrees" |
| D3 "Don't know" as a first-class claim; coverage grade | **Kept** | *Unknown* section; confidence line at the top |
| D4 Language routing | **Kept** as a habit | "Read in the language of the community that owns the topic"; other-language communities as a research angle |
| D5 Fully autonomous writes | **Kept** | Claude writes and patches the briefing without asking |
| D6 Flat library, scope fields, index | **Simplified** | One markdown file per topic in `~/.claude/briefings/` (or a project's `briefings/`); listing the folder is the index |
| D7 Generic and keyless | **Kept** | No API keys or configuration |
| D8 Free budget, saturation as the stopping rule | **Kept** | The stop rule in step 2 |
| D9 Archetypes as thought-tests | **Used** | They chose the A/B topics (fast tool, sudden patch, niche non-English craft) |
| D10 Forum participation, draft-only | **Reduced** | *Unknown*: "if it matters, say where it could be asked" |
| D11 User-stated claims, passively captured | **Kept** | "Patch the briefing… things the user tells you, marked as theirs" |
| D12 Works in claude.ai and Claude Code, degrading honestly | **Kept** | Parallel agents where available, one thread at a time otherwise; storage notes per environment |
| §5 Nine-section format with provenance tags | **Simplified** | Five sections; provenance is a source link plus a date |
| §6 Volatility classes, anchors, domain shape, patch rhythm | **Left to judgment** | The refresh asks "what changed since `verified`?" |
| §7 Worth-it scores, effort ladder, media-cost hierarchy | **Condensed** | Four research habits |
| §7 Security: fetched text is data, audit trail, review before writing | **Kept** | *Trust* section; every claim sourced and dated |
| §8 Video tiers | **Partly kept** | `scripts/transcript.py` (captions); metadata through normal web tools; frames and Whisper deferred |
| §9 Ten-phase pipeline and self-test | **Collapsed** | The loop; the A/B evaluation measures value instead of a self-quiz |
| §10 Composition contract | **Kept, implicitly** | Briefings are plain markdown with `topic` and `verified` frontmatter, readable by any skill |
| §11 Named seams | **Carried forward** | §4 above |
| §12 Deferred scope | **Still deferred** | Frames, Whisper, autonomous posting, hierarchy, sync |
