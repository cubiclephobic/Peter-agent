# skill-creator

Build a new skill file from a description. 

Ask the user to describe the skill: what triggers it, what it does, what tools it needs, what it outputs, and any guardrails. One skill, one job. If the description covers two separate workflows, stop and ask the user to split them before continuing.

Then create a SKILL.md in .claude/skills/[skill-name]/SKILL.md with:
- Skill name as H1
- Clear job description (one sentence)
- Step-by-step instructions
- Tool/connector dependencies listed explicitly
- Output format
- Any guardrails (what it never does)

Add the skill to the dispatch table in CLAUDE.md or RESOLVER.md. Commit and push when done.
