# Audit: claude-code-extensibility briefing

Audited 2026-10-06 against `examples/claude-code-extensibility.md`.

**Claims checked: 155 · correct: 146 · wrong: 5 · unverifiable: 3 · mis-cited: 1**

Method: each claim was checked first against its cited source, mostly the raw `.md` of each code.claude.com docs page plus the full changelog through 2.1.291. Where the cited source didn't settle it, I used other primary sources: the MCP spec, Anthropic and claude.com blogs, the GitHub advisory, and the vendors' own posts. Rows marked "correct" may still note a caveat in the evidence column.

## Claim-by-claim results

| Claim (short) | Verdict | Evidence |
| :- | :- | :- |
| 1. Claude Code is at 2.1.291 | correct | [changelog](https://code.claude.com/docs/en/changelog): 2.1.291 dated Oct 6, 2026 |
| 2. Newest models: Opus 5.5 (09-22), Sonnet 5.5 (09-28), Fable 5.1 (09-01) | correct | [changelog](https://code.claude.com/docs/en/changelog): 2.1.280 (Sep 22) adds `claude-opus-5-5`; 2.1.284 (Sep 28) adds `claude-sonnet-5-5`; 2.1.257 (Sep 1) adds `claude-fable-5-1` |
| 3. Since 2.1.280, Pro and Team Standard default to Opus | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.280: "default model on Pro and Team Standard plans from Sonnet to Opus" |
| 4. Six permission modes; `default` shown as "Manual" | correct | [permission modes](https://code.claude.com/docs/en/permission-modes): table of 6 modes; Manual = `default` |
| 5. Auto: classifier; launched 2026-03-24; default on Pro/Max/Team 2026-08-14; built-in start mode for terminal + VS Code on every plan since 2.1.283 | correct | [permission modes](https://code.claude.com/docs/en/permission-modes) ("auto with Claude Code v2.1.283 or later"); [default blog](https://claude.com/blog/auto-mode-default-in-claude-code) (Aug 14); [launch blog](https://claude.com/blog/auto-mode) dated 2026-03-24. Caveat: the changelog puts the "every plan and provider" change in 2.1.284 (Sep 28); 2.1.283 covered only third-party providers and telemetry-off sessions |
| 6. Admins disable auto mode with `permissions.disableAutoMode` | correct | [permissions](https://code.claude.com/docs/en/permissions); [permission modes](https://code.claude.com/docs/en/permission-modes) |
| 7. `defaultMode: auto` or `bypassPermissions` is ignored in project and local settings | correct | [permission modes](https://code.claude.com/docs/en/permission-modes), "Which mode a session starts in" |
| 8. New rule forms: `Tool(param:value)` (deny and ask only), `Agent(Name)`, `Agent(model:opus)`, `Cd(path)` | correct | [permissions](https://code.claude.com/docs/en/permissions) |
| 9. Rules evaluated deny → ask → allow; specificity doesn't matter | correct | [permissions](https://code.claude.com/docs/en/permissions): "rule specificity doesn't change the order" |
| 10. Commands and skills merged in v2.1.3 (2026-01-09) | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.3 (Jan 9): "Merged slash commands and skills" |
| 11. Command files are the legacy form and accept all skill frontmatter except `name` and `paths` | correct | [skills](https://code.claude.com/docs/en/skills) |
| 12. Everything is invoked through the Skill tool; the SlashCommand tool is gone | correct | [tools reference](https://code.claude.com/docs/en/tools-reference) lists `Skill` and no SlashCommand |
| 13. Arguments: `$ARGUMENTS`, `$ARGUMENTS[N]`/`$N`, named `$name` from `arguments:` | correct | [skills](https://code.claude.com/docs/en/skills), substitutions table |
| 14. Inline and fenced `!` injection; a failed or denied command aborts the whole invocation | correct | [skills](https://code.claude.com/docs/en/skills): "A failed command aborts the entire skill invocation"; deny rule aborts. Caveat: in auto mode, a command that needs approval doesn't abort |
| 15. Full skill frontmatter list (20 keys) | correct | [skills](https://code.claude.com/docs/en/skills) frontmatter reference: exact match |
| 16. Unknown keys silently ignored; `name` and `description` optional | correct | [skills](https://code.claude.com/docs/en/skills): "All fields are optional"; unrecognized fields ignored without error |
| 17. `${CLAUDE_*}` substitutions also expand in `allowed-tools` Bash rules | correct | [skills](https://code.claude.com/docs/en/skills). Caveat: the docs name only SKILL_DIR, PROJECT_DIR and plugin ROOT/DATA for `allowed-tools`, not SESSION_ID or EFFORT |
| 18. Listing keeps every name and drops descriptions over budget (1% of context, `skillListingBudgetFraction`), least-used first | correct | [skills](https://code.claude.com/docs/en/skills) |
| 19. `description` + `when_to_use` capped at 1,536 characters | correct | [skills](https://code.claude.com/docs/en/skills) |
| 20. `disable-model-invocation: true` removes a skill from the listing | correct | [skills](https://code.claude.com/docs/en/skills): "removes the skill from Claude's context entirely" |
| 21. After compaction: first 5k tokens per skill, 25k total | correct | [skills](https://code.claude.com/docs/en/skills): 5,000 and 25,000 tokens |
| 22. `context: fork` skills run in the background by default since 2.1.218 (07-22); `background: false`; narrower tools; no checkpoints; no conversation history | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.218; [skills](https://code.claude.com/docs/en/skills) |
| 23. One-way claude.ai skill sync since mid-Sep (2.1.273–2.1.275) to `~/.claude/skills/synced/` for `/login` sessions | correct | [skills](https://code.claude.com/docs/en/skills) (download-only, requires v2.1.273); [changelog](https://code.claude.com/docs/en/changelog) 2.1.275 (Sep 17) |
| 24. Synced skills run as `/anthropic-skills:<name>` or by short name | correct | [skills](https://code.claude.com/docs/en/skills) |
| 25. Locally, synced bodies don't run `!`, don't expand `@` files or `${CLAUDE_*}` variables | **wrong** | [skills](https://code.claude.com/docs/en/skills): only `${CLAUDE_PROJECT_DIR}` and `${CLAUDE_SESSION_ID}` are left unsubstituted (see correction) |
| 26. API-key, Bedrock and bare sessions don't sync; `syncClaudeAiSkills: false` opts out | correct | [skills](https://code.claude.com/docs/en/skills) |
| 27. Personal skills don't load in cloud, Cowork or routines; cloud also loads the repo's `.claude/skills/` | correct | [skills](https://code.claude.com/docs/en/skills); [cloud environments](https://code.claude.com/docs/en/cloud-environments) |
| 28. claude.ai uploads, Skills API and `package_skill.py` accept only 6 keys; other keys are a hard error | correct | [skills](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code), with the exact error text |
| 29. Skills API out of beta 2026-08-19; `skills-2025-10-02` header not needed | correct | [platform release notes](https://platform.claude.com/docs/en/release-notes/overview), Aug 19, 2026 |
| 30. Customize → Skills; Enterprise scanning and "Requires review" become defaults 2026-10-02 | correct | [provisioning article](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization): both switch on Oct 2, 2026 if unset |
| 31. Task renamed Agent in v2.1.63 (02-28); `Task(...)` still works as an alias | correct | [sub-agents](https://code.claude.com/docs/en/sub-agents) note; 2.1.63 dated Feb 28 |
| 32. Agent inputs include `subagent_type`, `model`, `run_in_background`, `name`, `isolation: "worktree"` | correct | [sub-agents](https://code.claude.com/docs/en/sub-agents); [changelog](https://code.claude.com/docs/en/changelog) 2.1.72 restored `model` |
| 33. Nesting on by default to depth 3 since 2.1.219 (07-24); env var; `1` disables; teammates can't nest | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.219; [sub-agents](https://code.claude.com/docs/en/sub-agents); [agent teams](https://code.claude.com/docs/en/agent-teams) |
| 34. Forks inherit the conversation and prompt cache; `subagent_type: "fork"`; `/subtask` | correct | [sub-agents](https://code.claude.com/docs/en/sub-agents) |
| 35. Fork mode on in interactive sessions since 2.1.232 (08-13); off in `-p`/SDK unless `CLAUDE_CODE_FORK_SUBAGENT=1` | correct | [sub-agents](https://code.claude.com/docs/en/sub-agents); [changelog](https://code.claude.com/docs/en/changelog) 2.1.232 |
| 36. Background subagents became the default in 2.1.198 (07-01); their prompts surface in the main session | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.198; [sub-agents](https://code.claude.com/docs/en/sub-agents) |
| 37. At most 20 concurrent (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`); 200-per-session cap removed | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.217 (cap of 20) and 2.1.224 (cap removed) |
| 38. Background subagents get restricted tools; AskUserQuestion, plan tools, Workflow and ScheduleWakeup stripped from every subagent | correct | [sub-agents](https://code.claude.com/docs/en/sub-agents) "Available tools". Caveat: forks skip both filters |
| 39. Explore inherits the session model, capped at Opus | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.198; [sub-agents](https://code.claude.com/docs/en/sub-agents) |
| 40. "New" built-in agents: `claude`, `claude-code-guide`, `statusline-setup`, `fork` | unverifiable | All four exist per [sub-agents](https://code.claude.com/docs/en/sub-agents). "New" is doubtful: the [Piebald prompt tracker](https://github.com/Piebald-AI/claude-code-system-prompts) (secondary) shows statusline-setup by v2.0.14 and claude-code-guide by v2.0.60 (2025) |
| 41. `/agents` wizard removed in 2.1.198 | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.198 |
| 42. New agent frontmatter: `disallowedTools`, `maxTurns`, `mcpServers`, `memory`, `background`, `effort`, `isolation`, `omitClaudeMd`, `initialPrompt` | correct | [sub-agents](https://code.claude.com/docs/en/sub-agents) frontmatter table |
| 43. SDK: omitting `settingSources` loads user, project and local settings; `[]` isolates | correct | [SDK features](https://code.claude.com/docs/en/agent-sdk/claude-code-features) |
| 44. Workflows (2.1.154, 05-28): JS with `agent()`/`parallel()`/`pipeline()`/`phase()`; `ultracode` or `/effort ultracode`; `/deep-research` bundled | correct | [workflows](https://code.claude.com/docs/en/workflows); [changelog](https://code.claude.com/docs/en/changelog) 2.1.154 |
| 45. `/goal` (2.1.139) with an evaluator model | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.139; [goal](https://code.claude.com/docs/en/goal) |
| 46. `/loop` (2.1.71); Cron tools; session-scoped; 7-day expiry | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.71; [scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks) |
| 47. Routines: research preview, Apr 2026; schedule (min 1h), API or GitHub trigger | correct | [routines](https://code.claude.com/docs/en/routines); [launch blog](https://claude.com/blog/introducing-routines-in-claude-code) dated 2026-04-14 |
| 48. Agent view: `claude --bg`, `claude agents`, `claude attach` | correct | [agent view](https://code.claude.com/docs/en/agent-view) |
| 49. Cross-session `ListAgents` + `SendMessage` (2.1.224) | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.224 |
| 50. Agent teams still experimental and off by default; a named Agent call launches a teammate | correct | [agent teams](https://code.claude.com/docs/en/agent-teams). Caveat: forks, calls passing `isolation`, and `-p` sessions are exceptions |
| 51. Hook timeout 600s since v2.1.3 (command/http/mcp_tool); 30s UserPromptSubmit and model switch; prompt 30s; agent 60s; SessionEnd 1.5s | correct | [hooks](https://code.claude.com/docs/en/hooks); [changelog](https://code.claude.com/docs/en/changelog) 2.1.3. Omits 10s for MessageDisplay |
| 52. 33 hook events (list) | correct | [hooks](https://code.claude.com/docs/en/hooks): same 33 events |
| 53. Five handler types; `http` (2.1.63), `mcp_tool` (2.1.118); `agent` experimental | correct | [hooks](https://code.claude.com/docs/en/hooks); [changelog](https://code.claude.com/docs/en/changelog) |
| 54. Handler fields `args`, `shell`, `if`, `async`, `asyncRewake`, `once`; `once` only in skill frontmatter | correct | [hooks](https://code.claude.com/docs/en/hooks) |
| 55. PostToolUse `updatedToolOutput` works for any tool (2.1.121) | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.121 |
| 56. Matcher semantics; `Edit.*` also matches `NotebookEdit` | correct | [hooks](https://code.claude.com/docs/en/hooks) "Matcher patterns" |
| 57. Hyphenated names exact-match since 2.1.195 (06-26); use `mcp__brave-search__.*` | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.195 |
| 58. Hooks hot-reload; `/hooks` is a read-only browser | correct | [hooks](https://code.claude.com/docs/en/hooks); [debug config](https://code.claude.com/docs/en/debug-your-config) |
| 59. JSON output read on every exit code | correct | [hooks](https://code.claude.com/docs/en/hooks) "Exit code output" |
| 60. "Exit 2 always blocks; exit 1 never blocks" | **wrong** | [hooks](https://code.claude.com/docs/en/hooks) per-event exit-code table (see correction) |
| 61. A Stop hook can force continuation at most 8 times in a row (2.1.143) | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.143; [hooks](https://code.claude.com/docs/en/hooks) |
| 62. Mods (2.1.287, 10-01): JS/TS, `modules` in `hooks/hooks.json`, `register(on)` | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.287; [mods](https://code.claude.com/docs/en/plugins/mods/overview); [mods reference](https://code.claude.com/docs/en/plugins/mods/reference) |
| 63. Mods are unsandboxed; they can draw UI (panes, status line, toasts), rewrite prompts and tool calls, call models, approve calls | correct | [mods](https://code.claude.com/docs/en/plugins/mods/overview); [mods interface](https://code.claude.com/docs/en/plugins/mods/interface) |
| 64. `tool.check` overrides ask rules and non-managed hook blocks, and also deny rules where there are no managed settings and no Team/Enterprise sign-in | correct | [permissions](https://code.claude.com/docs/en/permissions) "Extend permissions with hooks" |
| 65. `allowManagedModsOnly` | correct | [mods](https://code.claude.com/docs/en/plugins/mods/overview) |
| 66. Settings hooks not deprecated | correct | [mods](https://code.claude.com/docs/en/plugins/mods/overview) compares them as a current option; no deprecation notice |
| 67. Plugins no longer labelled beta; manifest optional; name from the entry or directory | correct | [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference): "The manifest is optional" |
| 68. Component list (incl. `.mcpb`, LSP, experimental themes and monitors, channels, `bin/`, settings, workflows, userConfig, mods) | correct | [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) |
| 69. In-session `/plugin install` opens a details pane (contents, context cost, scope) | correct | [install](https://code.claude.com/docs/en/plugins/install). Context cost appears only for official-marketplace plugins |
| 70. `/plugin install <name> --marketplace <src>` (2.1.275, 09-17) | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.275; [install](https://code.claude.com/docs/en/plugins/install) |
| 71. Shell CLI subcommand lists | correct | [CLI reference](https://code.claude.com/docs/en/plugins/cli-reference): exact match |
| 72. Version precedence: manifest, then entry, then SHA; a set `version` pins users | correct | [loading](https://code.claude.com/docs/en/plugins/loading) |
| 73. Auto-update on for official marketplaces, off for third-party | correct | [loading](https://code.claude.com/docs/en/plugins/loading). Exceptions: `knowledge-work-plugins` and `first-party-plugins` off; claude.ai-added on |
| 74. Dependencies: semver ranges against `<name>--v<ver>` tags | correct | [dependencies](https://code.claude.com/docs/en/plugins/dependencies) |
| 75. `${CLAUDE_PLUGIN_DATA}` = `~/.claude/plugins/data/<id>/`, persists across updates | correct | [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) |
| 76. claude.ai plugins sync as `name@synced` from mid-Sep 2026 | correct | [loading](https://code.claude.com/docs/en/plugins/loading) (v2.1.273+); [changelog](https://code.claude.com/docs/en/changelog) 2.1.275 |
| 77. Chat loads skills, commands and remote MCP; Cowork adds agents, hooks and local MCP; both refuse `bin/` | correct | [platform support](https://claude.com/docs/plugins/platform-support) |
| 78. Cloud: no `/plugin`, no user-scope or repo-declared plugins; managed and synced plugins load | correct | [cloud environments](https://code.claude.com/docs/en/cloud-environments); [on the web](https://code.claude.com/docs/en/claude-code-on-the-web); [changelog](https://code.claude.com/docs/en/changelog) 2.1.239 and 2.1.261 |
| 79. `claude-plugins-official` added automatically on first interactive start | correct | [Anthropic marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces) |
| 80. Community marketplace is `claude-plugins-community`; nearly all entries SHA-pinned | **wrong** | [Anthropic marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces): the marketplace name is `claude-community`. [catalog](https://github.com/anthropics/claude-plugins-community/blob/main/.claude-plugin/marketplace.json): 2,274 of 2,284 entries SHA-pinned (that part holds) |
| 81. `anthropics/claude-code` is only a demo marketplace | correct | [Anthropic marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces) |
| 82. Directory submission portal opened 2026-09-25 with validation, a security scan and human review | correct | [portal blog](https://claude.com/blog/build-plugins-for-claude) dated 2026-09-25; [directory](https://claude.com/docs/directory/publish) for review steps (the date isn't in the cited docs) |
| 83. claude.com/marketplace launched 2026-09-23 with 2,000+ connectors and plugins | correct | [marketplace blog](https://claude.com/blog/claude-marketplace) dated 2026-09-23: "more than 2,000" |
| 84. `claude plugin eval` "GA" (2.1.269, 09-11); 3 runs per case; with and without plugin; real usage | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.269; [plugin evals](https://code.claude.com/docs/en/plugin-evals). The sources never say "GA"; there's no preview label, but the manifest `evals` key sits under `experimental` |
| 85. Current MCP revision is 2026-07-28 ("stateless"); Willison calls it "MCP 2.0" | correct | [versioning](https://modelcontextprotocol.io/specification/versioning); [Willison](https://simonwillison.net/2026/Jul/31/stateless-mcp/) |
| 86. No `initialize` or `ping`; `_meta` carries version and capabilities; `server/discover` | correct | [spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) |
| 87. `subscriptions/listen` replaces the GET stream and `resources/subscribe` | correct | [spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) |
| 88. MRTR (`input_required`) replaces server-initiated sampling, elicitation and roots | correct | [spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) |
| 89. Tasks moved to an extension | correct | [spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) |
| 90. Roots, Sampling and Logging deprecated; DCR deprecated in favour of CIMD | correct | [spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) |
| 91. Streamable HTTP has no sessions or `Mcp-Session-Id` | correct | [spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) |
| 92. v2 runtime negotiates 2026-07-28 with HTTP servers; default since about 2.1.232; `MCP_SDK_GENERATION=v1` opts out | correct | [MCP](https://code.claude.com/docs/en/mcp) "MCP client runtimes" (2.1.274 for no-flag sessions) |
| 93. Tool Search defers all MCP tools by default; only names and server instructions load | correct | [MCP](https://code.claude.com/docs/en/mcp) |
| 94. 10% threshold opt-in via `ENABLE_TOOL_SEARCH=auto` / `auto:N` | correct | [MCP](https://code.claude.com/docs/en/mcp) |
| 95. Exempt with `alwaysLoad` or `_meta["anthropic/alwaysLoad"]` | correct | [MCP](https://code.claude.com/docs/en/mcp) |
| 96. Descriptions and server instructions capped at 2,048 chars | correct | [MCP](https://code.claude.com/docs/en/mcp) |
| 97. claude.ai connectors in Claude Code (2.1.46), subscription login only | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.46; [MCP](https://code.claude.com/docs/en/mcp) |
| 98. MCP Apps (`ui://`) hidden in Claude Code | correct | [MCP](https://code.claude.com/docs/en/mcp): UI resources are skipped from lists |
| 99. Official extensions: Apps, Tasks, OAuth Client Credentials, Enterprise-Managed Authorization, Skills over MCP (SEP-2640, `skill://`) | correct | [extensions](https://modelcontextprotocol.io/extensions/overview); [skills extension](https://modelcontextprotocol.io/extensions/skills/overview) |
| 100. Claude Code documents no support for Skills over MCP | correct | No mention of `skill://` or SEP-2640 in the Claude Code docs checked ([MCP](https://code.claude.com/docs/en/mcp), [skills](https://code.claude.com/docs/en/skills), others) |
| 101. AGENTS.md read when there's no CLAUDE.md since 2.1.277 (09-18); "Project instructions" can load both | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.277; [memory](https://code.claude.com/docs/en/memory) |
| 102. Agent Plugins 1.0 (08-06): AWS, Cursor, Microsoft, OpenAI, Vercel; Google joining; no Anthropic; `plugin.json` at root | correct | [GitHub changelog](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/): Anysphere (Cursor) and the others; Google core maintainer the same day |
| 103. agentskills.io lists 46 clients and names no governing foundation | correct | [clients](https://agentskills.io/clients): 46 entries; [home](https://agentskills.io/home): "originally developed by Anthropic", open standard |
| 104. CLAUDE.md under ~200 lines, owned and reviewed like code; path-scoped rules | correct | [steering post](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) (2026-06-18) |
| 105. Procedures go in skills; only descriptions load per session | correct | [steering post](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more); [features overview](https://code.claude.com/docs/en/features-overview) |
| 106. Instructions are "a request, not a guarantee"; put guarantees in hooks | correct | [features overview](https://code.claude.com/docs/en/features-overview) |
| 107. Subagents for side tasks that flood the context | correct | [features overview](https://code.claude.com/docs/en/features-overview) |
| 108. Use MCP to keep credentials out of context or govern access (as Anthropic guidance) | unverifiable | Not in the [steering post](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) or [features overview](https://code.claude.com/docs/en/features-overview). [Willison](https://simonwillison.net/2026/Jul/31/stateless-mcp/) supports only "easier to audit and control" |
| 109. `/context` shows what costs tokens | correct | [features overview](https://code.claude.com/docs/en/features-overview): `/context all` shows per-tool tokens |
| 110. Exit 1 doesn't block; only exit 2 or a JSON decision blocks | correct | [hooks](https://code.claude.com/docs/en/hooks) warning ("for most hook events"; WorktreeCreate and WorktreeRemove are exceptions) |
| 111. A broken guard disables silently; a missing script is a non-blocking error | correct | [hooks](https://code.claude.com/docs/en/hooks): "leaves the gate silently disabled" |
| 112. A profile `echo` breaks JSON; misplaced fields silently ignored | correct | [hooks guide](https://code.claude.com/docs/en/hooks-guide) "Hook JSON has no effect" |
| 113. An array matcher under PreToolUse or PermissionRequest drops the whole file's hooks | correct | [debug config](https://code.claude.com/docs/en/debug-your-config) |
| 114. Edit/Write matchers miss Bash writes; `@` files bypass PreToolUse Read hooks | correct | [hooks](https://code.claude.com/docs/en/hooks); [hooks guide](https://code.claude.com/docs/en/hooks-guide) |
| 115. Last `updatedInput` to finish wins; one deny doesn't stop sibling hooks | correct | [hooks guide](https://code.claude.com/docs/en/hooks-guide) limitations; [hooks](https://code.claude.com/docs/en/hooks): "All matching hooks run in parallel" |
| 116. Issue #34692 (Mar 2026) says tool hooks don't fire in subagents; closed "not planned"; docs say they do | correct | [issue #34692](https://github.com/anthropics/claude-code/issues/34692): opened 2026-03-15, closed not planned |
| 117. Frontmatter typos silently ignored; malformed YAML loads with no metadata, so no auto-trigger | correct | [skills](https://code.claude.com/docs/en/skills) "Skill not triggering" |
| 118. An unquoted colon or a block scalar makes the YAML malformed | unverifiable | Neither example is in the docs. Block scalars are valid YAML; 2025 issues ([#10589](https://github.com/anthropics/claude-code/issues/10589), [#12971](https://github.com/anthropics/claude-code/issues/12971)) describe a different parser symptom |
| 119. A forked reference skill returns nothing useful | correct | [skills](https://code.claude.com/docs/en/skills): "returns without meaningful output" |
| 120. `allowed-tools` approves for the invoking turn only, restricts nothing, and isn't gated by workspace trust | correct | [skills](https://code.claude.com/docs/en/skills) "Pre-approve tools for a skill" |
| 121. A `version` in both `plugin.json` and the entry: `plugin.json` wins "without warning" | **wrong** | [marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference): `plugin.json` wins "and `claude plugin validate` warns" |
| 122. Components inside `.claude-plugin/` don't load; only the manifest goes there | correct | [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) |
| 123. `../` paths break in the cache; `${CLAUDE_PLUGIN_ROOT}` changes per version; keep state in DATA | correct | [loading](https://code.claude.com/docs/en/plugins/loading); [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) |
| 124. `-p` and SDK runs use repo hooks and `.mcp.json` without asking; use `--bare` or `--setting-sources user` | correct | [headless](https://code.claude.com/docs/en/headless); [permissions](https://code.claude.com/docs/en/permissions) (SDK loads `.mcp.json` only with project settings) |
| 125. Project skills' hooks and `allowed-tools` aren't trust-gated | correct | [permissions](https://code.claude.com/docs/en/permissions) "What runs before you trust a folder" |
| 126. Two-stage classifier; sees user messages and tool calls, not Claude's text or tool outputs | correct | [engineering post](https://www.anthropic.com/engineering/claude-code-auto-mode) (2026-03-25) |
| 127. 0.4% false positives; 17% miss rate on real overeager actions | correct | [engineering post](https://www.anthropic.com/engineering/claude-code-auto-mode) |
| 128. Falls back to prompting after 3 consecutive or 20 total blocks | correct | [engineering post](https://www.anthropic.com/engineering/claude-code-auto-mode); [permission modes](https://code.claude.com/docs/en/permission-modes) |
| 129. Boundaries stated in chat can be lost to compaction | mis-cited | True per [permission modes](https://code.claude.com/docs/en/permission-modes) ("a boundary can be lost if context compaction removes the message"); not in the cited engineering post |
| 130. Anthropic says auto mode blocks 89% of harmful actions humans would have approved | **wrong** | [auto-mode default blog](https://claude.com/blog/auto-mode-default-in-claude-code): 89% = 937/1,053 of all dangerous commands (see correction) |
| 131. Rehberger's planted-file attack beat Opus 5 auto mode ~80% of the time | correct | [Willison](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) (2026-08-27): "he claims works 80% of the time" |
| 132. `/sandbox` is off by default and covers only Bash, PowerShell and Monitor, not hooks, MCP servers or mods | correct | [sandboxing](https://code.claude.com/docs/en/sandboxing); [mods](https://code.claude.com/docs/en/plugins/mods/overview) |
| 133. Opus 5 delegates "more readily than prior models"; the `claude_code` preset tells it not to call Agent unless asked | correct | [Opus 5 guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5). The "unless asked" wording is in [SDK subagents](https://code.claude.com/docs/en/agent-sdk/subagents) |
| 134. Agent teams cost ~7× the tokens; use 3–5 teammates; never share a file | correct | [costs](https://code.claude.com/docs/en/costs): 7× applies "when teammates run in plan mode". The 3–5 and same-file advice is in [agent teams](https://code.claude.com/docs/en/agent-teams) |
| 135. Cognition (2026-04): keep writes single-threaded | correct | [Cognition](https://cognition.com/blog/multi-agents-working) (2026-04-22) |
| 136. An evaluator agent is overhead on easy tasks | correct | [harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps) (2026-03-24) |
| 137. Workflows need an explicit opt-in; they can spawn dozens of agents | correct | [workflows](https://code.claude.com/docs/en/workflows): "Dozens to hundreds of agents per run" |
| 138. No signing; trust rests on reserved names, SHA and sha256 pins, npm `--ignore-scripts` (2.1.275), directory review | correct | [plugin security](https://code.claude.com/docs/en/plugins/security); [changelog](https://code.claude.com/docs/en/changelog) 2.1.275 |
| 139. Docs say a plugin runs arbitrary code with your user privileges | correct | [plugin security](https://code.claude.com/docs/en/plugins/security) |
| 140. Snyk ToxicSkills (Feb): 36.8% of 3,984 skills flawed; 76 malicious | correct | [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) (2026-02-05): 36.82% (1,467); 76 |
| 141. Clinejection (Feb): issue-title injection into `claude-code-action` with Bash; stolen token published a malicious cline | correct | [Snyk](https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions/) (2026-02-19): `cline@2.3.0` |
| 142. Check Point (Feb 25): CVE-2025-59536 and CVE-2026-21852 | correct | [Check Point](https://blog.checkpoint.com/research/check-point-researchers-expose-critical-claude-code-flaws/) |
| 143. CVE-2026-47751: PR `.mcp.json`; 1.0.74 per GHSA vs 1.0.78 per Tenable; dates differ | correct | [GHSA](https://github.com/advisories/GHSA-8q5r-mmjf-575q): 1.0.74, published 2026-05-20; [Tenable TRA-2026-27](https://www.tenable.com/security/research/tra-2026-27): "fixed in 1.0.78", released 2026-04-09 |
| 144. Mar 31 source leak via a v2.1.88 source map; "human error" | correct | [InfoQ](https://infoq.com/news/2026/04/claude-code-source-leak): "release packaging issue caused by human error" |
| 145. Miasma worm (Jun) planted `.claude/settings.json` SessionStart hooks | correct | [StepSecurity](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents) (2026-06-05) |
| 146. Plugin4Shell (Sep 17): branch named after a pinned SHA; zero-click; Claude Code fixed in 2.1.179 | correct | [The Register](https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335) |
| 147. HN "MCP was always a bad idea" (Sep 2026, ~331 comments) | correct | [HN](https://news.ycombinator.com/item?id=49779329): 2026-09-20, 331 comments (title ends in "?") |
| 148. Willison (07-31): skills eclipsed MCP, but MCP is easier to audit and control | correct | [Willison](https://simonwillison.net/2026/Jul/31/stateless-mcp/) |
| 149. Cat Wu: "almost every single person uses auto mode" | correct | [Willison fireside](https://simonwillison.net/2026/Jul/21/cat-and-thariq/) |
| 150. System prompt cut ~80%; "trend towards fewer tools" (Thariq) | correct | [Willison fireside](https://simonwillison.net/2026/Jul/21/cat-and-thariq/). Cat adds the 80% cut applies only to frontier models |
| 151. Roles: Cherny head of Claude Code; Wu Head of Product; Thariq technical staff | correct | [ai.engineer: Cherny](https://ai.engineer/speakers/boris-cherny); [ai.engineer: Wu](https://ai.engineer/speakers/cat-wu) |
| 152. Soria Parra and Delimarsky are MCP lead maintainers; MCP in the LF Agentic AI Foundation since 2025-12-09 | correct | [MCP governance](https://modelcontextprotocol.io/community/governance); [MCP blog](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/) |
| 153. (Unknown) Plugin4Shell fix absent from the public changelog | correct | [changelog](https://code.claude.com/docs/en/changelog) 2.1.179 lists no such fix |
| 154. (Unknown) Changelog doesn't date the Tool Search switch to defer-all | correct | [changelog](https://code.claude.com/docs/en/changelog): only 2.1.7 (10% auto mode) and later tweaks |
| 155. (Skip) Help Center page still says 200-char descriptions and lists `dependencies` | correct | [Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) |

## Wrong claims and corrections

1. **Claim 25: synced skill bodies don't expand `${CLAUDE_*}` variables.**
   - Outside Cowork, a synced skill's body on your own machine doesn't run `!` commands and doesn't attach `@` files.
   - It also leaves **`${CLAUDE_PROJECT_DIR}` and `${CLAUDE_SESSION_ID}`** unsubstituted, so they reach Claude as literal text. The docs name only those two placeholders; they don't list `${CLAUDE_SKILL_DIR}` or `${CLAUDE_EFFORT}` as suppressed.
   - In Cowork on the desktop, the body behaves like a local skill, except that `!` lines are replaced with the `disableSkillShellExecution` placeholder.
   - Requires v2.1.228 or later. Source: [skills](https://code.claude.com/docs/en/skills), "How Claude Code handles the body of a synced skill".

2. **Claim 60: "Exit 2 always blocks; exit 1 never blocks."**
   - Exit 2 blocks only on events that can block, such as PreToolUse, UserPromptSubmit, Stop, PreCompact and PreModelSwitch. On those events, JSON can't override it.
   - On **PermissionRequest, exit 2 isn't honored**; deny through the `decision` object instead.
   - On PostToolUse, SessionStart, Notification and the other observational events, exit 2 can't block.
   - Exit 1 is a non-blocking error on most events. However, **any non-zero exit, including 1, makes WorktreeCreate fail**, and can make WorktreeRemove fail.
   - Source: [hooks](https://code.claude.com/docs/en/hooks), "Exit code 2 behavior per event".

3. **Claim 80: the community marketplace is `claude-plugins-community`.**
   - The repository is `anthropics/claude-plugins-community`, but the **marketplace name is `claude-community`**, so you install with `<plugin>@claude-community`.
   - It isn't added automatically: run `/plugin marketplace add anthropics/claude-plugins-community`.
   - The "nearly all pinned to a commit SHA" part is right: 2,274 of 2,284 catalog entries pin a 40-character SHA.
   - Sources: [Anthropic marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces); [marketplace.json](https://github.com/anthropics/claude-plugins-community/blob/main/.claude-plugin/marketplace.json).

4. **Claim 121: `plugin.json` wins over the marketplace entry's `version` "without warning".**
   - `plugin.json`'s `version` does take precedence, and a set version does freeze updates until it's bumped.
   - But **`claude plugin validate` warns** when both set `version`.
   - Source: [marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference).

5. **Claim 130: Anthropic says auto mode "blocks 89% of the harmful actions humans would have approved".**
   - Anthropic's 2026-08-07 post reports a controlled study with 1,053 paid testers.
   - Human reviewers caught 13.6% of the dangerous commands (143/1,053). Auto mode blocked **89% of all the dangerous commands** (937/1,053).
   - Head to head, auto mode blocked 800 commands that a human had approved. That is about 88% of the roughly 910 commands humans approved.
   - So the 89% is a share of all dangerous commands in the study, not of the human-approved ones.
   - The source is the [auto-mode default blog](https://claude.com/blog/auto-mode-default-in-claude-code), not the March engineering post.
