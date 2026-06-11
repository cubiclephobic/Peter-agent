# wiki-lint

Scan all files in wiki/ and check for:
1. Duplicate entries across files
2. Pages where "Last updated" is missing or more than 30 days old
3. Missing required sections: one-line summary, "What to read this for", "Last updated"
4. Any topic files not listed in wiki/index.md

**Required page format** (validate against this):
- One-line summary at the top
- "What to read this for" section
- Body organized by subtopic
- "Last updated" field (YYYY-MM-DD)
- "Sources" line

Report all findings clearly. Do not make any changes to the files.
