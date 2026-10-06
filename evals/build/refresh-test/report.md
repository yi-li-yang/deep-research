I refreshed the briefing in place at `/tmp/claude-0/-home-user-deep-research/151ef1ca-aca1-555f-a2ff-694634cbbf04/scratchpad/refresh-test/briefings/claude-code-extensibility.md`; it is now marked verified 2026-10-06.

**(1) What changed**
- **Repaired:** the saved file was damaged. It said verified 2026-08-01 but held claims up to 2026-10-02. It had bullet groups missing their lead-ins (synced skills, mods, platform support), an empty memory section, and only one side of the auto-mode safety debate. A Log entry now records all this.
- **Corrected:**
  - Auto mode as the default on every plan: docs say 2.1.283, changelog says 2.1.284. Added the starting mode for `-p` and SDK runs.
  - The community marketplace is named `claude-community`.
  - Headless trust: `-p` ignores the repo's allow rules but still runs its hooks and `.mcp.json` servers.
  - The 200-agent spawn cap was removed in 2.1.224.
  - The 1.5s SessionEnd hook timeout can be raised.
- **Added (Aug–Oct):**
  - Mods, which run plugin code inside Claude Code (2.1.287), and AGENTS.md support (2.1.277).
  - claude.ai skills and plugins syncing to the terminal, plus safer plugin installs.
  - `/skill-doctor`, model-switch hooks, and subagent output marked so it can't pose as instructions.
  - Tool Search switching off behind proxies, the MCP Skills extension going Final, and the cross-vendor Agent Plugins 1.0 format.
  - Two incidents (GitSpawn, Plugin4Shell) and the missing auto-mode dissent (Rehberger 60–80%, arXiv 79%), plus new Unknowns.
- **Confirmed unchanged:** model release dates, the MCP 2026-07-28 spec, subagent nesting and forks, the Stop-hook cap, Skills API general availability.

**(2) Where SKILL.md was unclear**
- It says nothing about a saved briefing whose content post-dates its `verified` date, or is damaged. I treated those later claims as unverified and rebuilt the structure.
- Refresh scope is unclear: re-verify everything, or only what changed? I spot-checked older claims.
- It doesn't say where to write down the prior; I put it in the conversation.
- "Recently enough" has no threshold.
- It says nothing about very large sources. WebFetch's summary misdated a changelog entry, so I grepped the raw `.md` with curl.
- It's unclear whether spawning remote sessions counts as subagents. I used the solo fallback.
- There is no size limit; the briefing grew from 25KB to 41KB.

**(3) Usage**
- 11 web searches, none refused.
- 53 fetches: 11 WebFetch and 42 curl reads of docs and changelog `.md` pages.
- One oversized result was auto-saved outside the allowed folders. I didn't open it; I re-ran a narrower query instead.
