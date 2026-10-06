## Q1
Your existing agents keep working. They're still Markdown files with YAML frontmatter in `.claude/agents/` (project) or `~/.claude/agents/` (user), and `/agents` still creates and edits them. Here's what has changed.

**Creating and managing them**
- **More frontmatter fields** beyond `name`, `description`, `tools`, `model` and `color`:
  - `disallowedTools`
  - `permissionMode` (`default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`)
  - `maxTurns`
  - `skills`: preloads named skills. Subagents don't inherit your skills otherwise.
  - `mcpServers`: MCP servers scoped to just that agent.
  - `hooks`: PreToolUse/PostToolUse/Stop that apply only while the agent runs.
  - `memory: user|project|local`: a persistent memory directory with a `MEMORY.md` the agent reads and updates across sessions.
  - `background: true`
  - `isolation: worktree`: runs the agent in a temporary git worktree.
- **More places to define them.** `claude --agents '<json>'` adds session-only agents. Plugins can ship agents, but plugin agents ignore `hooks`, `mcpServers` and `permissionMode`.
- **Run your main session as an agent** with `claude --agent <name>` (or the `agent` setting). In that mode, `tools: Agent(worker, reviewer)` restricts which subagents it may spawn.
- **The Task tool is now called `Agent`.** Old `Task(...)` permission rules still work as aliases, and a deny rule like `"Agent(Explore)"` turns off a specific agent.

**How they behave when Claude uses them**
- **Built-in agents:** Explore (Haiku, read-only) and Plan. Claude now routinely hands codebase searches to Explore, so you'll see more delegation even without your custom agents.
- **Background subagents** run concurrently: ask for it, or press Ctrl+B on a running one. Their permissions are requested up front, and anything not pre-approved is auto-denied while they run.
- **Resumable subagents:** Claude can continue an earlier subagent with its full history instead of starting cold. Subagents keep their own transcripts and auto-compact.
- **New hook events:** `SubagentStart` and `SubagentStop`, which you can match on the agent type.
- **Unchanged:** delegation is still driven by `description`, subagents still get only their own system prompt plus environment details, and subagents still can't spawn subagents.
- **A separate, newer feature:** agent teams (experimental, enabled with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). These are several full sessions that share a task list and message each other. They aren't a replacement for subagents.

**Worth doing now with your old agents**
- Set `model` explicitly (`sonnet`/`opus`/`haiku`/`inherit`) instead of relying on the default.
- Tighten `tools`, or use `disallowedTools`.
- Add `skills` or `memory` where an agent would benefit.
## Q2
A skill is a folder: `.claude/skills/<name>/SKILL.md` for a project (`~/.claude/skills/` for personal use, `skills/` inside a plugin), plus any reference files and scripts that `SKILL.md` links to.

```markdown
---
name: api-conventions
description: Applies Acme REST conventions (naming, pagination, error envelopes). Use when writing or reviewing HTTP endpoints or OpenAPI specs.
---
# API conventions
Core rules here. Edge cases: see [reference.md](reference.md).
```

**Frontmatter Claude Code supports**
- `name`: lowercase letters, digits and hyphens, max 64 characters. It defaults to the folder name, so keep the two the same.
- `description`: what the skill does and when to use it. Without one, Claude Code falls back to the first paragraph, which is a poor substitute.
- `argument-hint`
- `disable-model-invocation: true`: only you can run the skill, via `/name`.
- `user-invocable: false`: hides it from the `/` menu, so only Claude loads it.
- `allowed-tools`: tools pre-approved while the skill is active.
- `model`
- `context: fork` plus `agent`: runs the skill in a forked subagent.
- `hooks`: hooks scoped to the skill.
- The open-standard fields `license`, `compatibility` and `metadata` are accepted. A few newer keys have landed in recent releases (I believe an `effort` override is one), so check the frontmatter reference for your version before relying on them.
- The body can use `$ARGUMENTS`/`$0`/`$1`, `${CLAUDE_SESSION_ID}`, and `` !`cmd` `` to inject a command's output before Claude sees the skill.
- `.claude/commands/*.md` files still work, because slash commands and skills are now the same mechanism.

**Description length**
- The Agent Skills spec, the API and claude.ai all cap `description` at 1,024 characters.
- Claude Code won't reject a longer one, but the skill listing Claude sees has a budget of roughly 2% of the context window, with a 16k-character fallback. You can raise it with `SLASH_COMMAND_TOOL_CHAR_BUDGET`.
- Skills that don't fit get dropped from that listing, and `/context` warns you when that happens. Long individual descriptions are also truncated in the listing; I'm not certain of the exact per-skill cap in current builds.
- So: stay under 1,024 characters, put the trigger words in the first sentence, and keep the body under about 500 lines, moving detail into linked files.

**claude.ai differences**
- **Upload:** a ZIP of the skill folder, through the Skills section of Settings, with code execution enabled.
- **Scope:** an uploaded skill is per-user unless a Team/Enterprise owner provisions it org-wide. Nothing syncs between claude.ai, Claude Code and the API, so build all three from one repo.
- **Validation at upload:** `name` and `description` are both required, the name is max 64 characters and the description max 1,024, neither can contain XML tags, and "anthropic" or "claude" can't appear in the name.
- **What applies:** only `name`, `description`, `license` and `metadata` mean anything there. The Claude Code-only keys, `$ARGUMENTS`, `` !`cmd` `` injection, hooks and forked context don't apply. I'm not sure whether the uploader ignores unknown keys or rejects them, so test one upload, or generate a stripped-down frontmatter for the claude.ai build.
- **Scripts** run in Anthropic's sandbox, not on your machine. They get none of your local tools or credentials, and network access depends on your org's settings.
## Q3
There is no `claude plugin publish` command. If you saw one mentioned somewhere, check `claude plugin --help` on your version, but as far as I know the plugin CLI only consumes and checks plugins:
- `install`, `uninstall`, `enable`, `disable`, `update`
- `marketplace add|list|update|remove`
- `validate`

Distribution is git-based, and the official marketplace is curated, not self-serve.

**Getting into claude-plugins-official** (the `anthropics/claude-plugins-official` repo, which Claude Code adds automatically):
1. Put the plugin in a public Git repo (GitHub is simplest), with `.claude-plugin/plugin.json` (name, version, description, author), a README and a license.
2. Run `claude plugin validate .` and test-install it from a local dev marketplace.
3. Submit it through Anthropic's plugin directory submission form, linked from that repo's README and the plugin docs. Anthropic reviews for quality and security, and acceptance isn't guaranteed. I don't believe a PR straight to the repo is the intake path for third-party plugins.

**Auth:** neither applies. There's no CLI upload, so you don't pass an API key and the CLI doesn't use your claude.ai login. You just fill in the form in a browser.

**Meanwhile, publish it yourself.** Add `.claude-plugin/marketplace.json` to a repo:

```json
{
  "name": "acme-plugins",
  "owner": { "name": "Acme" },
  "plugins": [
    { "name": "my-plugin", "source": "./plugins/my-plugin", "description": "..." }
  ]
}
```

Users then run `/plugin marketplace add your-org/your-repo` followed by `/plugin install my-plugin@acme-plugins`.
- Private repos use the user's existing git credentials. Background auto-updates need a token such as `GITHUB_TOKEN` in the environment.
- Bump `version` in `plugin.json` on each release so clients pick up the update.
## Q4
Yes. Besides `type: "command"`, hooks support three more types:
- `"http"`: POSTs the event JSON to a URL.
- `"prompt"`: a single LLM call that returns a yes/no decision.
- `"agent"`: a subagent with tool access that investigates before deciding.

**1. Check every Bash command with your policy service (HTTP hook)**

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "http",
        "url": "https://policy.internal.example.com/claude/pretooluse",
        "headers": { "Authorization": "Bearer $POLICY_TOKEN" },
        "allowedEnvVars": ["POLICY_TOKEN"],
        "timeout": 10
      }]
    }]
  }
}
```

- **What your endpoint receives:** the same JSON a command hook gets on stdin, including `session_id`, `cwd`, `tool_name` and `tool_input.command`.
- **To block:** return a 2xx with `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"..."}}`. Claude sees the reason.
- **To stay out of the way:** return an empty 2xx and the normal permission flow continues. Returning `"allow"` skips the permission prompt; `"ask"` forces one.
- **Caveat: this fails open.** A status code alone can't block. Non-2xx responses, timeouts and connection errors are all treated as non-blocking, so the command runs anyway. If you need fail-closed, use a command hook that pipes stdin to `curl -sf` and exits with code 2 on any failure.
- **Headers** only interpolate environment variables you list in `allowedEnvVars`.
- **For enforcement**, ship this in managed settings. I believe managed settings can also allowlist HTTP hook targets via `allowedHttpHookUrls`.

**2. Verify the task is actually done before Claude stops (agent Stop hook)**

```json
"Stop": [{
  "hooks": [{
    "type": "agent",
    "prompt": "Decide whether the user's request in this session is fully complete: requested changes made, tests pass, no leftover TODOs. Run the tests if relevant. Hook input: $ARGUMENTS",
    "timeout": 180
  }]
}]
```

- **How it decides:** the agent can read files and run checks, then replies `{"ok": true}` or `{"ok": false, "reason": "..."}`.
- **On `ok: false`:** Claude doesn't stop. It keeps working, with your reason as the instruction.
- **Cheaper option:** `type: "prompt"` makes one LLM call with no tools. Both types default to a fast model, and you can set `model` to change that.
- **Avoid loops:** keep the criteria objective. The hook input includes `stop_hook_active`, so tell the agent to approve unless something is clearly unfinished when that flag is already true.
- **Cost:** every stop adds latency and tokens.
- **Hard checks:** for tests and lint, a plain command Stop hook that exits 2 is deterministic and cheaper. Many teams run both kinds.
## Q5
Package everything as **one internal plugin** in a private Git **marketplace** repo, and turn it on through settings instead of copying files into 15 repos.

**Plugin layout**
- `skills/`
- `.mcp.json` with both servers
- `hooks/hooks.json`
- `.claude-plugin/plugin.json` with a `version`
- `${CLAUDE_PLUGIN_ROOT}` for paths to any bundled scripts

**Distribution**
- **Per repo:** commit `.claude/settings.json` with `extraKnownMarketplaces` pointing at your marketplace repo and `enabledPlugins: {"platform@acme": true}`. Engineers are prompted to install it when they trust the folder. Rolling this out is one small scripted PR per repo.
- **Per machine:** managed settings, deployed either as a `managed-settings.json` via MDM or as server-managed settings from the Claude admin console on Team/Enterprise (I'm not certain whether that is still in beta).
  - Pre-register the marketplace there and set `strictKnownMarketplaces`.
  - Put the must-not-bypass guardrail hooks and permission `deny` rules directly in managed settings, optionally with `allowManagedHooksOnly`.
  - Users can disable a plugin, but they can't disable managed settings.

**The personal API token**
- **Best:** run that MCP server remotely with OAuth. Each engineer authenticates once via `/mcp`, and the tokens live in their OS keychain.
- **Otherwise:** reference `${ACME_TOKEN}` in the headers or env of the plugin's `.mcp.json`. Use `${ACME_TOKEN:-}` so a missing variable doesn't break parsing. Each engineer exports the value from their shell or a secret manager.
- **Newer options** (check your version has them): `headersHelper`, a command that prints auth headers, and plugin `userConfig` prompts whose values marked sensitive are stored in the keychain.
- Never commit tokens.

**Claude Code on the web**
- Sessions run in a fresh cloud VM built from the repo, so `~/.claude`, managed settings on laptops and local keychains aren't there.
- Make sure each repo's committed settings declare the plugin. I'm not certain private-marketplace plugins install reliably in cloud sessions, so test it. The fallback is a SessionStart hook or setup script that installs it, or vendoring the critical hooks and skills into the repo.
- Engineers put their token in their cloud environment's environment variables.
- Prefer remote HTTP MCP servers over stdio servers that need local binaries.
- Allow your MCP host in the environment's network policy. It must also be reachable from the internet.

**Keeping it updated**
- Bump `version` on every release, since clients use it to detect updates.
- Run `claude plugin validate` in CI.
- Enable auto-update for your marketplace (third-party marketplaces default to off), or have people run `/plugin marketplace update`.
- For staged rollouts, pin `ref`/`sha` in marketplace entries or run a second "canary" marketplace.
## Q6
I can't give you a confident account of "mods". I don't know their release date or version, and I'm not certain they're a stable, publicly documented feature on every plan and build. Check the changelog and the plugins docs before committing to them.

**What they appear to be**
- Mods are a newer kind of plugin built from *function hooks*: code modules (JavaScript/TypeScript, as far as I know) that load into Claude Code itself, in the terminal UI or the desktop app's Code tab. A settings.json hook, by contrast, is an external command.
- That lets them do things settings.json hooks can't:
  - draw UI: a live pane or band, a custom status line, toasts;
  - keep state across events;
  - hot-reload while your session runs.
- They can also react to lifecycle events, like hooks do.

**How your settings.json hooks differ**
- They're declarative entries that run an external command (or an HTTP, prompt or agent hook) on events such as PreToolUse or Stop, talking over stdin JSON, exit codes and stdout JSON.
- What that buys you:
  - process isolation;
  - any language you like;
  - a stable, documented contract;
  - central enforcement through managed settings (`allowManagedHooksOnly`);
  - identical behavior in headless `claude -p`, CI and Claude Code on the web.
- What it costs you: no UI, and a new process for every call.

**Is porting worth it?**
- **Guardrails, policy checks, formatters and test gates:** generally no. Keep them as settings.json or managed hooks, because that path is enforceable and auditable. I wouldn't move security controls onto a newer in-process API whose permission model and headless/web coverage I can't vouch for.
- **Interactive ergonomics:** this is where mods make sense. Think live test or CI status, a context or cost dashboard, richer notifications, or anything you currently hack together with statusline scripts or notification hooks.

Start by building one mod for a UI need, and leave your existing hooks where they are.
## Q7
**Limits on output size**
- Claude Code warns when one MCP tool result exceeds about 10,000 tokens and caps it at 25,000 tokens by default.
- Each user can raise the cap with the `MAX_MCP_OUTPUT_TOKENS` environment variable, either in the shell or in the `env` block of settings.json.
- 100k+ characters of schema is roughly 25–35k tokens, so you'll hit the cap.
- Older versions return an error telling Claude to paginate or filter. Newer versions may save the oversized result to a file and give Claude a preview and the path. I'm not certain which behavior your developers' versions have.
- Even when the output fits, a blob that size takes a large share of the context window.

**Limits on long-running calls**
- `MCP_TOOL_TIMEOUT` (milliseconds) controls how long a tool call may run. `MCP_TIMEOUT` controls server startup.
- I'm not sure what the current default tool timeout is, so set it explicitly for your developers, e.g. `MCP_TOOL_TIMEOUT=900000` for 15 minutes.
- While a tool runs, Claude's turn is blocked. The user can press Esc to cancel.

**Server side: large results**
- Don't return the whole schema from one call. Split it into:
  - `list_tables(schema?, pattern?)`: names plus a one-line summary;
  - `describe_tables(names[])`: full detail for the tables Claude picks;
  - optionally `search_columns(pattern)`.
- Paginate with `limit`/`cursor`, and keep each response under about 10k tokens.
- Use a compact format, such as terse DDL instead of verbose JSON.
- Optionally expose schemas as MCP resources. For a local stdio server, you can also write the full dump to a file and return its path, so Claude can grep it.
- Say in each tool description how large its output can get and how to narrow it.

**Server side: the 5+ minute tool**
- Make it asynchronous. `start_job` returns a job ID immediately, then Claude calls `get_job_status(id)` and `get_job_result(id, cursor)`. The tool description should tell Claude to poll with backoff.
- If you keep it synchronous, send `notifications/progress` whenever the client supplies a progress token. On streamable HTTP, that also stops load-balancer and proxy idle timeouts (often 60–100s) from killing the request.
- Honor `notifications/cancelled`, and make jobs idempotent so retries are safe.
- The MCP spec now has an experimental async "tasks" mechanism, but I'm not certain Claude Code supports it yet, so don't depend on it.
## Q8
Neither a big interactive "spawn subagents until done" session nor an agent team is the right setup. This is 600 independent checks plus a verification pass, so use a **scripted, two-stage pipeline**: subagents do the work, and all state lives in files rather than in a chat context.

**1. Inventory the routes deterministically**
- Get the route list from the framework itself, through a route-table dump, a decorator scan or an AST script (Claude can write the script). Don't rely on the model's recall.
- Write it to `audit/routes.jsonl`: method, path, handler `file:line`, and the middleware and guards applied.
- This file is your coverage checklist.

**2. Write the rubric once**, as a skill or a section of CLAUDE.md:
- what counts as authorization in your code: global middleware, router guards, decorators, policy calls, ownership checks;
- the routes that are intentionally public;
- the finding types: no authentication, no role check, IDOR;
- the exact JSON output schema.

**3. Triage**
- Use an `authz-auditor` subagent definition with read-only tools (Read, Grep, Glob).
- Feed it batches of about 10–20 handlers, grouped by router so shared middleware is read once.
- Every verdict needs `file:line` evidence, and results go to files.

**4. Verify**
- Send each "missing" or "unclear" item to a fresh `authz-verifier` and tell it to *refute* the finding: trace middleware registration, inherited guards and gateway auth.
- Where possible, have it confirm the gap with an integration test that calls the route unauthenticated or as a low-privilege user and expects 401/403. If that test fails, the finding is confirmed.
- Only confirmed findings go in the report. Everything else goes on a short "needs human review" list.
- Use a cheaper model for triage and your strongest model for verification.

**5. Reconcile**
- Check that every route has a verdict.
- Spot-check a random sample of routes marked "protected".
- Seed a couple of known-bad canary routes to measure how many real gaps the pipeline catches.

**How to drive it**
- **Simplest robust option:** a shell script or the Agent SDK that calls `claude -p --agent authz-auditor --output-format json` (plus `--json-schema` if your version has it). Run calls in parallel and skip batches already done, so it can resume after interruption.
- **Workflow tool:** newer Claude Code builds have a scripted Workflow tool for exactly this kind of resumable fan-out-and-verify pipeline. If yours has it, that's the in-app equivalent, though I can't vouch for its exact API.
- **Interactive subagents:** this works only if the main session just reads and updates the manifest files. Subagents can't nest, and 600 results would otherwise crowd the orchestrator's context.

**Agent teams** are experimental and token-heavy, since every teammate is a full session. They pay off when workers need to talk to each other. At most, use a small team to argue out the high-severity findings.

**Other built-in tools:** `/security-review` only looks at your branch's pending changes, so it won't cover the whole repo. If your org has access to Claude Code Security (repo-wide scanning with its own verification step), it's worth running as a comparison.
