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
| "/debate [decision]" | `/debate` | Spawns Operator + Strategist subagents in parallel, synthesizes locked recommendation |
| "/situation-assessment [subject]" | `/situation-assessment` | Consulting OS — Diagnose stage. Current state, what's moving/stuck, context. On-demand only, not auto-triggered. |
| "/growth-barriers [subject]" | `/growth-barriers` | Consulting OS — Diagnose stage. Root-cause barriers ranked by impact x tractability. Chains from situation-assessment if one exists. |
| "/assumption-audit [plan]" | `/assumption-audit` | Consulting OS — Diagnose stage. Stress-tests load-bearing assumptions before commitment. |
| "/market-mapping [market]" | `/market-mapping` | Consulting OS — Map stage. Value chain, ecosystem players, structural forces. Routes external data to researcher subagent. |
| "/competitive-intel [subject]" | `/competitive-intel` | Consulting OS — Map stage. Competitor profiles, whitespace, biggest threat. Routes specific competitor data to researcher subagent. |
| "/customer-segmentation [business]" | `/customer-segmentation` | Consulting OS — Map stage. Segments by need/behavior, scores on attractiveness × fit, names priority tier. |
| "/profit-pool-analysis [market]" | `/profit-pool-analysis` | Consulting OS — Map stage. Where margin concentrates in the value chain, capture opportunities, extraction risks. |
| "/strategic-options [context]" | `/strategic-options` | Consulting OS — Choose stage. MECE option set, evaluated and ranked, with locked recommendation. Heavier version of /debate. |
| "/pricing-strategy [offer]" | `/pricing-strategy` | Consulting OS — Choose stage. Value-based price architecture — anchor / primary / entry — with competitive framing. |
| "/business-case-builder [decision]" | `/business-case-builder` | Consulting OS — Choose stage. Unit economics, sensitivity scenarios, go/no-go threshold. |
| "/portfolio-review [scope]" | `/portfolio-review` | Consulting OS — Choose stage. Classifies offers by growth × margin, surfaces resource misalignment, names highest-leverage shift. |
| Pipeline review | Built-in (Pipeline Pulse task) | Uses HubSpot MCP directly |
| Krisp transcript available | Built-in (Action Item Extraction task) | Extracts action items + due dates |
| Monday calendar check | Built-in (Calendar + BD Block task) | Uses Calendar MCP |
| Partner/client session just ended | Built-in (Follow-up Draft task) | Gmail draft via Gmail MCP |
| Retro summary pasted to inbox | Built-in (Retro Pattern Surfacing task) | Reads from corinnas.agent@gmail.com |

---

## Consulting OS (Corinna-facing, on-demand only)

Engagement backbone: Diagnose → Map → Choose → Execute → Govern → Communicate. Built one stage at a time; not wired into Peter's recurring jobs. These are deliverable tools Corinna invokes when working a client engagement or a strategic call for Zaradigm — Peter does not auto-trigger them.

- **Diagnose:** `situation-assessment`, `growth-barriers`, `assumption-audit` (built)
- **Map:** `market-mapping`, `competitive-intel`, `customer-segmentation`, `profit-pool-analysis` (built)
- **Choose:** `strategic-options`, `pricing-strategy`, `business-case-builder`, `portfolio-review` (built)
- **Execute, Govern, Communicate:** pending.

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
