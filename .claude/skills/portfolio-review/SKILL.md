# portfolio-review

Assess the full portfolio of offers, brands, and bets to find what to grow, what to hold, and what to stop — so resources go where they compound, not where they've always gone. Fourth skill in the Choose stage.

Run as: `/portfolio-review [scope — default: all Zaradigm offers]`

---

## Behavior

### 1. Map the portfolio

List every current offer or business unit in scope. For Zaradigm, pull from:
- `wiki/articles/services/` — all active offers with pricing and positioning.
- `wiki/articles/brands/zaradigm.md` and `coachilly-mag.md` — brand-level strategy and status.
- HubSpot (if available): pull closedwon revenue by deal name to see which offers are actually generating revenue, not just existing on a menu.

**Hard rule:** Zaradigm (B2B, active, growing) and Coachilly (B2C, winding down) are two separate portfolios. Never blend their economics or strategic logic in the same review.

### 2. Classify each offer

Score each offer on two dimensions:
- **Growth:** is revenue from this offer expanding, flat, or contracting? Is there realistic runway for growth given market dynamics and Corinna's capacity?
- **Margin:** what is the margin per unit of Corinna's time? High-margin offers generate more revenue per hour delivered. Low-margin offers require volume that doesn't exist for a solo operator.

Classify into quadrants:
- **Grow:** high growth, high margin — concentrate resources here.
- **Harvest:** high margin, low growth — extract value without heavy investment.
- **Fix or exit:** low margin, low growth — either find a structural fix or stop offering it.
- **Watch:** high growth potential but unproven margin or volume — worth a time-limited bet with a defined checkpoint.

### 3. Assess resource allocation vs. classification

Where is Corinna actually spending her time and attention right now? Compare it to the classification:
- Are Grow offers getting the most attention?
- Are Fix/Exit offers quietly consuming delivery bandwidth that should go elsewhere?
- Are Watch bets getting enough room to prove themselves before being killed or grown?

### 4. Output

**Format (scannable in under five minutes):**

- **Portfolio map:** table or grouped list — each offer, its quadrant classification, and one sentence of rationale.
- **Resource misalignment:** where attention is going vs. where classification says it should go — named plainly.
- **Recommended moves:** for each quadrant — what to do more of, what to hold, what to wind down or exit.
- **Highest-leverage shift:** the single reallocation that would have the biggest impact on revenue or margin.
- **So what:** handoff to `strategic-options` (if a major portfolio shift is being weighed) or `initiative-prioritizer` (if execution sequencing is the next question).

### 5. Guardrails

- This skill assesses the portfolio. It does not plan the wind-down of Coachilly — that's a separate decision Corinna has already made. Flag where Coachilly's status affects Zaradigm's portfolio, but don't relitigate the decision.
- Never blend Zaradigm and Coachilly economics. Treat them as two separate P&Ls.
- If the honest answer is "the portfolio is fine but the problem is execution bandwidth, not offer mix," say that plainly. A portfolio problem and a bandwidth problem have different fixes.
- This skill makes recommendations on offers, not on people. No client relationship should be characterized as "low value."
