Source: Built in Claude Code session, 2026-05-29 through 2026-06-03
Confidence: 0.95
Updated: 2026-06-03 — Initial article created
Updated: 2026-06-04 — Changed to weekly (Monday 7 AM); removed Market Snapshot and GitHub Radar sections
Updated: 2026-06-05 — Cost analysis done; redesign planned (see Pending below)

> STALE: Current setup is too expensive and Corinna doesn't read it daily. Claude processes the full script output just to prepend 2 small sections — poor token ratio. HubSpot queried twice (script + Claude connector). Redesign pending: weekly, Gmail delivery, remove Claude from pipeline, move calendar into the Python script directly. Prompt for redesign session is in log.md (2026-06-05 entry).

# Morning Brief Automation

## What It Is

A weekly Slack brief delivered to `#theshiftpractice` on **Monday at 7:00 AM** via the `daily_stock_brief` Slack bot. Built entirely in Claude Code using Python stdlib (no pip installs). Runs as a macOS launchd job.

---

## Files & Locations

| File | Path | Purpose |
|------|------|---------|
| Main script | `~/my-agents/morning_brief.py` | Fetches all data, assembles Block Kit, sends to Slack |
| Slack sender | `~/my-agents/slack_send.py` | Standalone script to post `brief_output.txt` to Slack |
| Scope doc | `~/my-agents/morning-brief-scope.md` | Design decisions and API key inventory |
| LaunchAgent | `~/Library/LaunchAgents/com.zaradigm.morningbrief.plist` | Schedules 7:30 AM run Mon–Fri |
| Keys | `~/AI CODE/.env` | MASSIVE_API_KEY, SLACK_BOT_TOKEN, SLACK_CHANNEL, NEWS_API_KEY, HUBSPOT_TOKEN |
| Log | `~/AI CODE/morning-brief.log` | stdout from each run |
| Error log | `~/AI CODE/morning-brief-error.log` | stderr — check here if brief stops arriving |

> **Important:** Script must live in `~/my-agents/` (home directory), NOT `~/Desktop/my-agents/`. macOS TCC sandboxing blocks launchd from accessing Desktop/Documents/Downloads. Moving to home directory fixed the `Operation not permitted` error.

---

## Sections (in order)

| Section | Source | Notes |
|---------|--------|-------|
| ☀️ Header | Static | Day + date |
| 🌤 Dallas Weather | Open-Meteo API | Free, no key. 8am / 12pm / 4pm temps + condition |
| 📚 Research Desk | NewsAPI (domains filter) | Only: hbr.org, sloanreview.mit.edu, mckinsey.com, gallup.com, kornferry.com, knowledge.wharton.upenn.edu, bcg.com. 3 insights/day, scored by data signals. Format: `N. Description (Source)` |
| 🔥 Pipeline Pulse | HubSpot private app | Two sub-sections only: (1) deals with stage = Meeting Scheduled; (2) contacts with email click > 0. No invented next steps. |
| 💬 Quote of the Day | Hardcoded list (31 quotes) | Rotates by day-of-year. Sources: Maya Angelou, Myles Munroe, Tony Robbins, Warren Buffett, Carly Fiorina, Michelle/Barack Obama, Sheryl Sandberg, Francis Chan, Rick Warren, Mark Cuban, Barbara Corcoran, Kevin O'Leary |
| 📊 Dashboard | Static link | `dashboard.zaradigm.com` with Zaradigm favicon via Block Kit context block |

> **Removed sections (2026-06-04):** Market Snapshot (Massive API, 13 tickers) and GitHub Radar were removed as too cumbersome. Removal cut run time from ~3 min to under 30 sec.

---

## Slack Bot Setup

- **Bot name:** `daily_stock_brief`
- **Workspace:** theshift-corp.slack.com
- **Channel:** `#theshiftpractice` (ID: `C0B745FUBL2`)
- **Token:** `xoxb-...` stored in `.env` as `SLACK_BOT_TOKEN`
- **Scopes:** `chat:write`
- **Delivery:** Slack Block Kit (`blocks` parameter) — `unfurl_links: false`, `unfurl_media: false`

---

## HubSpot Private App

- **App name:** Morning Brief
- **Scopes:** `crm.objects.deals.read`, `crm.objects.contacts.read`, `crm.objects.deals.write`
- **Token:** stored in `.env` as `HUBSPOT_TOKEN`

---

## Market Tickers Tracked

AAPL, B, BRK.B, CSCO, CVS, ELF, GOOGL, JBL, KLAR, LYFT, PHO, TSLA, VGT

> Note: AAPL occasionally returns no data from Massive API free tier. Monitor and swap if persistent.

---

## Key Design Decisions

- **Block Kit over plain text** — enables true 2-column layout (Leadership | AI & Work), styled blockquote for Quote, favicon in footer
- **NewsAPI domain filter over keyword search** — eliminates random news from unvetted sources; ensures Research Desk = trusted research only
- **`notes_last_contacted` not `hs_lastmodifieddate`** — `hs_lastmodifieddate` updates on any system event (email tracking pixels, syncs); `notes_last_contacted` only updates when a human logs a real interaction
- **Email clicks only for contacts** — opens are unreliable (preview panes, server-side pre-fetch); clicks are intentional engagement
- **No auto-generated next steps** — HubSpot stage labels are often stale; deal notes are not read; invented steps caused confusion and distrust

---

## Maintenance

- **If brief stops arriving:** Check `~/AI CODE/morning-brief-error.log`
- **To run manually:** `cd ~/my-agents && python3 morning_brief.py`
- **To reload schedule after edits:** `launchctl unload ~/Library/LaunchAgents/com.zaradigm.morningbrief.plist && launchctl load ~/Library/LaunchAgents/com.zaradigm.morningbrief.plist`
- **Market data gaps:** Free tier rate limit; gaps in morning run = API hit earlier that day during testing. Clears overnight.
- **Research Desk thin:** NewsAPI free tier returns ~30 articles; if fewer than 3 trusted-source articles are found, section shows "Nothing surfaced"

---

## n8n Update Reminder (added 2026-06-04)

An optional section (`section_n8n_update()`) added to `morning_brief.py` that checks GitHub for the latest n8n release and includes a Slack reminder when:
1. The release is **≥ 7 days old** (stability buffer — don't update on day of release)
2. **14+ days have passed** since the last reminder was sent (cooldown — not every day)

State file: `~/my-agents/.n8n_update_state.json` (tracks `last_notified_date` + `last_version_reminded`)

Format when triggered: `🔧 n8n Update Ready — vX.X.X released N days ago — stable enough to consider updating your VPS. [View changelog link]`

Fails silently if GitHub API is unreachable — never breaks the brief.

---

## Related

- [[hubspot]] — CRM where Pipeline Pulse data originates
- [[my-ai-tools.md]] — master inventory of all automations at `~/AI CODE/my-ai-tools.md`
