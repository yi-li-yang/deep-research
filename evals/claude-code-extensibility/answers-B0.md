## Q1
Your agent files (Markdown with YAML frontmatter in `.claude/agents/` or `~/.claude/agents/`) still load, but almost everything around them has changed ([sub-agents](https://code.claude.com/docs/en/sub-agents)).

**Creating and managing them**
- The `/agents` wizard was removed in 2.1.198 (2026-07-01). Edit the files directly, or ask Claude to write or change an agent.
- New frontmatter fields: `disallowedTools`, `maxTurns`, `mcpServers` (servers scoped to the agent), `memory`, `background`, `effort`, `isolation: worktree`, `omitClaudeMd` and `initialPrompt`.
- The Task tool is now **`Agent`** (v2.1.63, 2026-02-28). Its inputs now include `model`, `run_in_background`, `name` and `isolation: "worktree"`. Old `Task(...)` permission rules still work as aliases, and there are new rule forms `Agent(Name)` and `Agent(model:opus)` ([permissions](https://code.claude.com/docs/en/permissions)).
- Background sessions have their own agent view: `claude --bg`, `claude agents` and `claude attach`.

**How they behave**
- **Subagents run in the background by default** (2.1.198). Claude keeps working while they run, and their permission prompts appear in your main session. Up to 20 can run at once (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`). Background agents get a restricted set of built-in tools. Every subagent also loses `AskUserQuestion`, the plan-mode tools, `Workflow` and `ScheduleWakeup`, so an agent that used to ask you questions can't anymore. The new `background` field sets this per agent.
- **Nesting** (2.1.219): subagents can spawn their own subagents, up to 3 levels deep. `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` turns this off.
- **Forks** (on by default in interactive sessions since 2.1.232): a fork, started by Claude with `subagent_type: "fork"` or by you with `/subtask`, inherits the full conversation and its prompt cache. Your custom agents still start fresh.
- **Explore no longer runs on Haiku.** It now uses your session model (capped at Opus), which makes it smarter and more expensive. New built-in agents: `claude`, `claude-code-guide`, `statusline-setup` and `fork`.
- **Claude delegates less on its own.** Opus 5 delegates more readily than earlier models, so Claude Code's `claude_code` prompt tells it not to call Agent unless asked ([Opus 5 guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)). If your agents relied on "use proactively" descriptions, name them in your request.
- If you turn on agent teams (still experimental), any *named* Agent call launches a teammate instead of a subagent ([agent teams](https://code.claude.com/docs/en/agent-teams)).

**Checklist for your existing agents**
- Rewrite `Task(` rules as `Agent(`.
- Confirm each agent's `tools` still work under the background restrictions.
- Review `model`: agents set to inherit now run on Opus by default on Pro and Team Standard too (since 2.1.280).
- Re-test any hook-based guardrails inside subagents. The docs say tool hooks fire there, but issue #34692 reported that they don't and was closed "not planned".

## Q2
Give each skill its own folder: `.claude/skills/<name>/SKILL.md`, committed to the repo or shipped in a plugin, with scripts and reference files beside it. Repo skills also load in cloud sessions; `~/.claude/skills/` doesn't. Every skill is also a `/name` command, so you don't need separate command files (`.claude/commands/` is the legacy form).

```markdown
---
name: db-migration
description: "Creates and checks DB migrations. Use when the user adds or changes a table, column or index, or mentions a migration."
argument-hint: "[migration-name]"
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/check.sh *)
---
Critical rules first. Then the procedure, e.g. run
`${CLAUDE_SKILL_DIR}/scripts/check.sh $ARGUMENTS`.
```

**Frontmatter Claude Code supports** ([skills](https://code.claude.com/docs/en/skills)): `name`, `description`, `when_to_use`, `argument-hint`, `arguments` (named `$name` arguments), `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context` (`fork` runs the skill in a subagent, in the background by default, without your conversation history), `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license` and `compatibility`. In Claude Code, `name` (defaults to the folder name) and `description` are optional. Write a description anyway, because it is what triggers the skill.

**Length limits**
- `description` plus `when_to_use` is capped at **1,536 characters** combined.
- The whole skill listing also has a budget of about 1% of the context window (`skillListingBudgetFraction`). Past that, every name stays but descriptions are dropped, starting with the least-used skills, and auto-triggering gets worse.
- `disable-model-invocation: true` takes a skill out of the listing entirely. Use it for skills that should only run when someone types `/name`.

**Failures that happen quietly**
- Unknown or misspelled keys are ignored without a warning.
- Malformed YAML (an unquoted colon, or a `>`/`|` block scalar) loads the body with no metadata, so the skill never auto-triggers. Quote your descriptions.
- `allowed-tools` only pre-approves tools for that turn. It restricts nothing and isn't gated by workspace trust.
- After compaction only a skill's first 5k tokens survive, so put the rules first.

**What's different on claude.ai** ([outside Claude Code](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code))
- Uploads (and the Skills API) accept only six keys: `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. Any other key, such as `when_to_use`, `arguments`, `context`, `hooks` or `paths`, is a hard error: "Unexpected key(s) in SKILL.md frontmatter". Keep a portable variant, and fold the `when_to_use` text into `description`.
- Treat `name` and `description` as required there. The platform's rules have been a lowercase, hyphenated name of up to 64 characters that doesn't contain "claude" or "anthropic", and a description of up to 1,024 characters. Ignore the Help Center's outdated 200-character limit and its `dependencies` field.
- `$ARGUMENTS`, `!` commands and `${CLAUDE_*}` variables are Claude Code preprocessing, so don't rely on them on claude.ai.
- Skills uploaded to claude.ai sync one-way back into Claude Code for anyone signed in with `/login`, landing in `~/.claude/skills/synced/`. If the short name is already taken, the synced copy runs only as `/anthropic-skills:<name>`. Locally, synced copies don't run `!` commands or expand `${CLAUDE_*}`. So uploading a repo skill gives your team a second, weaker copy that competes with it.
- Enterprise organizations now scan uploaded skills and require review before publishing (the default since 2026-10-02).

## Q3
There is no `claude plugin publish`. The CLI's subcommands are `install`, `uninstall`, `enable`, `disable`, `update`, `list`, `details`, `configure`, `prune`, `init`, `tag`, `validate`, `eval` and `test`, plus `marketplace add|list|update|remove` ([CLI reference](https://code.claude.com/docs/en/plugins/cli-reference)). So choosing between your claude.ai login and an API key never comes up at the command line.

You submit to Anthropic through the **directory submission portal**, which opened on 2026-09-25. Each submission goes through automated validation, a security scan and then human review ([publish to the directory](https://claude.com/docs/directory/publish)). I can't confirm which sign-in the portal requires. I'd expect your Claude account, but check the page.

**Where it ends up.** `claude-plugins-official` is Anthropic's curated marketplace, and reserved marketplace names must come from github.com/anthropics. Third-party plugins in Anthropic's catalogs mostly live in `claude-plugins-community` (`anthropics/claude-plugins-community`), and nearly all are pinned to a commit SHA ([Anthropic marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)). That implies your updates reach users only when the pin is bumped. Anthropic decides which catalog takes your plugin.

**Before you submit**
- Run `claude plugin validate`. Only `plugin.json` belongs inside `.claude-plugin/`; components placed there don't load. Avoid relative `../` paths, which break once the plugin is copied to the cache, and keep state in `${CLAUDE_PLUGIN_DATA}`.
- Run `claude plugin eval` (generally available since 2.1.269). It runs each case 3 times, with and without your plugin, and reports the difference, which is evidence that the plugin actually helps. It spends real usage ([plugin evals](https://code.claude.com/docs/en/plugin-evals)).
- Decide on `version`. If it's set in `plugin.json`, users stay on that version until you bump it, and it silently overrides the version in the marketplace entry.
- If you want the plugin to work on claude.ai or Cowork, avoid a top-level `bin/` folder; those surfaces refuse plugins that have one.

**You don't need Anthropic to ship.** Put a `.claude-plugin/marketplace.json` in a GitHub repo, and users can install with `/plugin install <name> --marketplace <owner/repo>` (2.1.275 and later). Auto-update is off by default for third-party marketplaces, so tell users how to update.

## Q4
Yes. Hooks now have five handler types: `command`, `http` (2.1.63), `mcp_tool` (2.1.118), `prompt`, and `agent` (still experimental) ([hooks](https://code.claude.com/docs/en/hooks)). Here is a config covering both of your cases:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash|PowerShell|Monitor",
      "hooks": [{
        "type": "http",
        "url": "https://policy.internal.example/claude/pre-tool",
        "headers": { "Authorization": "Bearer $POLICY_TOKEN" },
        "allowedEnvVars": ["POLICY_TOKEN"],
        "timeout": 5
      }]
    }],
    "Stop": [{
      "hooks": [{
        "type": "agent",
        "prompt": "Decide whether the user's task is really finished: every requested change made, tests run and passing, nothing left as TODO. If not, say exactly what remains. Context: $ARGUMENTS",
        "timeout": 180
      }]
    }]
  }
}
```

**1. Policy check on every command (`http` PreToolUse hook)**

Claude Code POSTs the hook input (`tool_name`, `tool_input.command`, `cwd`, and so on) to your endpoint. To block a command, return a 2xx response with `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"…"}}`. To let it through, return `{}`. Don't return `allow`: that pre-approves the call and skips the normal permission flow.
- **It probably fails open.** As I understand the http handler, non-2xx responses, timeouts and connection errors are non-blocking errors, so the command runs. To fail closed, use a `command` hook that pipes stdin to `curl -sf --max-time 5 …` and exits 2 when curl fails. Exit 2 always blocks; exit 1 never does.
- **Set `timeout`.** The default for http hooks is 600s.
- **Cover every command tool.** `PowerShell` and `Monitor` also run commands. A matcher made only of names and `|`, like the one above, matches those exact tool names. The handler's `if` field (for example `Bash(git *)`) can narrow it further.
- **Deploy it through managed settings.** A mod's `tool.check` can override hook blocks that aren't in managed settings ([mods](https://code.claude.com/docs/en/plugins/mods/overview)).
- **Test it inside a subagent.** The docs say tool hooks fire there, but issue #34692 reported that they don't ([hooks guide](https://code.claude.com/docs/en/hooks-guide)).

**2. Checking that the task is really finished (a model-based Stop hook)**
- `prompt`: a single model call with no tools and a 30s default timeout. It's cheap, but it judges only from the hook input.
- `agent` (shown above): a subagent that can inspect files. It's experimental, and its default timeout is 60s, so raise `timeout`.
- When the hook decides the task isn't done, it blocks the stop and sends the reason back to Claude. Since 2.1.143, a Stop hook can force at most 8 continuations in a row.
- Keep deterministic checks such as tests and lint in a `command` Stop hook, and use the model only for judgment. An evaluator is wasted effort on easy tasks, so for the hard ones consider `/goal <condition>` instead (v2.1.139). It runs the same evaluator loop for a single task with no configuration ([goal](https://code.claude.com/docs/en/goal)).

Hooks are no longer snapshotted at startup: settings edits take effect immediately, and `/hooks` is now a read-only browser.

## Q5
Package everything as one plugin in a private marketplace, roll it out through managed settings, and put the guardrail hooks in managed settings as well.

**Package**
- Create one repo as your internal marketplace (`.claude-plugin/marketplace.json`). It holds a plugin with `skills/`, a `.mcp.json` for both servers, and `hooks/hooks.json`.
- Declare the personal API token in the plugin's `userConfig` and mark it sensitive. Each engineer is prompted for it when the plugin is enabled (or runs `claude plugin configure`), it's stored per user, and `.mcp.json` refers to it as `${user_config.<key>}` instead of a committed value ([manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference)).
- Put components at the plugin root; only `plugin.json` goes inside `.claude-plugin/`. Keep any state in `${CLAUDE_PLUGIN_DATA}`, which survives updates.

**Distribute.** Use server-managed settings (from the Claude admin console) or an MDM-deployed `managed-settings.json`. In it, register the marketplace (`extraKnownMarketplaces`), enable the plugin (`enabledPlugins`) and, if you want, allow only your marketplace (`strictKnownMarketplaces`). That beats editing `.claude/settings.json` in 15 repos, and it's also how the setup reaches the web.

**Claude Code on the web**
- Cloud sessions have no `/plugin` panel. They don't load user-scope plugins or plugins declared in the repo, only server-managed and claude.ai-synced ones ([cloud environments](https://code.claude.com/docs/en/cloud-environments)).
- Skills in `~/.claude/skills/` don't load there either, but a repo's `.claude/skills/` does.
- I can't confirm how a plugin's `userConfig` secret reaches a cloud session. The more reliable route for the token-based server is to run it as a remote MCP server with per-user OAuth and add it as an organization connector on claude.ai. Connectors then appear automatically in Claude Code for anyone signed in with a subscription (not API-key users), and in cloud sessions.

**Guardrails.** Put hooks that must always run in managed settings, not only in the plugin. Engineers can disable a plugin, and a mod can override hook blocks that aren't in managed settings; on machines without managed settings it can override deny rules too. Set `allowManagedModsOnly` ([mods](https://code.claude.com/docs/en/plugins/mods/overview)).

**Keeping it updated**
- Auto-update is off by default for marketplaces not run by Anthropic, so turn it on for yours.
- Use one source of truth for the version. Either bump `version` in `plugin.json` on every release, or leave it out and ship by commit SHA ([loading](https://code.claude.com/docs/en/plugins/loading)). Once `version` is set, users stay on it until you bump it, and it silently overrides the marketplace entry's version.
- In CI, run `claude plugin validate`, and run `claude plugin eval` when skills change (it spends real usage).
- Lock down the marketplace repo. Nothing is signed, and the Plugin4Shell attack showed that a branch named after a pinned SHA can take over the pin. Restrict who can push branches and tags, and keep Claude Code up to date.
- Tool Search defers all MCP tools by default. Keep tool descriptions and server instructions under 2,048 characters, and set `alwaysLoad` on any server whose tools must be loaded from the start.

## Q6
**What they are.** Mods are JavaScript or TypeScript *function* hooks that ship inside plugins. You list them under `modules` in the plugin's `hooks/hooks.json`, and each module exports `register(on)` to subscribe to events ([mods](https://code.claude.com/docs/en/plugins/mods/overview)). They shipped in v2.1.287 on 2026-10-01, less than a week ago.

**How they differ from your settings.json hooks**
- **Where they live.** Settings hooks can go in user, project, local or managed settings, in skill and agent frontmatter, or in plugins. Mods come only from plugins.
- **How they run.** Settings hooks are declared handlers (`command`, `http`, `mcp_tool`, `prompt`, `agent`) that receive JSON and answer with an exit code or JSON. A mod is code that registers callbacks.
- **What they can do.** Hooks can block or approve tool calls, rewrite tool input (`updatedInput`) and output (`updatedToolOutput`), and add context. Mods can also redraw the UI (panes, status line, toasts), rewrite prompts and tool calls, call models, and approve tool calls.
- **Power over permissions.** A mod's `tool.check` can override ask rules and hook blocks that aren't in managed settings. On machines without managed settings or a Team/Enterprise sign-in, it can override **deny rules** too ([permissions](https://code.claude.com/docs/en/permissions)).
- **Safety.** Mods are unsandboxed, `/sandbox` doesn't cover them, and nothing is signed. Admins can restrict them with `allowManagedModsOnly`.

**Should you port your hooks?** Mostly no.
- Settings hooks aren't deprecated. They work in any language and now take effect as soon as you edit them.
- Hooks in managed settings are the ones a mod can't override, so that's where guardrails belong.
- Write a mod only for things hooks can't do well: custom UI such as a live status pane or toasts, rewriting prompts, calling a model inside the hook, or keeping state across events.
- The API is a week old, so expect it to change.

Mods also change your security picture. Any plugin you install can now carry code that runs with your user privileges and can approve tool calls over your hooks. If you manage machines, set `allowManagedModsOnly` and move hooks that must always hold into managed settings.

## Q7
**Output limits.**
- As far as I know, Claude Code still caps MCP tool output by tokens. It warns above 10,000 tokens and has a default maximum of 25,000 tokens, which you can change with `MAX_MCP_OUTPUT_TOKENS`.
- I can't confirm today's defaults, or whether current builds truncate oversized results or save them to a file, so test with your real payloads.
- Either way, 100k+ characters is roughly 25k+ tokens. That is at or over the default cap, and even with a higher cap each call takes a large share of the context window.
- Tool descriptions and server instructions are capped at 2,048 characters.
- Tool Search now defers *all* MCP tools by default, so only tool names and server instructions load at startup ([MCP](https://code.claude.com/docs/en/mcp)).

**Timeouts.** `MCP_TOOL_TIMEOUT` (in milliseconds) sets the per-call timeout, and `MCP_TIMEOUT` sets the server startup timeout. I can't confirm the current default under the new v2 MCP runtime, so set `MCP_TOOL_TIMEOUT` explicitly (for example `900000`) in the `env` block of your team's settings. Also check your proxies and load balancers, since many cut idle HTTP requests after 60 seconds.

**What to do on the server side**
- **Make the large tools narrow.** Offer tools like `list_tables(filter)`, `describe_table(name)` and `search_schema(pattern)`, with `limit`/cursor pagination and a compact default format. When you truncate, say so and say how to get more, for example: "40 of 812 tables shown; pass cursor=…".
- **Hand off genuine full dumps.** Write the dump to a file (for a stdio server) or expose it as a resource, and return the path or link. Claude can then grep it or read it in pieces.
- **Turn the slow tool into a job.** A `start_…` tool returns an ID immediately, and `get_…_status` / `get_…_result` tools poll for it. Don't depend on MCP Tasks for this: the 2026-07-28 spec moved Tasks out of the core into an extension, and Claude Code doesn't document support for it. If you keep the call synchronous, send progress notifications so the stream isn't idle; I can't confirm whether Claude Code resets its timeout when it receives them.
- **Build HTTP servers for the 2026-07-28 "stateless" revision.** Claude Code's v2 runtime negotiates it by default (since about 2.1.232; `MCP_SDK_GENERATION=v1` opts out). The revision has no sessions and no `Mcp-Session-Id`, so key job state by job ID rather than by session ([spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)).
- **Write for deferred loading.** Because tools load only when needed, give them descriptive names and write server `instructions` that say when to use the server. Mark any tool that must always be loaded with `_meta["anthropic/alwaysLoad"]`.

## Q8
Use something else: a **Workflow** (v2.1.154). The `Workflow` tool runs a JavaScript script that orchestrates agents with `agent()`, `parallel()`, `pipeline()` and `phase()`. You opt in by putting `ultracode` in your prompt or by running `/effort ultracode` ([workflows](https://code.claude.com/docs/en/workflows)). It requires opting in because it can spawn dozens of agents. Six hundred independent, read-only checks followed by a verification pass is exactly the kind of job that justifies it. The bundled `/deep-research` command is a working example of the pattern.

Structure it in phases:
1. **Build the inventory with a script, not the model.** Dump every route (from the framework's route listing, or with an AST parser or grep) to `routes.json`, recording method, path and the handler's file:line. This is your coverage baseline: the run should end with 600 verdicts.
2. **Write down the criteria.** Define what counts as authorization (middleware, decorators, policy calls, guards at the router or gateway level) and list the routes that are meant to be public. Put this in a skill or a file that every agent reads.
3. **Scan in parallel.** Give each agent 20–30 handlers and only read-only tools, for example a custom agent with `tools: Read, Grep, Glob`. For each handler it returns a structured verdict (`protected`, `public-by-design` or `suspect`) with file:line evidence.
4. **Verify independently.** Send each suspect to a fresh agent that sees only the claim and tries to *refute* it, by tracing where the router is mounted and which middleware it inherits. Where you can run the app, the agent should confirm the finding with a request sent with no credentials or the wrong role, or with a failing test in a separate worktree. Only confirmed findings go in the final list; the rest go into a separate "needs human review" list.
5. **Report.** Group findings by root cause, since one unguarded router can explain 40 handlers, and give evidence and a fix for each. The audit is read-only, so running in parallel is safe. Apply the fixes later, one at a time.

**Why not the alternatives**
- **An agent team** is still experimental and off by default, uses about 7× the tokens, and works best with 3–5 teammates. It's designed for collaboration, not for fanning out 600 items ([agent teams](https://code.claude.com/docs/en/agent-teams), [costs](https://code.claude.com/docs/en/costs)).
- **Ad-hoc subagents** can work, but the main session has to track 600 items and absorb all the results, at most 20 subagents run at once, and Opus 5's `claude_code` prompt tells Claude not to delegate unless asked. Use them as the fallback if Workflows are disabled: the same phases, requested explicitly, with results written to files. Use fresh (non-fork) agents for verification, because a fork inherits the whole conversation, including the scan results.

**Cost and safety.** Explore and other agents that inherit the model now run on your session model. Consider Sonnet 5.5 for the scan and Opus 5.5 for verification. Run anything that executes the app inside a container: auto mode is a convenience, not a containment boundary ([sandboxing](https://code.claude.com/docs/en/sandboxing)).
