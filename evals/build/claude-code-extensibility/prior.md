# Prior: Claude Code extensibility (skills, plugins, hooks, subagents, MCP)

_Written by a fresh agent with no tools on 2026-10-06, as step 1 of the skill. Training-only beliefs. Its self-reported recall is detailed through about Jan 2026, thin for Feb–Jun 2026, and empty after that._

## Product context, timeline, people
- [high] Claude Code is Anthropic's agentic coding harness. It launched as a research preview on Feb 24 2025 (with Claude 3.7 Sonnet), went GA on May 22 2025 (with Claude 4), and later spread to IDE extensions, the web (claude.ai/code, Oct 2025), desktop and Slack (as of late 2025)
- [high] Claude Code 2.0 shipped Sept 29 2025 with Sonnet 4.5 (checkpoints/`/rewind`, native VS Code extension). The Claude Code SDK was renamed the Claude Agent SDK at the same time (as of Sept 2025)
- [medium] The 2.1.x line (from about early Jan 2026) focused on extensibility: skill hot-reload, `context: fork` for skills, hooks declared in skill and agent frontmatter, skills listed in the `/` menu, `*` wildcards in Bash permission rules, and MCP `list_changed` support (as of Jan 2026)
- [medium] Other Anthropic surfaces use the same skills and plugins formats. Cowork (an agentic desktop app for non-coding work, research preview Jan 2026) got plugins in late Jan 2026 (legal, finance, sales…) (as of Feb 2026)
- [medium] People who matter: Boris Cherny (creator/lead) and Cat Wu (product) on Claude Code; Thariq Shihipar (Agent SDK and features); David Soria Parra and Justin Spahr-Summers (MCP co-creators); Barry Zhang and Mahesh Murag (Agent Skills). Outside voices: Simon Willison, Geoffrey Huntley (Ralph loop), Jesse Vincent (obra/superpowers) (as of early 2026)

## Base layer: memory, settings, permissions
- [high] CLAUDE.md loads in layers (enterprise policy, `~/.claude/CLAUDE.md`, project `./CLAUDE.md`, parent directories, and nested subdirectory files when needed). It supports `@path` imports, stays in context all the time, and is advice to the model, not an enforced rule (as of late 2025)
- [medium] `.claude/rules/*.md` holds separate rule files, which can be limited to certain paths with `paths:` glob frontmatter (as of about Dec 2025)
- [high] settings.json precedence runs managed policy > CLI flags > `.claude/settings.local.json` > `.claude/settings.json` > `~/.claude/settings.json` (as of late 2025)
- [high] Permission rules are `Tool(specifier)` strings in allow/ask/deny lists. Deny beats allow. The modes are default, acceptEdits, plan and bypassPermissions (as of late 2025)
- [medium] Optional OS-level Bash sandboxing (bubblewrap on Linux, Seatbelt on macOS) arrived in Oct 2025 via `/sandbox` (as of Oct 2025)
- [medium] Enterprises control extensions through managed settings: `allowManagedHooksOnly`, `strictKnownMarketplaces`, MCP allow/deny lists plus `managed-mcp.json` (as of late 2025)

## Slash commands and Agent Skills
- [high] Custom slash commands are Markdown files in `.claude/commands/`, with frontmatter fields `description`, `argument-hint`, `allowed-tools`, `model` and `disable-model-invocation`; they support `$ARGUMENTS` and `!` bash lines (as of 2025)
- [high] Agent Skills launched Oct 16 2025 across claude.ai, Claude Code, the API and the Agent SDK. A skill is a folder with `SKILL.md` (`name` of up to 64 characters, `description` of up to 1024) plus optional scripts, references and assets (as of Oct 2025)
- [high] Skills rely on progressive disclosure: only the name and description stay in context; the body loads when it's relevant (as of late 2025)
- [high] Skills load from `~/.claude/skills/`, `.claude/skills/` and plugins. The model invokes them through the Skill tool, and `allowed-tools` is a field only Claude Code supports (as of late 2025)
- [medium] Slash commands and skills were merged in early 2026; `user-invocable: false` and `disable-model-invocation: true` control who can trigger a skill (as of Jan 2026)
- [medium] Agent Skills became an open standard (agentskills.io) around Dec 2025, adopted by Codex, Copilot, Cursor and others (as of Jan 2026)
- [medium] Anthropic ships document skills (docx, xlsx, pptx, pdf) and a `skill-creator` skill (as of Dec 2025)

## Subagents and multi-agent
- [high] Subagents are Markdown+YAML files in `.claude/agents/` (`name`, `description`, `tools`, `model`), launched through the Task tool. Each gets a fresh context and returns only its final message (as of late 2025)
- [high] Subagents cannot spawn their own subagents and never see the parent conversation (as of late 2025)
- [medium] The built-in subagents are general-purpose, Explore and Plan; newer frontmatter adds `permissionMode`, `skills` and `hooks`; subagents can run in the background (as of Jan 2026)
- [medium] "Agent teams" arrived as an experimental feature (about Feb 2026): teammates coordinate through a shared task list (as of Feb 2026)

## Hooks
- [high] Hooks live in settings.json under `hooks` → event → `[{matcher, hooks:[{type:"command", command, timeout}]}]`. Plugins ship hooks in `hooks/hooks.json` (as of late 2025)
- [medium] Events: PreToolUse, PostToolUse, UserPromptSubmit, Notification, Stop, SubagentStop, PreCompact, SessionStart, SessionEnd, PermissionRequest, SubagentStart (as of Jan 2026)
- [high] I/O: JSON on stdin; exit 2 blocks the action and passes stderr to Claude; the default timeout is 60s (as of late 2025)
- [high] PreToolUse returns `hookSpecificOutput.permissionDecision`; a Stop hook returning `decision:"block"` keeps Claude working (as of late 2025)
- [medium] Later additions: `updatedInput`, `type:"prompt"` hooks, `CLAUDE_ENV_FILE`, and hooks scoped to a skill's or subagent's frontmatter (as of Jan 2026)

## MCP
- [high] Open-sourced Nov 2024. Transports are stdio and Streamable HTTP; SSE is deprecated (as of 2025)
- [medium] Spec revisions: 2025-03-26, 2025-06-18, 2025-11-25 (Tasks, URL elicitation…); a 2026 revision is likely (as of Dec 2025)
- [medium] MCP was donated to the Linux Foundation's Agentic AI Foundation in Dec 2025; the MCP Registry is in preview; MCP Apps is the first official extension (as of Jan 2026)
- [high] `claude mcp add --transport … --scope local|project|user`; `.mcp.json` for the project scope; `/mcp` shows status and handles OAuth (as of late 2025)
- [medium] MCP Tool Search defers tools once they would take about 10% of context (as of Jan 2026)

## Plugins and marketplaces
- [high] Plugins (public beta Oct 2025) bundle commands, agents, skills, hooks and MCP servers; marketplaces are repos with `.claude-plugin/marketplace.json`; install with `/plugin install name@marketplace` (as of late 2025)
- [medium] Layout: `.claude-plugin/plugin.json` plus component folders at the plugin root; paths use `${CLAUDE_PLUGIN_ROOT}`; commands are namespaced `/plugin:cmd` (as of late 2025)
- [medium] Official marketplace `anthropics/claude-plugins-official` (as of Dec 2025)
- [medium] Plugins can ship LSP server configs (as of Dec 2025)

## Agent SDK and headless
- [high] The Claude Agent SDK is the Claude Code harness as a library; since 0.1.0 it loads no filesystem config unless asked via `settingSources` (as of Oct 2025)
- [high] Headless `claude -p` powers CI and `claude-code-action` (as of late 2025)

## Debates
- [medium] MCP vs CLIs plus skills (context cost vs governance and auth) (as of early 2026)
- [medium] Portability: AGENTS.md vs CLAUDE.md (as of early 2026)
- [medium] Supply chain: tool poisoning, malicious servers and skills; no common signing (as of Feb 2026)

## Most likely outdated
Version numbers and models; the hook events and types; how commands and skills relate; subagent mechanics (Task tool name, nesting, teams); MCP spec version and feature support; the plugin system (directory, CLI, controls, new components); permission modes; SDK API; AGENTS.md handling; docs URLs.

## Known unknowns
What shipped Feb–Oct 2026; deprecations; current hook events and types; MCP feature support; Agent Skills governance; plugin and skill trust and signing; concrete limits (description budget, subagent caps); agent teams; enterprise controls. Vague memories to check: an "auto" permission mode with a classifier; the Task tool renamed "Agent"; hook events Setup, PostToolUseFailure, TeammateIdle, TaskCompleted.
