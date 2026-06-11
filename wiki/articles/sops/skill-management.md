Source: Direct session observation 2026-06-03
Confidence: 0.95
Updated: 2026-06-03 — Article created after diagnosing skill persistence failure and fixing all 12 anthropic-skills
Updated: 2026-06-04 — Added z-design, Apple-design, c-design skills; documented ~/Desktop/my-agents/ as canonical agent folder; added Cowork skill availability issue
Updated: 2026-06-11 — All 8 commands now global in ~/.claude/commands/; global CLAUDE.md updated with wiki + my-ai-tools.md pointers

# Skill Management (Claude Code)

Skills are slash commands that give Claude Code specialized, persistent capabilities. Corinna's skills live under the `anthropic-skills:` namespace.

## Where skills live on disk
```
~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/
  [plugin-id]/[session-id]/skills/
    skill-name/
      SKILL.md        ← the skill definition
    skill-creator/
      skill-name.skill  ← the packaged artifact (what actually persists)
```

## Why skills disappear between sessions

Writing a `SKILL.md` file directly (via Claude's Write tool) is not sufficient for persistence. The Write tool can silently write to a sandboxed/temp path that gets cleaned up when a session ends.

**The two requirements for a skill to survive sessions:**
1. The `SKILL.md` must be written to disk via `bash` (not the Write tool)
2. The skill must be **packaged** into a `.skill` file immediately after writing

## Correct workflow for creating or updating a skill

```bash
# 1. Create the folder and write the SKILL.md via bash heredoc
mkdir -p "$SKILLS_BASE/skill-name"
cat > "$SKILLS_BASE/skill-name/SKILL.md" << 'SKILLEOF'
---
name: skill-name
description: >
  ...
---
[skill body]
SKILLEOF

# 2. Verify the file actually exists on disk
ls -la "$SKILLS_BASE/skill-name/"

# 3. Package it immediately
cd "$SKILLS_BASE/skill-creator"
python3 -m scripts.package_skill "$SKILLS_BASE/skill-name/"

# 4. Confirm the .skill file was created
ls "$SKILLS_BASE/skill-creator/skill-name.skill"
```

**Never** use the Write tool for skill files. **Never** skip the packaging step.

## Current anthropic-skills inventory (as of 2026-06-04)

All skills are packaged as `.skill` files and session-proof. Canonical copies of all agent/skill files live in **`~/Desktop/my-agents/`**.

| Skill | Purpose |
|---|---|
| automation-scoper | Scope automation opportunities |
| cleantalk-triage | WordPress malware scan triage (zaradigm.com + coachilly.com) |
| consolidate-memory | Consolidate session memory |
| docx | Word document creation/editing |
| pdf | PDF handling |
| pptx | PowerPoint creation/editing |
| pya-recap | PYA session recap |
| recap | General session recap |
| schedule | Create/update scheduled tasks |
| setup-cowork | Cowork session setup |
| xlsx | Excel spreadsheet handling |
| practice-lab-builder | Build AI practice labs for UpLeveled.ai with V2 format, 10-point QA, and structured JSON output |
| zaradigm-design | Zaradigm brand design system (original, partial — superseded by z-design) |
| z-design | Zaradigm full design system — violet/yellow palette, Nunito+Roboto, alternating sections |
| Apple-design | Apple.com-inspired system — SF Pro/Inter, full-pill buttons, cinematic dark/light, extreme restraint |
| c-design | Coachilly Magazine system — Lora+Open Sans, dense 3-col grid, square buttons, red-as-punctuation |

## Agents folder

All packaged `.skill` files are stored at `~/Desktop/my-agents/`. When creating a new skill, copy the `.skill` output there as the final step. The folder currently contains:
- `zaradigm-design.skill`
- `z-design.skill`
- `Apple-design.skill` (was named c-design during build; user renamed)
- `c-design.skill` (Coachilly Magazine system)

## Personal slash commands (separate from anthropic-skills)

Not all skills are packaged `.skill` files. Some are plain markdown files in `~/.claude/commands/` — these are simpler slash commands that don't require packaging and persist as long as the file exists on disk.

**Current personal commands (as of June 11, 2026) — all globally available in `~/.claude/commands/`:**

| Command | Purpose |
|---------|---------|
| `/log-linkedin` | Read open LinkedIn convo from Chrome → find HubSpot contact → log formatted note |
| `/shift-invite` | Batch the/SHIFT cohort outreach — HubSpot lookup, segment, draft, Gmail draft |
| `/biz-dev-email [name]` | Warm re-engagement email — pulls HubSpot context, drafts in Corinna's voice, saves Gmail draft |
| `/course-extract [URL]` | Extract Leland course session from Chrome → offline HTML reference |
| `/wrap` | End-of-session wiki updater — summarizes session, updates/creates articles, appends to log.md |
| `/wiki-update` | Pulls Krisp meetings + HubSpot activity → updates wiki. Run each morning. |
| `/ingest [source]` | Ingest any source (URL, file, pasted text, raw/ drop) → extract facts → update wiki |
| `/lint` | Audit knowledge-wiki for stale content, gaps, index integrity, contradictions |

> All 8 commands are in `~/.claude/commands/` (global). Previously `/wrap`, `/wiki-update`, `/ingest`, `/lint`, `/course-extract` were project-level only (`AI CODE/.claude/commands/`). Moved global 2026-06-11.

**⚠️ Naming collision risk:** Do not name a personal command the same as an existing FleetView/platform skill. `/shift-followup` collided with a platform skill and was renamed to `/shift-invite`. Check the available skills list before naming.

**Skill discoverability:** Corinna does not memorize skill names. Claude pattern-matches the situation and proposes the right approach. She approves or redirects. The three commands worth knowing by heart: `/wrap`, `/shift-invite`, `/log-linkedin`.

---

## Cowork: skill availability issue

**Known issue (observed 2026-06-04):** Skills created or installed during a Cowork session are not automatically available as slash commands within that same session. Even if a `.skill` file is packaged and saved, it won't appear in the active session's skill list until the session is restarted or the skill is re-installed through the Claude skills UI.

**Workaround:** After packaging a new skill in Cowork, the user must install it via the Claude skills panel (drag the `.skill` file in, or use the install flow) and start a fresh session before it appears as an invokable slash command.

**Invoking existing skills in Cowork:** The `Skill` tool works in Cowork for skills that were already installed before the session started. It does not pick up skills packaged mid-session.

---

## YAML gotcha in skill frontmatter

The `description:` field in SKILL.md frontmatter must not use double-quoted strings that contain double quotes inside them. This breaks YAML parsing and the packager will reject the skill.

**Wrong:**
```yaml
description: "Use when user says things like "every day" or "each morning"."
```

**Correct:**
```yaml
description: >-
  Use when user says things like "every day" or "each morning".
```

## Re-packaging all skills (maintenance command)

Run this to re-package every skill after a bulk edit:

```bash
SKILLS_BASE="~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/[plugin-id]/[session-id]/skills"
cd "$SKILLS_BASE/skill-creator"
for skill_dir in "$SKILLS_BASE"/*/; do
  skill_name=$(basename "$skill_dir")
  if [ "$skill_name" = "skill-creator" ]; then continue; fi
  python3 -m scripts.package_skill "$skill_dir"
done
```
