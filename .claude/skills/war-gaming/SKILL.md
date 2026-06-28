# war-gaming

Stress-test a strategy by playing out how competitors, markets, and clients might respond before the strategy is locked. The point is to find the weaknesses while there's still time to fix them — not to kill the strategy. First skill in the Govern stage.

Run as: `/war-gaming [strategy or decision]`

---

## Behavior

### 1. Establish the strategy being tested

Pull the chosen path from `strategic-options` if run this session, or have Corinna state the plan in 2–3 sentences. War-gaming without a specific strategy to test produces generic risk lists — not useful.

### 2. Define the adversarial scenarios

Generate 3–4 distinct war-game scenarios — each one a plausible external response or market development that would threaten the strategy. Scenarios should be:
- **Specific:** not "competition increases" but "a direct competitor launches a lower-priced group coaching product targeting the same ICP."
- **Plausible:** grounded in real market dynamics, not low-probability catastrophes.
- **Diverse:** cover different threat types — competitor moves, buyer behavior shifts, market timing failures, platform/channel changes.

For scenarios involving specific competitor behavior: route to the researcher subagent for any recent signals (new offers, pricing changes, hiring) that inform likelihood. Don't invent competitor behavior from training data.

### 3. Play out each scenario

For each scenario:
- **What happens:** describe how the scenario unfolds in the first 30–90 days.
- **Impact on the strategy:** which specific part of the plan breaks, slows, or gets neutralized?
- **Strategic vulnerability exposed:** what assumption does this scenario prove wrong?
- **Pre-emptive response:** what could be done now (before the scenario materializes) to reduce exposure?

### 4. Identify the most dangerous scenario

Which one, if it materialized, would do the most damage and be hardest to recover from? Name it and why.

### 5. Output

**Format (scannable in under five minutes):**

- **Strategy being tested:** one line.
- **Scenarios played (3–4):** for each — what happens, what breaks, what it exposes, pre-emptive response.
- **Most dangerous scenario:** named, with the vulnerability it reveals.
- **Net assessment:** does the strategy hold up under adversarial pressure, or does war-gaming reveal a structural weakness that changes the recommendation?
- **So what:** handoff to `risk-and-mitigation` (build the mitigation plan) or back to `strategic-options` (if a scenario reveals the strategy needs to change).

### 6. Guardrails

- War-gaming challenges the strategy — it doesn't kill it. End on what to do differently, not on whether the strategy is doomed.
- Don't manufacture unlikely catastrophes to look thorough. Three credible scenarios beat six dramatic ones.
- This skill focuses on external threats. Internal execution risks belong in `risk-and-mitigation`.
