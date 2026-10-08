## Q1
Your existing agent files still work. They're the same Markdown-plus-YAML files in `.claude/agents/` or `~/.claude/agents/`. Most of what changed is the tooling and behaviour around them.

**Creating and managing**
- **The `/agents` wizard is gone.** It was removed in v2.1.198 (mid-2026). `/agents` now only tells you to ask Claude ("create a subagent that…") or to edit the files yourself. `claude agents` is a different command: it opens the view for background sessions.
- **Bad files are skipped silently.** This happens when `name` or `description` is missing, when `name` starts with `-` or contains `:`, or when the YAML is invalid. Check yours with `claude plugin validate .claude/agents` (v2.1.233+).
- **New frontmatter fields.** `disallowedTools`, `permissionMode` (now including `auto`), `maxTurns`, `skills` (preloaded in full), `mcpServers` (scoped to that agent), `hooks`, `memory` (`user`, `project` or `local` persistent memory), `background`, `effort`, `isolation: worktree`, `omitClaudeMd`, `initialPrompt`.
  - `model` now also accepts `fable` and `inherit`.
  - `tools: Agent(worker, reviewer)` limits which agents this agent may spawn.
- **Invoking a specific agent.** `@"code-reviewer (agent)"` guarantees that agent is used, and `claude --agent code-reviewer` runs the whole session as it.
- **The Task tool is now called `Agent`** (v2.1.63, Feb 2026). `Task(...)` permission rules still work as aliases. Hook payloads now report `tool_name: "Agent"`, though, so hooks that matched `Task` silently stopped firing ([#29677](https://github.com/anthropics/claude-code/issues/29677)).
- **Folder trust.** Hooks and inline MCP servers in a *project* agent's frontmatter now only load after you trust the folder.

**How they behave**
- **Background by default.** In interactive sessions, subagents now run in the background, and their permission prompts surface in your main session.
  - Background subagents lose `Agent`, `AskUserQuestion`, the plan-mode tools and `Workflow`.
  - An agent designed to ask you questions will therefore behave differently than it did last fall.
- **Nesting and concurrency.** Subagents can spawn subagents, 3 levels deep by default since v2.1.219. Change the depth with `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`; `1` turns nesting off. At most 20 run at once.
- **Forks.** A fork (`subagent_type: "fork"`, or `/subtask` yourself) inherits the whole conversation and its prompt cache. Forks have been on by default in interactive sessions since v2.1.232. Your custom agents still start with a fresh context.
- **Model precedence** (since v2.1.251): the per-call `model`, then the agent's `model`, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the session model. To pin every subagent to one model, set `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`.
- **Built-in agents.** Explore no longer runs on Haiku; it uses your session's model (Opus if the session runs Fable). New built-in agents are `claude`, `claude-code-guide`, `statusline-setup` and `fork`.
- **Resuming.** A finished subagent can be resumed with `SendMessage` using its agent ID.

Sources: [sub-agents docs](https://code.claude.com/docs/en/sub-agents), [changelog](https://code.claude.com/docs/en/changelog), [run agents in parallel](https://code.claude.com/docs/en/agents).

## Q2
**Shape.** Put each skill in its own folder, `.claude/skills/<skill-name>/SKILL.md`, committed to the repo (or under `skills/` in a plugin). The file is YAML frontmatter followed by Markdown instructions.
- Keep the body under about 500 lines. Move detail into `references/` or `scripts/`, and point to those files with `${CLAUDE_SKILL_DIR}/…`.
- Every skill is also a `/name` command. Slash commands and skills are now one mechanism.

**Frontmatter Claude Code accepts.** Every field is optional, but always write a `description`.
- `name`: defaults to the folder name.
- `description` and `when_to_use` (appended to the description).
- `argument-hint` and `arguments`: named `$args`, alongside `$ARGUMENTS` and `$0`.
- `disable-model-invocation`: manual-only, and also removes the skill from Claude's listing. `user-invocable`.
- `allowed-tools`: pre-approves tools for the invoking turn only. It restricts nothing, and workspace trust doesn't gate it. `disallowed-tools`.
- `model`, `effort`, `context: fork`, `agent`, `background`, `shell`.
- `hooks`, `paths` (globs that limit when the skill activates), `metadata`, `license`, `compatibility` (≤500 characters).

Misspelled or unknown keys are ignored without any error. Malformed YAML (an unquoted colon, for example) loads the skill with no metadata, so it never auto-triggers. Lint with `claude plugin validate .claude/skills`.

**Description length in Claude Code**
- `description` plus `when_to_use` is truncated at **1,536 characters** in the skill listing. You can change that with `skillListingMaxDescChars`.
- The whole listing gets about **1% of the context window** (`skillListingBudgetFraction`). Once you have many skills, the least-used ones lose their descriptions first, and only their names stay.
- So put the trigger words first. `/context` and `/skill-doctor` show what your skills cost.
- After compaction, only the first 5k tokens of an invoked skill survive, so put critical rules at the top.

**What's different on claude.ai (and the Skills API)**
- **Only six keys are accepted:** `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. Any other key (`when_to_use`, `argument-hint`, `context`…) makes the upload fail with `Unexpected key(s) in SKILL.md frontmatter`.
- **`name` and `description` are both required.**
  - `name`: lowercase letters, digits and hyphens, at most 64 characters, and it must match the folder name. The API docs also reserve "anthropic" and "claude".
  - `description`: at most **1,024 characters**, with no XML tags.
  - The Help Center page still says 200 characters and shows a `dependencies` field. The current docs and the spec supersede it.
- **Uploading:** upload a ZIP whose top level is the skill folder, under Customize → Skills. Team and Enterprise plans can Share or Publish to org.
- **Body features:** `` !`cmd` `` injection doesn't run in chat. `${CLAUDE_SKILL_DIR}` resolves only in Claude Code and Cowork, so also make script paths work relative to SKILL.md.
- **Sync back to Claude Code:** skills enabled on claude.ai sync one-way into Claude Code (v2.1.273+, claude.ai login only).
  - A synced skill whose name clashes with a local one becomes `/anthropic-skills:<name>`.
  - On your machine, a synced skill's body doesn't run `!` commands.

**Practical rule.** For skills you'll use in both places, stick to spec-only frontmatter and a description of 1,024 characters or less, with the `when_to_use` text folded into it. Use Claude Code-only keys only in skills that will never be uploaded.

Sources: [Claude Code skills](https://code.claude.com/docs/en/skills), [claude.com: create custom skills](https://claude.com/docs/skills/how-to), [Agent Skills spec](https://agentskills.io/specification), [API skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Q3
There isn't one. The `claude plugin` CLI has no `publish` or `submit` subcommand. It has `validate`, `tag`, `eval`, `init` and so on, but nothing that sends a plugin to Anthropic.

You also can't submit straight into `claude-plugins-official`. That marketplace is curated: Anthropic's own plugins plus partner plugins. The docs say it "doesn't take submissions through the directory portal"; partners arrange a listing through their Anthropic contact.

**Option 1: Anthropic's directory**, through the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage) (short link `clau.de/plugin-directory-submission`).
1. Push the plugin to a GitHub repo, and run `claude plugin validate --strict ./your-plugin`.
2. In the portal, choose **Submit new → Plugin bundle**. Enter the repo, the plugin path and the branch or tag, then click **Validate**.
3. Check the listing details, which come from `plugin.json` and the README. Answer the data-handling questions, accept the compliance acknowledgements, and click **Submit for review**.
4. Every version gets automated validation and a security scan. A person reviews a new listing before it goes live, and by default a reviewer publishes each passing version.
5. Later releases flow from pushes to the tracked branch (via the GitHub webhook or a scheduled check). Each organization can make 10 submissions per 24 hours.

**Option 2: your own marketplace, today.** Add `.claude-plugin/marketplace.json` to the repo and push. Users then run `/plugin install <name> --marketplace <owner>/<repo>` (v2.1.275+). There's no review and no form.

**Authentication.** Submission uses your **claude.ai login, not an API key**. The old Claude Console form is retired.
- You need a paid plan. On Pro or Max, you submit from your own account. On Team or Enterprise, an Owner submits, or an Enterprise member with a custom role that has the Directory permission.
- Your GitHub account must be connected on claude.ai and have push access to the repo.
- The repo can stay private during review, as long as the Claude GitHub App is installed and you consent to the source upload. It must be public before the listing goes live.

**Where an approved plugin shows up**
- It's listed in the claude.ai directory. People who add it there get it in Claude Code through account sync, as `<name>@synced`.
- Approved third-party plugins also appear in the read-only community marketplace, which syncs nightly from the same review pipeline. Add it with `/plugin marketplace add anthropics/claude-plugins-community` and install from `@claude-community`.

Sources: [Publish a plugin](https://code.claude.com/docs/en/plugins/publish), [Submit your plugin](https://claude.com/docs/plugins/submit), [Publish to the directory](https://claude.com/docs/directory/publish), [Anthropic's marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces), [community repo](https://github.com/anthropics/claude-plugins-community).

## Q4
Yes. Besides `command`, hooks can now be `http`, `mcp_tool`, `prompt` (one model call) or `agent` (a subagent with tools, still experimental). Mods are a separate, newer mechanism (see Q6).

**1. Policy check on every Bash command: a PreToolUse `http` hook**
```json
{"hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [{
  "type": "http",
  "url": "https://policy.internal.example.com/claude/pretooluse",
  "headers": {"Authorization": "Bearer $POLICY_TOKEN"},
  "allowedEnvVars": ["POLICY_TOKEN"],
  "timeout": 10
}]}]}}
```
- **Request:** Claude Code POSTs the same JSON a command hook gets on stdin, including `tool_input.command`, `cwd`, `session_id` and `permission_mode`.
- **Response:** to block, return **2xx** with `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"…"}}`. `"ask"` forces a prompt. An empty 2xx body leaves the decision to your normal permission rules. Status codes alone can't block.
- **Rules interaction:** a hook's `deny` holds even in `bypassPermissions`. A hook's `allow` never overrides your own deny or ask rules.
- **It fails open.** A non-2xx response, a timeout or a connection failure is a non-blocking error, and the command runs anyway. If you need fail-closed, use a `command` hook that calls the service and exits 2 on any failure.
- **Timeout:** set it explicitly; the default is 600 s.
- **Where to put it:** in managed settings, so users can't remove it and a user-installed mod can't override its block. Admins can restrict endpoints and header variables with `allowedHttpHookUrls` and `httpHookAllowedEnvVars`.
- **Windows:** also match `PowerShell`.

**2. "Is it really done?" check: a Stop hook of type `prompt` or `agent`**
```json
{"hooks": {"Stop": [{"hooks": [{
  "type": "agent",
  "prompt": "Check whether the user's request is actually complete: inspect the diff and run the relevant tests. $ARGUMENTS",
  "timeout": 300
}]}]}}
```
- **Response:** both types return `{"ok": true}` or `{"ok": false, "reason": "…"}`. The reason becomes Claude's next instruction.
- **`prompt` hooks** make one call to the small background model (change it with `model`). The model sees the hook input, which includes `last_assistant_message`. It can also return `"impossible": true` to let the turn end.
- **`agent` hooks** can read files, search and run checks for up to 50 turns. The default timeout is only 60 s, so raise it.
- **Cost:** Stop fires after *every* response, including clarifying questions. Write the prompt so it allows those, and budget for the extra calls.
- **Loop guard:** after 8 consecutive blocks with no tool call in between, Claude Code lets Claude stop anyway (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` raises the limit).
- **Ad hoc version:** `/goal <condition>` is a built-in, per-session version of the same idea.

Sources: [hooks guide](https://code.claude.com/docs/en/hooks-guide), [hooks reference](https://code.claude.com/docs/en/hooks), [permissions](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks), [/goal](https://code.claude.com/docs/en/goal).

## Q5
**Recommendation:** one plugin in a private marketplace repo, pushed to everyone with **server-managed settings**, with per-user auth for the token-bearing MCP server.

**1. Package.** Create a private repo (say `acme/claude-plugins`) containing `.claude-plugin/marketplace.json` and one plugin, `acme-std`. The plugin holds:
- `skills/` and `hooks/hooks.json`;
- `.mcp.json` with both MCP servers;
- a `userConfig` entry for the personal token:
  ```json
  "userConfig": {"api_token": {"type": "string", "title": "API token", "description": "Your personal token", "sensitive": true}}
  ```
  Each engineer is prompted for it, or sets it via `/plugin` → Configure options. Claude Code stores the value in the OS keychain, and you reference it as `${user_config.api_token}` in that server's `env` or `headers`.

Run `claude plugin validate --strict` in CI. Either bump `version` on every release or leave it out so installs follow commits. A forgotten bump leaves everyone on the old version.

**2. Distribute.** In the claude.ai admin console, go to Organization settings → Claude Code → Managed settings and add:
```json
{"extraKnownMarketplaces": {"acme": {"source": {"source": "github", "repo": "acme/claude-plugins"}, "autoUpdate": true}},
 "enabledPlugins": {"acme-std@acme": true}}
```
- This turns the plugin on for every machine and every repo, and users can't disable it.
- `autoUpdate` matters: auto-update is off by default for non-Anthropic marketplaces. Updates download in the background and apply at the next start or on `/reload-plugins`.
- Engineers need git read access to the repo (`gh auth setup-git`, for example).
- Optionally lock sources down with `strictKnownMarketplaces`.
- **Alternative:** Organization settings → *Plugins & skills* syncs the repo through the org's GitHub connection, so engineers need no git credentials. It only reaches people signed in with claude.ai on v2.1.273+, though, and it rejects plugins with a top-level `bin/`.

**3. Guardrails.** Hooks that must hold belong in the managed settings themselves, as `http` hooks or self-contained commands. A user-installed mod can override a plugin hook's PreToolUse block, but not a managed one.

**4. Claude Code on the web.**
- **Doesn't load:** plugins enabled by a repo's `.claude/settings.json`, or anything from `~/.claude`.
- **Does load:** server-managed settings (the session waits for them before installing plugins), plus each repo's committed `.claude/skills/`, `.claude/settings.json` hooks and `.mcp.json` in single-repo sessions.
- **Per-user credentials:**
  - **Best:** make the token-bearing server a remote MCP server with OAuth, and have an admin add it as an org connector on claude.ai. Each engineer signs in once, and it works in the CLI (with claude.ai login) and in cloud sessions.
  - **Fallback:** each engineer puts the token in an env var in their *own* cloud environment. Anyone who uses an environment can read its env vars, so never use a shared one.
- **Unknown:** I couldn't find documentation on how a `sensitive` userConfig value behaves in cloud sessions, which have no keychain. Test that before you rely on it.

Sources: [org plugin management](https://code.claude.com/docs/en/plugins/org), [host a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace), [manifest/userConfig](https://code.claude.com/docs/en/plugins/manifest-reference), [cloud environments](https://code.claude.com/docs/en/cloud-environments), [claude.ai connectors](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claude-ai), [org rollout](https://claude.com/docs/plugins/org-rollout).

## Q6
**What a mod is.** A mod is a plugin whose JavaScript or TypeScript "hooks module" (for example `hooks/register.js`, referenced from `hooks/hooks.json`) exports `register(on)`.
- Its handlers run *inside* the Claude Code process on events such as `tool.call`, `tool.check`, prompts, turns and `ui.render`.
- A handler can observe an event, rewrite it, or handle it entirely.
- Through the mods API, a mod can draw panes and bands, restyle the spinner and tool rows, add `/commands` that run code without a Claude turn, call models, read files and make network requests.
- Claude Code's own `/diff` and AGENTS.md loading are built-in mods.

**When they shipped.** "Added Claude Mods" is in v2.1.287, released **Oct 1, 2026**, with mods on by default in the terminal. In the Desktop app they work from its bundled v2.1.286.
- Before that they were early access behind `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`, which is now ignored.
- The API is days old, and fix releases are still landing.

**How they differ from settings hooks**

| | Settings hook | Mod |
|---|---|---|
| What you write | A `command`/`http`/`mcp_tool`/`prompt`/`agent` entry in settings.json | JS/TS functions, installable only as a plugin |
| Where it runs | A separate process or HTTP request | In-process and unsandboxed; `/sandbox` doesn't cover it |
| What it can do | Block, allow or ask; rewrite tool input or output; add context | All of that, plus UI, commands, model calls, rewriting prompts and requests, and state shared between handlers |
| Permission power | A hook's `allow` can't beat your deny or ask rules | `tool.check` answers *after* rules and hooks. It can approve ask-rule calls, override non-managed PreToolUse blocks, and skip the auto-mode classifier |

Mods and deny rules: deny rules hold over mods by default only on machines with managed settings or a Team/Enterprise sign-in. Anywhere else, a mod can override a deny rule too.

Where they run: mod hooks run in the terminal, Desktop, VS Code and `-p`/SDK, but a mod's UI draws only in the terminal and Desktop.

**Should you port your hooks? Mostly no.**
- Settings hooks aren't deprecated. Anthropic's own comparison says to use a settings hook to block, allow or log with a script you already have, and a mod when you want a pane, a command, or to rewrite events.
- Keep guardrails as settings hooks, ideally managed ones. They're language-agnostic, auditable and run out of process. A managed PreToolUse block is also something a mod can't override.
- Port a hook only when it needs UI, in-process state, or to hold a call while it asks the user. The `blast-radius` sample does that last one.

Because a mod can undo your guardrails, review any mod before you install it: `claude plugin validate ./mod` lists its `hooks:` and `calls:`. Admins can restrict mods with `allowManagedModsOnly`.

Sources: [mods overview](https://code.claude.com/docs/en/plugins/mods/overview), [permissions: extend with hooks](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks), [changelog](https://code.claude.com/docs/en/changelog).

## Q7
**Output limits**
- **Thresholds.** Claude Code warns when a tool result exceeds 10k tokens. The default cap is `MAX_MCP_OUTPUT_TOKENS` = 25,000. A separate threshold applies to text results: anything over **50,000 characters** goes to disk regardless of its token count.
- **What happens over either limit.** The result isn't truncated. Claude Code saves it to the session's `tool-results` directory and gives Claude the file path, so Claude reads or greps it as needed. Error results (`isError: true`) over about 11k characters are cut to the first 5k and last 5k.
- **Server-side override.** Add `_meta["anthropic/maxResultSizeChars"]` to the tool's `tools/list` entry, up to 500,000. For text, it replaces both the 50k-character threshold and the token cap, so users don't need to set anything.
- **Inlining isn't free.** A 100k-character schema costs roughly 25–35k tokens of context every time it's returned inline. Usually better:
  - offer `list_tables`, `describe_tables(names)` and `search_schema(pattern)` tools;
  - paginate, and return compact DDL;
  - let the rare full dump spill to a file.
- **Descriptions.** Tool descriptions and server instructions are truncated at 2,048 characters, and Tool Search defers all MCP tools by default. Put the key words first.

**Long-running calls**
- **Wall clock:** the per-server `timeout` (in ms) in the server config. If that's unset, `MCP_TOOL_TIMEOUT`; if that's unset too, about 28 hours. Progress notifications don't extend it.
- **Idle timeout:** a call with no response *and no progress notification* for 5 minutes is aborted. That's the limit for HTTP, SSE, WebSocket and claude.ai connector servers; stdio servers get 30 minutes. Change it with `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT`. A per-server `timeout` of 1000 ms or more also acts as a floor for the idle timeout (v2.1.203+).
- **HTTP first-byte timer:** each HTTP request must start responding within max(60 s, the tool timeout, `MCP_TIMEOUT`). With default settings, a plain JSON response that only arrives after 5 minutes fails at 60 s.
- **Backgrounding:** main-conversation calls still running after 2 minutes become background tasks (v2.1.212+), so the session isn't blocked. Calls from subagents or `-p` aren't backgrounded.

**What to do on the server**
1. Over Streamable HTTP, answer the long tool with an SSE stream right away. Send `notifications/progress` every 30–60 s; that keeps the idle timer alive and shows progress in `/tasks`.
2. Ship a recommended `"timeout": 900000` in the `.mcp.json` or plugin config you hand out.
3. For work that may outlive a session or run inside subagents, use a job pattern: `start_*` returns an ID, then `get_*_status` and `get_*_result` poll it. Make these calls idempotent.
4. Claude Code doesn't document support for the MCP Tasks extension, so don't build on it yet.

Source: [Claude Code MCP docs](https://code.claude.com/docs/en/mcp) (output limits, timeouts, tool search).

## Q8
Use a **dynamic workflow**. It's built for exactly this job, and the docs' own example prompt is "use a workflow to audit every route handler under src/routes/ for missing authentication checks, and adversarially verify each finding before reporting it".

**Why not the alternatives**
- **Subagents:** Claude orchestrates them turn by turn, and every result lands in its context. That's fine for a few side tasks, not 600 items.
- **Agent teams:** still experimental and off by default. They're meant for a handful of long-running peers, and the docs estimate about 7× the tokens of a normal session.
- **Workflows:** a JS script the runtime executes.
  - Intermediate results stay in script variables rather than in Claude's context.
  - A run can use dozens to hundreds of agents (16 concurrent by default, 1,000 per run), and it can resume within the session.
  - Verify-before-report is a pattern the script can encode.

**Setup**
1. From the main session, type `ultracode: …` or "use a workflow to …". On Pro, first enable Dynamic workflows in `/config`. Read the script before approving it (`Ctrl+G` or **View raw script**).
2. Ask for explicit phases:
   - **Inventory.** Produce a schema'd list of every handler (file, line, method, path). Also describe how auth is *actually* applied: global middleware, router-level guards, decorators, gateway rules. Missing this is where most false positives come from.
   - **Audit.** Run `pipeline()` over batches of about 10–20 handlers. Each agent returns JSON: a verdict, an evidence chain with file:line references, and a confidence.
   - **Verify.** For each candidate finding, 2–3 independent agents try to prove the route *is* protected by tracing middleware and mounts. Keep only the findings that survive a majority vote. Label the ones that couldn't be checked "unverified", not confirmed. Optionally, have an agent write a failing integration test or an unauthenticated request for each survivor.
   - **Report.** Deduplicate, rank by severity, and include the evidence.
3. The default size guideline is `medium` (under 10 agents). Raise it with `/config workflowSizeGuideline=large`, or ask for scale explicitly ("~60 audit agents").
4. Pilot on one service first, and watch token use in `/workflows`. Consider a cheaper model for the inventory phase and your strongest model for verification.
5. Pre-allow read-only tools so agents don't stall on permission prompts. Then press `s` in `/workflows` to save the script as `/audit-routes` for future runs.

Sources: [dynamic workflows](https://code.claude.com/docs/en/workflows), [run agents in parallel](https://code.claude.com/docs/en/agents), [costs](https://code.claude.com/docs/en/costs).
