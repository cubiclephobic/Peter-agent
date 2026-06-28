# strategic-options

Generate and evaluate a structured set of strategic paths before committing to one. The heavier version of `/debate` — use this when the decision has real resource implications and deserves MECE analysis, not just a two-sided pressure test. First skill in the Choose stage.

Run as: `/strategic-options [decision context or subject]`

---

## Behavior

### 1. Establish the decision context

Pull from earlier Diagnose or Map stage outputs in this session if they exist. The "so what" from `growth-barriers` and the competitive framing from `market-mapping` or `competitive-intel` are the natural inputs — don't re-derive what's already established.

If starting fresh: do a quick baseline — what's the goal, what's the constraint, what's already been ruled out and why.

### 2. Generate a MECE option set

Produce 3–4 strategic paths that are **mutually exclusive** (each is a genuinely different choice, not variations on the same move) and **collectively exhaustive** (they cover the realistic strategic space — not a straw man paired with two versions of the preferred option).

Name each option plainly: not "Option A," but a short label that captures its logic (e.g., "Concentrate on one ICP and deepen," "Expand to adjacent market," "Productize and reduce custom delivery").

### 3. Evaluate each option

For each path, assess:
- **Strategic logic:** what theory of winning does this path rely on?
- **Financial return:** revenue and margin potential, rough timeline to impact.
- **Execution requirements:** what capabilities, time, and resources does this actually require from a solo operator?
- **Key risk:** the single most likely way this path fails.
- **Reversibility:** if this doesn't work, what's the cost to redirect?

Where external data is needed (market size, competitor response likelihood, pricing benchmarks): route to the researcher subagent. Don't estimate strategic economics from inference when they're checkable.

### 4. Compare and surface a recommended path

After evaluating all options:
- Which one has the best combination of return, tractability, and reversibility given the actual constraints (solo operator, $5K–$15K/month revenue target, active delivery load)?
- What trade-off is the recommended path making, and is that trade-off acceptable?
- What is the second-best option, and under what conditions would it become the right call?

### 5. Output

**Format (scannable in under five minutes):**

- **Options on the table:** one-line summary of each path.
- **Evaluation grid:** for each option — return, execution load, key risk, reversibility. Keep it tight.
- **Recommended path:** direct. What to do and the primary reason. Not hedged.
- **The trade-off being made:** one sentence — what is explicitly being deprioritized by this choice.
- **What would change this call:** the single condition that, if different, would flip the recommendation.
- **So what:** handoff to `business-case-builder` (if financial modeling needed) or `initiative-prioritizer` (if execution sequencing needed).

### 6. Guardrails

- Always lock a recommendation. "It depends" is not an output — name what it depends on and resolve it.
- Don't pad the option set to look comprehensive. Three real options beat five that include obvious non-starters.
- This is the heavier-weight version of `/debate`. If the decision is fast and low-stakes, use `/debate` instead.
- Never recommend a path that requires sending, publishing, or committing on Corinna's behalf — the recommendation names the move, Corinna makes it.
