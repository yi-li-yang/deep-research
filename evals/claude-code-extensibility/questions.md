## Q1
Last fall I set up a few custom subagents in Claude Code using the /agents wizard, and I haven't touched them since. I'm getting back into it now: what has changed about subagents since then, both in how I create and manage them and in how they behave when Claude uses them?
## Q2
I'm about to write my first batch of Claude Code skills for our team. What does a SKILL.md need to look like these days: which frontmatter fields does Claude Code actually support, and is there a length limit on the description before it gets cut off? I'd also like to upload some of the same skills to claude.ai, so flag anything that works differently there.
## Q3
I just finished my first Claude Code plugin. What's the exact `claude plugin publish` command to submit it to Anthropic's official claude-plugins-official marketplace, and does it authenticate with my claude.ai login or do I need to pass an API key?
## Q4
Can Claude Code hooks do more than run shell scripts now? Two things I want: every Bash command checked against our internal policy service (it's just an HTTP endpoint) before it runs, and something smarter than a script to verify that Claude has actually finished the task before it stops. How would I set those up?
## Q5
I'm on a platform team rolling out a standard Claude Code setup to about 50 engineers across ~15 repos: a handful of skills, two MCP servers (one needs each engineer's personal API token), and a few guardrail hooks. Some people also use Claude Code on the web. What's the best way to package and distribute this today, and keep it updated?
## Q6
People keep talking about Claude Code "mods". What exactly are they, when did they ship, and how are they different from the hooks I already have in settings.json? Is it worth porting my hooks over?
## Q7
I'm building an internal MCP server that our developers will use from Claude Code. A couple of tools return really large results (full database schemas, easily 100k+ characters), and one tool can take five or more minutes to finish. What limits does Claude Code currently put on MCP tool output and on long-running tool calls, and what should I do on the server side so this works smoothly?
## Q8
I want Claude Code to audit all ~600 route handlers in our monorepo for missing authorization checks and give me a list of findings that have actually been verified, not a pile of maybes. What's the right way to set this up in Claude Code today: a bunch of subagents, an agent team, or something else?
