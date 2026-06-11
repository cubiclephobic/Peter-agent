Source: Claude Code session, 2026-06-04
Confidence: 0.95
Updated: 2026-06-04 — Article created
Updated: 2026-06-08 — Added L3-S1 session; key agent OS concepts

# Course Extractions — AI Builder Program

## What They Are

Offline, self-contained HTML reference files extracted from Leland course sessions. Preserve all course content (including collapsed cards, prompts, troubleshooting, Go Further sections) permanently — accessible without a Leland subscription or internet connection.

---

## Location

All files live in:
```
/Users/corinnas/AI CODE/AI Builder Program/
```

Open any file by double-clicking in Finder — no server needed. They are fully self-contained.

**Shortcut to folder:** `Cmd+Shift+G` → paste path above → Enter.

---

## Files

| File | Session | Topic |
|------|---------|-------|
| `ai-builder-l2-session1.html` | L2 S1 | Build and Ship Your Automation Roadmap |
| `ai-builder-l2-session2.html` | L2 S2 | Build Your First Cloud Automation |
| `ai-builder-l2-session3.html` | L2 S3 | Build Your Custom Agentic Automation |
| `ai-builder-l2-session4.html` | L2 S4 | Build Your Second Brain |
| `ai-builder-cold-outbound-email-agent.html` | Standalone | Cold Outbound Email Agent (Build Workshop) |
| _(not yet extracted)_ | L3 S1 | Build Your Agentic Ops System — file-native agents, agent OS, heartbeat, phone delegation |

---

## Design System

All files use the **Apple-design** system: `#F5F5F7` off-white background, `#1D1D1F` text, SF Pro / Inter typography, full-pill badges (`border-radius: 980px`), white cards on off-white, zero decoration.

---

## How to Extract Future Sessions

Use the `/course-extract [URL]` skill. Requirements:
- Chrome open and logged into lelandcourses.com
- Run `/course-extract https://www.lelandcourses.com/ai-builder/[session-slug]/`
- Skill expands all collapsed elements, extracts full content, writes HTML to the `AI Builder Program/` folder
- Naming pattern: `ai-builder-l[N]-session[N].html`

Skill file: `/Users/corinnas/AI CODE/.claude/commands/course-extract.md`

---

## L3 Program — Key Concepts (from S1, 2026-06-08)

Level 3 focus: building autonomous "file-native" agents. Relevant because Peter (Corinna's agent) and the Knowledge Wiki connect in L3-S2.

| Concept | What it means |
|---------|--------------|
| **File-native agent** | Agent identity lives in a GitHub repo as CLAUDE.md; runs in Claude Code cloud (no computer needed) |
| **Agent OS stack** | Identity → Memory → Skills → Context (each layer builds on the last) |
| **Agent identity file** | Repo-specific CLAUDE.md — persona, priorities, routing rules, communication style |
| **Agent loop** | Reason → Act → Observe (repeating). Autonomy spectrum: suggest → approve → fully autonomous |
| **Heartbeat / routine** | Cron-scheduled task; agent wakes up, checks something, posts to Slack. Set in Claude Code "Routines" tab |
| **Code tab (mobile)** | Delegate tasks to cloud agent from iPhone; computer does NOT need to be on |
| **Chief of staff agent** | Coordinates other specialized sub-agents; knows Corinna's priorities and context |

**Corinna's agent:** Named "Peter" — GitHub repo `peter-agent` — communicates via private Slack channel.

**L3-S2 preview:** Connecting the Knowledge Wiki to Peter as persistent context. Direct relevance to wiki system.

---

## Related

- [[skill-management]] — /course-extract skill documentation
- [[leland-ai]] — Leland platform context and AI Builder program history
