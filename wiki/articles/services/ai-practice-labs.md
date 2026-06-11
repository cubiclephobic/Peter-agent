Source: Google Drive — "CSS_AI-PracticeLabs" (migrated 2026-06-02)
Updated: 2026-06-10 — Sales AI Practice Lab fully built and live (7 courses deployed); landing page live at zaradigm.com/sales-skills-ai-roleplay/; embed code resolved for Sales set; career coaching set queued as next build
Updated: 2026-06-11 — Career Conversations Practice Lab built (12 courses); embed code resolved — distribution_id is partner-level (same ID for all Zaradigm sets)
Updated: 2026-06-11 (session 2) — Career Conversations Practice Lab fully live: 9 broken courses deleted, slugs fixed, Building a Mentorship Relationship added to set, embed live on landing page; all 12 courses confirmed complete with grading criteria and key phrases

# AI Practice Labs (UpLeveled.ai Build)

**Last Updated:** June 9, 2026
**Owner:** Corinna Hagen / Zaradigm
**Platform:** UpLeveled.ai
**Purpose:** Track design, build, and quality state of Zaradigm's AI-powered leadership practice labs. Resume at the live edge of work each session.

---

## What This Is

A library of AI-powered behavioral practice labs on UpLeveled.ai designed to scale leadership development without constant one-off delivery. Each lab pairs named AI counterparts with a fixed archetype-per-scenario design, behaviorally-anchored rubrics, and a mapped set of key phrases. The library doubles as an enterprise-facing demo artifact for Bloomberg, S5 Tech, and NBA pipeline conversations.

Two platform categories: **The/SHIFT** and **HSC Book Companion**. Some practices appear in both.

---

## Current Status (as of June 11, 2026)

**Sales AI Practice Lab:** Fully built and live. 7 courses deployed June 9–10. Landing page live at https://zaradigm.com/sales-skills-ai-roleplay/ with working UpLeveled embed.

**Career Conversations Practice Lab:** Fully built and live as of June 11, 2026. 12 courses in the set, all with complete grading criteria (4 rubrics each) and 10 key phrases. Landing page embed live (same distribution_id as Sales set). 9 originally broken courses deleted; slugs corrected; Building a Mentorship Relationship (`a67771d0`) built from scratch and added. Telling Your Career Story criteria confirmed complete (not broken — was built correctly in a prior session).

**Sprint structure:** Days 1 through 11 (Day 4 split into A and B), followed by four dedicated HSC Book Companion builds, plus new standalone builds. "Day N" labels are internal sequencing only -- not learner-facing.

**Two prompt format generations:**
- V1: Days 1 through 7 (original format)
- V2 (enhanced): Day 8 forward, validated at 90% in playtest

All practices use the name-bug-proof two-part prompt pattern.

**UpLeveled MCP integration:** Partner API token (`mcp_7d25fc086e...`) is scoped to a specific distribution. Only 16 courses visible via API. Courses created via `create_course` land outside scope. Correct workflow: `duplicate_course` from accessible source. Joe (UpLeveled) notified of scope issue -- fix pending.

**Correct deployment workflow (confirmed June 9, 2026):**
1. `duplicate_course` from an accessible source course → creates unlinked draft revision
2. Edit scenarios via `update_scenario` (field is `rolePrompt`, NOT `counterpartyPrompt`)
3. Set rubrics via `update_grading_criteria` -- MUST use full rubric format with `rubric_scale` 0-4, `score_type: "rubric"`, `criterion_id`, `grading_version: "2.0"`. Simplified format (`id`/`label`/`weight`) causes client-side UI crash.
4. `validate_revision` → `create_hidden_course`
5. User activates in UI, sets difficulty levels and adds to set manually
6. Deactivate superseded versions in UI (hard delete not always possible)

**DO NOT use `create_course_revision`** -- creates a linked revision that cannot be published via API.

**Critical field names (learned from session):**
- Scenario role prompt field: `rolePrompt` (not `counterpartyPrompt`)
- Key phrases field: `gradingCriteria.instructor_notes.key_phrases` (array) inside `update_grading_criteria`
- Rubric format: must include `rubric_scale` with 0-4 anchors or UI crashes on course load

**practice-lab-builder skill:** Installed to `~/.claude/skills/practice-lab-builder/` with reference files for V2 format spec, quality checks (10-point QA), and existing practice library.

---

## Practice Library

| # | Title | Lab | Day/Source | Scenarios | Notes |
|---|-------|-----|------------|-----------|-------|
| 1 | SAR Leadership Under Pressure | The/SHIFT | Pre-sprint | Hannah, Derek, Nathaniel, Gabrielle, Aaron | V.2 live. Normal play 80%, sabotage 0% |
| 2 | Delegation Under Pressure | The/SHIFT | Day 1 | Zoe, Marsha, Samira, Phil, Kendrick | First name-bug-proof practice |
| 3 | Accountability Without Damage | The/SHIFT | Day 2 | Jamal, Diana, Rafael, Priya, Marcus | |
| 4 | Objection Handling for Leaders | The/SHIFT | Day 3 | Tanya, Victor, Simone, Wesley, Catherine, Jordan | Stakeholder-focused, NOT sales. Victor playtest: 86% |
| 5 | Self-Advocacy for Promotion | The/SHIFT + HSC | Day 4A | Elena, Martin, Leah, Gerald, Rachel | |
| 6 | When They Ask for the Next Level | The/SHIFT | Day 4B | Nadia, Owen, Keisha, Travis, Damien, Alicia | Leader-as-responder perspective |
| 7 | Leading Through Uncertainty | The/SHIFT + HSC | Day 5 | Megan, Andre, Sonia, Leon, Nina, Charles | Connects to HSC crisis communication chapter |
| 8 | Running the Room | The/SHIFT | Day 6 | Grace, Kirk, Paul/Renata, Frankie, Dominic, Beth/Omar/Elena | First multi-character scenarios |
| 9 | Feedback That Lands | The/SHIFT | Day 7 | Lydia, Sam, Vanessa, Terrence, Isla, Marco | First positive-feedback-only scenario (Lydia) |
| 10 | Peer Influence and Boundaries | The/SHIFT | Day 8 | Bridget, Theo, Janelle, Corey, Vivian, Roman | First V2 format. Playtest: 90% |
| 11 | Prioritization and Time Management | The/SHIFT | Day 9 | Daria, Glenn, Renee, Mitchell, Warren, Paige | All titles kept as-is (first time) |
| 12 | Authentic and Agile Leadership | The/SHIFT + HSC | Day 10 | Camille, Jared, Naomi, Felix, Lorraine, Dante | Dual-placed |
| 13 | Mastering Sales Objection Handling | The/SHIFT | Day 11 | Iris, Malcolm, Serena, Hector, Claudia, Nolan | First sales/biz dev practice |
| 14 | Mastering Persuasive Storytelling | HSC Ch 3.1 | HSC build | Greta, Owen, Joseph, Victor, Dominique | |
| 15 | Communicate Complex Ideas Clearly | HSC Ch 2.3 | HSC build | Priscilla, Ray, Selena, Desmond | Four-scenario practice |
| 16 | Mastering Strategic Negotiations and Positioning | HSC Ch 4.1 | HSC build | Adrienne, Mitchell, Luisa, Kendall, Tobias | |
| 17 | Executive Presence: Commanding the Room | HSC Ch 3.2 + 4.2 | HSC build | Patricia, Andre, Sterling, Vivienne, Margot | First non-verbal AI scenario (Sterling) |
| 18 | Mastering Active Listening | HSC Ch 4.3 | New build | Nadine, Derek, Sonia, Graham, Phoebe | courseId=5e416da9, slug=mastering-active-listening-v2. LIVE (activated by Corinna June 9). Phoebe scenario prompts manually pasted by Corinna. Deactivate intermediate draft (294d34a2) and original Ch 4.3 (eb1b8493). |
| 19 | Mastering the Hiring Interview | The/SHIFT | New build | Dominic, Mariana, Wesley, Simone, Kenji, Vivian | slug=master-effective-interview-techniques. LIVE. Description fix needed: remove "Grounded in real client needs:" prefix. Prompts need manual paste (blocked on Joe MCP fix). Wesley description corrected by Corinna. |
| 20 | Building Trust and Psychological Safety | HSC Ch 2.1 | New build | Helena, Terrell, Roxanne, Calvin, Loretta | courseId=738c66b5, slug=building-trust-and-psychological-safety. LIVE. Rebuilt from cold read; full V2 prompts deployed via API. |
| 21 | Engaging in Difficult Conversations | HSC Ch 2.1 | New build | Marcus, Priya, Donna, Jerome, Serena | courseId=c2def197, slug=engaging-in-difficult-conversations-2. LIVE (activated by Corinna June 9). Two broken hidden versions remain (8ae4b56d, bbc8d7a1) -- cannot be hard-deleted by UI. |

---

## In Progress / Open Items

- **Mastering the Hiring Interview:** LIVE. Needs: (1) description fix -- remove "Grounded in real client needs:" from last sentence, (2) narrator+role prompts pasted manually into all 6 scenarios (blocked on Joe MCP fix).
- **Active Listening cleanup:** Deactivate 294d34a2 (intermediate draft) and eb1b8493 (original Ch 4.3 shell). Corinna to do in UI.
- **Building Trust cleanup:** Deactivate e0ef57e6 (original shell). Corinna to do in UI.
- **MCP API scope issue:** Partner token sees 16 courses. Joe notified. Fix pending.
- **Sales AI Practice Lab:** Planning done. 8 new builds queued (see Sales Lab section below). Building now.
- **Docx conversions:** Cold Reads for Days 2 through 11 and HSC builds pending.
- **Content extraction:** YouTube/social key phrases for all practices pending.

**PARKED -- requires Joe's MCP fix first:**
Update remaining courses not in accessible 16: De-escalating Heated Conversations, Communicate Complex Ideas Clearly, Mastering Strategic Negotiations, Leading Through Uncertainty, Delegation, Self-Advocacy, Running the Room, Mastering Effective Feedback, Peer Influence and Boundaries, Authentic and Agile Leadership, Mastering Sales Objection Handling, Executive Presence, Mastering Promotion Conversations, Objection Handling for Leaders, Prioritization and Time Management.

---

## Sales AI Practice Lab

**Set URL:** https://www.upleveled.ai/pro/zaradigm-upleveled/set/sales-ai-practice-lab
**Landing page:** https://zaradigm.com/sales-skills-ai-roleplay/
**Embed:** `embed-set/sales-ai-practice-lab?distribution_id=23713cba-b105-4187-a558-0c6b3f53dbba&whitelabel=true`
**Status:** LIVE. All 7 new courses built and hidden-published. Corinna activates each in UI, fixes slug, uploads sales thumbnail.

---

## Embed Code

**CONFIRMED (June 2026):** UpLeveled set pages do NOT have an embed button in the instructor dashboard. The embed URL pattern is:
`embed-set/[set-slug]?distribution_id=[distribution_id]&whitelabel=true`

**KEY DISCOVERY (June 2026):** `distribution_id` is partner-level (Zaradigm account), NOT per-set. The same ID works for all Zaradigm sets.

**Zaradigm distribution_id (all sets):** `23713cba-b105-4187-a558-0c6b3f53dbba`

**Sales set embed (confirmed working):**
```html
<iframe id="upleveled-embed-sales" src="https://www.upleveled.ai/embed-set/sales-ai-practice-lab?distribution_id=23713cba-b105-4187-a558-0c6b3f53dbba&whitelabel=true" style="width:100%; height:700px; border:none; border-radius:8px;" allow="microphone" title="Sales AI Practice Lab"></iframe>
<script>window.addEventListener("message",function(e){if(e.data&&e.data.type==="upleveled-resize"){document.getElementById("upleveled-embed-sales").style.height=e.data.height+"px";}});</script>
```

**Career Conversations embed (confirmed working — tested June 2026):**
```html
<iframe id="upleveled-embed-career" src="https://www.upleveled.ai/embed-set/career-conversations-practice-lab?distribution_id=23713cba-b105-4187-a558-0c6b3f53dbba&whitelabel=true" style="width:100%; height:700px; border:none; border-radius:8px;" allow="microphone" title="Career Conversations Practice Lab"></iframe>
<script>window.addEventListener("message",function(e){if(e.data&&e.data.type==="upleveled-resize"){document.getElementById("upleveled-embed-career").style.height=e.data.height+"px";}});</script>
```

**Note:** `allow="microphone"` is required — all labs are audio/voice roleplay, not text chat.

---

## Career Conversations Practice Lab

### Courses in set (all live or pending activation)

| # | Title | CourseId | Status | Notes |
|---|-------|----------|--------|-------|
| 1 | Mastering Sales Objection Handling (Day 11) | existing | Live | 6 scenarios: Iris/Malcolm/Serena/Hector/Claudia/Nolan |
| 2 | Price Objections: Reading the Buyer | built prior session | Live | 5 archetypes: negotiation tactic, budget-locked champion, value gap, late-stage flinch, comparison shopper |
| 3 | Timing Objections: Not Right Now | built prior session | Live | 5 archetypes: genuine not-ready, serial delayer, quarter-end procrastinator, budget-frozen, avoidance disguised as timing |
| 4 | Mastering the Discovery Call | c3206345-7e7c-40da-8e44-28a10dee1e3c | Hidden — activate | Talker / tight-lipped exec / multi-stakeholder / skips to solution / first-time buyer |
| 5 | The Napkin Pitch | eab7197c-289f-4fb6-98fb-1b043d91b167 | Hidden — activate | Coffee referral / elevator / dinner party / inbound lead / skeptic in room |
| 6 | Closing the Deal | a538e3c1-2579-4784-8f81-1305438d71c0 | Hidden — activate | Stalled proposal / verbal yes / scope creep / competitor / decision paralysis |
| 7 | Negotiating the Deal | d596e172-b1e2-48ed-acb8-d9077b8f30aa | Hidden — activate | Vague discount ask / procurement / mid-engagement cut / low anchor / multi-issue table |
| 8 | Renewal and Expansion | 0b209d11-4f8c-4c9e-b2cf-5639683af464 | Hidden — activate | Renewal opener / static account / scope cut / referral conversion / strategic review |

**Per-course manual tasks (Corinna):** activate in UI + fix slug (auto-generates as `engaging-in-difficult-conversations-2-1`) + upload sales thumbnail (`AI Lab Sales THUMBpng.png`)

---

**Career Conversations set courses (12 total, all Live as of June 11):**
The Salary Negotiation, Telling Your Career Story, Building a Mentorship Relationship, The Career Conversation With Your Manager, Making the Case for a Promotion, The Career Pivot Conversation, Networking Without Cringing, The Job Interview, Asking for Sponsorship, Receiving Feedback, The Informational Interview, Navigating a Resume Gap.

**Landing page copy (written June 11):**
- Headline: "Practice the Career Conversations That Propel You Forward"
- Intro: "The conversations that shape careers are also the ones most people avoid. Asking for a promotion, making the pivot case, negotiating salary, building a mentorship — these aren't soft skills. They're the difference between good work that goes unnoticed and a career that actually moves. This lab gives you a place to practice them before they matter. Twelve scenarios across the full arc of career development: from getting the job to advancing in it, from asking for what you need to knowing when to move on."

---

## Next Steps

1. **Corinna:** Activate courses 4–8 in UI, fix slugs, upload sales thumbnails.
2. **Build Career Coaching set** -- next session (planned June 11+).
3. **Corinna:** Deactivate Active Listening cleanup (294d34a2, eb1b8493) and Building Trust shell (e0ef57e6).
4. **Corinna: fix Hiring Interview description** -- remove "Grounded in real client needs:" prefix.
5. **Await Joe's MCP fix** -- then paste Hiring Interview prompts and tackle parked courses.
6. Convert remaining Cold Reads to branded docx.
7. Extract key phrase content banks for all practices.

---

## Open Decisions

- **Narrator prompt format:** If narrator prompts are shown verbatim to learners, the V2 format needs a learner-facing layer. Pending investigation (platform bug blocking testing). Waiting on: Joe fix + Corinna confirmation.
- AI counterpart naming: first names only, or first plus last? Default: first names only. Waiting on: Corinna.
- Productize the three-tier Solo Playtest Protocol as a standalone Zaradigm methodology artifact. Waiting on: Corinna.
- YouTube shorts production workflow: solo filming or studio production. Waiting on: Corinna.
- Retrofit Days 1 through 7 with enhanced V2 prompt format. Waiting on: Corinna after further testing.
- S6 Roman scenario title: "Handling Resistance With Political Savvy" vs. alternative "Breaking Through Passive Resistance." Waiting on: Corinna.

---

## Key Decisions (Locked)

- Fixed archetype-per-scenario pattern. No single adaptive counterpart.
- Every AI counterpart gets a name. No nameless role plays.
- Every Role Prompt opens with: "AI INSTRUCTIONS. PLAY THIS CHARACTER: [Name]"
- Every Narrator Prompt opens with a ROLES IN THIS PRACTICE block.
- Behavioral anchors over vague descriptors in rubrics. Every scoring item must be observable.
- Three-tier Solo Playtest Protocol (Cold Read, Stress Play, Sabotage Play) runs before any lab goes live.
- No em-dashes in any Zaradigm document.
- Scoring: range-based. L0=0, L1=5, L2=8-10, L3=10-11, L4=11+.
- Brand palette: Popart Purple #4600FE (primary), Black (primary). Secondary: Deep Gray #afa8a8, Light Gray #d6d6d6, Popart Yellow, Popart Red.
- Fonts: GAEOL (logo only), DONAU (tagline only), Nunito (headlines/body), Kollektif (tight spaces).
- Header/footer: first page uses purple ZARADIGM logo; subsequent pages use black-and-white logo; footer carries page numbers.

---

## Scenario Count Guideline (Locked)

The right number is the fewest that cover all four rubrics without orphaning any, while spanning the full difficulty range. Driver is coverage, not volume.

- **Four scenarios:** Tight domain, naturally limited dynamics. Two beginner, two intermediate/advanced.
- **Five scenarios:** Full difficulty spread (2B/2I/1A), or one archetype deserves its own lane.
- **Six scenarios:** Wide domain with genuinely distinct dynamics at each tier (2B/2I/2A).

Test: if the last scenario feels like a remix, or a rubric only appears as secondary everywhere, adjust count.

---

## Build Delivery Format (Locked)

Every new practice delivered as ONE consolidated copy-paste block in this order:

1. Practice title and subtitle
2. Practice Lab placement
3. Course Description (one paragraph)
4. Rubrics (4 total) with behavioral anchors at all five levels (L0 through L4)
5. 10 Key Phrases mapped to rubric items
6. All scenarios in sequence, each containing: scenario number and character name, difficulty level, description, Narrator Prompt (full text), Role Prompt (full text)

Do not split across messages. Do not omit elements. Do not change the order.

UpLeveled builder extracts roughly 80% correctly. User manually paste-replaces Narrator and Role Prompts. User edits titles to her voice.

**MCP API path (June 8 forward):** With UpLeveled MCP server connected, Claude can populate courses directly via API -- creating courses, scenarios, rubrics, and pasting full prompts without browser automation. Also outputs structured JSON for n8n automation bridge.

**Standard thumbnails by lab category:**
- The/SHIFT: `/AI Practice Labs/thumbnails/shift-thumbnail.png`
- HSC Book: `/AI Practice Labs/thumbnails/hsc-thumbnail.png`
- Sales Lab: `/AI Practice Labs/thumbnails/sales-thumbnail.png`
- Career Lab: `/AI Practice Labs/thumbnails/career-thumbnail.png`

---

## Prompt Format V2 (Locked, Day 8 Forward)

**Narrator Prompt structure:**

```
ROLES IN THIS PRACTICE
Leader (human player): [one-line description]
[Character Name] (AI): [one-line description]

CONTEXT FOR THE AI
[Paragraph setting the scene]

WHAT THE LEADER IS PRACTICING
[One to two sentences naming the core skill]

WHAT GOOD LOOKS LIKE
[Observable success behaviors]

WHAT POOR LOOKS LIKE
[Observable failure modes]

SCENARIO FLOW
[Numbered sequence with branching based on leader choices]
```

**Role Prompt structure:**

```
AI INSTRUCTIONS. PLAY THIS CHARACTER: [Name].

[Opening paragraph establishing character and scene]

YOUR PERSONALITY
[Traits, motivations, style]

YOUR SIGNATURE MOVE
[One specific behavior the AI must exhibit at least once]

HOW YOU PLAY THE SCENE
[Bulleted behavioral instructions]

STAY IN CHARACTER. Do not coach, break frame, or reference that this is a practice.
```

---

## Title Conventions (Locked)

**Pattern:** Active verb + the workplace situation the leader faces. No metaphors, no lesson-framing, no cleverness.

**Rules:**
- Use active gerunds: Managing, Responding, Navigating, Addressing, Calling Out, Handling, Setting
- Name the situation, not the lesson
- Keep under 8 words when possible
- No quotes, question marks, or "How to" framing
- Professional noun-phrase style, not conversational
- Course-level: "Mastering [Skill]" is the preferred pattern
- HSC titles: no chapter labels in the title; chapter references go in the description

**Selected title edits (Corinna's vs. original):**

| Original | Corinna's Edit |
|----------|---------------|
| Drawing Out the Room When Nobody Speaks | Managing a Quiet Room |
| Your Team Just Learned AI Is Changing Their Work | Addressing Your Team's AI Uncertainty |
| Explaining a Reversed Decision to the Person It Affects | Conveying a Change of Direction |
| Speaking Up When the Room Is Performing | A Colleague Challenges Your Leadership |
| Keeping Momentum When They Stall | Handling a Timing Objection |
| Selling Through Your Champion | Navigating a Hidden Decision-Maker |
| Creating Awareness Without Condescension | Uncovering a Need the Prospect Does Not See |

---

## QA Workflow (Locked)

1. User uploads screenshot to Google Drive after building in UpLeveled.
2. Claude downloads via Drive MCP.
3. Agent extracts and transcribes all visible text.
4. Line-by-line comparison against originals: titles, descriptions, difficulty levels, rubric names, key phrases, prompt content.
5. Title changes logged for pattern learning.
6. Discrepancies flagged with specific fix instructions.

---

## Playtest Log

| Practice | Scenario | Difficulty | Score | Notes |
|----------|----------|------------|-------|-------|
| SAR Leadership | Normal play | Mixed | 80% | V.2 validated |
| SAR Leadership | Sabotage play | Mixed | 0% | Sabotage protocol confirmed |
| Delegation | Kendrick | Mixed | 59% | Name-bug fix confirmed working |
| Objection Handling | Victor | Beginner | 86% (38/44) | Calibrated easy for skilled user |
| Peer Influence | Unknown | Unknown | 90% (40/44) | V2 prompt format validated |

---

## Cold Read Files

Local path: `/AI Practice Labs/`

All sprint-built practices and HSC builds have Tier 1 Cold Reads. Delegation and SAR Leadership also have branded .docx versions with header/footer. Remaining Cold Reads (Days 2 through 11 and HSC builds) are pending docx conversion.

---

## Related Resources

- ZARADIGM Brand Kit 2026.pdf
- [How-To: AI Continuity](https://docs.google.com/document/d/1P9x1mbg69za8cmEUOCVcU0fMLClQ3q53qSc63umH1PQ/edit?usp=drive_link)
- Claude Cowork session: "Build AI roleplay scenarios for leadership labs"
- Practice Lab Catalog xlsx (updated with all builds, framework additions, and backlog queue)
- practice-lab-builder skill: `~/.claude/skills/practice-lab-builder/` (SKILL.md + references/)
- UpLeveled MCP server: configured in `~/.claude.json` (HTTP transport)
- Build files folder: Google Drive `AI Practice Labs/`

---

## Related

- [[zaradigm]] — parent brand; AI Practice Labs is a Zaradigm differentiator
- [[leland-ai]] — AI Practice Lab featured in Leland deck
- [[s5tech-coaching]] — S5Tech engagement includes AI Practice Labs discussion
- [[the-shift]] — AI Practice Lab is an add-on to the/SHIFT coaching

---

## Drive Folder (Products + Services)

Main folder (2_P+S): https://drive.google.com/open?id=12wqmR_XdP4xPRBv4es-h9-TSkuI1O0V1

| Resource | Link |
|----------|------|
| AI - Upleveled subfolder | https://drive.google.com/drive/folders/1TCNhxbQD0TS1IAozJ6YRe3uVnyKe2RNL |
| AI Comms PractiseLab Onboarding Script v1.1 | https://drive.google.com/file/d/14bdoUydBKFMUdJtpjr9fqes8C7PI4d32 |
| PY HIPE OFFER subfolder | https://drive.google.com/drive/folders/1ok4RChfMvMeTtrnXEb7yMnWbdz0_Tvuj |
| HIPE Zaradigm Landing Page Copy | https://drive.google.com/file/d/13CTDjkL-_BMsivQWcXcdR_ZcrZPufQTQ |
