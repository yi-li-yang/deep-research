## Q1
Your agent files still work. They are the same Markdown-plus-frontmatter files in `.claude/agents/` or `~/.claude/agents/`. Almost everything around them has changed (Claude Code is at 2.1.291).

**Creating and managing them**
- **The `/agents` wizard is gone.** It was removed in v2.1.198 (Jul 2026). `/agents` now only reminds you to ask Claude to write an agent, or to edit the files yourself. Running subagents show in a panel under the prompt, and `/tasks` lists them and opens their transcripts.
- **Task is now Agent.** The tool was renamed in v2.1.63 (Feb 2026). `Task(...)` rules still work as aliases, but write new rules as `Agent(my-agent)`. A `tools: Agent(worker, researcher)` entry limits which agents a subagent may spawn.
- **New frontmatter:**
  - `disallowedTools`, `permissionMode` (including `auto`), `maxTurns`
  - `skills` (preloaded), `mcpServers`, `hooks`
  - `memory` (persistent user, project or local memory), `background`, `effort`
  - `isolation: worktree`, `omitClaudeMd`, `color`, `initialPrompt`
  - `model` now also accepts `fable`.
- **Model order:** the per-call `model`, then frontmatter, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the session model.

**How they behave**
- **Background by default** (v2.1.198).
  - You keep working while they run.
  - Their permission prompts appear in your main session, labelled with the agent's name.
  - Background subagents get a reduced built-in tool set.
  - `AskUserQuestion`, the plan-mode tools, `Workflow` and `ScheduleWakeup` are removed from every subagent.
  - At most 20 run at once (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`).
- **Nesting** (v2.1.219). Subagents can spawn subagents up to 3 levels deep. Change the depth with `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`; `1` turns nesting off.
- **Forks** (on by default in interactive sessions since v2.1.232).
  - Claude starts one with `subagent_type: "fork"`, and you start one with `/subtask`.
  - A fork inherits the whole conversation and its prompt cache. Your custom agents still start with a clean context.
  - With fork mode on, Claude can't ask for a foreground run. If you relied on blocking subagents, set `CLAUDE_CODE_FORK_SUBAGENT=0` or `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.
- **Built-in agents changed.** Explore no longer runs on Haiku: it uses your session's model, or Opus if you run Fable on a subscription. There are new `claude`, `claude-code-guide`, `statusline-setup` and `fork` agents.
- **Claude delegates more.** Opus 5-generation models delegate more readily, so make each `description` precise about when the agent should and shouldn't be used.

**To check after the upgrade**
- Rename `Task` to `Agent` in permission rules and `tools:` lists.
- Re-check cost for any agent that assumed Haiku.
- Add `disallowedTools` (e.g. `Edit, Write`) to agents that should stay read-only.

Sources: [sub-agents](https://code.claude.com/docs/en/sub-agents), [changelog](https://code.claude.com/docs/en/changelog)
## Q2
**Layout.** Put each skill in its own folder: `.claude/skills/<name>/SKILL.md` in the repo (commit it for the team), or `skills/<name>/SKILL.md` inside a plugin. The file is YAML frontmatter followed by Markdown instructions. Keep it under about 500 lines and move detail into referenced files and scripts. Commands and skills merged in v2.1.3, so every skill is also a `/name` command.

```markdown
---
name: release-notes
description: Drafts release notes from merged PRs. Use when asked for release notes, a changelog entry or "what shipped".
---
Steps…
```

**Frontmatter Claude Code accepts.** Everything is optional: `name` defaults to the folder name, and `description` defaults to the first non-empty line of the body.
- **Fields:** `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context` (`fork`), `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`, `compatibility`.
- **Unknown keys are silently ignored,** so a typo just does nothing.
- **Malformed YAML** (for example an unquoted colon) loads the body with no metadata, so the skill never auto-triggers. Catch it in CI with `claude plugin validate .claude` (v2.1.233+).
- **`allowed-tools` only pre-approves** tools for the turn that invokes the skill. It restricts nothing; `disallowed-tools` is the field that restricts.

**Description length**
- **Per skill:** `description` plus `when_to_use` is truncated at **1,536 characters** in the skill listing (`skillListingMaxDescChars`).
- **Across all skills:** the listing has a budget of about **1% of the context window** (`skillListingBudgetFraction`). Over budget, Claude Code drops descriptions, least-used skills first, and those skills stop triggering reliably.
- **How to stay inside it:**
  - Put the trigger words first.
  - Mark manual-only skills `disable-model-invocation: true`, which removes them from the listing.
  - Check the cost with `/doctor` or `/skill-doctor`.
- **After compaction,** only the first 5k tokens of a skill survive, so put critical rules at the top.

**What changes on claude.ai**
- **Only six keys are allowed.** Uploads (like the Skills API and `package_skill.py`) accept only `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. Any other key is a hard error: "Unexpected key(s) in SKILL.md frontmatter". There's no `when_to_use`, so put trigger phrases in `description`.
- **`name` is required:** at most 64 characters, lowercase letters, digits and hyphens only, no "claude" or "anthropic", and no XML.
- **`description` is required** and capped at **1,024 characters** (the Agent Skills spec limit), which is stricter than Claude Code's 1,536.
- **Claude Code-only body features don't work there.** That includes `` !`cmd` `` injection, `$ARGUMENTS` and `${CLAUDE_*}` substitutions.
- **The Help Center's "200 characters" limit is outdated.**
- **Uploaded skills sync back into Claude Code.**
  - Skills enabled on claude.ai sync to anyone signed into Claude Code with claude.ai (v2.1.273+), under `~/.claude/skills/synced/`.
  - They run as `/name`, or as `/anthropic-skills:name` when the short name is taken.
  - Synced copies don't run `!` commands.
  - Uploading a skill that also lives in the repo therefore gives people two listed copies, so keep one source of truth (`syncClaudeAiSkills: false` opts a user out).

A safe pattern is a portable core that uses only the six spec keys, with Claude Code-only keys added in the repo copy.

Sources: [skills](https://code.claude.com/docs/en/skills), [Agent Skills spec](https://agentskills.io/specification), [platform skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
## Q3
There isn't one, for two reasons.

1. **The CLI has no `publish` subcommand.** `claude plugin` offers `install`, `uninstall`, `enable`, `disable`, `update`, `list`, `details`, `configure`, `prune`, `init`, `tag`, `validate`, `eval`, `test` and `marketplace add|list|update|remove`.
2. **`claude-plugins-official` doesn't take open submissions.** It is Anthropic's curated catalog of its own and partner plugins, and the docs say it "doesn't take submissions through the directory portal". If you have an Anthropic partner contact, ask them about a listing there.

**What you can submit to is Anthropic's directory, through a web portal:**
1. **Validate locally.** Run `claude plugin validate --strict ./your-plugin` and work through the [pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist): README, license and `plugin.json` metadata.
2. **Submit in the portal.**
   - At [claude.ai/directory/manage](https://claude.ai/directory/manage), choose **Submit new**, then **Plugin bundle**.
   - Give the GitHub repo, the plugin path and the tracked branch or tag, then select **Validate**.
   - Fill in the listing details, data-handling questions and compliance step, then **Submit for review**.
3. **Review.** Every version gets automated validation and a security scan. A person reviews a new listing, and by default a reviewer publishes each passing version.
4. **Updates.** Merge to the tracked branch (an optional GitHub push webhook speeds pickup), and bump `version` each release if you set it.

**Authentication uses neither the CLI nor an API key.**
- You use the portal while signed in to **claude.ai** on a paid plan. Pro and Max users submit from their own account. On Team or Enterprise, an Owner submits, or someone given the Directory permission.
- You also **connect your GitHub account on claude.ai**, and the portal checks that it can push to the repo.
- The repo can be private during review if you install the Claude GitHub App and consent to the source upload. It must be public before the listing goes live.
- The old Console submission form is retired, and each organization can make 10 submissions per 24 hours.

**After listing.** People add the plugin on claude.ai or in Cowork, and it reaches their Claude Code as `name@synced` via account sync. Approved community plugins are also mirrored nightly into the `claude-community` marketplace ([anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community)).

**To ship today without review,** host your own marketplace. Commit `.claude-plugin/marketplace.json` to the repo; users then run `/plugin install your-plugin --marketplace you/repo` (v2.1.275+).

Sources: [publish a plugin](https://code.claude.com/docs/en/plugins/publish), [submit your plugin](https://claude.com/docs/plugins/submit), [directory](https://claude.com/docs/directory/publish), [CLI reference](https://code.claude.com/docs/en/plugins/cli-reference)
## Q4
Yes. Hooks now have five handler types: `command`, `http`, `mcp_tool`, `prompt` and `agent` (still experimental).

**1. Check every Bash command against your policy service** with a PreToolUse `http` hook:

```json
{"hooks":{"PreToolUse":[{"matcher":"Bash","hooks":[{
  "type":"http","url":"https://policy.internal.example/claude/pretooluse",
  "headers":{"Authorization":"Bearer $POLICY_TOKEN"},"allowedEnvVars":["POLICY_TOKEN"],
  "timeout":10}]}]}}
```

Claude Code POSTs the hook input as JSON: session ID, `cwd`, `tool_name`, `tool_input.command` and so on. To block a command, your service must return **2xx with a JSON body**:

`{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"…"}}`

It can also return `ask` or `allow`; an empty 2xx means no opinion.
- **It fails open.** A non-2xx response, a connection failure or a timeout is a non-blocking error. If you need fail-closed, use a `command` hook that calls the service and exits with code 2 on any error.
- **Set a short `timeout`.** The default is 600 s.
- **An `allow` never overrides your deny or ask rules.**
- **Ship it in managed settings** so users can't remove it.
  - `allowedHttpHookUrls` and `httpHookAllowedEnvVars` restrict which URLs and variables http hooks may use.
  - A mod can approve a call that a non-managed hook blocked, but not one blocked by a managed hook.
- **On Windows,** match `Bash|PowerShell`.
- **Test that it fires inside subagents.** The docs say it does; issue #34692 reported otherwise.

**2. Check that the task is really finished** with a model-evaluated Stop hook:

```json
{"hooks":{"Stop":[{"hooks":[{"type":"agent","timeout":180,
  "prompt":"Decide if the user's request is fully done. Input: $ARGUMENTS (read transcript_path, inspect the changed files). Reply {\"ok\":true} or {\"ok\":false,\"reason\":\"what is still missing\"}."}]}]}}
```

- **`prompt` type:** a single LLM call on the hook input.
  - It uses the background (small, fast) model unless you set `model`, and times out after 30 s by default.
  - On `ok:false`, the `reason` becomes Claude's next instruction. `impossible:true` lets Claude stop anyway.
- **`agent` type:** a subagent with tools (Read, Grep, Glob and others) that runs for up to 50 turns, with a 60 s default timeout. Use it when the check needs to look at files. It is experimental.
- **If "done" means "tests pass",** a `command` Stop hook that runs them and exits with code 2, with the failure on stderr, is cheaper and deterministic.
- **Loops are capped.** After 8 forced continuations in a row the turn ends (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`). `stop_hook_active` in the input tells you you're already in a continuation.
- **For a single session,** `/goal <condition>` is a built-in prompt-based Stop hook that needs no configuration.

Sources: [hooks](https://code.claude.com/docs/en/hooks), [permissions](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks), [/goal](https://code.claude.com/docs/en/goal)
## Q5
Ship **one plugin in a private marketplace repo**, and push it out with **managed settings**.

**1. Package.**
- One repo holds `.claude-plugin/marketplace.json` plus the plugin: `skills/`, `.mcp.json` with both servers, `hooks/hooks.json`, and scripts referenced as `${CLAUDE_PLUGIN_ROOT}/scripts/…`.
- Avoid a top-level `bin/` folder; claude.ai's organization sync rejects it.
- Gate merges with `claude plugin validate --strict` in CI.

**2. Personal token.**
- Declare it in `plugin.json` under `userConfig` with `"sensitive": true`, and reference it as `${user_config.api_token}` in that server's `env` or `headers`.
- Claude Code prompts each engineer for it and stores it in the OS credential store. They can change it with `claude plugin configure`.
- **Better, if that server can be remote with OAuth:** add it as an organization connector on claude.ai. Each engineer signs in once, and it appears in the CLI (with a claude.ai login), on the web and in Desktop, with no token handling.

**3. Distribute.** On Team or Enterprise, an Owner sets server-managed settings (Organization settings → Claude Code → Managed settings):

```json
{"extraKnownMarketplaces":{"acme":{"source":{"source":"github","repo":"acme/claude-standard"},"autoUpdate":true}},
 "enabledPlugins":{"standard@acme":true}}
```

- This force-enables the plugin everywhere. It's also the only managed source that reaches **cloud sessions**.
- On MDM-managed laptops, `managed-settings.json` is harder for users to tamper with, but it doesn't reach the web.
- Don't rely on 15 repos' `.claude/settings.json`: it needs workspace trust, and cloud sessions ignore plugins declared there.

**4. Guardrails.**
- Hooks from a plugin that managed settings force-enable keep running even under `allowManagedHooksOnly`.
- Checks that must hold no matter what belong directly in managed `hooks`. Users approve them once, and user-installed mods can't override them.
- Consider `allowManagedModsOnly`.

**5. Updates.**
- Third-party marketplaces don't auto-update unless you set `autoUpdate` as above.
- Bump `version` every release, or omit it so installs track commits.
- Each laptop needs non-interactive git credentials for the private repo (`gh auth login && gh auth setup-git`). Without them, background updates fail silently.

**6. Web users.**
- **What loads:** cloud sessions load the repo's `.claude/skills`, `.claude/settings.json` hooks and `.mcp.json`, plus server-managed and claude.ai-synced plugins. They don't load plugins users installed themselves.
- **The token:** the keychain-stored token doesn't exist in the cloud VM. Cloud "API credentials" aren't available on Team or Enterprise yet. So either use the OAuth connector, or have each engineer use a **personal** cloud environment with the token as an env var. Never put it in an org-shared environment, which every member can read.
- **Network:** allow the MCP server's host in the environment's network settings.
- **Optional:** also sync the same repo via claude.ai **Organization settings → Plugins & skills**. That reaches chat, Cowork and Claude Code (as `name@synced`) without engineers needing git access.

Verify with `/plugin` and `claude doctor` (its "Managed settings" line).

Sources: [org plugins](https://code.claude.com/docs/en/plugins/org), [hosting](https://code.claude.com/docs/en/plugins/host-marketplace), [userConfig](https://code.claude.com/docs/en/plugins/manifest-reference#user-configuration), [cloud environments](https://code.claude.com/docs/en/cloud-environments), [rollout routes](https://claude.com/docs/plugins/org-rollout), [server-managed settings](https://code.claude.com/docs/en/server-managed-settings)
## Q6
**What they are.** A mod is a **plugin of JavaScript or TypeScript event handlers that run inside Claude Code's own process**. Its `hooks/hooks.json` points at a module that exports `register(on)`.
- **Events:** handlers fire on `tool.call`, `tool.check`, prompts, turns, `ui.render` and more. Each handler can observe the event, rewrite it, or answer it itself.
- **What the mods API lets them do:**
  - draw panes, bands above the prompt and status elements
  - restyle Claude Code's own UI (but never the permission prompt)
  - add `/commands` that run code instantly, without a Claude turn
  - hold or answer tool calls, and call models
  - share state between handlers

**When they shipped.** **v2.1.287 on 1 Oct 2026** ("Claude Mods"), on by default; Desktop has them from its bundled 2.1.286. Before that they were early access behind `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`, which is now ignored. Fixes have landed in 2.1.288–2.1.290. `/diff`, AGENTS.md loading and the "You should know" side agent are built-in mods.

**How they differ from your settings hooks**
- **Settings hooks** are a shell command, HTTP call, MCP tool, prompt or agent, declared in a settings file. They run outside Claude Code on 33 lifecycle events and can block or allow actions, edit tool input and output, and add context. You can write them in any language and enforce them through managed settings.
- **Mods** are in-process JS/TS and ship **only as plugins** from a marketplace. They can rewrite far more and draw UI, but drawing only shows in the terminal and Desktop. Their handlers still run in VS Code, `-p`, the SDK and cloud sessions.
- **Trust is the big difference.**
  - Mods are **unsandboxed** and run with your permissions.
  - A mod's `tool.check` can approve calls that your ask rules or non-managed PreToolUse hooks would stop, and can skip the auto-mode classifier.
  - On machines without managed settings or a Team/Enterprise sign-in, it can override **deny rules** too.
- **Controls:**
  - Admins have `allowManagedModsOnly`. You have `disableAllHooks` or `--safe-mode`.
  - Before installing a mod, run `claude plugin validate` on it; its `hooks:` and `calls:` lines list what it does.
  - Test mods with `claude plugin test`.

**Is it worth porting? Mostly no.** Settings hooks aren't deprecated. They are language-agnostic and easier to audit, and managed ones can't be overridden by a mod, which is what you want for guardrails. Port a hook only if you need what mods add:
- UI
- instant commands
- in-memory state shared across events
- avoiding a process spawn per event on a hot path

Mods are five days old and still getting daily fixes, so wait for the API to settle before moving anything critical.

Sources: [mods overview](https://code.claude.com/docs/en/plugins/mods/overview), [permissions](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks), [changelog](https://code.claude.com/docs/en/changelog)
## Q7
**Output limits (enforced by Claude Code)**
- **Warning and cap.** Claude Code warns above 10,000 tokens. The default cap is 25,000 tokens (`MAX_MCP_OUTPUT_TOKENS`, an environment variable each user would have to set).
- **Large text goes to a file, not into context.** This happens to a text result over **50,000 characters**, or over the token cap. Claude Code saves it to the session's `tool-results` folder and gives Claude the path to read or grep. Raising `MAX_MCP_OUTPUT_TOKENS` doesn't change the 50k threshold.
- **Server-side override.** Set `"_meta": {"anthropic/maxResultSizeChars": 200000}` on the tool in `tools/list`. That raises the threshold for that tool, up to a hard ceiling of **500,000 characters**, whatever the env var says. Images still obey the token cap.
- **Error results.** An `isError` result over about 11k characters keeps only its first and last 5k.
- **Descriptions.** Tool descriptions and server instructions are cut at 2,048 characters. All MCP tools are deferred behind Tool Search by default, so your server instructions are what Claude sees first.

**Long-running calls**
- **Wall clock:** `MCP_TOOL_TIMEOUT` (about 28 h if unset), or a per-server `"timeout"` in milliseconds in `.mcp.json`. Progress notifications don't extend it.
- **First byte (HTTP and SSE):** the server must start responding within the largest of 60 s, the applicable tool timeout, and `MCP_TIMEOUT`.
- **Idle timeout:** a call with no response and no progress for **5 min** (HTTP, SSE, connectors) or 30 min (stdio) is aborted. `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` changes it, and a per-server `timeout` acts as a floor.
- **Auto-backgrounding:** after **2 min**, a call from the main conversation moves to the background (v2.1.212+). Claude gets a task ID and keeps working, and the result arrives as a notification. The task shows in `/tasks` and dies with the session.

**What to do on the server**
1. **Schemas.**
   - Make them navigable: `list_tables`, `describe_tables(names, detail)`, cursors, compact DDL.
   - Use `maxResultSizeChars` only if Claude truly needs the whole schema inline; 100k characters is about 25k tokens of context per call.
   - Otherwise, the default of saving large results to a file works fine.
2. **The 5-minute tool.**
   - Over HTTP, start the SSE response immediately.
   - Send `notifications/progress` every 30–60 s when the request carries a `progressToken`.
   - Commit a project `.mcp.json` with `"timeout": 900000` for that server; this also raises the first-byte timer and the idle floor.
   - Make the tool idempotent, since 2.1.288 fixed calls occasionally running twice.
3. **Jobs that can outlive a session.** Offer a start-and-poll pair: `start_x` returns a job ID, and `get_x_status` reports on it. The MCP Tasks extension exists, but Claude Code doesn't document support for it as of today.
4. **Test against both client runtimes** (`MCP_SDK_GENERATION=v1` and `v2`). v2, the default since about 2.1.232, uses the stateless 2026-07-28 protocol with HTTP servers that support it.

Source: [Claude Code MCP docs](https://code.claude.com/docs/en/mcp)
## Q8
Use a **dynamic workflow**, not a pile of subagents or an agent team.

**Why not the other two**
- **Subagents:** Claude orchestrates them turn by turn and every result lands in its context. Across 600 handlers, at most 20 at a time, the context floods and the plan drifts. They're fine for a 20-handler slice.
- **Agent teams:** still experimental (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). They're designed for 3–5 long-running peers who discuss, and cost about 7× a single session. Wrong shape for 600 uniform checks.

**Why a workflow (v2.1.154+)**
- Claude writes a JavaScript script (`agent()`, `pipeline()`, `parallel()`, `phase()`) that runs in the background. Intermediate results stay in script variables, not in Claude's context.
- It's built for scale: 16 agents run at once by default, a `pipeline()` takes up to 4,096 items, and a run can use 1,000 agents.
- Runs are resumable and can include an adversarial verification phase. The docs use almost exactly your task as their example.

**Setup**
1. **Establish ground truth.**
   - Build the handler inventory deterministically, with router introspection or an AST/grep script. Output `routes.json` with file:line, method, path and middleware.
   - Add a short rules or skill file saying what counts as authorization in your code: middleware, decorators, policy calls, tenant scoping, and intentionally public routes. Global and router-level guards cause most false positives.
2. **Prompt with the opt-in keyword:**
   > `ultracode: audit every handler in routes.json for missing authorization. Phase 1: read-only auditors, ~10–15 handlers each, grouped by router, returning JSON findings (handler, file:line, missing check, evidence). Phase 2: for each candidate, two independent verifiers try to refute it (global/router middleware, gateway config, checks in callees); keep only findings both confirm, mark disagreements "needs review" and unverifiable ones "unverified". Phase 3: dedupe, rank, and include a coverage table proving every handler was examined.`
3. **Adjust settings.**
   - Raise the size guideline, which defaults to `medium` (under 10 agents), or `small` on Pro: `/config workflowSizeGuideline=large`.
   - Pre-allow any Bash the agents need, such as `Bash(rg *)`, because a run can't take input midway.
   - On Pro, turn on Dynamic workflows in `/config`.
4. **Pilot on one module.** Watch token spend in `/workflows`, then run the rest. Consider a cheaper model for Phase 1 and your strongest for verification.
5. **Optional proof:** for each confirmed finding, have an agent write a failing test or request that demonstrates the unauthorized access.
6. **Save it for reuse.** In `/workflows`, press `s` to save the script to `.claude/workflows/`, so `/authz-audit` reruns it each release.

Sources: [workflows](https://code.claude.com/docs/en/workflows), [agent teams](https://code.claude.com/docs/en/agent-teams), [sub-agents](https://code.claude.com/docs/en/sub-agents)
