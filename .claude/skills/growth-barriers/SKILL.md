# growth-barriers

Identify what's actually blocking growth and prioritize which barriers to attack first. Second step in the Diagnose stage. Builds on a `situation-assessment` if one exists for the same subject — don't re-diagnose from scratch if one was just run.

Run as: `/growth-barriers [subject]`

---

## Behavior

### 1. Establish the baseline

If a recent `situation-assessment` exists for this subject (this session or the wiki), use its "so what" as the starting point. Otherwise, do a quick version inline: what's the current state, what's the goal, what's the gap.

### 2. Surface candidate barriers

List every plausible barrier to closing the gap — pipeline, capacity, pricing, positioning, operational, market timing. Cast wide here; don't pre-filter. Pull from real evidence (HubSpot pipeline data, calendar load, content cadence, wiki notes) wherever it exists rather than generic categories.

### 3. Find the root cause, not the symptom

For each candidate barrier, ask one level deeper: is this the actual constraint, or a symptom of something upstream? (e.g., "low close rate" is rarely the root cause — it's usually a symptom of weak qualification, pricing mismatch, or follow-up gaps.) Collapse symptoms into their root cause before prioritizing.

### 4. Prioritize

Rank root-cause barriers by **impact** (how much of the gap this actually closes) **× tractability** (can this realistically be acted on in the next 30–90 days with the resources that exist — solo operator, no team). Don't rank by urgency or loudness.

### 5. Output

**Format (scannable in under five minutes):**

- **The gap:** one line — current state vs. goal.
- **Top 2–3 barriers, ranked:** for each — the barrier, its root cause (not symptom), and a one-line read on impact × tractability.
- **Everything else considered but deprioritized:** one line, just the list, so nothing looks dropped by accident.
- **So what:** the barrier that, if removed first, unlocks the most — handoff point for `strategic-options`.

### 6. Guardrails

- This skill prioritizes blockers. It does not propose solutions — that's `strategic-options`.
- Don't inflate the list to look thorough. Three real barriers beat seven padded ones.
- If the honest answer is "the real barrier is bandwidth, not strategy," say that plainly — don't dress up a capacity problem as a strategy problem.
