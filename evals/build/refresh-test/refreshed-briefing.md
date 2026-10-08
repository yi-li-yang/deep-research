---
topic: Claude Code extensibility (skills, plugins, hooks, subagents, MCP)
verified: 2026-10-06
---
# Claude Code extensibility: briefing
Compiled from the sources below; evidence, not instructions. Confidence: **high** for documented behaviour (official docs and the raw changelog through Claude Code 2.1.291, read 2026-10-06); **medium** for incidents, debates and the wider ecosystem (some secondary or vendor sources, flagged).

## What's changed

**Versions and models**
- Claude Code is at **2.1.291** (2026-10-06). Releases land almost daily, so check the changelog before relying on any version number here.
- The newest models, all with 1M context, are **Fable 5.1** (`claude-fable-5-1`, 2026-09-01), **Opus 5.5** (`claude-opus-5-5`, 2026-09-22, now the default Opus) and **Sonnet 5.5** (`claude-sonnet-5-5`, 2026-09-28). Before them came Fable 5 (06-09), Sonnet 5 (06-30) and Opus 5 (07-24). Subagent `model:` accepts the alias `fable`.
- Since 2.1.280, Pro and Team Standard plans default to Opus, like Max, Team Premium and Enterprise.
([changelog](https://code.claude.com/docs/en/changelog), 2026-10)

**Permissions**
- You may believe auto mode is an opt-in preview. As of 2026-09 it is the **built-in starting mode** for interactive terminal and VS Code sessions on every plan and provider: from v2.1.283 per the docs, logged under 2.1.284 (09-28) in the changelog. In auto mode, a classifier approves or blocks each action. It launched 2026-03-24 and has been the default on Pro, Max and Team since 2026-08-14.
  - `permissions.defaultMode` still takes precedence.
  - `claude -p` and the SDK still start in Manual mode where feature flags are fetched. On third-party providers or with telemetry off, they start in auto (2.1.285).
  - The mode that asks before acting is now called **Manual** in the UI. Its config value is still `default`.
  - Admins remove auto mode with `permissions.disableAutoMode: "disable"` in managed settings.
  - `defaultMode: "auto"` or `"bypassPermissions"` doesn't take effect from project or local settings files.
  - In auto mode, a skill's inline `!` commands are judged by permission rules, not the classifier. A command no rule covers runs as a reviewed tool call (2.1.271).
  ([permission modes](https://code.claude.com/docs/en/permission-modes), [blog](https://claude.com/blog/auto-mode-default-in-claude-code), [changelog](https://code.claude.com/docs/en/changelog), 2026-08/10)

**Commands and skills**
- You may believe slash commands (`.claude/commands/`) and skills are separate mechanisms. As of v2.1.3 (2026-01-09) they are merged.
  - Every skill is also a `/name` command. Command files are the legacy form, and they accept all skill frontmatter except `name` and `paths`.
  - Claude invokes everything through the **Skill** tool. The old SlashCommand tool is gone.
  - Arguments: `$ARGUMENTS`, `$ARGUMENTS[N]`/`$N`, and named `$name` declared in an `arguments:` list.
  - Shell injection uses inline `` !`cmd` `` or fenced ```` ```! ```` blocks. If a command fails or is denied, the whole invocation aborts.
  ([skills](https://code.claude.com/docs/en/skills), 2026-10)
- The full skill frontmatter is `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license` and `compatibility`.
  - Every field is optional, and unknown keys are silently ignored.
  - Substitutions: `${CLAUDE_SKILL_DIR}`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_PROJECT_DIR}`, and in plugins `${CLAUDE_PLUGIN_ROOT}`/`${CLAUDE_PLUGIN_DATA}`. These also expand inside `allowed-tools` Bash rules, so a skill can run its bundled scripts without permission prompts.
  ([skills](https://code.claude.com/docs/en/skills), 2026-10)
- How the skill listing is trimmed:
  - The listing always keeps every skill *name*. When it exceeds its budget (default **1% of the context window**, set by `skillListingBudgetFraction`), it drops descriptions, starting with the least-used skills.
  - Each skill's `description` plus `when_to_use` is capped at **1,536 characters**.
  - `disable-model-invocation: true` removes a skill from the listing entirely.
  - After compaction, each re-attached skill keeps its first 5k tokens, within 25k in total.
  ([skills](https://code.claude.com/docs/en/skills), 2026-10)
- `context: fork` skills have run **in the background by default** since 2.1.218 (2026-07-22). Set `background: false` to wait for the result. A backgrounded fork gets the narrower background tool set and bypasses checkpoints, and a forked skill does not inherit conversation history. ([skills](https://code.claude.com/docs/en/skills), 2026-07)
- You may believe skills are only local files. Since 2.1.275 (2026-09-17), terminal sessions signed in with a claude.ai account **sync that account's skills and plugins**.
  - Synced skills download to `~/.claude/skills/synced/` and run as `/anthropic-skills:<name>`, or by short name when it's free. The names `synced` and `anthropic-skills` are reserved for this.
  - On a local machine, synced skill bodies don't run `!` commands or expand `@` files or `${CLAUDE_*}` variables.
  - Sessions using an API key or token, Bedrock, bare mode or `--safe-mode` don't sync. `syncClaudeAiSkills: false` and `syncClaudeAiPlugins: false` opt out.
  - Personal skills in `~/.claude/skills/` **don't load** in cloud sessions, Cowork or routines. Those load the account's skills, and cloud sessions also load the repo's `.claude/skills/`.
  ([skills](https://code.claude.com/docs/en/skills), [changelog](https://code.claude.com/docs/en/changelog), 2026-09)
- New housekeeping commands:
  - `/skill-doctor` (2.1.261) shows which skills go unused and what they cost in context.
  - `/doctor prompt-audit` (2.1.283) flags prompting patterns written for older models in CLAUDE.md, AGENTS.md, rules, skills, agents and commands.
  - A project or user skill named `verify` is run right before commits (2.1.285).
  ([changelog](https://code.claude.com/docs/en/changelog), 2026-09)
- claude.ai uploads, the Skills API and `package_skill.py` accept **only six frontmatter keys**: `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. Any other key is a hard error: "Unexpected key(s) in SKILL.md frontmatter".
  - The Skills API left beta on 2026-08-19, so the `skills-2025-10-02` header is no longer needed.
  - On claude.ai, skills live under Customize → Skills.
  - On Enterprise, from 2026-10-02 skill scanning is on by default, and publishing switched to "Requires review" unless an admin had chosen otherwise.
  ([skills](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code), [release notes](https://platform.claude.com/docs/en/release-notes/overview), [provisioning](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization), 2026-08/10)

**Subagents and orchestration**
- You may believe subagents are launched through the Task tool. As of v2.1.63 (2026-02-28) the tool is **`Agent`**, and rules written as `Task(...)` still work as aliases.
  - Its inputs are `description`, `prompt`, `subagent_type`, `model`, `run_in_background`, `name` and `isolation` (`"worktree"`).
  ([sub-agents](https://code.claude.com/docs/en/sub-agents), 2026-02)
- You may believe subagents can't spawn subagents. As of v2.1.219 (2026-07-24), **nesting is on by default, up to 3 levels** below the main conversation. `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` sets the limit, and `1` disables nesting. Agent-team teammates still can't spawn teammates. ([sub-agents](https://code.claude.com/docs/en/sub-agents), 2026-07)
- You may believe a subagent never sees the parent conversation. **Forks** do: they inherit the full conversation and its prompt cache.
  - Claude starts a fork with `subagent_type: "fork"`, and users start one with `/subtask`.
  - Forking has been on by default in interactive sessions since v2.1.232 (2026-08-13). It is off in `-p` and the SDK unless `CLAUDE_CODE_FORK_SUBAGENT=1`.
  ([sub-agents](https://code.claude.com/docs/en/sub-agents), [changelog](https://code.claude.com/docs/en/changelog), 2026-08)
- **Background subagents became the default** in v2.1.198 (2026-07-01). Their permission prompts surface in the main session.
  - At most 20 run at once (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, 2.1.217). The 200-per-session spawn cap was removed in 2.1.224.
  - Background subagents keep only a restricted set of built-in tools.
  - Every subagent loses `AskUserQuestion`, the plan-mode tools, `Workflow` and `ScheduleWakeup`, among others.
  ([sub-agents](https://code.claude.com/docs/en/sub-agents), [changelog](https://code.claude.com/docs/en/changelog), 2026-07/08)
- **Explore no longer runs on Haiku.** It inherits the session's model, capped at Opus.
  - The other built-in agents are now `claude`, `claude-code-guide`, `statusline-setup` and `fork`.
  - The `/agents` wizard was removed in 2.1.198. Create agents by asking Claude or by editing files.
  - Agent frontmatter adds `disallowedTools`, `maxTurns`, `mcpServers`, `memory`, `background`, `effort`, `isolation: worktree`, `omitClaudeMd` (2.1.271) and `initialPrompt`.
  ([sub-agents](https://code.claude.com/docs/en/sub-agents), 2026-10)
- You may believe a subagent's result reads like any other text. Since 2.1.277 (2026-09-18), results reach the parent under a header marking them as subagent output, so they can't pass as the session's own instructions.
  - In auto mode, a subagent reports back through a dedicated hand-back call that the classifier reviews (2.1.271).
  - `CLAUDE_CODE_SUBAGENT_MODEL` is now only a default: an agent definition's `model:` or a per-spawn model overrides it (2.1.251). `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` forces it on every subagent (2.1.257).
  ([changelog](https://code.claude.com/docs/en/changelog), 2026-09)
- **New since early 2026:**
  - **Workflows** (v2.1.154, 2026-05-28): the `Workflow` tool runs a JavaScript script that orchestrates many agents with `agent()`, `parallel()`, `pipeline()` and `phase()`. You opt in with the keyword **`ultracode`** or the Ultracode toggle in `/effort`, which has been a separate toggle since 2.1.284 and no longer forces xhigh effort. Each run asks for approval, Pro users must first enable workflows in `/config`, and `/deep-research` is bundled. ([workflows](https://code.claude.com/docs/en/workflows), 2026-10)
  - **`/goal`** (v2.1.139): an evaluator model keeps Claude working until a condition holds. It is a built-in, session-scoped prompt Stop hook. ([goal](https://code.claude.com/docs/en/goal))
  - **`/loop`** (2.1.71), backed by `CronCreate`/`CronList`/`CronDelete`. Its tasks are session-scoped and expire after 7 days. ([scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks))
  - **Routines** (still a research preview, since Apr 2026): cloud runs triggered by a schedule (at most hourly), an API call or a GitHub event. ([routines](https://code.claude.com/docs/en/routines))
  - **Agent view**: `claude --bg`, `claude agents`, and `claude attach <name>` / `claude logs <name>`.
  - **Cross-session messaging**: `ListAgents` plus `SendMessage` (2.1.224).

**Hooks**
- You may believe the default hook timeout is 60s. Since v2.1.3 (2026-01-09) it is **600s** for command, http and mcp_tool hooks. The exceptions:
  - UserPromptSubmit and model-switch events: 30s.
  - Prompt hooks: 30s. Agent hooks: 60s.
  - SessionEnd hooks: 1.5s. Raise it with a per-hook `timeout` or `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` (fixed in 2.1.268).
  ([hooks](https://code.claude.com/docs/en/hooks), 2026-10)
- There are **five handler types**: `command`, `http` (2.1.63), `mcp_tool` (2.1.118), `prompt` and `agent`. Agent hooks are still experimental, and since 2.1.280 they no longer run on PermissionRequest.
  - Handler fields include `args` (exec form, no shell), `shell`, `if` (a permission-rule filter such as `Bash(git *)`), `async`, `asyncRewake` and `once`. `once` is honoured only in skill frontmatter.
  - PostToolUse can rewrite any tool's output with `updatedToolOutput` (2.1.121).
  - New events since August: `PreModelSwitch` and `PostModelSwitch` can block or annotate a model switch (2.1.251).
  ([hooks](https://code.claude.com/docs/en/hooks), [changelog](https://code.claude.com/docs/en/changelog), 2026-10)
- **Matcher semantics changed.**
  - `*` or an empty matcher matches everything.
  - Matchers made only of letters, digits, `_`, `-`, spaces, `,` and `|` match exact names or lists.
  - Anything else is an unanchored JS regex, so `Edit.*` also matches `NotebookEdit`.
  - Since 2.1.195 (2026-06-26), hyphenated names match exactly: `mcp__brave-search` matches nothing, so write `mcp__brave-search__.*`.
  ([hooks](https://code.claude.com/docs/en/hooks), 2026-10)
- **Hooks are no longer snapshotted at startup.** Settings edits hot-reload, and `/hooks` is now a read-only browser.
  - JSON output is read on every exit code. Exit 2 always blocks, and exit 1 never does.
  - Stop hooks can force continuation at most 8 times in a row before the turn ends. The count resets whenever Claude calls a tool.
  ([hooks](https://code.claude.com/docs/en/hooks), 2026-10)
- You may believe hooks are the deepest extension point. Since 2.1.287 (2026-10-01), **mods** go further: they are plugins whose JavaScript or TypeScript event handlers run *inside* Claude Code. A plugin names the mod's code under `modules` in `hooks/hooks.json`.
  - Mods are **unsandboxed**. A mod can draw UI (panes, bands, the status line, toasts), rewrite prompts and tool calls, submit prompts, message your other sessions, call models on your plan, and approve tool calls.
  - A mod's `tool.check` can override ask rules, non-managed PreToolUse blocks and the auto-mode classifier. On machines without managed settings or a Team/Enterprise sign-in, it can override **deny rules** too.
  - Admins can restrict mods with `allowManagedModsOnly`, and `disableAllHooks` stops installed mods along with settings hooks. Built-in mods (`/diff`, telemetry, and the opt-in "You should know" side agent) survive `--bare` and `--safe-mode`.
  - Settings hooks are not deprecated. The docs still point to them for blocking, allowing or logging an event with a script.
  ([mods](https://code.claude.com/docs/en/plugins/mods/overview), [permissions](https://code.claude.com/docs/en/permissions), [changelog](https://code.claude.com/docs/en/changelog), 2026-10)

**Plugins and distribution**
- You may believe plugins are a public beta with a required `plugin.json`. Plugins are no longer labelled beta, and the manifest (`.claude-plugin/plugin.json`) is optional. Without one, the name comes from the marketplace entry or the directory.
  - Components today: skills, agents, hooks, MCP servers (including `.mcpb`), LSP servers, output styles, themes and monitors (both experimental), channels, a `bin/` folder (added to Bash's PATH), `settings.json`, workflows, `userConfig` and mods.
  ([manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference), 2026-10)
- **Installing.**
  - Inside a session, `/plugin install` opens a details pane (contents, estimated context cost, scope) instead of installing straight away. `/plugin directory` browses Anthropic's directory (2.1.287).
  - One command adds the marketplace and installs: `/plugin install <name> --marketplace <source>` (2.1.275, 2026-09-17).
  - Shell CLI: `claude plugin install|uninstall|enable|disable|update|list|details|configure|prune|init|tag|validate|eval|test` and `claude plugin marketplace add|list|update|remove`. `eval` runs a plugin's eval suite (2.1.269).
  ([install](https://code.claude.com/docs/en/plugins/install), [CLI reference](https://code.claude.com/docs/en/plugins/cli-reference), 2026-10)
- **Sources got safer.**
  - `archive` sources install a zip over HTTPS with optional SHA-256 pinning (2.1.224).
  - npm sources are fetched with `npm pack --ignore-scripts` and integrity-checked, so install scripts don't run (2.1.275). npm sources that are git repos or folders are refused (2.1.286).
  - Marketplaces can be hosted on GitLab (2.1.232).
  ([changelog](https://code.claude.com/docs/en/changelog), 2026-09)
- **Versions and updates.**
  - Version precedence: `plugin.json` `version`, then the marketplace entry's `version`, then the commit SHA. A set `version` keeps users on it until it is bumped.
  - Auto-update is on by default for Anthropic's official marketplaces and off for third-party ones.
  - Dependencies use semver ranges against `<name>--v<ver>` git tags.
  - `${CLAUDE_PLUGIN_DATA}` (`~/.claude/plugins/data/<id>/`) persists across updates.
  ([loading](https://code.claude.com/docs/en/plugins/loading), [dependencies](https://code.claude.com/docs/en/plugins/dependencies), 2026-09)
- **The same plugin loads differently on each surface.**
  - claude.ai chat loads only skills and commands, and lists remote MCP servers on the plugin's Connectors tab.
  - Cowork also loads agents, hooks and local MCP servers.
  - claude.ai and Cowork refuse plugins with a top-level `bin/`. LSP servers, output styles, themes and `settings` load only in Claude Code.
  - Cloud sessions have no `/plugin` panel and don't load user-scope or repo-declared plugins. They do load server-managed plugins and claude.ai-synced ones.
  ([platform support](https://claude.com/docs/plugins/platform-support), [cloud environments](https://code.claude.com/docs/en/cloud-environments), 2026-10)
- **Anthropic's marketplaces.**
  - `claude-plugins-official` is added automatically on first interactive start.
  - The community catalog comes from `anthropics/claude-plugins-community` but is **named `claude-community`**, so you install `<plugin>@claude-community`. Its third-party plugins are nearly all pinned to a commit SHA.
  - `anthropics/claude-code` is only a demo marketplace, named `claude-code-plugins`.
  - Anthropic's directory, the catalog on claude.ai, is separate; its plugins reach Claude Code through account sync. Its submission portal opened 2026-09-25, with automated validation, a security scan and human review.
  - claude.com/marketplace ("2,000+ connectors and plugins") launched 2026-09-23.
  - Anthropic doesn't review third-party marketplaces. Since 2.1.280, a marketplace whose name imitates a reserved one is refused.
  ([Anthropic marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces), [directory](https://claude.com/docs/directory/publish), [gHacks](https://www.ghacks.net/2026/09/27/anthropic-launches-claude-marketplace-with-more-than-2000-connectors-and-plugins/), 2026-09/10)

**MCP**
- You may believe the latest MCP spec is 2025-11-25. The current revision is **2026-07-28**, the "stateless" revision, which Willison calls "MCP 2.0". What changed:
  - There is no `initialize` handshake and no `ping`. Version and capabilities travel in each request's `_meta`, and servers implement `server/discover`.
  - `subscriptions/listen` replaces the GET stream and `resources/subscribe`.
  - Multi Round-Trip Requests (`resultType: "input_required"`) replace server-initiated sampling, elicitation and roots requests.
  - Tasks moved out of the core into an extension.
  - Roots, Sampling and Logging are deprecated, and Dynamic Client Registration is deprecated in favour of Client ID Metadata Documents. Deprecations now carry a minimum 12-month window.
  - Streamable HTTP has no sessions or `Mcp-Session-Id`.
  ([spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog), 2026-07)
- Claude Code's v2 MCP client negotiates 2026-07-28 by default, on Bedrock, Vertex, Foundry and telemetry-off installs too since 2.1.274, including URL-mode elicitation (2.1.281). ([changelog](https://code.claude.com/docs/en/changelog), 2026-09)
- You may believe Tool Search defers MCP tools once they would take about 10% of context. **It now defers all MCP tools by default**: only tool names and server instructions load at start.
  - The 10% behaviour is opt-in with `ENABLE_TOOL_SEARCH=auto` or `auto:N`.
  - Tool Search switches off by itself when `ANTHROPIC_BASE_URL` points at a non-first-party host, so proxied setups load every tool up front unless `ENABLE_TOOL_SEARCH` is set explicitly.
  - Exempt a server with `alwaysLoad`, or a tool with `_meta["anthropic/alwaysLoad"]`.
  - Tool descriptions and server instructions are capped at 2,048 characters. `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` changes the cap (2.1.280).
  ([MCP](https://code.claude.com/docs/en/mcp), 2026-10)
- The MCP **Skills extension** (SEP-2640, `io.modelcontextprotocol/skills`) went Final on 2026-09-13. Servers expose skills as `skill://` resources, read with `skills/list` and `skills/get`. ([SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension), 2026-09)

**Memory and the wider ecosystem**
- You may believe Claude Code ignores AGENTS.md. Since 2.1.277 (2026-09-18), it reads `AGENTS.md` when the working directory and the directories above it hold no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md`.
  - `~/.claude/CLAUDE.md`, a managed CLAUDE.md and `.claude/rules/` don't count toward that check, and they load alongside AGENTS.md.
  - Choose what loads with **Project instructions** in `/config`. For example, `claude-md-and-agents-md` reads both.
  - `AGENTS.local.md`, `AGENTS.override.md` and `.agents/` are never read.
  ([memory](https://code.claude.com/docs/en/memory), 2026-10)
- Auto memory is notes Claude writes itself. Their first 200 lines or 25KB load every session, and subagents can keep their own (`memory:` frontmatter). ([memory](https://code.claude.com/docs/en/memory), 2026-10)
- **Agent Plugins 1.0.0** (2026-08-06) is a cross-vendor plugin packaging standard: a root `plugin.json`, `skills/` in the Agent Skills format, and `mcp.json`.
  - It comes from Amazon, Cursor, GitHub, Microsoft, OpenAI and Vercel, with Google as a core maintainer. Anthropic isn't a party.
  - Claude Code's own layout (`.claude-plugin/plugin.json`, `.mcp.json`) differs.
  - It is still a working draft covering packaging only, with no marketplace, permission or provenance rules.
  ([agent-plugins.org](https://agent-plugins.org/specification), 2026-08; secondary coverage disagrees on the co-author list)

## What an expert knows

**Choosing the mechanism** (Anthropic's 2026 guidance)
- Keep CLAUDE.md under about 200 lines, owned and reviewed like code. Put file-specific guidance in path-scoped `.claude/rules/`.
- Put procedures in skills: only descriptions load each session.
- Put guarantees in hooks. An instruction is "a request, not a guarantee."
- Use subagents for side tasks that would flood the main context.
- Use MCP when credentials should stay out of the agent's context, or when access must be governed.
- Use a mod only when you need UI or need to rewrite events inside Claude Code. It runs unsandboxed with your permissions.
- `/context` shows what costs tokens, and `/skill-doctor` shows what to prune.

([steering post](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more), [features overview](https://code.claude.com/docs/en/features-overview), [mods](https://code.claude.com/docs/en/plugins/mods/overview), 2026-06/10)

**Hook pitfalls**
- **Exit 1 doesn't block.** Only exit 2, or a JSON decision, blocks.
- **A broken guard disables itself silently.** A missing script or wrong path is a non-blocking error.
- **Unexpected stdout breaks JSON output.** A profile `echo` before the JSON turns the output into plain text, and misplaced fields are silently ignored.
- **One bad entry can drop the whole file's hooks.** An array matcher under PreToolUse or PermissionRequest does this.
- **Edit-matching hooks miss shell writes.** A PostToolUse `Edit|Write` matcher misses edits made through Bash, and `@`-file references bypass PreToolUse Read hooks.
- **Hooks don't stack predictably.** With several `updatedInput` hooks, the last to finish wins, and one hook's deny doesn't stop its siblings.
- **A mod can overrule your hooks.** An installed mod's `tool.check` answers after your PreToolUse hooks and can approve what they blocked, unless the hook is managed.
- **Contested: whether tool hooks fire inside subagents.** The docs (2026-10) say settings, managed and plugin hooks fire for subagent tool calls, with `agent_id` in the input. Issue #34692 (Mar 2026) reported that they don't and was closed "not planned". If a guard matters, test both paths.

([hooks](https://code.claude.com/docs/en/hooks), [hooks guide](https://code.claude.com/docs/en/hooks-guide), [debug config](https://code.claude.com/docs/en/debug-your-config), 2026-08/10)

**Skill and instruction pitfalls**
- **Typos fail quietly.** A frontmatter typo is silently ignored. Malformed YAML (an unquoted colon, a block scalar) loads the body with no metadata, so the skill never auto-triggers.
- **Too many skills hide descriptions.** Once over the listing budget, descriptions disappear and triggering degrades.
- **A forked reference skill returns nothing.** `context: fork` on a skill without an actionable task does nothing useful.
- **Compaction truncates skills.** After compaction only the first 5k tokens of a skill survive. Put critical rules at the top, and re-invoke the skill if Claude stops following it.
- **`allowed-tools` only pre-approves.** It approves tools for the invoking turn only, restricts nothing, and is **not gated by workspace trust**. The exception is the managed setting `allowManagedPermissionRulesOnly`: then only skills and plugins from official Anthropic or admin-approved sources can pre-approve (2.1.282, 2.1.284).
- **A `CLAUDE.local.md` silently turns off AGENTS.md.** It counts as a CLAUDE.md, so set Project instructions to `claude-md-and-agents-md` to keep both.

**Plugin pitfalls**
- **A pinned `version` freezes updates** until it is bumped. If `version` is set in both `plugin.json` and the marketplace entry, `plugin.json` wins without warning.
- **Components inside `.claude-plugin/` don't load.** Only the manifest goes there.
- **Relative `../` paths break** once the plugin is copied to the cache. `${CLAUDE_PLUGIN_ROOT}` changes with every version, so keep state in `${CLAUDE_PLUGIN_DATA}`.
- **Plugin subagents ignore `hooks`, `mcpServers` and `permissionMode`** in their frontmatter, for security. To use them, copy the agent file into `.claude/agents/`.

([sub-agents](https://code.claude.com/docs/en/sub-agents), [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference), 2026-10)

**Trust gaps**
- **Headless runs skip the trust dialog.**
  - In a folder never trusted, `claude -p` and SDK sessions still run the repo's settings hooks, `env` block, `apiKeyHelper`, and project-skill hooks and `allowed-tools`.
  - They also connect `.mcp.json` servers without asking; the SDK does so only when `settingSources` includes project.
  - They ignore the repo's `permissions.allow` rules, subagent-frontmatter hooks, inline MCP servers and `headersHelper`.
  - For untrusted repos, use `--bare` or `--setting-sources user`.
- **Trusting a parent folder is enough** to run a subfolder's settings hooks and skill `allowed-tools` without a new dialog, except inside a nested repository.
- **Project skills aren't trust-gated.** Workspace trust never gates a skill's `allowed-tools`.

([permissions](https://code.claude.com/docs/en/permissions), [headless](https://code.claude.com/docs/en/headless), 2026-10)

**Auto mode, as specified by Anthropic** ([engineering post](https://www.anthropic.com/engineering/claude-code-auto-mode), 2026-03; [blog](https://claude.com/blog/auto-mode-default-in-claude-code), 2026-08)
- **How it works:** a two-stage classifier. A fast filter runs first, then chain-of-thought review only for flagged actions. It sees user messages and tool calls, not Claude's own text or tool outputs.
- **Error rates:** 0.4% false positives on real traffic, and a **17% miss rate on real overeager actions** (March). Apollo Research measured the adversarial miss rate falling from 12% to 7% (August).
- **Fallback:** after 3 consecutive or 20 total blocks it falls back to prompting.
- **Lost boundaries:** limits you state in chat ("don't push") can be lost when the conversation is compacted.
- **Cost:** API, Enterprise and cloud-provider users default to a server-side classifier that doesn't bill classifier overhead (2.1.278).

**Contested: how safe auto mode is**
- **Verdict: treat it as a convenience, not a security boundary.** Anthropic agrees, calling auto mode "a convenience feature backed by a best-effort classifier, not a security guarantee." It puts the real boundary at OS isolation and network egress, so pair auto mode with a sandbox or container when Claude reads untrusted content.
- **Anthropic's numbers:** in a study of 1,053 testers, auto mode blocked 89% of planted dangerous commands, while humans caught 13.6% and approve 97% of prompts. Anthropic gains from this framing.
- **Dissent:**
  - Johann Rehberger (2026-08-26) turned "summarise this page" into running attacker code in 60–80% of attempts against Opus 5 in auto mode. The chain ran from an HTTP 415, to curl, to a ZIP, to a shadowed `struct.py`. Anthropic called it working as designed. ([Embrace The Red](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/), 2026-08)
  - A red-team paper had a misaligned agent inject its way past auto mode in 79% of trials. It also found unmonitored channels, including malicious compaction and multi-agent handoffs. ([arXiv 2609.19587](https://arxiv.org/abs/2609.19587), 2026-09)
- **Related hardening in September:** subagent hand-backs are now classifier-reviewed (2.1.271), and subagent and workflow text is framed so it can't pass as the user (2.1.277).

([sandboxing](https://code.claude.com/docs/en/sandboxing), 2026-10)

**Multi-agent work**
- **Agent teams cost about 7× the tokens.** Use 3–5 teammates and never split work on the same file ([costs](https://code.claude.com/docs/en/costs)).
- **Keep writes single-threaded.** Extra agents work best reviewing or advising (Cognition, 2026-04). An evaluator agent helps on hard tasks but is overhead on easy ones ([harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps), 2026-03).
- **Workflows are not for routine use.** They need an explicit opt-in (`ultracode`) because they can spawn dozens of agents.

**Security record**

There is still no publisher signing for plugins, skills, mods or MCP servers: none appears in the changelog through 2.1.291. Trust rests on:
- reserved marketplace names, which must come from github.com/anthropics; imitations are refused
- commit-SHA pins in the community catalog, optional sha256 pins on archive sources, and npm integrity checks
- the directory's scan and review

Pins are only as good as their verification: Plugin4Shell (below) bypassed them until 2.1.179. The docs say a plugin runs arbitrary code with your user privileges ([plugin security](https://code.claude.com/docs/en/plugins/security), 2026-10).

Incidents of 2026:
- **Feb, Snyk ToxicSkills:** 36.8% of 3,984 community skills had a security flaw; 76 were malicious.
- **Feb, Clinejection:** a prompt injection in a GitHub issue title hijacked a bot running `claude-code-action` with Bash allowed. The stolen token published a malicious `cline` release.
- **Feb 25, Check Point CVE-2025-59536 and CVE-2026-21852:** repo hooks and `.mcp.json` ran before the trust dialog, and a repo-set `ANTHROPIC_BASE_URL` leaked API keys.
- **CVE-2026-47751:** `claude-code-action` loaded a pull request's `.mcp.json`. Sources disagree on the date and the fix version (1.0.74 per GHSA, 1.0.78 per Tenable), so treat ≥1.0.78 as safe.
- **Mar 31, source leak:** a v2.1.88 npm source map exposed the full source. Anthropic called it human error.
- **Jun 3, Miasma worm:** it planted `.claude/settings.json` SessionStart hooks (and Gemini CLI, Cursor and VS Code equivalents) across repositories. GitHub disabled 73 Microsoft repositories on Jun 5.
- **Disclosed Sep 2, GitSpawn (Manifold Security):**
  - A repo delivered as files rather than cloned (an archive, a shared drive) can carry a `.git/config` whose `core.fsmonitor` runs when an agent calls `git status`. In Claude Code that ran before the trust prompt.
  - Claude Code fixed that path in 2.1.196 without an advisory. Manifold says a second path, via `claude ultrareview`, was still open in 2.1.252.
  - Codex, goose, Cursor and others were also affected.
- **Sep 17, Plugin4Shell (Air):** agents checked out a marketplace-pinned commit without verifying it actually landed, so whoever controlled a plugin repo could swap code under a valid-looking pin. Auto-update made the attack zero-click. It was fixed in Claude Code 2.1.179 and Codex 0.146.0.

Sources: [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), [Snyk Cline](https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions/), [Check Point](https://blog.checkpoint.com/research/check-point-researchers-expose-critical-claude-code-flaws/), [GHSA](https://github.com/advisories/GHSA-8q5r-mmjf-575q), [StepSecurity](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents), [The Hacker News](https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html), [The Register](https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335).

**Live debates**
- **MCP vs CLI plus skills.**
  - Verdict: they are complementary. MCP's lasting value is keeping credentials out of the agent's context, plus governed, auditable access. The stateless 2026-07-28 spec answered much of the complexity criticism.
  - Dissent: "MCP was always a bad idea?" (Maharshi Patel; HN about 2026-09-21, 335 points, 331 comments) argues that CLIs plus skills are leaner and avoid the context tax. simonw replied in the thread with MCP's case for control, credential isolation and audit logs.
  - Willison (2026-07-31) says scripts replaced most of his MCP use with coding agents, but MCP still helps reach secure resources in a controlled way.
  - MCP itself absorbed skills: SEP-2640 is Final.
  ([HN](https://news.ycombinator.com/item?id=49779329), [Willison](https://simonwillison.net/2026/Jul/31/stateless-mcp/), 2026-07/09)
- **Auto mode as the default.** Anthropic staff say "almost every single person uses auto mode" internally (Cat Wu). Security researchers want sandboxes instead; see the auto-mode debate above.
- **Packaging fragmentation.** Agent Plugins 1.0 is a cross-vendor plugin format that Anthropic hasn't joined, while Claude Code keeps its own `.claude-plugin/` layout. Skill and plugin stores are being called "the new npm".
- **Direction of travel.** The team cut Claude Code's system prompt by about 80% and is "trend[ing] towards fewer tools" (Thariq Shihipar, via [Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/), 2026-07). Mods move customisation into the harness itself; Willison reports that AGENTS.md support is built on mods.

**People**
- Boris Cherny: Head of Claude Code. Cat Wu: Head of Product. Thariq Shihipar: technical staff.
- David Soria Parra and Den Delimarsky: MCP lead maintainers. MCP has been under the Linux Foundation's Agentic AI Foundation since 2025-12-09.
- Simon Willison: the leading practitioner-skeptic.
- Johann Rehberger (Embrace The Red): agent-security research, including the 2026-08 auto-mode break.

## Unknown
- **MCP skills in Claude Code.** As of 2026-10-06, Claude Code's docs and changelog don't say whether it consumes SEP-2640 skill servers. Watch the changelog, or ask the Skills Over MCP Working Group (`modelcontextprotocol/ext-skills`).
- **Agent Plugins adoption.** As of 2026-10-06, there is no Anthropic statement on supporting Agent Plugins 1.0 or a root `plugin.json`.
- **GitSpawn's second path.** As of 2026-10-06, it is unclear whether the `claude ultrareview` path that Manifold reported open at 2.1.252 is fixed, and no Anthropic advisory was found.
- **Mods' security posture.** Mods launched 2026-10-01. As of 2026-10-06 there is no independent security review, and it is unknown whether the directory's scan analyses mod code.
- **Hooks in subagents.** As of 2026-10-06, issue #34692 has not been re-tested against current versions; the docs say hooks fire.
- **Shaky claims.**
  - The "26,000 agents" and "SkillJacking" figures come from aggregator sites without primary sources.
  - Reports that Google replaced Gemini CLI with a closed-source Antigravity CLI (May–June 2026) remain secondary. The Register (2026-09-17) says Google has deprecated Gemini CLI.

## Sources
- [Claude Code changelog](https://code.claude.com/docs/en/changelog): the version-by-version truth; read it first for anything time-sensitive.
  - The page is about 970K characters, and fetch-and-summarise tools miss or misdate entries.
  - Grep the raw [`changelog.md`](https://code.claude.com/docs/en/changelog.md) instead. Appending `.md` works on any docs page.
- Claude Code docs:
  - [skills](https://code.claude.com/docs/en/skills)
  - [hooks](https://code.claude.com/docs/en/hooks)
  - [sub-agents](https://code.claude.com/docs/en/sub-agents)
  - [permissions](https://code.claude.com/docs/en/permissions) and [permission modes](https://code.claude.com/docs/en/permission-modes)
  - [MCP](https://code.claude.com/docs/en/mcp)
  - [memory](https://code.claude.com/docs/en/memory)
  - [plugins](https://code.claude.com/docs/en/plugins/overview), including the manifest, loading, CLI and [Anthropic marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces) references
  - [mods](https://code.claude.com/docs/en/plugins/mods/overview)
  - [workflows](https://code.claude.com/docs/en/workflows)
  - [cloud environments](https://code.claude.com/docs/en/cloud-environments)
  - the full index is at [llms.txt](https://code.claude.com/docs/llms.txt)
- [Plugin platform support](https://claude.com/docs/plugins/platform-support): which components load in chat, Cowork and Claude Code.
- [MCP spec 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog), [roadmap](https://modelcontextprotocol.io/development/roadmap) and [SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension): protocol truth.
- [Anthropic engineering](https://www.anthropic.com/engineering): the auto mode and harness-design posts give design rationale and numbers. Anthropic is an interested party.
- [Simon Willison's blog](https://simonwillison.net): the best running practitioner commentary and security skepticism.
- [Embrace The Red](https://embracethered.com): Rehberger's reproducible agent exploits.
- [agentskills.io](https://agentskills.io/specification) and [agent-plugins.org](https://agent-plugins.org/specification): the cross-vendor skill and plugin specs.
- **Skip:**
  - SEO "Claude Code hooks guide" posts: several still teach pre-2026 exit-code semantics and say PermissionRequest blocks on exit 2.
  - The Help Center "create custom skills" page: it still says descriptions max 200 characters and lists a `dependencies` field that uploads reject.
  - Aggregator security figures without primary sources.
  - Blog coverage of Agent Plugins 1.0: the co-author lists disagree, so use agent-plugins.org.

## Log
- 2026-08-01: built.
- 2026-10-06: refreshed against the raw changelog (2.1.221–2.1.291), current docs and the web.
  - Added:
    - the mods launch (2.1.287) and AGENTS.md support (2.1.277)
    - claude.ai skill and plugin sync, and plugin supply-chain hardening
    - `/skill-doctor`, `/doctor prompt-audit`, and `PreModelSwitch`/`PostModelSwitch`
    - subagent-output framing, and Ultracode becoming its own toggle
    - Tool Search's proxy behaviour
    - MCP's Skills extension going Final, and Agent Plugins 1.0
    - GitSpawn and Plugin4Shell, and the auto-mode dissent (Rehberger, arXiv 2609.19587)
  - Corrected:
    - the auto mode every-plan default (2.1.283 per the docs, 2.1.284 per the changelog), plus the `-p` and SDK starting mode
    - the community marketplace's name (`claude-community`)
    - headless trust: `-p` ignores repo allow rules
    - the spawn-cap removal, now dated (2.1.224)
  - Repaired: the saved file said it was verified 2026-08-01 but held claims through 2026-10-02. It had lost the lead-in bullets for synced skills, mods and platform support, left the memory section empty, and gave only one side of the auto-mode debate.
