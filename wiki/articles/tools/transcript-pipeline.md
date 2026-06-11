Source: Built in Claude Code session 2026-06-04
Updated: 2026-06-04 — Two bugs fixed: (1) --dangerouslySkipPermissions → --dangerously-skip-permissions in both scripts; (2) ANTHROPIC_API_KEY now exported from .env before claude CLI runs to fix "Not logged in" error in non-interactive shell
Confidence: 0.95

# Transcript Pipeline — Krisp → Content Seeds

Automated daily pipeline that pulls meeting transcripts from Krisp, clusters them by meeting type, generates structured recaps via Claude API, and appends content seeds to the wiki.

---

## Files

| File | Purpose |
|------|---------|
| `/Users/corinnas/AI CODE/transcript_processor.py` | Core processor — Claude API call, recap generation, wiki seed append |
| `/Users/corinnas/AI CODE/scripts/krisp-fetch.sh` | Shell script invoked by launchd — calls Claude CLI with Krisp MCP |
| `/Users/corinnas/AI CODE/scripts/krisp-fetch-prompt.md` | Claude prompt for Krisp fetch + clustering logic |
| `/Users/corinnas/AI CODE/krisp-transcripts/[CLUSTER]/` | Raw transcripts saved by cluster before processing |
| `/Users/corinnas/AI CODE/Content Seeds via Trans/[CLUSTER]/` | Processed recap .md files, sorted by cluster |
| `/Users/corinnas/AI CODE/knowledge-wiki/articles/sops/content-seeds-log.md` | Running wiki log of all seeds — auto-appended per run |
| `/Users/corinnas/AI CODE/processed_log.json` | Deduplication log — prevents reprocessing |
| `/Users/corinnas/AI CODE/krisp-fetch.log` | Run log |
| `~/Library/LaunchAgents/com.corinna.transcript-watcher.plist` | launchd agent — fires daily at 5 PM |

---

## Schedule

Runs daily at **5:00 PM CST** via launchd (`com.corinna.transcript-watcher`).

---

## Cluster Categories

Meetings are classified into one cluster before processing. Priority order: EDU → COACHING → PARTNER → CLIENT → OTHER.

| Cluster | Signals |
|---------|---------|
| `COACHING` | Any 1:1 coaching session — all platforms (Torch, Leland, the/SHIFT, Zaradigm direct). No distinction made between platforms. |
| `PARTNER` | Participant is a known partner (see list below) |
| `EDU` | Meeting name/content mentions NCI, AI Builder, or Mediation (training context) |
| `CLIENT` | Other client coaching/consulting delivery sessions |
| `OTHER` | Internal, admin, vendor, unclassified |

**Partner list (PARTNER cluster):**
Joe Weston, Dave Ward, Danny Brassell, Tameka, Jerica, Kirsty Best, LifeCoachHub / LCH, Atlas, Michael Beas, Fabiana, John Largent

---

## Output per Transcript

Each processed transcript produces:
1. **Recap file** → `Content Seeds via Trans/[CLUSTER]/YYYY-MM-DD_[type]_[name].md`
   - Meeting type, participants, 3–5 bullet summary, action items, 2–4 content seeds
2. **Wiki seed entry** → appended to `content-seeds-log.md`, newest first, tagged `[ZARADIGM]` / `[COACHILLY]` / `[BOTH]` and by cluster

---

## Brand Sorting (Content Seeds)

| Brand tag | Signals |
|-----------|---------|
| `[COACHILLY]` | Career coaching, job search, resume, interview prep, executive presence, salary, LinkedIn profile, Leland, BHS |
| `[ZARADIGM]` | Entrepreneurship, business strategy, AI in business, consulting, brand building, B2B, Zaradigm clients |
| `[BOTH]` | Genuine overlap — kept short by design |

Claude makes the primary call; keyword list cross-checks as sanity layer.

---

## Manual Run Commands

```bash
# Process a single file
python3 "/Users/corinnas/AI CODE/transcript_processor.py" --file path/to/transcript.txt --cluster PARTNER

# Batch process a cluster folder
python3 "/Users/corinnas/AI CODE/transcript_processor.py" --batch --folder "/Users/corinnas/AI CODE/krisp-transcripts/COACHING/" --cluster COACHING

# Run the full Krisp fetch manually
bash "/Users/corinnas/AI CODE/scripts/krisp-fetch.sh"

# Watch live log
tail -f "/Users/corinnas/AI CODE/krisp-fetch.log"
```

---

## API Cost

~$0.01–$0.15 per transcript depending on length. At 1–5 transcripts/week: **under $1/month**.
Uses `ANTHROPIC_API_KEY` from `/Users/corinnas/AI CODE/.env`.

---

## Status

**Live as of 2026-06-04 — first successful run pending confirmation.** Full backfill completed: 94 transcripts processed across all clusters, 97 recap files generated, wiki seeds log populated with ~1,200 lines of content seeds.

- launchd agent loaded and scheduled at 5 PM daily
- plist updated to run `krisp-fetch.sh`
- `dotenv override=True` fix applied (was silently failing to load API key in Python processor)
- `corespeechd` meetings now skipped automatically in fetch prompt
- processed_log.json has 91 entries — deduplication working

**Known bugs fixed (2026-06-04):**
- `--dangerouslySkipPermissions` (camelCase) → `--dangerously-skip-permissions` (hyphenated) — wrong flag caused silent fail at 5 PM
- Added `export ANTHROPIC_API_KEY` from `.env` to both `krisp-fetch.sh` and `wiki-nightly-update.sh` — Claude CLI returns "Not logged in" when run from launchd/non-interactive shell without explicit API key in environment
