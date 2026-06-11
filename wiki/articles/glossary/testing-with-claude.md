Source: iPhone shortcut — 2026-06-02 21:31
Confidence: 0.90

# Testing with Claude

## What This Is

A reference article for testing wiki functionality — specifically the end-to-end flow of the iPhone shortcut → iCloud Inbox → Mac watcher → raw/ → wiki article.

## Test Results (2026-06-02)

- iPhone shortcut sends note to iCloud "Wiki Inbox" folder ✅
- Mac watcher (launchd, runs every 60 sec) picks up file ✅
- File moved to `knowledge-wiki/raw/` with timestamp ✅
- `/ingest` or manual review promotes raw note to wiki article ✅
- Full Disk Access granted to `/bin/bash` — required for watcher to read iCloud Drive ✅

## Weekend Note

First live note added via iPhone shortcut on the evening of 2026-06-02. Pipeline confirmed working end-to-end.

## Related

- [[sources]] — tools and integrations overview
- [[ai-terms]] — wiki system concepts
