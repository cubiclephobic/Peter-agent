# initiative-prioritizer

Take a list of potential initiatives and sequence them for maximum impact given real constraints. The job is to prevent the solo-operator trap of doing everything at 60% instead of the right things at 100%. Second skill in the Execute stage.

Run as: `/initiative-prioritizer [initiative list or context]`

---

## Behavior

### 1. Establish the initiative list

Pull from earlier skills if they exist:
- `operating-model-design` — the operating gaps produce candidate initiatives.
- `growth-barriers` — the prioritized barriers are the source of the initiative list.
- `strategic-options` — the chosen path implies a set of moves.

If no list exists from prior skills, ask Corinna for the list of things she's considering doing. Don't generate a list of initiatives from scratch — prioritization requires a real list, not a hypothetical one.

### 2. Score each initiative

Rate every item on three dimensions:
- **Impact:** how much does this move the needle on the primary goal (revenue, pipeline, capacity, or whatever the strategy is targeting)? High / Medium / Low — with one-line rationale.
- **Effort:** how much of Corinna's time, attention, and energy does this require to execute? Include setup cost, not just steady-state. High / Medium / Low.
- **Dependency:** does anything else need to happen first for this initiative to work? Name the dependency explicitly — dependencies create sequencing constraints that override impact scoring.

### 3. Sequence, don't just rank

Ranking by impact ÷ effort is the starting point, but sequencing is the real output:
- **Now (0–30 days):** high-impact, low-effort, no dependencies — do these first.
- **Next (30–90 days):** high-impact, higher-effort, or blocked by a "Now" dependency.
- **Later (90+ days):** important but not urgent, or dependent on things not yet in place.
- **Drop / park:** low-impact items that are consuming attention. Name them explicitly — making the cut visible is part of the job.

### 4. Flag the bandwidth ceiling

For a solo operator, the real constraint is always time. Check the current calendar load if available (Google Calendar MCP). If the "Now" bucket is already oversubscribed against Corinna's actual available hours, say so — don't sequence more than the bandwidth ceiling allows.

### 5. Output

**Format (scannable in under five minutes):**

- **Full initiative list scored:** impact / effort / dependency for each.
- **Sequenced buckets:** Now / Next / Later / Drop — with rationale for anything non-obvious.
- **Bandwidth check:** does the Now bucket fit within available hours? If not, what gets pushed to Next?
- **The one thing:** if only one initiative could be started this week, which one, and why.
- **So what:** handoff to `transformation-roadmap` (build the full phased plan) or direct to execution.

### 6. Guardrails

- Don't generate initiatives to fill the list. Prioritize what exists — don't add scope.
- "Do everything" is not a prioritization. If the list is too long for the bandwidth available, make explicit cuts.
- Flag anything in the "Drop" bucket that Corinna has emotional investment in — naming it is more useful than silently excluding it.
