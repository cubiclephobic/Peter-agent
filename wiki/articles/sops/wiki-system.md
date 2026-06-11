Source: session 2026-06-02/03 — wiki build + deployment
Confidence: 0.95
Updated: 2026-06-04 — Added my-ai-tools.md registry and auto-update hooks
Updated: 2026-06-05 — Migrated to Cloudflare Access; wiki is now auth-protected; DNS on Cloudflare; SSL via Origin Certificate
Updated: 2026-06-11 — Added Claude.ai access decision (Projects); Claude.ai chat capture workflow; article count updated

# Wiki System — How It Works

The knowledge wiki is Corinna's second brain and persistent memory across all AI sessions. Built and deployed in one session on 2026-06-02/03.

---

## What It Is

- **59+ markdown articles** organized by type (core/, brands/, services/, sops/, glossary/, tools/, people/)
- **Local path:** `/Users/corinnas/AI CODE/knowledge-wiki/`
- **Live URL:** https://wiki.zaradigm.com — protected by Cloudflare Access (email OTP, 1-week session)
- **Obsidian vault:** open the `knowledge-wiki/` folder directly in Obsidian

## Security (as of 2026-06-05)
- DNS: Cloudflare (nameservers: doug + laura .ns.cloudflare.com)
- SSL: Cloudflare Origin Certificate (wildcard *.zaradigm.com, expires 2041); Traefik uses file provider at `/docker/n8n/certs/`
- Edge auth: Cloudflare Zero Trust Access — corinna@zaradigm.com only, 1-week session
- VPS firewall: ports 80/443 restricted to Cloudflare IPs (iptables DOCKER-USER chain)
- Claude automations fetching from wiki.zaradigm.com: need CF-Access-Client-Id + CF-Access-Client-Secret headers (service token — store in `/Users/corinnas/AI CODE/.env`)

---

## Commands (run in Claude Code)

| Command | What it does |
|---------|-------------|
| `/wrap` | End-of-session — summarizes session, updates wiki articles, appends to log.md |
| `/wiki-update` | Morning ritual — pulls Krisp meetings + HubSpot activity from last 24h, updates wiki |
| `/ingest [source]` | Ad-hoc — ingests any URL, file, or pasted text into the right wiki article |
| `/lint` | Audit — 7-check scan: stale articles, missing fields, dead wikilinks, contradictions, low-confidence |

---

## Automated Pipelines

### iPhone → raw/ (every 5 minutes)
1. Say "Hey Siri, Wiki Note" → type or dictate note
2. Saves to iCloud Drive / Wiki Inbox / phone-note.txt
3. Mac watcher script picks it up every 5 min → moves to `raw/` with timestamp
4. **Requires:** Full Disk Access granted to `/bin/bash` in System Settings

### Nightly update (1am)
- Script: `/Users/corinnas/AI CODE/scripts/wiki-nightly-update.py`
- Reads `content-seeds-log.md` (new seeds from transcript_processor.py)
- Pulls recent HubSpot notes via API
- Calls Anthropic API to process → updates wiki articles
- **Does NOT spawn Claude CLI** — pure Python/API call, no conflicts
- LaunchAgent: `com.corinna.wiki-nightly-update`

### VPS sync (2am)
- Script: `/Users/corinnas/AI CODE/scripts/sync-wiki-to-vps.sh`
- Regenerates wiki.html, rsyncs to VPS
- LaunchAgent: `com.corinna.wiki-sync-vps`

### Transcript processing (on-demand)
- Script: `/Users/corinnas/AI CODE/transcript_processor.py`
- Watch Downloads/ for Krisp transcript exports
- Calls Anthropic API → extracts content seeds → appends to `articles/sops/content-seeds-log.md`
- Run: `python3 transcript_processor.py --watch` or `--file path` or `--batch`

---

## How to Add Content

| Situation | What to do |
|-----------|-----------|
| Quick note from phone | "Hey Siri, Wiki Note" → dictate |
| Quick note from Terminal | `note "your text"` |
| Meeting happened | Run `/wiki-update` next morning |
| Drop a file or URL | Run `/ingest [path or URL]` |
| End of Claude Code session | Run `/wrap` |
| Valuable Claude.ai/chat session | Ask Claude to summarize → paste into Claude Code → run `/ingest` |
| Periodic cleanup | Run `/lint` |

### Capturing Claude.ai conversations

Claude.ai chats are invisible to the wiki by default — nothing flows in automatically. At the end of any chat worth keeping (strategy discussion, client thinking, content decision, positioning work), do this:

1. Ask Claude.ai: *"Summarize the key decisions and insights from this conversation as a wiki note."*
2. Copy the summary
3. Open Claude Code → paste the summary → run `/ingest`

The `/ingest` command will extract the key facts and route them to the right article(s). Takes under 2 minutes and closes the gap.

---

## Architecture

```
iPhone shortcut → iCloud Inbox → watcher → raw/
Krisp transcript export → transcript_processor.py → content-seeds-log.md
/wiki-update → Krisp MCP + HubSpot API → wiki articles
Nightly Python script → HubSpot API + seeds log → wiki articles
2am rsync → wiki.zaradigm.com (VPS, nginx, Traefik HTTPS)
```

---

## Key Technical Facts

- **VPS:** 167.88.43.189 / srv1306803.hstgr.cloud, Ubuntu 24.04
- **SSH key:** `~/.ssh/dashboard_deploy_key`
- **Docker path on VPS:** `/docker/wiki/`
- **Wiki served by:** nginx:alpine, Traefik handles HTTPS
- **D3.js graph:** force-directed, nodes = articles, edges = `[[wikilinks]]`
- **Confidence scores:** 0.9+ = Corinna's own words; 0.7-0.89 = transcripts/tool data; <0.5 = flag for lint
- **Wiki not accessible from Claude Web/Chat via URL** — Claude.ai cannot do authenticated HTTP requests (no header injection, no cookie storage, no OAuth). Claude Code and Cowork fetch via service token in `.env`.
- **Claude.ai phone access solution:** Claude Projects — upload wiki.html to a "Zaradigm Brain" Project; every chat inside that Project has full wiki context. Re-upload manually when wiki changes significantly. Options evaluated and rejected: token URL (sensitive URL in conversation history), public filtered subdomain (truly public, no fence — unacceptable for client data).

---

## LaunchAgents (running)

| Label | Schedule | Does |
|-------|----------|------|
| `com.corinna.wiki-inbox-watcher` | Every 5 min | Moves iCloud inbox files → raw/ |
| `com.corinna.wiki-nightly-update` | 1:00 AM | Python API script updates wiki from Krisp + HubSpot |
| `com.corinna.wiki-sync-vps` | 2:00 AM | Regenerates wiki.html + rsyncs to VPS |

---

## Related

- [[ai-terms]] — glossary of AI concepts referenced here
- [[sources]] — full list of tools and integrations
- [[content-seeds-log]] — auto-appended seeds from transcript_processor.py
