# biz-dev-email

Draft a warm re-engagement email grounded in real HubSpot relationship context. Save as Gmail draft in corinna@zaradigm.com.

Run as: `/biz-dev-email [contact name]`

See full instructions in ~/.claude/commands/biz-dev-email.md (installed locally). This file is a pointer — the canonical skill lives in the local commands directory.

**Summary of behavior:**
1. Pull last 5 notes + 3 email engagements from HubSpot for the contact
2. Classify relationship depth: A (personal/coaching alumni), B (professional warm), C (B2B corporate)
3. Draft email following structure: earned opener → news/angle → why it matters to them → CTA scaled to depth
4. Apply Zaradigm voice: no em-dashes, no banned words, short paragraphs, punchy sentences
5. Self-check before presenting (specificity, warmth calibration, CTA match)
6. Ask "Save as Gmail draft?" then use Gmail MCP to create draft in corinna@zaradigm.com
