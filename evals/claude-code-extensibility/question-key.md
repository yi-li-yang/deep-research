# Question key: Claude Code extensibility (judge only)

Snapshot date: 2026-10-06. The latest Claude Code release at the time of writing is v2.1.291 (2026-10-06).

How sources are cited:
- Docs pages on code.claude.com carry no date of their own, so they are cited as "accessed 2026-10-06".
- Version and date pairs come from the official changelog at https://code.claude.com/docs/en/changelog, which mirrors https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md.
- "Week NN" refers to the official weekly digests at https://code.claude.com/docs/en/whats-new (for example https://code.claude.com/docs/en/whats-new/2026-w27).

Each question lists:
- **Core facts.** A correct, current answer should get most of these right.
- **Strong-answer extras.** These separate deep or current answers from adequate ones.
- **Red flags.** These are outdated or wrong claims to penalize.

---

## Q1: recent-change (subagents since fall 2025)

The user created subagents with the `/agents` wizard in fall 2025 and asks what has changed since.

**Core facts** (a good answer covers at least 3 of these 4):
1. **The `/agents` wizard is gone.**
   - It was removed in v2.1.198 (2026-07-01). The changelog says: "Removed the `/agents` wizard; ask Claude to create or manage subagents, or edit `.claude/agents/` directly".
   - `/agents` now only prints a reminder.
   - You create and edit subagents by asking Claude, or by editing the Markdown files in `.claude/agents/` (project) or `~/.claude/agents/` (user).
   - Claude Code watches those directories and picks up changes within seconds, with no restart. A restart is still needed for the first file in a newly created `agents` dir and for `--add-dir` dirs.
   - Sources: changelog v2.1.198 (2026-07-01); https://code.claude.com/docs/en/sub-agents (Quickstart note, "Write subagent files") and https://code.claude.com/docs/en/commands (`/agents` row), both accessed 2026-10-06.
2. **Subagents run in the background by default.**
   - This shipped in v2.1.198, Week 27 (2026-06-29 to 07-03).
   - Fork mode has been on by default in interactive sessions since v2.1.232 (2026-08-13, Week 33). As a result, every subagent Claude spawns in an interactive session runs in the background, and Claude cannot ask for the foreground (the `run_in_background` parameter is removed).
   - In `-p` runs and the Agent SDK, fork mode is off by default. `CLAUDE_CODE_FORK_SUBAGENT` overrides this.
   - Background subagents surface their permission prompts in the main session instead of auto-denying them (Week 26, 2026-06-22 to 26).
   - Sources: sub-agents doc, sections "Run subagents in foreground or background" and "Turn fork mode on or off" (accessed 2026-10-06); https://code.claude.com/docs/en/whats-new/2026-w27 and /2026-w33.
3. **Forks.**
   - A `fork` subagent inherits the full conversation and its prompt cache.
   - Users start one with `/subtask <task>` (v2.1.212 and later). On v2.1.161 through v2.1.211 this command was `/fork`.
   - With agent view on, `/fork` now copies the whole session into a new background session instead.
   - Source: sub-agents doc, "Fork the current conversation" (accessed 2026-10-06).
4. **Nested subagents.**
   - Subagents can spawn their own subagents since v2.1.172 (2026-06-10, Week 24). At first this was capped at five levels.
   - The current default is up to three layers below the main conversation (since v2.1.219, 2026-07-24).
   - `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` changes the limit. A value of `1` turns nesting off.
   - To stop one specific subagent from spawning, omit `Agent` from its `tools` or add `Agent` to its `disallowedTools`.
   - Sources: sub-agents doc, "Let subagents spawn their own subagents" (with its version-history note), accessed 2026-10-06; https://code.claude.com/docs/en/whats-new/2026-w24.

**Strong-answer extras:**
- **Concurrency.**
  - Spawning fails with `Concurrent subagent limit reached` once 20 subagents are running. `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` changes this (v2.1.217, 2026-07-21).
  - The old cap of 200 subagents per session was removed (Week 32, 2026-08-03 to 07).
  - Sources: sub-agents doc, "Concurrent subagent limit"; https://code.claude.com/docs/en/whats-new/2026-w32.
- **Tool and API renames.**
  - The Task tool was renamed `Agent` in v2.1.63 (2026-02-28). `Task(...)` still works as an alias in rules and in agent `tools`.
  - The Agent tool's `resume` parameter was removed. Claude continues a subagent with `SendMessage` (v2.1.77, 2026-03-17), and named subagents can message each other.
  - The Agent tool's `mode` parameter was deprecated in v2.1.212 (2026-07-17). Subagents inherit the parent's permission mode unless `permissionMode` is set.
  - When the parent session is in auto, acceptEdits, or bypassPermissions mode, a subagent's `permissionMode` is ignored.
  - Sources: sub-agents doc, the note "In version 2.1.63...", "Resume subagents", and "Permission modes"; changelog.
- **New frontmatter fields since fall 2025:**
  - `memory` with `user`, `project`, or `local` scope (v2.1.33, 2026-02-06)
  - `background` (v2.1.49, 2026-02-19)
  - `isolation: worktree` (v2.1.49 and v2.1.50, 2026-02-19 and 20). This is the only valid value.
  - `effort`
  - `initialPrompt` (v2.1.83, 2026-03-25)
  - `omitClaudeMd` (v2.1.271, 2026-09-14)
  - `color`
  - `experimental.cacheTtl` (v2.1.248)
  - `model` now also accepts `fable` and full model IDs. `permissionMode` now also accepts `auto` and `manual`.
  - Plugin-shipped agents ignore `hooks`, `mcpServers`, `permissionMode`, and `initialPrompt`.
  - Sources: sub-agents doc, "Frontmatter reference"; https://code.claude.com/docs/en/plugins/components ("Frontmatter fields in plugin agents"), accessed 2026-10-06; changelog.
- **Explore model.** The built-in Explore agent now runs on the main session's model, capped at Opus, instead of Haiku (https://code.claude.com/docs/en/whats-new/2026-w27).
- **Output scanning.** Subagent final reports are scanned for instruction-shaped text before Claude reads them (v2.1.210, 2026-07-14; sub-agents doc, "Subagent output scanning").
- **Description budget.** Claude Code shows a startup warning when the combined descriptions of custom subagents exceed 15,000 tokens (sub-agents doc intro).
- **Not the same command.** `/agents` is different from `claude agents`. `claude agents` is agent view for background sessions, added in Week 20 (2026-05-11 to 15). Source: https://code.claude.com/docs/en/agents.
- "Sub-agents doc" in this section means https://code.claude.com/docs/en/sub-agents (accessed 2026-10-06). The version and date pairs come from https://code.claude.com/docs/en/changelog.

**Red flags:**
- Telling the user to run `/agents` to open the create/edit wizard.
- Saying subagents can't spawn subagents.
- Saying subagents always block the main conversation until they finish.
- Saying nesting is capped at five levels. That was true only for v2.1.172 through v2.1.216.

---

## Q2: current-fact (SKILL.md format and limits; claude.ai differences)

**Core facts:**
1. **Format and location.**
   - A skill is a directory containing `SKILL.md`: YAML frontmatter between `---` lines, then a Markdown body.
   - Project skills live at `.claude/skills/<name>/SKILL.md`. Personal skills live at `~/.claude/skills/<name>/SKILL.md`.
   - Plugin skills are namespaced as `/plugin-name:skill-name`.
   - Custom slash commands were merged into skills in v2.1.3 (2026-01-09). Files in `.claude/commands/*.md` still work.
   - Claude Code follows the Agent Skills open standard (agentskills.io).
   - Sources: https://code.claude.com/docs/en/skills (accessed 2026-10-06); changelog v2.1.3 (2026-01-09).
2. **Frontmatter in Claude Code.**
   - Every field is optional. `description` is recommended; without it, Claude Code uses the first non-empty line of the body.
   - `name` defaults to the directory name.
   - Supported fields: `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context` (`fork`), `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`, `compatibility`.
   - Unrecognized fields are ignored silently.
   - Source: skills doc, "Frontmatter reference" (accessed 2026-10-06).
3. **Description length.**
   - In the skill listing Claude sees, the combined `description` and `when_to_use` text is cut at 1,536 characters per skill.
   - The `skillListingMaxDescChars` setting changes this (default 1536). The cap was raised from 250 to 1,536 in v2.1.105 (2026-04-13).
   - The whole listing has a budget of 1% of the model's context window. `skillListingBudgetFraction` (default 0.01) changes it, or `SLASH_COMMAND_TOOL_CHAR_BUDGET` sets a fixed character count.
   - Over budget, Claude Code drops the descriptions of the least-used skills but keeps their names.
   - Advice: put the key use case first.
   - Sources: skills doc, "Skill descriptions are cut short"; https://code.claude.com/docs/en/settings-reference (`skillListingBudgetFraction`, `skillListingMaxDescChars`), accessed 2026-10-06; changelog v2.1.105 (2026-04-13).
4. **How claude.ai and the Skills API differ.**
   - Uploads to claude.ai or the Skills API, and packaging with `package_skill.py`, accept only the six Agent Skills spec fields: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
   - A Claude Code-only field such as `argument-hint`, `context`, or `disable-model-invocation` causes a hard error: "Unexpected key(s) in SKILL.md frontmatter ...".
   - On those surfaces `name` and `description` are required.
     - `name`: at most 64 characters; lowercase letters, numbers, and hyphens only; must not contain "anthropic" or "claude".
     - `description`: at most 1,024 characters; no XML tags.
   - Claude Code-only body features, such as `!` dynamic context injection, don't work there.
   - Sources: skills doc, "Using skill frontmatter outside Claude Code"; https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview; https://agentskills.io/specification (all accessed 2026-10-06).

**Strong-answer extras:**
- **Who can invoke.**
  - `disable-model-invocation: true` makes a skill user-only and keeps its description out of context.
  - `user-invocable: false` makes a skill Claude-only.
- **Running in a subagent.**
  - `context: fork` with `agent` runs the skill in a subagent.
  - That subagent runs in the background by default since v2.1.218. Set `background: false` to wait for its result.
- **Substitutions and grants.**
  - Substitutions include `${CLAUDE_SKILL_DIR}`, `$ARGUMENTS`, `$0`, and named `arguments`.
  - An `allowed-tools` grant lasts only for the turn that invokes the skill.
- **Size.** Keep SKILL.md under about 500 lines and move detail into supporting files.
- **Diagnostics and overrides.**
  - `/skill-doctor` reports each skill's context cost and usage. The changelog adds it in v2.1.261 (2026-09-04); the docs say it requires v2.1.252 or later.
  - `/doctor` and `/context` also show the listing's cost.
  - `claude plugin validate .claude/skills` finds frontmatter parse errors (v2.1.233 and later).
  - The `skillOverrides` setting can hide a skill or list it by name only.
- **Sync from claude.ai.**
  - Skills enabled on your claude.ai account now sync down into terminal sessions signed in with that account (v2.1.273, 2026-09-15), under `anthropic-skills:` names.
  - The sync is one-way: Claude Code never uploads.
  - The platform overview page still says custom skills don't sync across surfaces. The Claude Code skills doc is newer on this point.
- **Compaction.** After compaction, Claude Code re-attaches invoked skills, keeping up to the first 5,000 tokens of each and 25,000 tokens in total.
- Sources for these extras: https://code.claude.com/docs/en/skills ("Control who invokes a skill", "Run skills in a subagent", "Available string substitutions", "Find unused skills", "Override skill visibility from settings", "Skills synced from claude.ai", "Skill content lifecycle"), accessed 2026-10-06; changelog v2.1.261 (2026-09-04) and v2.1.273 (2026-09-15).

**Red flags:**
- Saying the description is capped at 250 characters. That is stale (v2.1.86 to v2.1.104, March to April 2026).
- Saying the listing budget is 2% of context. That is stale (v2.1.32, 2026-02-05).
- Saying `name` and `description` are required in Claude Code.
- Saying claude.ai accepts the Claude Code-only fields.
- Listing only `name`, `description`, and `allowed-tools` as the available fields.

---

## Q3: TRAP (a `claude plugin publish` command does not exist)

**Why it is a trap:** Claude Code has no `claude plugin publish` command and no `/plugin publish` session command. There is therefore no exact command, flag set, CLI review queue, or API-key authentication to describe.

**Evidence:**
- **The CLI reference has no publish command.**
  - The plugin commands reference lists every `claude plugin` subcommand: `init`, `install`, `uninstall`, `enable`, `disable`, `update`, `list`, `details`, `configure`, `prune`, `eval`, `eval init`, `tag`, `test`, `validate`, and `marketplace add|list|remove|update`. None of them publishes or submits.
  - The in-session `/plugin` table lists every session form. It states that any unrecognized first word after `/plugin` just opens the Discover tab.
  - Source: https://code.claude.com/docs/en/plugins/cli-reference (accessed 2026-10-06).
- **The changelog never added one.** The full changelog, from v0.2.x through v2.1.291 (2026-10-06), has no entry adding a plugin publish or submit command. Source: https://code.claude.com/docs/en/changelog.
- **Publishing means listing in a marketplace.**
  - The publish guide says: "Publishing a Claude Code plugin means listing it in a marketplace."
  - For your own marketplace: "Once the file is in the repository, the plugin is published, with no submission form."
  - Source: https://code.claude.com/docs/en/plugins/publish (accessed 2026-10-06).
- **Anthropic's directory uses a web portal.**
  - You submit through the developer portal at claude.ai/directory/manage.
  - Submitting requires a paid claude.ai plan. Pro and Max users submit from their own account. On Team and Enterprise an Owner submits, and Enterprise can grant a Directory permission to other members.
  - A directory listing reaches claude.ai, Cowork, and Claude Code. Claude Code loads it through account sync as `<name>@synced`.
  - Sources: same publish page; https://claude.com/docs/plugins/submit.
- **The official marketplace is not self-serve.**
  - The docs say `claude-plugins-official` "doesn't take submissions through the directory portal. If you work with an Anthropic partner contact, ask them about an official-marketplace listing" (publish page, accessed 2026-10-06).
  - The repo README at https://github.com/anthropics/claude-plugins-official (accessed 2026-10-06) says third-party partners can submit for inclusion through a "plugin directory submission form" (clau.de/plugin-directory-submission), subject to quality and security review.
  - Either way, the listing is reviewed by Anthropic. It is not a CLI push.
- **Misinformation exists online.** A DEV Community post dated 2026-01-25 (https://dev.to/rajeshroyal/plugins-share-your-entire-claude-code-setup-with-one-command-294n) claims `/plugin publish` and `/plugin publish --private --org ...` exist. Neither appears in the official docs or the changelog.

**What a good answer does:**
1. It states plainly that the command doesn't exist and that no API key is involved.
2. It gives the real paths:
   - **Your own marketplace.**
     - Add `.claude-plugin/marketplace.json` to a git repo and push.
     - Users run `/plugin marketplace add owner/repo`, then `/plugin install name@marketplace`.
     - Check the plugin with `claude plugin validate --strict` before pushing.
     - Tag releases with `claude plugin tag --push`, which creates `<name>--v<version>` tags (added in v2.1.118, 2026-04-23), and bump `version`.
   - **Anthropic's directory.** Submit through the developer portal (paid plan, reviewed).
   - **The official marketplace.** This is not self-serve.
3. It explains authentication correctly:
   - A self-hosted marketplace relies on git and the users' git credentials.
   - The directory portal uses your claude.ai account in the browser.

**Penalize:**
- Inventing syntax or flags for `claude plugin publish`.
- Saying it needs an API key or Console token.
- Inventing a CLI review-queue command.

Note for the judge: the `--no-publish` flag on `claude plugin eval` only keeps the eval HTML report local. It has nothing to do with publishing a plugin.

---

## Q4: current-fact (hook handler types: HTTP policy check, "is it really done" check)

**Core facts:**
1. **There are now five hook handler types:** `command`, `http`, `mcp_tool`, `prompt`, and `agent`.
   - HTTP hooks were added in v2.1.63 (2026-02-28).
   - `mcp_tool` hooks were added in v2.1.118 (2026-04-23).
   - Prompt-based Stop hooks have existed since v2.0.30 (2025-10-30).
   - Agent hooks are experimental.
   - Sources: https://code.claude.com/docs/en/hooks, "Hook handler fields" (accessed 2026-10-06); changelog.
2. **The policy check is a `PreToolUse` HTTP hook.**
   - Configure it with `"matcher": "Bash"` and a handler such as `{"type": "http", "url": "...", "headers": {...}, "allowedEnvVars": [...]}`.
   - Claude Code POSTs the event JSON, including `tool_input.command`, as the request body.
   - The service answers with a 2xx response whose JSON body is like `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny"|"allow"|"ask", "permissionDecisionReason": "..."}}`. `updatedInput` can rewrite the command.
   - Environment variables are interpolated into headers only if they are listed in `allowedEnvVars`.
   - An `allowedHttpHookUrls` allowlist, set at any settings level including managed settings, restricts which URLs HTTP hooks may call.
   - Source: hooks doc, "HTTP hook fields" and "PreToolUse decision control" (accessed 2026-10-06).
3. **Caveat: HTTP hooks fail open.**
   - An HTTP hook can't block through its status code. A non-2xx status, a connection failure, or a non-JSON body is a non-blocking error, and the command proceeds.
   - The default timeout is 600 seconds.
   - For a hard guarantee, pair the hook with permission deny rules or use a command hook that fails closed. Deny and ask rules are still evaluated whatever the hook returns.
   - Sources: hooks doc, "HTTP response handling"; https://code.claude.com/docs/en/permissions, "Extend permissions with hooks" (accessed 2026-10-06).
4. **The "did Claude really finish" check is a Stop hook.**
   - **`type: "prompt"`.**
     - This is a single LLM call. It uses the model Claude Code uses for background tasks by default, which the `model` field can override, and its default timeout is 30 seconds.
     - The model replies `{"ok": false, "reason": "..."}` to keep Claude working; the reason is fed back to Claude.
     - It replies `{"ok": true}` to allow the stop. It can add `impossible: true` to let the turn end when the condition can never be met.
   - **`type: "agent"`** (experimental).
     - This spawns a verifier subagent that can use tools such as Read, Grep, and Glob to inspect files and test output.
     - It runs for up to 50 turns, with a default timeout of 60 seconds.
   - Source: hooks doc, "Prompt-based hooks" and "Agent-based hooks" (accessed 2026-10-06).

**Strong-answer extras:**
- **The `if` field** takes permission-rule syntax, for example `"if": "Bash(git push *)"`, to narrow when a hook runs (v2.1.85, 2026-03-26). The filter is best-effort and applies only on tool events.
- **`mcp_tool` alternative.** If the policy service is exposed over MCP, an `mcp_tool` handler can call it, with fields `server`, `tool`, and `input` (which supports `${tool_input.command}` substitution).
- **Stop-loop safeguards.**
  - Stop hook input includes a `stop_hook_active` field.
  - Claude Code caps stop-hook continuations at 8 in a row. `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` changes this.
- **`/goal`** (Week 20, May 2026) is a built-in shortcut for a session-scoped, prompt-based Stop hook.
- **Not every event supports every type.**
  - `SessionStart` and `Setup` support only `command` and `mcp_tool`.
  - `PermissionRequest` no longer runs agent hooks (v2.1.280, 2026-09-22).
- **Command hooks.** Exec form (an `args` array, v2.1.139, 2026-05-11) avoids shell quoting problems.
- **`/hooks` is read-only.** It is now a browser; you edit hooks in the settings JSON.
- **Subagents.** Hooks also fire inside subagents, and their input carries `agent_id` and `agent_type`.
- Sources for these extras: https://code.claude.com/docs/en/hooks ("Common fields", "MCP tool hook fields", "Stop input", "Prompt-based hooks", "The `/hooks` menu", "Exec form and shell form", "Hook locations"), accessed 2026-10-06; https://code.claude.com/docs/en/whats-new/2026-w20 (`/goal`); changelog v2.1.85 (2026-03-26), v2.1.139 (2026-05-11), v2.1.280 (2026-09-22).

**Red flags:**
- Saying hooks can only run shell commands, or that a curl wrapper script is the only option.
- Saying a non-2xx response from the HTTP endpoint blocks the command.
- Saying prompt hooks exist only for Stop. Many events support them now.

---

## Q5: judgment (rolling out a shared setup to 50 engineers across 15 repos, including web users)

**Expected recommendation (core facts):**
1. **Package the setup as plugins in a private marketplace.**
   - Use one plugin, or a few plugins plus a "bundle" plugin that pulls them in through `dependencies`.
   - The marketplace is a git repo containing `.claude-plugin/marketplace.json`. It can live on GitHub, GitLab (bare gitlab.com URLs are supported since v2.1.232, 2026-08-13), or another git host. It can also be a hosted `marketplace.json` URL or a shared directory.
   - A plugin can carry skills, agents, hooks (`hooks/hooks.json`), and MCP servers (`.mcp.json`).
   - Sources (all accessed 2026-10-06):
     - https://code.claude.com/docs/en/plugins/overview
     - https://code.claude.com/docs/en/plugins/host-marketplace
     - https://code.claude.com/docs/en/plugins/dependencies
2. **Choose a rollout mechanism.**
   - **Organization-wide, through managed settings.**
     - Set `extraKnownMarketplaces` and `enabledPlugins`, with `autoUpdate: true`.
     - Deliver them as server-managed settings from the claude.ai admin console, through MDM, or in `managed-settings.json`.
     - Managed `enabledPlugins` force-enables the plugins, so users can't disable them at their own scope.
     - `strictKnownMarketplaces` can lock users to approved marketplaces.
   - **Per repository.**
     - Run `claude plugin marketplace add org/mkt --scope project` and commit the `.claude/settings.json` it writes.
     - These entries apply only after each contributor trusts the folder.
     - Plugins whose entries point at external sources still need each contributor to install them.
   - **Team and Enterprise plans.**
     - Use Organization settings > Plugins & skills on claude.ai (org sync). It needs a private or internal repo and rejects plugins with a top-level `bin/` directory.
     - These plugins sync into terminal sessions signed in with claude.ai as `<name>@synced` (v2.1.273, 2026-09-15).
   - Sources: https://code.claude.com/docs/en/plugins/org, /plugins/host-marketplace, /plugins/loading (accessed 2026-10-06).
3. **Handle the personal API token safely.**
   - Never commit it in `.mcp.json`.
   - Declare it in `userConfig` with `"sensitive": true`. The input is masked, and the value is stored in the OS keychain or secure credential store, not in settings.json (available since v2.1.83, 2026-03-25).
   - Reference it as `${user_config.api_token}` in the plugin's MCP server config. Hooks receive it as `CLAUDE_PLUGIN_OPTION_<KEY>`.
   - If the server supports OAuth, prefer a remote HTTP MCP server with per-user sign-in through `/mcp` or `claude mcp login` (Week 26, June 2026).
   - Sources: https://code.claude.com/docs/en/plugins/manifest-reference ("User configuration") and /plugins/components (accessed 2026-10-06).
4. **Know what reaches cloud sessions (Claude Code on the web).**
   - Cloud sessions don't load plugins enabled in user settings or in a repo's `.claude/settings.json`.
   - Only server-managed settings reach a cloud session, and the session waits for them before it installs plugins.
   - The alternative is to commit `.claude/skills/`, `.claude/agents/`, a project-scope `.mcp.json`, and hooks in `.claude/settings.json` to each repo. Cloud sessions do load those.
   - Sources: https://code.claude.com/docs/en/cloud-environments ("What carries over from your setup"); /plugins/install (Cloud session tab); /plugins/org ("When each surface applies the plugin keys"), all accessed 2026-10-06.

**Strong-answer extras:**
- **Guardrails that must hold.**
  - Use managed settings for these: managed hooks plus `allowManagedHooksOnly`, and permission deny rules.
  - Otherwise users can turn off hooks with `disableAllHooks` or disable the plugin. A user-level `disableAllHooks` can't disable managed hooks.
  - Hooks from plugins force-enabled in managed `enabledPlugins` are exempt from `allowManagedHooksOnly`.
- **Plugin limitations.**
  - Plugin agents can't carry their own `hooks`, `mcpServers`, or `permissionMode`.
  - A `CLAUDE.md` at the plugin root isn't loaded, so put instructions in skills.
- **Versioning.**
  - A `version` in plugin.json pins users to that version until you bump it.
  - Tag releases as `<name>--v<version>` with `claude plugin tag` (v2.1.118).
  - Dependency semver ranges such as `^` and `~` resolve against those tags.
  - Auto-update is off for third-party marketplaces until someone turns it on.
  - Auto-update from a private repo needs git credentials that work without prompting.
- **Quality gates in CI.**
  - Run `claude plugin validate --strict`. Its MCP checks were added in v2.1.281.
  - Run `claude plugin eval` against a no-plugin baseline (v2.1.269, 2026-09-11; https://code.claude.com/docs/en/plugin-evals).
- **Plugin hooks.** Use exec form `args` with `${CLAUDE_PLUGIN_ROOT}`. Store persistent dependencies under `${CLAUDE_PLUGIN_DATA}`.
- Sources for these extras (accessed 2026-10-06):
  - https://code.claude.com/docs/en/hooks ("Hook locations", "Disable or remove hooks")
  - https://code.claude.com/docs/en/sub-agents (plugin subagent note)
  - https://code.claude.com/docs/en/plugins/components and /plugins/manifest-reference ("Standard layout": a plugin-root CLAUDE.md isn't loaded)
  - https://code.claude.com/docs/en/plugins/dependencies ("Tag plugin releases for version resolution")
  - https://code.claude.com/docs/en/plugins/host-marketplace ("Keep users up to date", "What background auto-update does with credentials")
  - https://code.claude.com/docs/en/plugins/cli-reference ("plugin validate")
  - changelog v2.1.118 (2026-04-23) and v2.1.281 (2026-09-23)

**Red flags:**
- Committing the personal token in `.mcp.json` or settings.
- Saying plugins enabled through repo settings load in web or cloud sessions.
- Relying on a `CLAUDE.md` at the plugin root.
- Putting guardrails only in CLAUDE.md or skills, which are advisory.
- Giving a generic "copy the files into each repo" answer with no mention of plugins or marketplaces.

---

## Q6: recent-change (mods)

**Core facts:**
1. **When they shipped.**
   - Mods shipped on 2026-10-01 in Claude Code v2.1.287. The changelog line is "Added Claude Mods: plugins may now modify deeper behavior".
   - They are on by default. In the Desktop app's Code tab they work from v2.1.286.
   - Sources: changelog v2.1.287 (2026-10-01); https://code.claude.com/docs/en/plugins/mods/overview (accessed 2026-10-06). Third-party coverage in early October 2026 also reports the v2.1.287 / Oct 1 launch, for example https://dev.to/max_quimby/claude-code-mods-just-turned-agents-into-a-platform-5gc0 (published 2026-10-04).
2. **What a mod is.**
   - A mod is a plugin whose `hooks/hooks.json` has a `modules` entry pointing to a JavaScript or TypeScript "hooks module". The module exports `register(on, options)`.
   - Its handlers are in-process middleware functions with the signature `($, e, next)`. They can observe, rewrite, or answer events such as `tool.call`, `tool.check`, `prompt.submit`, `turn.step`, `turn.complete`, `ui.render`, `agent.spawn`, `skill.prompt`, and `session.*`.
   - Through the mods API, a mod can:
     - draw panes and bands;
     - restyle built-in UI, except the permission prompt;
     - add slash commands and tools;
     - call models and run timers;
     - read files and use the network.
   - Sources: https://code.claude.com/docs/en/plugins/mods/overview and /plugins/mods/reference (accessed 2026-10-06).
3. **How mods differ from settings.json hooks.**
   - Settings hooks are external handlers (command, http, mcp_tool, prompt, or agent) configured in JSON. They communicate through stdin, stdout, exit codes, or HTTP, and they can't draw UI or keep state inside Claude Code.
   - Mods are code running inside Claude Code. They can share state between handlers, and they must be written in JavaScript or TypeScript.
   - Settings hooks keep working alongside mods. Mods see them as `classic.<Event>` events.
   - Sources: mods overview, "Compare mods, settings hooks, skills, and MCP servers"; https://code.claude.com/docs/en/hooks intro (accessed 2026-10-06).
4. **Porting advice.**
   - There is no need to port settings hooks that already work for blocking, allowing, logging, or formatting. They remain supported, they are simpler, and they can be written in any language.
   - Use a mod when you need UI, in-process state, event rewriting, custom commands or tools, or per-request model and effort routing.

**Strong-answer extras:**
- **Security.**
  - Mods aren't sandboxed. They run with your permissions, can read secrets, see every prompt and tool call, and approve tool calls.
  - A mod handling `tool.check` can override ask rules, blocks from non-managed PreToolUse hooks, and the auto-mode classifier.
  - Without managed settings or a Team/Enterprise sign-in, such a mod can even approve calls that a deny rule refuses.
  - Run `claude plugin validate` on a mod before installing it; it lists the mod's `hooks:` and `calls:`.
  - Sources: mods overview, "Decide whether to trust a mod"; https://code.claude.com/docs/en/permissions, "Extend permissions with hooks" (accessed 2026-10-06).
- **Making a mod.**
  - Ask Claude. The built-in `plugin-authoring` skill writes the mod to `~/.claude/dev-mods/<session-id>/` and hot-reloads it after you approve.
  - Or write it by hand, load it with `--plugin-dir`, and refresh with `/reload-plugins`.
  - Test it with `claude plugin test`, which runs `*.test.ts` files.
  - Distribute it through a marketplace.
- **Where mods run.**
  - Their hooks run in the CLI, Desktop, the VS Code extension, `-p` runs, the Agent SDK, and cloud sessions.
  - Their drawing appears only in the terminal and the Desktop app.
- **Turning mods off.**
  - Users can disable a mod in `/plugin`, start with `--safe-mode`, or set `disableAllHooks`. `disableAllHooks` also stops settings hooks.
  - Admins can set `allowManagedModsOnly` under `pluginConfigs` > `cc-plugin-sec-default@builtin` > `options`.
  - The early-access variable `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` is ignored from v2.1.287.
- **Built-in mods.**
  - The `/diff` pane.
  - AGENTS.md support. AGENTS.md support was added in v2.1.277 (2026-09-18).
  - The opt-in "You should know" side agent, enabled with `/plugin enable cc-plugin-you-should-know@builtin`.
- **Example code.**
  - Sample mods live in the anthropics/claude-code-playground repo under `claude-code/mods`.
  - The source of some built-in mods lives in anthropics/claude-code under `mods/`.
- Sources for these extras (accessed 2026-10-06):
  - https://code.claude.com/docs/en/plugins/mods/create ("Ask Claude for a mod")
  - https://code.claude.com/docs/en/plugins/mods/overview ("Where mods run", "Turn mods on or off", "Mods built into Claude Code", "Try a sample mod")
  - https://code.claude.com/docs/en/plugins/mods/admin ("Stop user-installed mods from loading")
  - https://code.claude.com/docs/en/plugins/cli-reference ("plugin test")
  - changelog v2.1.277 (2026-09-18) and v2.1.287 (2026-10-01)

**Red flags:**
- Saying mods don't exist, are a rumor, or are a third-party project.
- Confusing mods with MCP servers or the status line.
- Saying settings.json hooks are deprecated or replaced by mods.
- Recommending that every hook be ported.

---

## Q7: current-fact (MCP output size and long-running calls)

**Core facts:**
1. **Output size limits.**
   - Claude Code warns when an MCP tool result exceeds 10,000 tokens and caps results at 25,000 tokens by default. Users change the cap with the `MAX_MCP_OUTPUT_TOKENS` environment variable.
   - A successful result over the limit is not simply truncated. Claude Code saves it to a file in the session's `tool-results` directory and replaces it with a message naming the path, so Claude can read the file when it needs the content.
   - For tools without the `anthropic/maxResultSizeChars` annotation (item 2), text results longer than 50,000 characters are saved to a file whatever `MAX_MCP_OUTPUT_TOKENS` is set to.
   - Source: https://code.claude.com/docs/en/mcp, "MCP output limits and warnings" (accessed 2026-10-06).
2. **What the server author can do about size.**
   - Set `_meta["anthropic/maxResultSizeChars"]` on the tool in its `tools/list` entry. This raises that tool's threshold up to a hard ceiling of 500,000 characters (added in v2.1.91, 2026-04-02).
   - The annotation applies to text content, independent of `MAX_MCP_OUTPUT_TOKENS`. Image results remain subject to the token limit.
   - Pagination or summarization still helps.
   - Sources: mcp doc, "Raise the limit for a specific tool"; changelog v2.1.91.
3. **Long-running calls.**
   - **Automatic backgrounding.** An MCP call in the main conversation that is still running after 2 minutes moves to a background task (v2.1.212, 2026-07-17). `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` changes the threshold. Claude keeps working, and the result arrives as a task notification. Calls from subagents and in `-p` runs aren't backgrounded by default.
   - **Idle timeout.** A call that sends no response and no progress notification is aborted after 5 minutes for HTTP, SSE, WebSocket, and connector servers, and after 30 minutes for stdio servers. `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` changes this. The remote 5-minute abort arrived in v2.1.187 (2026-06-23), and stdio was covered from v2.1.203. The server should therefore send MCP progress notifications during long work.
   - **Wall-clock limit.** Set a per-server `timeout` in milliseconds in `.mcp.json`, or `MCP_TOOL_TIMEOUT`, which defaults to about 28 hours when unset. Progress notifications don't extend the wall-clock limit.
   - Source: mcp doc, Tips and "Automatic backgrounding of long tool calls" (accessed 2026-10-06).

**Strong-answer extras:**
- **Description cap.** Tool descriptions and server instructions are truncated at 2,048 characters by default, so key information should come first. The 2KB cap dates from v2.1.84 (2026-03-26); `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` changes it since v2.1.280 (2026-09-22).
- **Tool search.**
  - Tool search is on by default, so only tool names and server instructions load upfront. That makes clear server instructions important.
  - `alwaysLoad` on the server, or `_meta["anthropic/alwaysLoad"]` on a tool, exempts it from deferral.
- **Time to first byte.** HTTP and SSE servers also have a per-request timer up to the first response byte. It equals the largest of 60 seconds, the tool timeout, and `MCP_TIMEOUT`, so the server should respond or start streaming early.
- **Error results.** Error text longer than about 11,000 characters is cut to its first and last 5,000 characters.
- **Images.** Image results are also saved to a file (v2.1.283, 2026-09-25).
- **Transport.** Use streamable HTTP. The SSE transport is deprecated, and since v2.1.265 `--transport http` falls back to SSE automatically.
- Sources for these extras: https://code.claude.com/docs/en/mcp ("For MCP server authors", "Configure tool search", "Exempt a server from deferral", Tips, "MCP output limits and warnings", "Images in tool results", "Option 2: Add a remote SSE server"), accessed 2026-10-06; changelog v2.1.84 (2026-03-26), v2.1.280 (2026-09-22), v2.1.283 (2026-09-25).

**Red flags:**
- Saying there's no limit.
- Saying results over 25k tokens are just truncated or dropped, with no mention of saving to a file.
- Saying the only fix is for users to raise `MAX_MCP_OUTPUT_TOKENS`.
- Saying long MCP calls block the session indefinitely.
- Recommending SSE.

---

## Q8: judgment (verified audit of ~600 route handlers)

**Expected recommendation (core facts):**
1. **Use a dynamic workflow.**
   - Dynamic workflows were introduced in v2.1.154 (2026-05-28, Week 22).
   - To start one, ask in your own words ("use a workflow") or put the `ultracode` keyword in the prompt, for example `ultracode: audit every route handler under ... for missing auth checks`. The keyword was renamed from `workflow` to `ultracode` in v2.1.160 (2026-06-02).
   - Claude writes a JavaScript orchestration script. The runtime fans it out to many subagents in the background: up to 16 concurrent agents by default and up to 1,000 agents per run.
   - Intermediate results stay in script variables, not in the main context.
   - The script can have independent agents adversarially verify each finding before it is reported.
   - You approve the planned phases, monitor the run with `/workflows`, and can resume the run within the session.
   - You can save the script as a reusable `/command` in `.claude/workflows/`.
   - Sources: https://code.claude.com/docs/en/workflows (accessed 2026-10-06); changelog v2.1.154 (2026-05-28) and v2.1.160 (2026-06-02).
2. **Why not plain subagents.**
   - With subagents, Claude orchestrates turn by turn and every result lands in the main context.
   - Only 20 subagents can run at once by default.
   - That suits a handful of tasks, not 600 files plus verification.
   - Sources: workflows doc, "When to use a workflow"; https://code.claude.com/docs/en/sub-agents, "Concurrent subagent limit".
3. **Why not agent teams.**
   - Agent teams are experimental and disabled by default; `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` turns them on.
   - They suit a handful of long-running peers that collaborate, at a high token cost.
   - They are not the tool for a fan-out audit.
   - Sources: https://code.claude.com/docs/en/agent-teams and https://code.claude.com/docs/en/agents (accessed 2026-10-06).
4. **Practicalities.**
   - **Cost.** Cost scales with the number of agents, so pilot the workflow on one directory first. Claude Code shows a "Large workflow" warning past 25 agents or a projected 1.5M tokens.
   - **Size guideline.** The `workflowSizeGuideline` setting is advisory. Its default is medium (fewer than 10 agents), or small on Pro. State the scale you want in the prompt, or raise the guideline.
   - **Availability.** On Pro, turn Dynamic workflows on in `/config`. Admins can turn workflows off with `disableWorkflows`.
   - **Permissions.** Pre-allow the read-only tools the agents need so the run doesn't stall on prompts.

**Strong-answer extras:**
- `/batch` is meant for large changes split across 5 to 30 worktree-isolated subagents, not for audits.
- `/effort ultracode` makes Claude plan a workflow for every substantive task in the session, which costs more tokens.
- Workflows run in the CLI, Desktop, IDE extensions, `-p`, and the Agent SDK. In `-p` runs, the workflow needs a `Workflow` allow rule (or another approval route) to start.
- A custom read-only reviewer subagent, or a structured output schema for findings, helps.
- The bundled `/deep-research` workflow is a working example.
- Sources for these extras: https://code.claude.com/docs/en/agents (`/batch`); https://code.claude.com/docs/en/workflows ("Let Claude decide with ultracode", "Approve the plan before it runs", "Turn workflows off", "Bundled workflows"), accessed 2026-10-06.

**Red flags:**
- Saying only "spawn subagents in parallel" with no awareness of dynamic workflows.
- Recommending agent teams as the default or production-ready choice.
- Saying hundreds of subagents can run concurrently by default.
- Suggesting `/batch` as the audit tool.
