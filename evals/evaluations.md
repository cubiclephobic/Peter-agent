<!--
This file is a running log of rubric-scored outputs for each agent (one section per agent,
populated by the /eval-output skill), plus a Review Queue of candidate fixes for any dimension
that scored below 5. Scoring rows are append-only. Each agent's section is owned exclusively
by that agent — never edit another agent's rows when scoring a different agent.
-->

## researcher

| Date | Test Case | On-target | Source quality | Evidence over assertion | Structure & scannability | Actionability | Overall | Status | Batch |
|------|-----------|-----------|-----------------|---------------------------|----------------------------|-----------------|---------|--------|-------|
| 2026-06-18 | 1 | 5 | 3 | 5 | 5 | 5 | 4.6 | PASS | |
| 2026-06-18 | 2 | 5 | 3 | 5 | 5 | 5 | 4.6 | PASS | |
| 2026-06-18 | 1 | 5 | 3 | 5 | 5 | 5 | 4.6 | PASS | 2026-06-18 |
| 2026-06-18 | 2 | 5 | 4 | 5 | 5 | 5 | 4.8 | PASS | 2026-06-18 |

## Review Queue

| Date | Agent | Test Case | Dimension | Score | Fix Type | Risk | Suggested Change | My Change | Action | Batch |
|------|-------|-----------|-----------|-------|----------|------|-------------------|-----------|--------|-------|
| 2026-06-18 | researcher | 2 | Source quality | 3 | Prompt | Low | In `.claude/agents/researcher.md` under "Research Standards," add a step requiring the agent to confirm each cited URL actually resolves and matches the title/publisher attributed to it before including it, and to never reuse one URL as the source for two differently-titled citations. Test case 2 cited the same right.com URL under two different titles/publishers ("Evaluating the Best Executive Coaching Companies" — Right.com, and "How to Choose an Executive Coaching Firm" — Tandem Coaching), and test case 1 cited two sources (Loeb Leadership, Global Coach Group) that returned 403/gated without flagging them as unverifiable in the body text (only in the source list). | | Applied | 2026-06-18 |
