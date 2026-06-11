# RESOLVER — Skill Dispatch Rules

Peter reads this before routing any task. Match the input to the first rule that fits.

---

## Skill Dispatch Table

| Trigger | Skill | Notes |
|---|---|---|
| "Draft an email to [name]" | `/biz-dev-email` | Pulls HubSpot context, applies voice rules, saves as Gmail draft |
| Incoming messages need triage | `/message-triage` | Reads Gmail + Slack, ranks, chains to draft-writer → personal-tone → qa-check |
| Reply draft requested | `/draft-writer` | Raw draft only; called by message-triage or directly |
| Rewrite draft in Corinna's voice | `/personal-tone` | Pulls Gmail sent history for pattern matching |
| Final QA on a draft | `/qa-check` | Grammar, tone, completeness check |
| "Ingest [source] into wiki" | `/wiki-ingest` | Paste, Gmail, Slack, or Drive → structured wiki page |
| "Audit the wiki" | `/wiki-lint` | Read-only scan for format issues, stale pages, missing sections |
| "Where do I find info about X?" | `/wiki-query` | Returns file names + relevance reasons, never answers directly |
| "Build a new skill for [job]" | `/skill-creator` | Interviews, then writes SKILL.md and updates this table |
| Pipeline review | Built-in (Pipeline Pulse task) | Uses HubSpot MCP directly |
| Krisp transcript available | Built-in (Action Item Extraction task) | Extracts action items + due dates |
| Monday calendar check | Built-in (Calendar + BD Block task) | Uses Calendar MCP |
| Partner/client session just ended | Built-in (Follow-up Draft task) | Gmail draft via Gmail MCP |
| Retro summary pasted to inbox | Built-in (Retro Pattern Surfacing task) | Reads from corinnas.agent@gmail.com |

---

## Guardrails (apply to all skills)

- Never send emails without Corinna's explicit approval
- Never update HubSpot contact records without confirmation
- Never merge or delete records
- Never mix Zaradigm and Coachilly branding
- When ambiguous, make a reasonable call and state the assumption — don't ask unless the decision has real consequences

---

## Tool Dependencies

| Tool | MCP / Connector | Used by |
|---|---|---|
| Gmail (corinna@zaradigm.com) | Gmail MCP (OAuth) | biz-dev-email, message-triage, draft-writer, personal-tone, follow-up draft |
| HubSpot | HubSpot MCP | biz-dev-email, pipeline pulse |
| Slack | Slack MCP | message-triage |
| Google Calendar | Calendar MCP | calendar + BD block task |
| Krisp | Krisp MCP | action item extraction |
