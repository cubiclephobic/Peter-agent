# HubSpot

Source: Google Drive — "CSS_HubSpot" (migrated 2026-06-02)
Confidence: 0.85
Updated: 2026-06-03 — Added data reliability rules and stage label mappings from morning brief build
Updated: 2026-06-04 — LinkedIn→HubSpot sync automation built and live; private app token confirmed working for notes creation

## What This Is

Current State Summary of AI-assisted HubSpot activity. Part of an ongoing Biz Dev Sprint launched March 20, 2026. Full sprint details: [CSS_BizDev Sprint](https://docs.google.com/document/u/0/d/1Dq4vSvcPtyGZCtWF30igl0movJPYHUvxaflxGLLFQGM/edit)

---

## Session Recap — March 5, 2026

### Outreach Sent (7 people)

| Contact | Channel | Message Type |
|---------|---------|-------------|
| Alli | LinkedIn DM + email | the/SHIFT invite, call slots offered |
| Ramona | LinkedIn DM + email | the/SHIFT invite, free month saved for call |
| Michele | Email + text | Relationship check-in, no pitch |
| Jaime | Email | Check-in + the/SHIFT intro |
| Jamie K | Email | Pure check-in |
| Matthew | Email | Check-in on job search |
| Nicole | Email | Check-in, soft hint, follow-up task set for 2 weeks |

### HubSpot Changes Made

- Added 5 new lead statuses
- Updated 13 contact records
- Flagged duplicate records: Joseph Coleman and Liz Buard (pending merge)

---

## Current State

### Lead Statuses (as of March 5, 2026)

New / Do Not Contact / Existing / Warm - Re-engaging / Active Opportunity / Nurture / Customer / Paused

### Duplicate Records to Merge

- Joseph Coleman: IDs 472901 + 515151
- Liz Buard: IDs 120599439543 + 31892955756

### Known Record Issues

- Matthew Smith (ID 207340526188) — not findable by name search; only findable by email filter

### Segments Needing Bulk Updates

- "SBA ..." lists — all qualify for CATALYST outreach → set to Nurture status
- "TalentConnect 25" — nurture list for leadership/team coaching prospects (HiPe TC targets)

---

## Key Decisions

### Outreach Strategy

- **Warm/personal outreach** (today's contacts): Corinna writes with AI support. Relationship-first, never automated.
- **Scale outreach** (the other 90-95%): Prospecting Agent territory. Systematized but still uses Corinna's voice/tone. Identified as the next major unlock.

### Per-Contact Commitments

- **Ramona**: Free first month honored from June 2025 cancellation agreement. Held for the call — not mentioned in email. Be prepared if she brings it up.
- **Michele**: Not pitched the/SHIFT. Between-session peer engagement gap (her feedback) has not been addressed. Do not re-invite until pairing approach is designed.
- **Jamie K**: Nurture only. Treats development as a job-transition tool, not ongoing growth. Re-engage when she has a specific need.
- **Nicole Ardiet**: Follow-up task set for ~March 19. If she's landed a role → invite to the/SHIFT. If still searching → check-in only, no pitch.

---

## Next Steps (Prioritized)

1. **Between-session engagement design for the/SHIFT** (pairing approach) — blocks Michele's re-invitation
2. **Prospecting Agent setup** — voice/selling profiles, Corinna's tone
3. **SBA + TalentConnect 25 bulk status updates**
4. **Prospecting Workspace** — daily operating rhythm dashboard

---

---

## Data Reliability Rules (learned 2026-06-03)

These rules apply any time Claude or an automation reads HubSpot data:

### Fields to trust
| Field | Reliability | Notes |
|-------|-------------|-------|
| `notes_last_contacted` | ✅ Reliable | Updates only when a human logs a call, email, or meeting note. Use for "last real contact." |
| `hs_email_click` | ✅ Reliable | Intentional action — someone clicked a link in your email. Strong re-engagement signal. |
| `dealname`, `amount` | ✅ Reliable | Static, manually set. |

### Fields NOT to trust as engagement signals
| Field | Why it's unreliable |
|-------|-------------------|
| `hs_lastmodifieddate` | Updates on ANY system event — email tracking pixel fires, automated syncs, background updates. Does NOT mean human engagement. |
| `hs_email_open` | Triggers on email preview panes, server-side pre-fetch, tracking pixels. Many "opens" are not real. Use clicks instead. |
| `dealstage` | Often stale — Corinna doesn't always update stages after conversations. Treat as a rough indicator only. |

### Stage label translations
HubSpot's default stage names are internal jargon. Plain-English equivalents:

| HubSpot Stage ID | Plain English |
|-----------------|---------------|
| `appointmentscheduled` | Meeting Scheduled |
| `qualifiedtobuy` | Qualified |
| `presentationscheduled` | Proposal Out |
| `decisionmakerboughtin` | In Discussion (champion aligned — NOT a final decision) |
| `contractsent` | Contract Sent |
| `closedwon` | Won ✅ |
| `closedlost` | Lost ❌ |

> `decisionmakerboughtin` is frequently misread as "almost won." It means the internal advocate is aligned, not that a deal is closing. Stage may also be stale.

### Deals closed lost (2026-06-03)
- Elan Website Recovery — marked Closed Lost (was 170d past close date, Michael went rogue)
- SBA Catalyst Kenya — marked Closed Lost (unresponsive)

### Active outreach deals (as of 2026-06-03)
- Rohit-SHIFT Group and SHIFT - Ali S — left open, part of active the/SHIFT cohort outreach

---

## LinkedIn → HubSpot Sync (live as of 2026-06-04)

Automated sync of LinkedIn conversations to HubSpot notes. Runs **Tuesday and Friday at 4:00 PM CST** via launchd.

### How it works
1. Opens LinkedIn messaging in Chrome
2. Reads all conversation previews from the sidebar
3. Haiku classifies each as genuine (mutual interaction) vs solicitation (cold outreach to Corinna)
4. Clicks through each genuine conversation and reads the thread
5. Finds the matching HubSpot contact by name
6. Creates a "Logged LinkedIn Message" note on their Activity feed
7. Skips contacts logged in the past 3 days (duplicate prevention)

### Files
| File | Path |
|------|------|
| Python script | `~/AI CODE/scripts/linkedin-hubspot-sync.py` |
| Shell wrapper | `~/AI CODE/scripts/linkedin-hubspot-sync.sh` |
| LaunchAgent | `~/Library/LaunchAgents/com.zaradigm.linkedin-sync.plist` |
| State file | `~/AI CODE/scripts/linkedin-sync-state.json` |
| Log | `~/AI CODE/scripts/linkedin-sync.log` |

### Dependencies
- Chrome must be open and logged into LinkedIn at 4pm on Tue/Fri
- `HUBSPOT_TOKEN` — from `~/AI CODE/scripts/.env` (existing private app, confirmed working for notes)
- `ANTHROPIC_API_KEY` — from `~/AI CODE/.env` (uses `claude-haiku-4-5` model)
- Chrome must have **View → Developer → Allow JavaScript from Apple Events** enabled

### HubSpot private app scopes confirmed working
`crm.objects.contacts.read`, `crm.objects.deals.read`, `crm.objects.deals.write`, `crm.objects.notes.write` (notes write confirmed via test — no explicit scope needed beyond existing)

### To run manually
```bash
bash "/Users/corinnas/AI CODE/scripts/linkedin-hubspot-sync.sh"
```

### Known behavior
- Contacts not in HubSpot → logged as `NO_CONTACT` in log, skipped silently
- Solicitations filtered by Haiku → skipped, counted in summary
- Stop hook was built first but abandoned — caused infinite token-burning loop. Python script approach is correct.

---

## Related

- [[bizdev-sprint]] — active sprint using HubSpot for outreach tracking
- [[the-shift]] — the/SHIFT outreach sequences live in HubSpot
- [[s5tech-coaching]] — client record lives in HubSpot
- [[ai-terms]] — see "MCP" for how HubSpot connects to Claude
