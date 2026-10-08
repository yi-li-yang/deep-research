## Q1
Your existing agent files still work unchanged. What has changed is the tooling around them and the defaults for how Claude runs them. (Claude Code is at v2.1.291 as of Oct 6, 2026.)

**Creating and managing them**
- **The `/agents` wizard is gone.** Since v2.1.198 (early July 2026), running `/agents` only prints a reminder ([issue #72945](https://github.com/anthropics/claude-code/issues/72945)). To create or change an agent, either ask Claude (for example, "create a read-only reviewer subagent in .claude/agents that uses Sonnet") or edit the Markdown file yourself.
  - Edits load live, without a restart.
  - `claude plugin validate .claude/agents/` checks the frontmatter.
  - The wizard's "Running" tab is replaced by `/tasks`. Named background agents also appear in the `@` typeahead.
  - Don't confuse this with `claude agents`. That command opens agent view, which manages background *sessions*, not subagents.
- **Many new frontmatter fields:** `disallowedTools`, `permissionMode`, `skills` (preloads whole skills), `mcpServers`, `hooks` (scoped to that agent), `memory` (persistent memory at `user`, `project` or `local` scope), `background`, `isolation: worktree`, `maxTurns`, `effort`, `initialPrompt`, `omitClaudeMd`.
- **More ways to define and invoke agents:**
  - Agents can now come from the `--agents` JSON flag, from managed settings, or from plugins.
  - `claude --agent <name>` (or the `agent` setting) runs a whole session as that agent.
  - `@"name (agent)"` makes Claude use one specific agent.

**How Claude uses them**
- **Task was renamed Agent** in v2.1.63 (late Feb 2026). `Task(...)` permission rules still work as aliases. Hook scripts that check `tool_name == "Task"` stopped matching, though ([issue #29677](https://github.com/anthropics/claude-code/issues/29677)).
- **Background is the default** since v2.1.198. Claude keeps working while a subagent runs and gets notified when it finishes. Background agents get a smaller set of built-in tools: MCP tools are kept, but `AskUserQuestion` is removed. Their permission prompts appear in your main session.
- **Fork mode is on by default** in interactive sessions since v2.1.232 (mid-Aug 2026). For side tasks, Claude may now start a *fork*, which inherits the whole conversation, instead of one of your agents, which start with fresh context.
  - `/subtask` starts a fork by hand.
  - `CLAUDE_CODE_FORK_SUBAGENT=0` turns fork mode off.
- **Other behavior changes:**
  - Subagents now inherit the session's extended-thinking setting. Before v2.1.198, thinking was off for them.
  - Claude can resume a finished subagent by its ID using `SendMessage`.
  - Subagents can start their own subagents, up to 3 levels deep by default.
- **Which model runs:** a model named in the individual call wins, then your `model:` frontmatter, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the main session's model.
- **Permission mode:** if the main session is in auto, acceptEdits or bypass mode, subagents run in that mode and ignore their own `permissionMode`.
- **Limits:**
  - 20 concurrent subagents.
  - A warning if all agent descriptions together exceed 15k tokens.
  - Hooks in a project agent's frontmatter run only after you trust the folder.

**What to do now**
- Search your hooks for "Task".
- Re-check your descriptions, since they still decide which agent Claude picks.
- Consider `memory: project` for reviewer agents and `isolation: worktree` for agents that edit code.

Docs: [subagents](https://code.claude.com/docs/en/sub-agents), [running agents in parallel](https://code.claude.com/docs/en/agents).
## Q2
**Shape.** Put each skill in its own folder, such as `.claude/skills/<name>/SKILL.md` or a plugin's `skills/<name>/`. Each folder holds a `SKILL.md` with YAML frontmatter and Markdown instructions. Keep `SKILL.md` under about 500 lines. Put longer material in `references/`, `assets/` or `scripts/` and point to it by path.

```markdown
---
name: release-notes
description: Drafts release notes from merged PRs in our house format. Use when asked for release notes, a changelog entry, or "what shipped".
---
1. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/prs.py` ...
```

**Frontmatter fields Claude Code supports** ([docs](https://code.claude.com/docs/en/skills)). All are optional, but `description` is strongly recommended.
- **Identity:** `name` (defaults to the folder name), `description`, `when_to_use`.
- **Invocation:** `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`.
- **Tools:** `allowed-tools`, `disallowed-tools`.
- **Execution:** `model`, `effort`, `context: fork` (with `agent` and `background`), `hooks`, `paths` (globs that limit when Claude loads the skill automatically), `shell`.
- **Agent Skills spec fields:** `metadata`, `license`, `compatibility`. Claude Code accepts these but ignores them.

The skill body can use `$ARGUMENTS`/`$0`, `${CLAUDE_SKILL_DIR}` and other substitutions, plus `` !`cmd` `` to inject shell output.

**Description length in Claude Code**
- **Per-skill cap:** `description` plus `when_to_use` is cut at **1,536 characters** in the skill listing Claude sees. You can change this with `skillListingMaxDescChars`.
- **Total listing budget:** the whole listing gets **1% of the context window**. When you have many skills and the listing overflows, Claude Code drops the descriptions of your least-used skills and keeps only their names.
  - To raise the budget, set `skillListingBudgetFraction` or `SLASH_COMMAND_TOOL_CHAR_BUDGET`.
  - To free space, mark low-priority skills `"name-only"` in `skillOverrides`.
  - `/doctor` and `/skill-doctor` show what the listing costs.
- **Put the trigger words first.** Some earlier 2026 builds cut descriptions at 250 characters ([example](https://github.com/backnotprop/plannotator/issues/412)).

**What's different on claude.ai** ([guide](https://claude.com/docs/skills/how-to))
- **Only six fields are allowed:** `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. Any other key makes the upload fail with `Unexpected key(s) in SKILL.md frontmatter`; it isn't silently ignored. That includes `when_to_use`, `argument-hint`, `disable-model-invocation`, `model`, `context`, `hooks` and `paths`.
- **`name` is required** and may contain only lowercase letters, digits and hyphens, up to **64 characters**. It must match the folder name.
- **`description` is required**, up to **1,024 characters**. That is stricter than Claude Code's 1,536.
- **Packaging:** upload a ZIP whose top level is the folder (`my-skill/SKILL.md`) under Customize > Skills. On Team and Enterprise plans you can also Share a skill or Publish it to your org.
- **Claude Code-only body features:** `` !`cmd` `` injection and `${CLAUDE_*}` substitutions only work in Claude Code. In claude.ai chat, scripts run in the code-execution sandbox, so make script paths work relative to `SKILL.md` too.
- **Sync back into Claude Code:**
  - Skills you enable on claude.ai also appear in Claude Code. That includes cloud sessions and terminal sessions signed in with a claude.ai account.
  - They show up as `/anthropic-skills:<name>`.
  - On your own machine, their `!` commands don't run.
  - If the same skill also lives in the repo, the local copy takes `/name`.

**Practical rule:** keep any skill you'll upload to the six portable fields and at most 1,024 characters of description. Check it with `skills-ref validate` or `claude plugin validate`.
## Q3
There's no such command. Claude Code has no `claude plugin publish` (or `submit`) subcommand. The `claude plugin` CLI covers installing, enabling, updating, `validate`, `eval`, `tag` and marketplaces.

The target is also wrong: the docs say `claude-plugins-official` "doesn't take submissions through the directory portal". Listings there go through an Anthropic partner contact ([docs](https://code.claude.com/docs/en/plugins/publish)).

You have two real routes:

**1. Anthropic's directory** (the public catalog on claude.ai, Cowork and Claude Code; [guide](https://claude.com/docs/plugins/submit)). You submit in a browser at **claude.ai/directory/manage**:
1. Choose Submit new, then Plugin bundle.
2. Enter the repository, plugin path and branch, then run Validate.
3. Fill in the listing details, the data-handling questions and the compliance acknowledgements.
4. Submit for review.

Requirements:
- The plugin must be in a github.com repo. It can stay private during review but must be public before it goes live.
- Your GitHub account must be connected on claude.ai with push access to the repo. Private repos also need the Claude GitHub App installed.
- You need a paid claude.ai plan. On Pro or Max you submit from your own account. On Team or Enterprise, an Owner submits, or a member with the Directory permission (Enterprise only).

After you submit:
- Every version is scanned, and publishing goes through Anthropic review.
- Later versions come from your tracked branch, picked up by a push webhook or a scheduled check.
- Users who add your plugin get it in Claude Code as `<name>@synced`.

**2. Your own marketplace.** Commit `.claude-plugin/marketplace.json` to a git repo. Once that file is pushed, the plugin is published; there's no submission step. Users then run:

```bash
claude plugin marketplace add your-org/your-repo
claude plugin install your-plugin@your-marketplace
```

**Authentication:** there's no API key and nothing to authenticate from the CLI. The directory uses your claude.ai login in the browser plus your connected GitHub account. If you once used the old Claude Console submission form, there's a path to move that submission into the portal.

**Before submitting:**
- Run `claude plugin validate --strict ./your-plugin`. The portal runs extra checks beyond this.
- Include a README and a LICENSE.
- Bump `version` for every release.
- Don't use a reserved name. `claude plugin validate` errors on names starting with `claude-` or `anthropic-` ([manifest reference](https://code.claude.com/docs/en/plugins-reference)).
- Optionally run `claude plugin eval`.
## Q4
Yes. Settings hooks now have five handler types:
- **`command`:** runs a shell script, as before.
- **`http`:** POSTs the hook's JSON to a URL. Added in v2.1.63.
- **`mcp_tool`:** calls a tool on one of your MCP servers.
- **`prompt`:** a single model call returns the decision.
- **`agent`:** a subagent can use tools before it decides. This type is experimental.

(Mods, covered in Q6, are a separate mechanism.) Docs: [hooks guide](https://code.claude.com/docs/en/hooks-guide), [hooks reference](https://code.claude.com/docs/en/hooks).

**1. Every Bash command checked by your policy service (HTTP hook)**
```json
{ "hooks": { "PreToolUse": [ { "matcher": "Bash|PowerShell", "hooks": [ {
  "type": "http",
  "url": "https://policy.internal.example.com/claude/pre-tool-use",
  "headers": { "Authorization": "Bearer $POLICY_TOKEN" },
  "allowedEnvVars": ["POLICY_TOKEN"],
  "timeout": 10 } ] } ] } }
```
- **What the endpoint receives:** the same JSON a command hook gets on stdin, including `tool_name`, `tool_input.command`, `cwd` and `session_id`.
- **What it returns:**
  - To block, return 2xx with `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"…"}}`.
  - `"ask"` forces a permission prompt.
  - An empty 2xx body means "no objection".
- **Caveats:**
  - **It fails open.** Status codes alone can't block. A non-2xx response, a connection failure or a timeout is a non-blocking error, so the command runs. If you need fail-closed, use a `command` hook that curls the service and exits 2 when the call fails.
  - **Deny always wins; allow doesn't.** A deny holds even in bypass-permissions mode, but an "allow" can't override deny rules.
  - **Make it hard to remove.** Deploy the hook through managed settings so users can't remove it. A managed `PreToolUse` block also can't be overridden by a user's mod.
  - **URL allowlist.** If your org sets `allowedHttpHookUrls`, add your endpoint to it.
  - **Windows.** The `PowerShell` matcher covers Windows users.

**2. Checking that Claude actually finished (Stop hook)**

There are two options:
- **`type: "prompt"`:** a model reads the hook input (`$ARGUMENTS`) and replies `{"ok": true}` or `{"ok": false, "reason": "…"}`. On `false`, Claude keeps working and uses the reason as its next instruction. Adding `"impossible": true` lets Claude stop anyway. It's cheap, but it only sees the hook input.
- **`type: "agent"`:** better for "actually finished". It starts a verifier that can read files and run commands, for up to 50 tool turns. The default timeout is 60 s, so raise it:
```json
{ "hooks": { "Stop": [ { "hooks": [ { "type": "agent", "timeout": 300,
  "prompt": "Decide if the user's request is fully done. Input: $ARGUMENTS. Read the transcript, check git diff, run the relevant tests. If Claude is just asking the user something, return ok:true; otherwise ok:false with what remains." } ] } ] } }
```

Caveats for Stop hooks:
- `agent` hooks are experimental.
- Stop fires at the end of *every* turn, not only when the task completes, and not on interrupts. Write the prompt so it lets through turns that end with a question to the user.
- Claude Code overrides a Stop hook after 8 blocks in a row with no tool call in between. You can change this with `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`.
- Every stop costs a model run.

For a one-off session, `/goal <condition>` is a built-in, session-scoped version of the prompt-based Stop hook. Its evaluator doesn't run tools ([docs](https://code.claude.com/docs/en/goal)).
## Q5
Package everything as a plugin, distribute it through managed settings, and keep the must-hold guardrails in managed settings themselves.

**1. Package.** Create one private marketplace repo with a `.claude-plugin/marketplace.json` that lists one or a few plugins by relative path. The plugin holds:
- `skills/`
- `hooks/hooks.json` plus its scripts
- both MCP servers

In CI, run `claude plugin validate --strict` and optionally `claude plugin eval`.

**2. Per-engineer token.** Declare it in the manifest's `userConfig` with `"sensitive": true`. Claude Code asks each engineer for the value when the plugin is enabled and stores it in the OS credential store, not in `settings.json`. Reference it as `${user_config.api_token}` in the server's `headers` or `env` ([manifest reference](https://code.claude.com/docs/en/plugins-reference)). If that server can do OAuth, per-user sign-in through `/mcp`, or an org connector on claude.ai, is even simpler.

**3. Distribute.** Don't edit 15 repos. On Team or Enterprise, an Owner pastes this into Organization settings > Claude Code > Managed settings ([docs](https://code.claude.com/docs/en/plugins/org)):
```json
{ "extraKnownMarketplaces": { "acme": { "source": { "source": "github", "repo": "acme/claude-plugins" }, "autoUpdate": true } },
  "enabledPlugins": { "acme-core@acme": true } }
```
- **What this does:** the plugin installs at each engineer's next session start and can't be disabled. Each engineer needs read access to the marketplace repo.
- **Server-managed vs MDM:**
  - Server-managed settings refresh hourly, and they're the only managed source that reaches web sessions.
  - MDM or a `managed-settings.json` file is more tamper-resistant on company laptops, but doesn't reach the web.
  - Server-managed settings apply to everyone in the org; there's no per-group targeting ([docs](https://code.claude.com/docs/en/server-managed-settings)).
- **Optional:** add `strictKnownMarketplaces` if you also want to lock down where plugins can come from.
- **Without admin access:** commit the same two keys to each repo's `.claude/settings.json`. This applies after the folder-trust prompt, and cloud sessions ignore it.

**4. Guardrails.** Put hooks that must always hold directly in managed settings.
- Managed `PreToolUse` blocks are final.
- Hooks anywhere else can be switched off by a user's `disableAllHooks` or overridden by a user's mod.
- Users see an approval dialog for managed hooks.
- HTTP hooks mean you don't have to ship scripts to every machine.

**5. Claude Code on the web** ([docs](https://code.claude.com/docs/en/cloud-environments))
- **What cloud sessions load:**
  - your repo's committed `.claude/` skills, agents and hooks
  - the repo's `.mcp.json` (single-repo sessions only)
  - server-managed settings, including your managed plugins
  - skills enabled on claude.ai
- **What they ignore:** plugins declared in the repo and anything in `~/.claude`.
- **Tokens on the web:** on Team and Enterprise, secrets go in cloud-environment variables, and anyone who uses that environment can read them. Have engineers keep personal tokens in their own environment, not an org-shared one. If you need the same setup locally and on the web, reading an env var (`${ACME_TOKEN}` expansion works in MCP configs) is simpler than `userConfig`.
- **Unconfirmed:** I couldn't confirm two things in the docs, so test them before rollout:
  - how a cloud session clones a *private* marketplace repo
  - how sensitive `userConfig` values behave in cloud sessions
- **Remote MCP servers:** if both servers are remote HTTP servers, `managedMcpServers` (v2.1.259+) can deliver them directly from server-managed settings.

**6. Updates**
- Third-party marketplaces don't auto-update by default. `autoUpdate: true` on the managed entry turns it on and stops users from turning it off.
- Bump `version` with each release, or leave it out so Claude Code tracks the commit SHA.
- Updates download in the background shortly after a session starts. Running sessions pick them up with `/reload-plugins`.
- **Canary channel:** use a second marketplace delivered through endpoint-managed settings.
- **Adoption:** track it with the OpenTelemetry event `claude_code.plugin_loaded`.
## Q6
**What they are.** A mod is a plugin whose `hooks/` folder holds a JavaScript or TypeScript module. Claude Code calls its functions *in-process* on events such as `tool.call`, `tool.check`, `prompt.submit`, `ui.render` and session events. Each function can watch the event, rewrite it, or answer it itself, using a `$` API for UI, files, processes, HTTP, model calls, MCP and storage.

That lets mods do things settings hooks can't:
- draw panes, a band above the prompt, status-line content or toasts
- restyle Claude Code's own UI, except the permission prompt
- add `/commands` that run instantly with no Claude turn
- rewrite prompts or tool output, for example to redact secrets
- share state between handlers

You install a mod like any plugin. Claude can write one for you using the built-in `plugin-authoring` skill, and there are samples in `anthropics/claude-code-playground`. Several built-in features are themselves mods: the `/diff` pane, AGENTS.md loading, telemetry, and the `sec-default` guard ([overview](https://code.claude.com/docs/en/plugins/mods/overview)).

**When they shipped.** Mods were announced on **Oct 1, 2026** ([blog](https://claude.com/blog/claude-code-mods)) in Claude Code **v2.1.287** ([changelog](https://code.claude.com/docs/en/changelog)), and they're on by default. The Desktop app gets them from its bundled v2.1.286. Before that there was a September early-access period behind `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`, which is now ignored.

**How they differ from your settings.json hooks**
- **Settings hooks** are external handlers you configure in JSON: `command`, `http`, `mcp_tool`, `prompt` or `agent`. They can allow, deny or ask on a tool call, adjust tool input, block a stop, or add context. You can write them in any language, a separate process starts for each event, and they run everywhere Claude Code runs. Admins can enforce them through managed settings.
- **Mods** are code that runs inside Claude Code with your full user permissions, and they aren't sandboxed. Their handlers run in every session that loads the plugin. What they *draw* only shows in the terminal and the Desktop app's Code tab, not in the VS Code panel, `-p`, the SDK or cloud sessions.
- **The interaction matters for safety:**
  - A mod that handles `tool.check` can approve a call that a `PreToolUse` hook *outside* managed settings blocked, or that an `ask` rule would have prompted for.
  - Managed `PreToolUse` hooks run before any mod, and their block is final.
  - Deny rules also hold wherever the `sec-default` guard loads, which is on machines with managed settings or with a Team/Enterprise sign-in ([admin docs](https://code.claude.com/docs/en/plugins/mods/admin)).

**Is it worth porting? Mostly not.** Anthropic's admin docs say settings hooks "run as before, alongside mods. Nothing about them is deprecated." Keep guardrails, formatters, notifications and policy checks as settings hooks. They're simpler, work in any language, run on every surface, and can be enforced (put anything security-related in managed settings).

Write a mod when you need something hooks can't do:
- a UI, such as a live context or cost pane, or a confirm-before-`rm -rf` dialog
- rewriting prompts or tool results
- in-process state shared across events
- instant commands
- avoiding a new process on very frequent events

If you manage a team, decide your mod policy now:
- `allowManagedModsOnly` in managed settings keeps user-installed mods from loading.
- `claude plugin validate` lists a mod's hooks and API calls before you install it.
- `--safe-mode` turns mods off when you're debugging.
## Q7
Current limits, from the [MCP docs](https://code.claude.com/docs/en/mcp):

**Output size**
- **Defaults:** Claude Code warns when a result is over 10,000 tokens. The default maximum is 25,000 tokens, set by `MAX_MCP_OUTPUT_TOKENS`.
- **Large results go to a file:** a successful text result over the token limit, or over **50,000 characters** whatever its token count, isn't put inline. Claude Code saves it under the session's `tool-results` directory and gives Claude the file path to read when needed. Your 100k-character schema won't be cut off, but Claude will have to read it from a file in chunks.
- **Per-tool override:** on your server, set `_meta["anthropic/maxResultSizeChars"]` on the tool in `tools/list`, up to a hard ceiling of **500,000 characters**. It applies to text content regardless of `MAX_MCP_OUTPUT_TOKENS`, so users don't need to change anything. Images still count against the token limit.

**Long-running calls**
- **Overall timeout:** a per-server `"timeout"` (milliseconds) in `.mcp.json`, otherwise `MCP_TOOL_TIMEOUT`. The default is about 28 hours. Progress notifications don't extend it.
- **Idle timeout:** a call is aborted if it gets no response and no progress notification within the idle window. That window is **5 minutes for HTTP, SSE, WebSocket and claude.ai connector servers** and **30 minutes for stdio**. You can change it with `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT`. A per-server `timeout` also sets a minimum for it (v2.1.203+).
- **HTTP and SSE first byte:** each request must get its first response byte within the largest of 60 s, the server's tool timeout, and `MCP_TIMEOUT`.
- **Backgrounding:** a call from the main conversation that's still running after 2 minutes moves to a background task (v2.1.212+, `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`). Claude keeps working and gets notified when it finishes. This doesn't apply to calls from subagents or `-p` runs.
- **MCP Tasks:** I found no sign that Claude Code supports MCP Tasks (SEP-1686, call now and fetch the result later) yet. There's an open request ([#76571](https://github.com/anthropics/claude-code/issues/76571)), so don't rely on it.

**What to do on the server**
1. **Make the schema browsable instead of dumping it.** Offer tools such as `list_tables`, `describe_tables(names)` and `search_schema(query)` with cursors and compact DDL. Keep a full-dump tool for when it's truly needed, and annotate it with `anthropic/maxResultSizeChars` (for example 300000).
2. **Keep the slow HTTP tool alive.** Start a streaming (SSE) response straight away so the first byte goes out well under 60 s. Then send `notifications/progress` (using the request's `progressToken`) every 30–60 s to reset the idle timer. Make sure proxies and load balancers don't drop idle streams.
3. **Ship a per-server timeout** in the shared config, for example `"timeout": 1200000`. This raises the first-byte timer and the idle minimum as well.
4. **Use a job pattern for slow or flaky work.** If a run can go past roughly 10–20 minutes or is unreliable, have `start_job` return an ID immediately and let `job_status` / `job_result` poll. Make the tools idempotent and respect cancellation.
5. **Keep error results short and actionable.**
## Q8
Use **something else**: a **dynamic workflow** ([docs](https://code.claude.com/docs/en/workflows)). Claude writes a JavaScript orchestration script, and a runtime executes it in the background. The script fans work out to subagents and cross-checks their findings. Intermediate results live in script variables rather than Claude's context.
- **Scale:** it handles hundreds of agents: up to 1,000 per run, with 16 running at once by default (adjustable up to 256).
- **Resumable:** you can resume a run in the same session.
- **Reusable:** you can save it as a command and rerun it.
- **Fit:** the docs' own example is "audit every route handler … for missing authentication checks, and adversarially verify each finding before reporting it."

**Why not the other two** ([comparison](https://code.claude.com/docs/en/agents)):
- **Plain subagents:** Claude coordinates them one turn at a time, every result lands in its context, and only 20 can run at once. At 600 handlers, results get dropped and the work gets sloppy.
- **Agent teams:** they're experimental and off by default. They're designed for a handful of long-running peers working together, and they have no built-in verification step.

**Setup**
1. **Inventory the routes deterministically.** Dump the ~600 routes from the router, or with an AST script, into a file. Then you can check that every route ends up as safe, a finding, or exempt.
2. **Write a rubric**, such as `AUTHZ.md`, that spells out:
   - what counts as authorization in your codebase: middleware, decorators, policy calls, ownership or tenant checks (as opposed to just being logged in)
   - where global or router-level guards live
   - which routes are public on purpose
3. **Prompt for the workflow:**
   `ultracode: use a workflow to audit every route in routes.json for missing authorization per AUTHZ.md. Batch ~15 handlers per auditor; return structured findings (route, file:line, missing check, call-chain evidence). For each finding run 2 independent verifiers told to refute it (trace middleware, router guards, gateway config). Report only findings both confirm, list unverifiable ones separately, and account for every route.`
4. **Size and pilot.**
   - The default size guideline is `medium` (fewer than 10 agents). For this run, set `/config workflowSizeGuideline=unrestricted`.
   - Expect the advisory "Large workflow" warning.
   - Try one module first to calibrate cost and the false-positive rate.
   - Pre-allow read-only tools so hundreds of agents don't each prompt you.
   - Ask for a cheaper model on the first audit pass and the strongest one for verification.
5. **Watch and save.** Follow the run in `/workflows`. When you're happy with it, press `s` to save it to `.claude/workflows/`, then rerun it as `/audit-authz`. It can also run in CI with `claude -p` and a `Workflow(audit-authz)` allow rule.

Workflows are on all paid plans; on Pro, turn them on in `/config`. "Verified" here means two independent agents failed to refute a finding. That isn't proof, so have a person review each confirmed finding and turn it into a failing test before you fix it.
