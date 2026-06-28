# transformation-roadmap

Build a phased, time-anchored roadmap that turns a strategy into a concrete sequence of work — with milestones, dependencies, and a clear first 90 days. Third skill in the Execute stage.

Run as: `/transformation-roadmap [strategy or initiative]`

---

## Behavior

### 1. Anchor to the strategy and priority list

Pull from earlier skills if they exist:
- `strategic-options` — the chosen path defines the destination.
- `initiative-prioritizer` — the sequenced Now / Next / Later buckets are the raw material for the roadmap.
- `operating-model-design` — capability gaps define what needs to be built before certain phases can run.

If starting fresh, establish: what's the goal, what's the time horizon, and what are the 3–5 most important things that need to happen?

### 2. Phase the work

Structure the roadmap in three phases regardless of the overall timeline:
- **Phase 1 — Foundation (0–90 days):** the highest-leverage, lowest-dependency work. Quick wins that create momentum and evidence. Capability building that unlocks Phase 2.
- **Phase 2 — Build (90–180 days):** the harder, higher-effort moves that depend on Phase 1 being in place. Where the strategy starts to compound.
- **Phase 3 — Scale/Sustain (180+ days):** the steady-state operating rhythm. What does "this is working" look like as a repeatable system?

For shorter horizons (e.g., a 30-day sprint), compress the phases — but keep the logic: foundation → build → sustain still applies even over a few weeks.

### 3. Anchor each phase with milestones

For each phase, define:
- **What "done" looks like:** a concrete, observable outcome — not "make progress on X" but "X is live / Y is closed / Z is running without manual input."
- **Dependencies:** what must be in place before this phase can start?
- **Owner and support:** for Zaradigm — Corinna owns everything, but flag what's supported by automation vs. requires her active time.

### 4. Define the first 90 days in detail

The further out the roadmap goes, the less certain it is. Phase 1 should be specific enough to act on Monday morning:
- Week-by-week or sprint-by-sprint breakdown for the first 30 days.
- Milestone checkpoints for days 30, 60, and 90.
- The one thing that, if not done in Week 1, creates downstream delay — name it.

### 5. Output

**Format (scannable in under five minutes):**

- **Goal and horizon:** one line.
- **Phase 1 (0–90 days):** milestones, dependencies, owner (Corinna / automation / tool).
- **Phase 2 (90–180 days):** milestones and what Phase 1 must deliver to unlock this.
- **Phase 3 (180+):** what the steady-state looks like.
- **First 30 days, week by week:** specific enough to act on.
- **The critical path:** the 2–3 dependencies where delay cascades — name them.
- **So what:** handoff to `kpi-architect` (how to track progress) or `value-realization` (how to confirm the strategy is working).

### 6. Guardrails

- Specificity degrades with distance. Phase 1 should be detailed; Phase 3 should be directional. Don't pretend otherwise.
- Never build a roadmap that requires a team that doesn't exist. Design for Corinna plus tools and automation.
- If the honest assessment is "this roadmap requires more bandwidth than currently exists," say so and recommend what to defer or drop — don't paper over a capacity problem with an optimistic timeline.
