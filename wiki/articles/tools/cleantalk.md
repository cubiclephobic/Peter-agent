Source: Direct session observation 2026-06-03
Confidence: 0.95
Updated: 2026-06-03 — Article created from security triage sessions on both WordPress sites

# CleanTalk Security (WordPress)

CleanTalk Security is the malware scanner plugin installed on both of Corinna's WordPress sites. It runs automatic scans and sends email alerts when it flags files or pages as Critical, Suspicious, or Frontend Malware.

## Sites covered
- **zaradigm.com** — WordPress admin user: Corinna
- **coachilly.com** (Coachilly Magazine) — WordPress admin user: COACHILLY MAG

## Scanner URL
`https://[site]/wp-admin/options-general.php?page=spbc&spbc_tab=scanner`

## Scan results sections
- **Files scan results:** Critical, Suspicious, Approved, Cure Log, Unknown
- **OS Cron Analysis:** Oscron
- **DB Trigger Analysis:** Db Trigger
- **Pages scan results:** Frontend Malware, Frontend Scan Results Approved

## Known false positive patterns

These trigger CleanTalk alerts on every scan and are always safe to approve:

| Pattern | Detection type | Why it's a false positive |
|---|---|---|
| `wp-content/cache/[id]-nitropack/...` | Any | NitroPack cache files. Purge NitroPack cache after approving — files reappear until cache is cleared. |
| `wp-content/cache/*/` with detection `SEO_SPAM_test` | SEO_SPAM_test | Cached page artifact, not actual spam injection |
| `wp-content/plugins/[plugin]/languages/*.l10n.php` | Suspicious: unreadable | Compiled binary locale/translation files — normal for any multilingual plugin |

**Observed on coachilly.com (2026-06-03):**
- 3× NitroPack cache files flagged Critical
- 4× `hostinger-ai-assistant/languages/*.l10n.php` files flagged Suspicious (he_IL, hi_IN, ja, th locales)

**Observed on zaradigm.com (2026-06-03):** All clean — 0 Critical, 0 Suspicious, 0 Frontend Malware.

## Escalation triggers (do NOT approve — report to Corinna)
- Any file not matching the false positive patterns above
- Frontend Malware pages containing: `eval()`, `base64_decode()`, obfuscated JS, `<script src>` loading from unknown external domains

## Triage workflow
Use the `/cleantalk-triage` skill. It handles both sites, classifies all items before touching anything, uses bulk approval (not file-by-file), purges NitroPack cache when needed, and re-runs the scan to confirm clean.

**Bulk approval method:** Bulk actions dropdown → "Approve" → "Apply to all" — clears an entire section in one click once all items are confirmed safe.

## NitroPack dashboard
Navigate via WordPress sidebar → NitroPack (not via direct URL — path varies per install).
Purge cache → confirm → return to CleanTalk scanner → Perform Scan → verify Critical count drops to 0.

## Related plugins on coachilly.com
- **NitroPack** — performance/cache plugin; free tier; causes recurring false positives
- **Hostinger AI Assistant** — plugin with multilingual locale files; causes recurring Suspicious flags
