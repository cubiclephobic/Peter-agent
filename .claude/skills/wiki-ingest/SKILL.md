# wiki-ingest

Convert a raw source into a structured wiki page matching the format in wiki/index.md.

**Required page format** (must match exactly — wiki-lint and wiki-query depend on this):
- One-line summary at the top
- "What to read this for" section
- Body organized by subtopic
- "Last updated" field (YYYY-MM-DD)
- "Sources" line listing where each major section came from

**Before doing anything, ask two questions:**
1. "What's the target topic / file name for this wiki page?"
2. "What's the source?" Options: Paste text | Gmail | Slack | Google Drive | Mixed

**If Paste:** Ask user to paste the raw material, then write the wiki page.

**If live tool (Gmail, Slack, Google Drive, Mixed):**
- Ask for a relevance filter: topic keywords, date range (default: last 30 days), specific channels/senders/pages
- Fetch from the relevant tool using those filters
- Show a brief summary of what was found and ask the user to confirm before writing
- If results seem thin or off-topic, flag it and ask whether to adjust filters or supplement with a paste

**Multi-source rules:**
- Deduplicate overlapping information
- When sources conflict, note both versions and flag with "(sources disagree)"
- Add a "Sources" line listing where each major section came from

**Never silently overwrite an existing wiki file.** Propose the change as a diff and wait for approval.
