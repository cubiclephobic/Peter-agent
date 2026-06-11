# message-triage

Read incoming messages from connected inboxes (Gmail via Gmail MCP, Slack via Slack MCP). Rank each message: High, Medium, Low, or No Reply Needed.

**High:** Time-sensitive, from a client or active lead, requires decision or action today.
**Medium:** Needs a reply but not urgent — within 24–48 hours is fine.
**Low:** FYI, newsletters, no action required soon.
**No Reply Needed:** Automated, spam, or informational only.

For every message rated High or Medium, immediately invoke the /draft-writer skill with the full original message text and sender context.

Present a triage table first: sender, subject/preview, urgency rating, reason. Then hand off High/Medium messages one at a time to /draft-writer.
