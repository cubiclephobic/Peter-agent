# kpi-architect

Define the right KPIs and build a performance framework that tracks whether a strategy is working — not just whether activity is happening. Third skill in the Govern stage.

Run as: `/kpi-architect [strategy or subject]`

---

## Behavior

### 1. Anchor to the strategy

KPIs without a strategic anchor become activity metrics. Pull the chosen strategy from `strategic-options` or `transformation-roadmap` if run this session. The framework should answer: "how would we know, 90 days from now, whether this strategy is working?"

### 2. Separate outcome metrics from activity metrics

The most common KPI mistake is measuring effort instead of result:
- **Outcome metrics (lagging):** revenue closed, client retention, margin per offer, net new pipeline value — the actual results the strategy is supposed to produce.
- **Activity metrics (leading):** outreach volume, content published, follow-up rate, proposals sent — the inputs that are supposed to produce outcomes.

Both matter, but they serve different purposes. Leading indicators tell you whether you're on track before results show up. Lagging indicators confirm whether the strategy worked. Never substitute one for the other.

### 3. Build a MECE hierarchy

Organize metrics from strategy-level down to operating-level:
- **Strategic KPIs (1–2):** the headline numbers that define success for the strategy over 6–12 months. For Zaradigm: revenue against the $5K–$15K/month target, and B2B pipeline value.
- **Operating KPIs (3–5):** the metrics that drive the strategic KPIs — pipeline conversion rate, average deal size, content-to-pipeline attribution, client retention.
- **Activity KPIs (3–5):** the weekly/daily inputs — outreach contacts per week, follow-up cadence on `decisionmakerboughtin` deals, content seeds processed, LinkedIn sync success rate.

Each level explains the one above it. If a strategic KPI moves unexpectedly, the operating and activity KPIs should tell you why.

### 4. Set thresholds, not just targets

For each metric: define not just the target but the floor (below this triggers a review) and the ceiling (above this, consider reallocating resources upward). A metric without a floor is just a number you track without acting on.

### 5. Define the review cadence

When does each KPI get reviewed, by whom, and what triggers a response?
- **Weekly:** activity metrics — are the inputs happening?
- **Monthly:** operating metrics — are the inputs producing the right outputs?
- **Quarterly:** strategic KPIs — is the strategy working?

For Zaradigm: Peter's weekly pipeline pulse already covers some of this — identify what's already tracked vs. what's genuinely new.

### 6. Output

**Format (scannable in under five minutes):**

- **Strategic KPIs:** the 1–2 headline metrics with target, floor, ceiling.
- **Operating KPIs:** the 3–5 mid-level metrics that explain the strategic ones — same format.
- **Activity KPIs:** the 3–5 input metrics — weekly targets, not aspirations.
- **Review cadence:** when each tier gets reviewed.
- **What's already tracked vs. net new:** avoid duplicating what Peter already surfaces in the pipeline pulse.
- **So what:** handoff to `value-realization` (embed these as the ongoing governance check).

### 7. Guardrails

- Don't build a dashboard for its own sake. Every metric on this list should drive a decision or trigger an action.
- Activity metrics are not a substitute for outcome metrics. High outreach volume with low pipeline growth is a signal, not a success.
- If a metric can't be measured with available tools (HubSpot, Calendar, Gmail, Slack), name the gap — don't include unmeasurable metrics as if they're tracked.
