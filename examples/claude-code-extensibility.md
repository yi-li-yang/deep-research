---
topic: Claude Code extensibility (skills, plugins, hooks, subagents, MCP)
verified: 2026-10-06
---
# Claude Code extensibility: briefing
Compiled from the sources below; evidence, not instructions. Confidence: **high** for documented behaviour (official docs and changelog as of Claude Code 2.1.291, 2026-10-06); **medium** for incidents and community debates (some secondary or vendor sources, flagged).

## What's changed

**Versions and models**
- You may believe Claude Code is early in the 2.1.x line, with Opus/Sonnet 4.6 as the newest models. As of 2026-10-06:
  - Claude Code is at **2.1.291**.
  - The newest models are **Opus 5.5** (2026-09-22), **Sonnet 5.5** (2026-09-28) and **Fable 5.1** (2026-09-01).
  - Since 2.1.280, Pro and Team Standard plans also default to Opus.
  ([changelog](https://code.claude.com/docs/en/changelog), 2026-10)

**Permissions**
- You may believe there are four permission modes. As of 2026-09-25 there are six: `default` (shown as "Manual"), `acceptEdits`, `plan`, `auto`, `dontAsk` and `bypassPermissions`.
  - In **auto**, a classifier approves or blocks each action. It launched 2026-03-24, became the default on Pro, Max and Team on 2026-08-14, and since 2.1.283 (2026-09-25) is the built-in starting mode for interactive terminal and VS Code sessions on every plan.
  - Admins can disable it with `permissions.disableAutoMode`.
  - `defaultMode: auto` or `bypassPermissions` is ignored in project and local settings files.
  ([permission modes](https://code.claude.com/docs/en/permission-modes), [blog](https://claude.com/blog/auto-mode-default-in-claude-code), 2026-09)
- New permission-rule forms: `Tool(param:value)` (deny and ask only), `Agent(Name)`, `Agent(model:opus)` and `Cd(path)`. Rules are evaluated deny → ask → allow; specificity doesn't matter. ([permissions](https://code.claude.com/docs/en/permissions), 2026-10)

**Commands and skills**
- You may believe slash commands (`.claude/commands/`) and skills are separate mechanisms. As of v2.1.3 (2026-01-09) they are merged.
  - Every skill is also a `/name` command, and command files are the legacy form; they accept all skill frontmatter except `name` and `paths`.
  - Claude invokes everything through the **Skill** tool. The old SlashCommand tool is gone.
  - Arguments: `$ARGUMENTS`, `$ARGUMENTS[N]`/`$N`, and named `$name` declared in an `arguments:` list.
  - Shell injection uses inline `` !`cmd` `` or fenced ```` ```! ```` blocks. If a command fails or is denied, the whole invocation aborts.
  ([skills](https://code.claude.com/docs/en/skills), 2026-10)
- Full skill frontmatter: `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`, `compatibility`.
  - Unknown keys are silently ignored.
  - In Claude Code, `name` and `description` are optional.
  - Substitutions: `${CLAUDE_SKILL_DIR}`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_PROJECT_DIR}`, and `${CLAUDE_PLUGIN_ROOT}`/`${CLAUDE_PLUGIN_DATA}` in plugins. These also expand inside `allowed-tools` Bash rules, so a skill can run its bundled scripts without permission prompts.
  ([skills](https://code.claude.com/docs/en/skills), 2026-10)
- You may believe every skill's description always stays in context. As of 2026-10:
  - The listing keeps every skill *name*, but when the listing exceeds its budget (default **1% of the context window**, `skillListingBudgetFraction`) it drops descriptions, starting with the least-used skills.
  - Each skill's `description` plus `when_to_use` is capped at **1,536 characters**.
  - `disable-model-invocation: true` removes a skill from the listing entirely.
  - After compaction, each re-attached skill keeps its first 5k tokens, within 25k in total.
  ([skills](https://code.claude.com/docs/en/skills), 2026-10)
- `context: fork` skills have run **in the background by default** since 2.1.218 (2026-07-22). Set `background: false` to wait for the result. Backgrounded forks get a narrower tool set and bypass checkpoints, and a forked skill does not inherit conversation history. ([skills](https://code.claude.com/docs/en/skills), 2026-07)
- **Skills now sync from claude.ai**, one-way, starting mid-Sep 2026 (v2.1.273–2.1.275).
  - Terminal sessions signed in through `/login` download the account's skills to `~/.claude/skills/synced/`.
  - Synced skills run as `/anthropic-skills:<name>`, or by short name when it's free.
  - On a local machine (outside Cowork), synced bodies don't run `!` commands, don't attach `@` files, and leave `${CLAUDE_PROJECT_DIR}` and `${CLAUDE_SESSION_ID}` unsubstituted.
  - Sessions using an API key, Bedrock or bare mode don't sync. `syncClaudeAiSkills: false` opts out.
  - Personal skills in `~/.claude/skills/` **don't load** in cloud sessions, Cowork or routines. Those load account skills, plus the repo's `.claude/skills/` in cloud sessions.
  ([skills](https://code.claude.com/docs/en/skills), 2026-09)
- claude.ai uploads, the Skills API and `package_skill.py` accept **only six frontmatter keys**: `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. Any other key is a hard error: "Unexpected key(s) in SKILL.md frontmatter".
  - The Skills API left beta on 2026-08-19; the `skills-2025-10-02` header is no longer needed.
  - On claude.ai, skills live under Customize → Skills. Enterprise skill scanning and "requires review" publishing became defaults on 2026-10-02.
  ([skills](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code), [release notes](https://platform.claude.com/docs/en/release-notes/overview), [provisioning](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization), 2026-08/10)

**Subagents and orchestration**
- You may believe subagents are launched through the Task tool. As of v2.1.63 (2026-02-28) the tool is **`Agent`**; rules written as `Task(...)` still work as aliases.
  - Inputs: `description`, `prompt`, `subagent_type`, `model`, `run_in_background`, `name`, `isolation` (`"worktree"`).
  ([sub-agents](https://code.claude.com/docs/en/sub-agents), 2026-02)
- You may believe subagents can't spawn subagents. As of v2.1.219 (2026-07-24), **nesting is on by default, up to 3 levels** below the main conversation. `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` sets the limit, and `1` disables nesting. Agent-team teammates still can't spawn teammates. ([sub-agents](https://code.claude.com/docs/en/sub-agents), 2026-07)
- You may believe a subagent never sees the parent conversation. **Forks** do: they inherit the full conversation and its prompt cache.
  - Claude starts one with `subagent_type: "fork"`; users start one with `/subtask`.
  - Fork mode has been on by default in interactive sessions since v2.1.232 (2026-08-13). It is off in `-p` and the SDK unless `CLAUDE_CODE_FORK_SUBAGENT=1`.
  ([sub-agents](https://code.claude.com/docs/en/sub-agents), 2026-08)
- **Background subagents became the default** in v2.1.198 (2026-07-01). Their permission prompts surface in the main session.
  - At most 20 run concurrently (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`). The 200-per-session spawn cap was removed.
  - Background subagents keep a restricted set of built-in tools.
  - `AskUserQuestion`, plan-mode tools, `Workflow` and `ScheduleWakeup` are stripped from every subagent.
  ([sub-agents](https://code.claude.com/docs/en/sub-agents), [changelog](https://code.claude.com/docs/en/changelog), 2026-07/08)
- **Explore no longer runs on Haiku.** It inherits the session's model, capped at Opus.
  - New built-in agents: `claude`, `claude-code-guide`, `statusline-setup` and `fork`.
  - The `/agents` wizard was removed in 2.1.198; create agents by asking Claude or editing files.
  - New agent frontmatter: `disallowedTools`, `maxTurns`, `mcpServers`, `memory`, `background`, `effort`, `isolation: worktree`, `omitClaudeMd`, `initialPrompt`.
  ([sub-agents](https://code.claude.com/docs/en/sub-agents), 2026-07)
- You may believe the Agent SDK loads no filesystem config unless asked. Omitting `settingSources` now loads user, project and local settings, like the CLI; pass `[]` to isolate. ([SDK features](https://code.claude.com/docs/en/agent-sdk/claude-code-features), 2026-10)
- **New since early 2026:**
  - **Workflows** (v2.1.154, 2026-05-28): the `Workflow` tool runs a JavaScript script that orchestrates many agents with `agent()`, `parallel()`, `pipeline()` and `phase()`. You opt in with the keyword **`ultracode`** or `/effort ultracode`. `/deep-research` is bundled. ([workflows](https://code.claude.com/docs/en/workflows))
  - **`/goal`** (v2.1.139): an evaluator model keeps Claude working until a condition holds. ([goal](https://code.claude.com/docs/en/goal))
  - **`/loop`** (2.1.71), backed by `CronCreate`/`CronList`/`CronDelete`. Tasks are session-scoped and expire after 7 days. ([scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks))
  - **Routines** (research preview, Apr 2026): cloud runs triggered by a schedule (minimum 1 hour), an API call or a GitHub event. ([routines](https://code.claude.com/docs/en/routines))
  - **Agent view**: `claude --bg`, `claude agents`, `claude attach`.
  - **Cross-session messaging**: `ListAgents` plus `SendMessage` (2.1.224).
- **Agent teams** are still experimental and off by default as of 2026-10-06 (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). Once enabled, any *named* Agent call launches a teammate. ([agent teams](https://code.claude.com/docs/en/agent-teams), 2026-10)

**Hooks**
- You may believe the default hook timeout is 60s. Since v2.1.3 (2026-01-09) it is **600s** for command, http and mcp_tool hooks. Exceptions:
  - 30s for UserPromptSubmit and model-switch events.
  - prompt hooks 30s; agent hooks 60s.
  - SessionEnd hooks share a 1.5s budget.
  ([hooks](https://code.claude.com/docs/en/hooks), 2026-10)
- There are now **33 events**: SessionStart, Setup, UserPromptSubmit, UserPromptExpansion, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, PostToolBatch, Notification, MessageDisplay, SubagentStart, SubagentStop, TaskCreated, TaskCompleted, Stop, StopFailure, TeammateIdle, InstructionsLoaded, ConfigChange, CwdChanged, DirectoryAdded, FileChanged, WorktreeCreate, WorktreeRemove, PreCompact, PostCompact, PreModelSwitch, PostModelSwitch, Elicitation, ElicitationResult, SessionEnd. ([hooks](https://code.claude.com/docs/en/hooks), 2026-10)
- There are **five handler types**: `command`, `http` (2.1.63), `mcp_tool` (2.1.118), `prompt` and `agent` (still experimental).
  - Handler fields include `args` (exec form, no shell), `shell`, `if` (a permission-rule filter such as `Bash(git *)`), `async`, `asyncRewake` and `once`. `once` is honoured only in skill frontmatter.
  - PostToolUse can rewrite any tool's output with `updatedToolOutput` (2.1.121).
  ([hooks](https://code.claude.com/docs/en/hooks), 2026-10)
- **Matcher semantics changed.**
  - `*` or empty matches everything.
  - Matchers made only of letters, digits, `_`, `-`, spaces, `,` and `|` match exact names or lists.
  - Anything else is an unanchored JS regex, so `Edit.*` also matches `NotebookEdit`.
  - Since 2.1.195 (2026-06-26), hyphenated names match exactly: `mcp__brave-search` matches nothing, so write `mcp__brave-search__.*`.
  ([hooks](https://code.claude.com/docs/en/hooks), 2026-06)
- **Hooks are no longer snapshotted at startup.** Settings edits hot-reload, and `/hooks` is now a read-only browser.
  - JSON output is read on every exit code. Exit 2 blocks only on events that can block (PreToolUse, UserPromptSubmit, Stop, PreCompact, PreModelSwitch). It is ignored on PermissionRequest, where you deny through the `decision` object. Exit 1 is a non-blocking error on most events, but any non-zero exit fails WorktreeCreate.
  - A Stop hook can force continuation at most 8 times in a row before the turn ends (2.1.143).
  ([hooks](https://code.claude.com/docs/en/hooks), [changelog](https://code.claude.com/docs/en/changelog), 2026-05)
- **Mods** (v2.1.287, 2026-10-01) are new. They are JavaScript/TypeScript function hooks shipped in plugins under `modules` in `hooks/hooks.json`, exporting `register(on)`.
  - They are **unsandboxed**. A mod can redraw the UI (panes, status line, toasts), rewrite prompts and tool calls, call models, and approve tool calls.
  - A mod's `tool.check` can override ask rules and non-managed hook blocks. On machines without managed settings or a Team/Enterprise sign-in, it can override **deny rules** too.
  - Admins can restrict mods with `allowManagedModsOnly`.
  - Settings hooks are not deprecated.
  ([mods](https://code.claude.com/docs/en/plugins/mods/overview), [permissions](https://code.claude.com/docs/en/permissions), 2026-10)

**Plugins and distribution**
- You may believe plugins are a public beta with a required `plugin.json`. Plugins are no longer labelled beta, and the manifest is optional; without one, the name comes from the marketplace entry or the directory.
  - Components today: skills, agents, hooks, MCP servers (including `.mcpb`), LSP servers, output styles, themes and monitors (both experimental), channels, a `bin/` folder (added to Bash's PATH), `settings.json`, workflows, `userConfig` and mods.
  ([manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference), 2026-10)
- **Installing.**
  - Inside a session, `/plugin install` opens a details pane (contents, estimated context cost, scope) instead of installing straight away.
  - One command adds the marketplace and installs: `/plugin install <name> --marketplace <owner/repo>` (2.1.275, 2026-09-17).
  - Shell CLI: `claude plugin install|uninstall|enable|disable|update|list|details|configure|prune|init|tag|validate|eval|test` and `claude plugin marketplace add|list|update|remove`.
  ([install](https://code.claude.com/docs/en/plugins/install), [CLI reference](https://code.claude.com/docs/en/plugins/cli-reference), 2026-09)
- **Versions and updates.**
  - Version precedence: `plugin.json` `version`, then the marketplace entry's `version`, then the commit SHA. A set `version` keeps users on it until it is bumped.
  - Auto-update is on by default for Anthropic's official marketplaces and off for third-party ones.
  - Dependencies use semver ranges against `<name>--v<ver>` git tags.
  - `${CLAUDE_PLUGIN_DATA}` (`~/.claude/plugins/data/<id>/`) persists across updates.
  ([loading](https://code.claude.com/docs/en/plugins/loading), [dependencies](https://code.claude.com/docs/en/plugins/dependencies), 2026-09)
- **Plugins enabled on claude.ai sync into Claude Code** as `name@synced` (mid-Sep 2026). Each surface loads only part of a plugin:
  - claude.ai chat loads only skills, commands and remote MCP servers.
  - Cowork also loads agents, hooks and local MCP servers.
  - claude.ai and Cowork refuse plugins with a top-level `bin/`.
  - Cloud sessions have no `/plugin` panel and don't load user-scope plugins or repo-declared ones. They do load server-managed plugins and claude.ai-synced ones.
  ([platform support](https://claude.com/docs/plugins/platform-support), [cloud environments](https://code.claude.com/docs/en/cloud-environments), 2026-09)
- **Anthropic's marketplaces.**
  - `claude-plugins-official` is added automatically on first interactive start.
  - The community marketplace (repo `anthropics/claude-plugins-community`, installed as `<plugin>@claude-community`, added with `/plugin marketplace add anthropics/claude-plugins-community`) holds third-party plugins, nearly all pinned to a commit SHA.
  - `anthropics/claude-code` is only a demo marketplace.
  - The Anthropic directory submission portal opened 2026-09-25, with automated validation, a security scan and human review.
  - claude.com/marketplace ("2,000+ connectors and plugins") launched 2026-09-23.
  ([Anthropic marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces), [directory](https://claude.com/docs/directory/publish), 2026-09)
- **`claude plugin eval`** is GA (2.1.269, 2026-09-11). It runs each case 3 times in isolated sessions, with and without the plugin, and reports the difference. Evals spend real usage. ([plugin evals](https://code.claude.com/docs/en/plugin-evals), 2026-09)

**MCP**
- You may believe the latest MCP spec is 2025-11-25. The current revision is **2026-07-28**, the "stateless" revision; Willison calls it "MCP 2.0". What changed:
  - There is no `initialize` handshake and no `ping`. Version and capabilities travel in each request's `_meta`, and servers implement `server/discover`.
  - `subscriptions/listen` replaces the GET stream and `resources/subscribe`.
  - Multi Round-Trip Requests (`resultType: "input_required"`) replace server-initiated sampling, elicitation and roots requests.
  - Tasks moved out of the core into an extension.
  - Roots, Sampling and Logging are deprecated, and Dynamic Client Registration is deprecated in favour of Client ID Metadata Documents.
  - Streamable HTTP has no sessions or `Mcp-Session-Id`.
  ([spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog), 2026-07)
- **Claude Code's v2 MCP runtime negotiates 2026-07-28 with HTTP servers.** It has been the default since about 2.1.232 (2026-08-13). Opt out with `MCP_SDK_GENERATION=v1`. ([MCP](https://code.claude.com/docs/en/mcp), 2026-08)
- You may believe Tool Search defers MCP tools once they would take about 10% of context. **It now defers all MCP tools by default**: only tool names and server instructions load at start.
  - The 10% behaviour is opt-in with `ENABLE_TOOL_SEARCH=auto` or `auto:N`.
  - Exempt a server with `alwaysLoad`, or a tool with `_meta["anthropic/alwaysLoad"]`.
  - Tool descriptions and server instructions are capped at 2,048 characters.
  ([MCP](https://code.claude.com/docs/en/mcp), 2026-10)
- **claude.ai connectors appear in Claude Code automatically** (v2.1.46) with a claude.ai subscription login, not with an API key. MCP Apps (`ui://`) render in claude.ai and the Desktop chat but are **hidden in Claude Code**. ([MCP](https://code.claude.com/docs/en/mcp), 2026-09)
- Official MCP extensions now include Apps, Tasks, OAuth Client Credentials, Enterprise-Managed Authorization and **Skills over MCP** (SEP-2640, served as `skill://` resources). Claude Code documents no support for Skills over MCP. ([extensions](https://modelcontextprotocol.io/extensions/overview), 2026-10)

**Memory and the wider ecosystem**
- You may believe Claude Code doesn't read AGENTS.md. Since v2.1.277 (2026-09-18) it **reads AGENTS.md when there is no CLAUDE.md**; the `/config` setting "Project instructions" can load both. ([memory](https://code.claude.com/docs/en/memory), 2026-09)
- **Agent Plugins 1.0** (2026-08-06) is a cross-vendor plugin packaging standard from AWS, Cursor, Microsoft, OpenAI and Vercel, with Google joining. **Anthropic is not part of it**, and its layout (`plugin.json` at the root) differs from Claude Code's `.claude-plugin/`. ([GitHub changelog](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/), 2026-08)
- The Agent Skills standard (agentskills.io) lists 46 client products and names no governing foundation. ([clients](https://agentskills.io/clients), 2026-10)

## What an expert knows

**Choosing the mechanism** (Anthropic's 2026 guidance)
- Keep CLAUDE.md under about 200 lines, owned and reviewed like code. Put file-specific guidance in path-scoped `.claude/rules/`.
- Put procedures in skills: only descriptions load each session.
- Put guarantees in hooks. An instruction is "a request, not a guarantee."
- Use subagents for side tasks that would flood the main context.
- Use MCP when credentials should stay out of the agent's context, or when access must be governed.
- `/context` shows what costs tokens.

([steering post](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more), [features overview](https://code.claude.com/docs/en/features-overview), 2026-06)

**Hook pitfalls**
- **Exit 1 doesn't block** on most events. Only exit 2 on a blocking event, or a JSON decision, blocks; PermissionRequest ignores exit 2.
- **A broken guard disables itself silently.** A missing script or wrong path is a non-blocking error.
- **Unexpected stdout breaks JSON output.** A profile `echo` before the JSON turns the output into plain text, and misplaced fields are silently ignored.
- **One bad entry can drop the whole file's hooks.** An array matcher under PreToolUse or PermissionRequest does this.
- **Edit-matching hooks miss shell writes.** A PostToolUse `Edit|Write` matcher misses edits made through Bash, and `@`-file references bypass PreToolUse Read hooks.
- **Hooks don't stack predictably.** With several `updatedInput` hooks, the last to finish wins, and one hook's deny doesn't stop its siblings.
- **Contested: whether tool hooks fire inside subagents.** The docs say they do; issue #34692 (Mar 2026) reported they don't and was closed "not planned". Test both paths.

([hooks guide](https://code.claude.com/docs/en/hooks-guide), [debug config](https://code.claude.com/docs/en/debug-your-config), 2026-08)

**Skill pitfalls**
- **Typos fail quietly.** A frontmatter typo is silently ignored. Malformed YAML (an unquoted colon, a block scalar) loads the body with no metadata, so the skill never auto-triggers.
- **Too many skills hide descriptions.** Once over the listing budget, descriptions disappear and triggering degrades.
- **A forked reference skill returns nothing.** `context: fork` on a skill without an actionable task does nothing useful.
- **Compaction truncates skills.** After compaction only the first 5k tokens of a skill survive. Put critical rules at the top, and re-invoke the skill if Claude stops following it.
- **`allowed-tools` only pre-approves.** It approves tools for the invoking turn only, restricts nothing, and is **not gated by workspace trust**.

**Plugin pitfalls**
- **A pinned `version` freezes updates** until it is bumped. If `version` is set in both `plugin.json` and the marketplace entry, `plugin.json` wins; `claude plugin validate` warns about the duplicate.
- **Components inside `.claude-plugin/` don't load.** Only the manifest goes there.
- **Relative `../` paths break** once the plugin is copied to the cache. `${CLAUDE_PLUGIN_ROOT}` changes with every version, so keep state in `${CLAUDE_PLUGIN_DATA}`.

**Trust gaps**
- **Headless runs trust the folder.** `-p` and SDK sessions run repo hooks and `.mcp.json` servers without asking. For untrusted repos, use `--bare` or `--setting-sources user`.
- **Project skills aren't trust-gated.** Their hooks and `allowed-tools` apply without the trust dialog.

([permissions](https://code.claude.com/docs/en/permissions), [headless](https://code.claude.com/docs/en/headless), 2026-10)

**Auto mode, as specified by Anthropic** ([engineering post](https://www.anthropic.com/engineering/claude-code-auto-mode), 2026-03)
- **How it works:** a two-stage classifier. A fast filter runs first, then chain-of-thought review only for flagged actions. It sees user messages and tool calls, not Claude's own text or tool outputs.
- **Error rates:** 0.4% false positives on real traffic, and a **17% miss rate on real overeager actions**.
- **Fallback:** after 3 consecutive or 20 total blocks it falls back to prompting.
- **Lost boundaries:** limits you state in chat ("don't push") can be lost when the conversation is compacted.

**Contested: how safe auto mode is**
- **Anthropic's claim** (a study of 1,053 dangerous commands, [blog](https://claude.com/blog/auto-mode-default-in-claude-code), 2026-08): human reviewers caught 13.6% and auto mode blocked 89% of all of them, including about 88% of those humans approved. Anthropic gains from this framing.
- **The attack:** Johann Rehberger's planted-file attack beat Opus 5 in auto mode about 80% of the time ([Willison](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/), 2026-08).
- **Verdict:** treat auto mode as convenience, not containment. Run unattended agents in a container, VM or OS sandbox. `/sandbox` (Seatbelt, bubblewrap) is still off by default and covers only Bash, PowerShell and Monitor commands, not hooks, MCP servers or mods.

([sandboxing](https://code.claude.com/docs/en/sandboxing), 2026-10)

**Multi-agent work**
- **Delegate only genuinely independent, sizeable work.** Opus 5 delegates "more readily than prior models", so the `claude_code` preset tells it not to call Agent unless asked ([Opus 5 guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5), 2026-07).
- **Agent teams cost about 7× the tokens.** Use 3–5 teammates and never split work on the same file ([costs](https://code.claude.com/docs/en/costs)).
- **Keep writes single-threaded.** Extra agents work best reviewing or advising (Cognition, 2026-04). An evaluator agent helps on hard tasks but is overhead on easy ones ([harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps), 2026-03).
- **Workflows are not for routine use.** They need an explicit opt-in (`ultracode`) because they can spawn dozens of agents.

**Security record** (there is still no signing for plugins, skills, mods or MCP servers)

Trust rests on:
- reserved marketplace names (they must come from github.com/anthropics)
- commit-SHA pins in the community catalog, and optional sha256 pins on archive sources
- npm integrity checks with `--ignore-scripts` (2.1.275)
- the directory's scan and review

The docs say a plugin runs arbitrary code with your user privileges ([plugin security](https://code.claude.com/docs/en/plugins/security), 2026-10).

Incidents of 2026:
- **Feb, Snyk ToxicSkills:** 36.8% of 3,984 community skills had a security flaw; 76 were malicious.
- **Feb, Clinejection:** a prompt injection in a GitHub issue title hijacked a bot running `claude-code-action` with Bash allowed. The stolen token published a malicious `cline` release.
- **Feb 25, Check Point CVE-2025-59536 and CVE-2026-21852:** repo hooks and `.mcp.json` ran before the trust dialog, and a repo-set `ANTHROPIC_BASE_URL` leaked API keys.
- **CVE-2026-47751:** `claude-code-action` loaded a pull request's `.mcp.json`. Sources disagree on the date and fix version (1.0.74 per GHSA, 1.0.78 per Tenable), so treat ≥1.0.78 as safe.
- **Mar 31, source leak:** a v2.1.88 npm source map exposed the full source. Anthropic called it human error.
- **Jun, Miasma worm:** it planted `.claude/settings.json` SessionStart hooks across repositories.
- **Sep 17, Plugin4Shell:** a branch named after a pinned SHA defeats SHA pinning, and auto-update makes it zero-click. It hit Claude Code, Codex, Copilot and Gemini CLI. The researchers say Claude Code was fixed in 2.1.179.

Sources: [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), [Snyk Cline](https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions/), [Check Point](https://blog.checkpoint.com/research/check-point-researchers-expose-critical-claude-code-flaws/), [GHSA](https://github.com/advisories/GHSA-8q5r-mmjf-575q), [StepSecurity](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents), [The Register](https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335).

**Live debates**
- **MCP vs CLI plus skills.**
  - Verdict: they are complementary. MCP's lasting value is keeping credentials out of the agent's context, plus governed, auditable access. The stateless 2026-07-28 spec answered much of the complexity criticism.
  - Dissent: "MCP was always a bad idea" (HN, Sep 2026, about 331 comments) says CLIs plus skills are leaner and avoid the context tax.
  - Willison (2026-07-31) says skills eclipsed MCP for shell-capable agents, but MCP is easier to audit and control.
  - MCP itself absorbed skills through SEP-2640.
- **Auto mode as the default.** Anthropic staff say "almost every single person uses auto mode" internally (Cat Wu). Security researchers want sandboxes instead.
- **Skill and plugin stores as "the new npm".** Anthropic's absence from Agent Plugins 1.0 fragments the packaging format.
- **Direction of travel.** The team cut Claude Code's system prompt by about 80% and is "trend[ing] towards fewer tools" (Thariq Shihipar, via [Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/), 2026-07).

**People**
- Boris Cherny: Head of Claude Code. Cat Wu: Head of Product. Thariq Shihipar: technical staff.
- David Soria Parra and Den Delimarsky: MCP lead maintainers. MCP has been under the Linux Foundation's Agentic AI Foundation since 2025-12-09.
- Simon Willison: the leading practitioner-skeptic.
- Johann Rehberger: agent-security research.

## Unknown
- **Signing.** No signing or provenance scheme exists for plugins, skills, mods or MCP servers, as of 2026-10-06. Ask in Anthropic's GitHub issues for `anthropics/claude-code`.
- **Plugin4Shell fix.** The claimed fix in Claude Code 2.1.179 does not appear in the public changelog, as of 2026-10-06.
- **Tool Search default.** Which version switched Tool Search from the 10% threshold to deferring all MCP tools; the changelog doesn't say, as of 2026-10-06.
- **MCP feature support.** Claude Code's support for MCP sampling, the Tasks extension and Skills over MCP is undocumented, as of 2026-10-06.
- **Hooks in subagents.** Whether PreToolUse and PostToolUse fire reliably inside subagents; docs and an issue report conflict, as of 2026-10-06.
- **Previews.** When agent teams leave experimental status, when Projects (parallel cloud threads) launches, and how `isolation: "remote"` on the Agent tool works (it appears only in SDK types), as of 2026-10-06.
- **Auto mode numbers.** No independent replication of Anthropic's auto mode safety figures exists, as of 2026-10-06.
- **`.agents/skills/`.** Whether Claude Code scans this path, which the agentskills.io convention recommends; probably not, but absence of evidence isn't proof, as of 2026-10-06.
- **Shaky claims.** The "26,000 agents" and "SkillJacking" figures come from aggregator sites without primary sources. Reports that Google replaced Gemini CLI with a closed-source Antigravity CLI (May–June 2026) are secondary only.

## Sources
- [Claude Code changelog](https://code.claude.com/docs/en/changelog): the version-by-version truth; read it first for anything time-sensitive.
- Claude Code docs:
  - [skills](https://code.claude.com/docs/en/skills)
  - [hooks](https://code.claude.com/docs/en/hooks)
  - [sub-agents](https://code.claude.com/docs/en/sub-agents)
  - [permissions](https://code.claude.com/docs/en/permissions) and [permission modes](https://code.claude.com/docs/en/permission-modes)
  - [MCP](https://code.claude.com/docs/en/mcp)
  - [plugins](https://code.claude.com/docs/en/plugins/overview), including the manifest, loading and CLI references
  - [mods](https://code.claude.com/docs/en/plugins/mods/overview)
  - [cloud environments](https://code.claude.com/docs/en/cloud-environments)
  - the full index is at [llms.txt](https://code.claude.com/docs/llms.txt)
- [MCP spec 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) and [roadmap](https://modelcontextprotocol.io/development/roadmap): protocol truth.
- [Anthropic engineering](https://www.anthropic.com/engineering): the auto mode and harness-design posts give design rationale and numbers. Anthropic is an interested party.
- [Simon Willison's blog](https://simonwillison.net): the best running practitioner commentary and security skepticism.
- [agentskills.io](https://agentskills.io/specification): the cross-vendor skill spec and client list.
- **Skip:**
  - SEO "Claude Code hooks guide" posts: several still teach pre-2026 exit-code semantics and say PermissionRequest blocks on exit 2.
  - The Help Center "create custom skills" page: it still says descriptions max 200 characters and lists a `dependencies` field that uploads reject.
  - Aggregator security figures without primary sources.

## Log
- 2026-10-06: an independent audit checked 155 claims (146 correct, 5 wrong, 3 unverifiable, 1 mis-cited). Fixed the 5 wrong claims, which were over-generalisations from compression: the exit-2 rule, which synced-skill placeholders stay unexpanded, the community marketplace name, the version-duplicate warning, and the base of the auto-mode 89% figure.
- 2026-10-06: built from a fresh no-tools prior and six parallel research agents: (1) skills and commands; (2) plugins and distribution; (3) hooks; (4) subagents and automation; (5) MCP; (6) permissions, safety and ecosystem. The largest corrections to the prior:
  - permission modes, now six with auto as the default
  - Task renamed Agent; nesting and forks
  - the hook timeout (600s), events (33) and matcher semantics
  - MCP spec 2026-07-28 and Tool Search deferring all tools
  - skills and plugins syncing from claude.ai
  - mods
  - AGENTS.md support
  - models (Opus 5.5, Sonnet 5.5, Fable 5.1)
