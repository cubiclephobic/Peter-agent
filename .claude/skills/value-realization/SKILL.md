# value-realization

Track whether a strategy or initiative is actually delivering the value it promised — and course-correct before too much time or resource is lost. Fourth skill in the Govern stage. The skill most organizations skip.

Run as: `/value-realization [strategy or initiative]`

---

## Behavior

### 1. Establish the value promise

What was the strategy supposed to deliver, by when? Pull from:
- `business-case-builder` — the financial model and go/no-go threshold established there.
- `kpi-architect` — the metrics and thresholds defined there are the baseline for this comparison.
- `transformation-roadmap` — the phase milestones define what "on track" looks like at each checkpoint.

If none of those exist, establish the baseline in this session: what was the expected outcome, and what's the measurement timeframe?

### 2. Pull actuals

Gather what's actually happened vs. what was expected:
- HubSpot (if available): revenue, pipeline, deal stages, close rates — compare to the business case model.
- Calendar: are the time investments happening as planned?
- Wiki or session notes: any qualitative signals (client feedback, market response, operational friction) that don't show up in the numbers yet.

Don't estimate actuals. If the data isn't available, name the gap rather than inferring.

### 3. Diagnose the variance

For each metric that's off-track:
- Is this a **timing variance** (on track but lagging the schedule)?
- Is it an **assumption failure** (a key variable from the business case turned out to be wrong)?
- Is it an **execution gap** (the right activities aren't happening)?
- Is it a **model error** (the financial model or KPI hierarchy was wrong)?

Each type of variance has a different response. Diagnosing before responding prevents the wrong fix.

### 4. Recommend a course correction

Based on the variance diagnosis:
- **Continue as planned:** if the variance is timing-related and the trajectory is sound.
- **Adjust the execution:** if the right moves aren't being made consistently.
- **Revisit the assumptions:** if a key assumption has been proven wrong — route back to `assumption-audit` or `strategic-options`.
- **Stop or pivot:** if the evidence says the strategy isn't working and the cost of continuing exceeds the cost of redirecting.

Name the recommendation plainly. Don't dress up a "stop" as a "pause."

### 5. Output

**Format (scannable in under five minutes):**

- **Value promised:** the original target and timeframe — one line.
- **Actuals vs. expected:** metric-by-metric comparison.
- **Variance diagnosis:** what type of variance is each gap — timing, assumption failure, execution gap, model error.
- **Course correction:** specific and direct — continue, adjust, revisit, or stop.
- **Next checkpoint:** when to review again, and what needs to be true by then.

### 6. Guardrails

- This skill assesses whether value is being captured. It doesn't relitigate the strategy decision — if the strategy was sound and execution is off, fix execution. If the strategy itself was wrong, route back to `strategic-options`.
- Never use positive activity metrics to mask a lagging outcome shortfall. "We sent a lot of outreach" is not evidence that the strategy is working.
- If the honest answer is "too early to tell," say so and name the earliest date at which the data would be meaningful — don't manufacture a verdict before the evidence exists.
