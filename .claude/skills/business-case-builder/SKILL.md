# business-case-builder

Build a financial case for a decision, investment, or new offer — with unit economics, a go/no-go threshold, and sensitivity scenarios. Third skill in the Choose stage. The point isn't a perfect model; it's knowing what has to be true for this to work, and whether those conditions are realistic.

Run as: `/business-case-builder [decision or initiative]`

---

## Behavior

### 1. Establish the decision being modeled

Name what's being evaluated: a new offer, a pricing change, a market expansion, a partnership investment, a time commitment (workshops, programs, retainers). Pull inputs from earlier skills if they exist:
- `assumption-audit` — use its exposed assumptions as the sensitivity variables.
- `pricing-strategy` — use its architecture as the revenue model input.
- `strategic-options` — the recommended path is often what's being modeled here.

Check `wiki/articles/sops/finance-invoice-expense.md` for any relevant cost benchmarks.

### 2. Build the revenue model

Work from unit economics, not top-down projections:
- **Unit:** what is one sale? (one client, one seat, one retainer month, one workshop)
- **Price per unit:** from `pricing-strategy` if run, or from wiki/HubSpot data.
- **Volume assumption:** how many units is it realistic to sell in the time window, given current pipeline, bandwidth, and conversion rates? Don't assume a step-change in conversion without naming what drives it.
- **Revenue:** price × volume.

### 3. Layer in costs and investment

- **Delivery cost:** Corinna's time (at what opportunity cost?), any hard costs (licensing, tools, contractors).
- **Acquisition cost:** what does it take to generate one sale — outreach time, content investment, event costs?
- **One-time investment:** setup, design, tooling, launch effort.
- **Margin:** revenue minus delivery and acquisition cost per unit.

### 4. Identify the go/no-go threshold

What conditions must hold for this to be worth doing?
- **Breakeven:** minimum volume at which the math works.
- **Payback period:** how long until the initial investment is recovered?
- **Floor case:** if everything goes 30% worse than planned, does this still make sense?

### 5. Run the sensitivities

Vary the two or three assumptions that matter most (usually: close rate, price point, and volume) and show what the outcome is under pessimistic / base / optimistic scenarios. Don't model every variable — only the ones where being wrong would flip the decision.

### 6. Output

**Format (scannable in under five minutes):**

- **What's being modeled:** one line.
- **Unit economics:** price / cost / margin per unit.
- **Base case:** volume × margin = total impact in the time window.
- **Sensitivities:** 2–3 scenarios — pessimistic / base / optimistic — with the key variable named for each.
- **Go/no-go threshold:** the minimum that makes this worth doing.
- **Verdict:** does the base case clear the threshold? Is the downside acceptable?
- **So what:** handoff to `initiative-prioritizer` (how to sequence execution) or `strategic-options` (if the case changes the strategic choice).

### 7. Guardrails

- This is a decision tool, not a pitch deck. Precision is less important than surfacing the right variables.
- Never model more decimal places of precision than the underlying assumptions support.
- If a key input isn't knowable yet (e.g., close rate on a new offer), say so explicitly and show how sensitive the outcome is to that variable — don't paper over it with a guess.
- Do not build a case that's designed to justify a decision already made. If the numbers don't work, say so plainly.
