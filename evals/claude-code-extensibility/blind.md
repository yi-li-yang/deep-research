## Q1

**Question:** Last fall I set up a few custom subagents in Claude Code using the /agents wizard, and I haven't touched them since. I'm getting back into it now: what has changed about subagents since then, both in how I create and manage them and in how they behave when Claude uses them?

### Answer 1

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

### Answer 2

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

### Answer 3

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

**Question:** I'm about to write my first batch of Claude Code skills for our team. What does a SKILL.md need to look like these days: which frontmatter fields does Claude Code actually support, and is there a length limit on the description before it gets cut off? I'd also like to upload some of the same skills to claude.ai, so flag anything that works differently there.

### Answer 1

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

### Answer 2

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

### Answer 3

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

**Question:** I just finished my first Claude Code plugin. What's the exact `claude plugin publish` command to submit it to Anthropic's official claude-plugins-official marketplace, and does it authenticate with my claude.ai login or do I need to pass an API key?

### Answer 1

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

### Answer 2

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

### Answer 3

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

**Question:** Can Claude Code hooks do more than run shell scripts now? Two things I want: every Bash command checked against our internal policy service (it's just an HTTP endpoint) before it runs, and something smarter than a script to verify that Claude has actually finished the task before it stops. How would I set those up?

### Answer 1

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

### Answer 2

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

### Answer 3

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

**Question:** I'm on a platform team rolling out a standard Claude Code setup to about 50 engineers across ~15 repos: a handful of skills, two MCP servers (one needs each engineer's personal API token), and a few guardrail hooks. Some people also use Claude Code on the web. What's the best way to package and distribute this today, and keep it updated?

### Answer 1

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

### Answer 2

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

### Answer 3

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

**Question:** People keep talking about Claude Code "mods". What exactly are they, when did they ship, and how are they different from the hooks I already have in settings.json? Is it worth porting my hooks over?

### Answer 1

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

### Answer 2

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

### Answer 3

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

**Question:** I'm building an internal MCP server that our developers will use from Claude Code. A couple of tools return really large results (full database schemas, easily 100k+ characters), and one tool can take five or more minutes to finish. What limits does Claude Code currently put on MCP tool output and on long-running tool calls, and what should I do on the server side so this works smoothly?

### Answer 1

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

### Answer 2

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

### Answer 3

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

**Question:** I want Claude Code to audit all ~600 route handlers in our monorepo for missing authorization checks and give me a list of findings that have actually been verified, not a pile of maybes. What's the right way to set this up in Claude Code today: a bunch of subagents, an agent team, or something else?

### Answer 1

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

### Answer 2

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

### Answer 3

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
