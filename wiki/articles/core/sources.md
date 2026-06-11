Source: interview 2026-06-02 + CLAUDE.md + my-ai-tools.md + ai-terms.md
Confidence: 0.90

# Sources — References, Tools, People, and Inputs I Rely On

---

## AI Tools

| Tool | Role | Notes |
|------|------|-------|
| **Claude Code** (this) | Primary AI work environment | Agentic, file system access, MCP integrations; where the wiki, skills, and automations live |
| **Claude Web / claude.ai** | Secondary; quick tasks, web-accessible sessions | No file system access; uses wiki via URL once VPS sync is built |
| **n8n** (self-hosted on VPS) | Workflow automation | Daily wiki update, email manager, morning brief; open-source, runs on Corinna's VPS |
| **NotebookLM** | Research and pattern analysis | Used for client intel analysis (see client-intel-marketing.md); conversation-based synthesis |

---

## Connected Integrations (MCP)

All connected via Model Context Protocol — Claude can read/write to these during sessions:

| Integration | What It's Used For |
|------------|-------------------|
| **HubSpot** | CRM: contacts, pipeline, session notes, deal tracking; primary BD tool |
| **Gmail** | Email: client comms, outreach, proposals |
| **Google Calendar** | Scheduling: coaching sessions, discovery calls, mediations |
| **Google Drive** | Documents, proposals, client materials, CSS documents |
| **Krisp** | Meeting transcripts and action items from coaching/client sessions |
| **Slack** | Team/async comms |
| **Canva** | Design: brand assets, social content, presentations, brand kits |
| **Typeform** | Intake forms, surveys, client onboarding |
| **Apollo** | Prospecting and contact sourcing for outreach |
| **Leland** | Coaching marketplace presence; events and bookings |

---

## Business Tools

| Tool | Role |
|------|------|
| **HubSpot CRM** | Pipeline, contact records, outreach sequences, notes |
| **Apollo.io** | Lead prospecting, contact enrichment |
| **Zoom** | Client sessions, Torch coaching, events |
| **Canva** | All brand design work; brand kits live here for Zaradigm, CMAG, and client brands |
| **PowerPoint** | Decks, proposals, workshop materials |
| **PDF Tools** | Reading, signing, extracting from PDFs |

---

## Coaching and Facilitation Tools

| Tool | Role |
|------|------|
| **PrinciplesYou™ / PrinciplesUs™** | Personality and team assessments used in HiPe TC and individual coaching; licensed through ZARADIGM |
| **Torch** | B2C coaching platform; structured 45-min sessions with individual clients |
| **Coaching.com** | Marketplace for PYA debriefs and sponsored coaching |
| **Solution Focused Team Coaching® framework** | Methodological foundation for HiPe TC |

---

## Learning Sources

### Courses and Certifications

| Source | What It Provided |
|--------|-----------------|
| **AI Builder Course** | Current — AI automation, n8n workflows, agentic tools, building with Claude; active learning being ingested into wiki |
| **UTD Mediation Certification** | Business mediation foundations; governs mediation practice under Texas law |

### Books and Frameworks Referenced in Work

| Source | How It's Used |
|--------|---------------|
| **Andrej Karpathy's LLM Wiki pattern** | Foundation for this wiki's architecture — "compounding artifact" concept, ingest/query/lint cycles |
| **Solution Focused coaching literature** | Underpins HiPe TC methodology |
| **CAR Method** | Communication framework used with clients (Context → Action → Result) |
| **Eisenhower Priority Matrix** | Productivity framework referenced in coaching and CMAG content |
| **"Flying at the same altitude" analogy** | Signature Zaradigm communication metaphor — used in client work and content |

---

## People and Influences

| Person / Source | Why They Matter |
|----------------|----------------|
| **Andrej Karpathy** | LLM wiki pattern (gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f); the conceptual foundation for this wiki |
| **Joe Weston** | Current collaborator; building MCP server for course deployment at scale; creating thumbnails, demo videos, and sales page testing version; meeting June 16 |
| **Tameka Kee** | Active referral partner |
| **Coaching.com / PrinciplesYou marketplace** | Inbound lead source for sponsored coaching and PYA debriefs |
| **AI-Ready CMO** | Reference model for content writing — cutting to the chase, practical, concise, relatable; cited in both brand kits as voice inspiration |

---

## Content Reference Sources

| Source | Role |
|--------|------|
| **Own client transcripts and session notes** | Primary source for content; anonymized patterns and insights feed the/SHIFT newsletter and blog |
| **ICF Global Coaching Study** | Statistical references in CMAG content (e.g., coaching rates article cites 2025 data) |
| **HBR, Forbes** | Industry reference for the/SHIFT topic bank ("leading through uncertainty/ambiguity" per 2026 data) |
| **Zippia research** | Statistics cited in HiPe TC materials (27% sales increase from communication improvement) |

---

## File and Knowledge Locations

| Location | What Lives There |
|----------|-----------------|
| `/Users/corinnas/AI CODE/` | Primary AI work directory; wiki, scripts, dashboard |
| `/Users/corinnas/Desktop/my-agents/` | Skills (.skill files), scripts, environment config |
| `~/.claude/commands/` | Slash commands (/log-linkedin, /shift-invite, /biz-dev-email, /course-extract) |
| `Google Drive / AI CONTEXT/` | CSS documents (now migrated to wiki); context docs for Claude sessions |
| `Canva` | Brand kits for Zaradigm (DAG9TEoJLsM), CMAG (DAG9TehMscw), USVA (DAHBoYxZYpw) |

---

## Related

- [[ai-terms]] — definitions of AI tools and concepts referenced here
- [[hubspot]] — CRM details and automation status
- [[zaradigm]] — brand that relies on these sources
- [[domain]] — expertise these sources support
