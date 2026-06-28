# risk-and-mitigation

Identify the risks a strategy or initiative is exposed to and design specific mitigations — before they become problems. Second skill in the Govern stage. Complements `war-gaming` (which covers external/adversarial risks) by focusing on operational and execution risk.

Run as: `/risk-and-mitigation [strategy or initiative]`

---

## Behavior

### 1. Establish scope

What's being de-risked: a strategy, a specific initiative, a new offer launch, a client engagement? Pull from `war-gaming` if run this session — external risks identified there don't need to be re-generated here. Focus this skill on operational, financial, reputational, and execution risks.

### 2. Surface the risk inventory

Cast wide before filtering. Categories to cover:
- **Execution risks:** things that could go wrong in delivery — capacity overrun, quality shortfall, dependency failure.
- **Financial risks:** revenue doesn't materialize at projected volume, cost exceeds estimate, cash timing mismatch.
- **Reputational risks:** a client outcome that reflects badly, content that lands wrong, a public commitment that can't be met.
- **Dependency risks:** a tool, partner, platform, or automation that fails and creates downstream gaps (e.g., LinkedIn sync outage, HubSpot data error, Krisp transcript gap).
- **Concentration risks:** over-reliance on one client, one offer, one channel, or one revenue source.

### 3. Score and filter

For each risk: **likelihood** (High / Medium / Low, given current trajectory) × **impact** (how much damage if it materializes). Focus mitigation effort on High × High and High × Medium — not the full list.

### 4. Design mitigations

For each material risk, name a specific response:
- **Avoid:** change the plan to eliminate the risk entirely.
- **Reduce:** action that lowers likelihood or impact — what specifically?
- **Accept:** acknowledge the risk, define the threshold at which it becomes a problem, and decide in advance what to do when it hits.

Don't build a mitigation for every risk — that's risk theater. Build one for risks that are material and addressable.

### 5. Set early warning indicators

For each material risk: what's the earliest observable signal that this risk is materializing? Name the indicator and the threshold at which Corinna should act.

### 6. Output

**Format (scannable in under five minutes):**

- **Risk inventory:** full list, one line each — just the risk and its likelihood × impact.
- **Material risks (top 3–4):** for each — description, likelihood × impact, mitigation, early warning indicator.
- **Accepted risks:** named explicitly so they're not revisited constantly.
- **So what:** handoff to `kpi-architect` (embed early warning indicators as tracked metrics) or `value-realization` (monitor risk signals as part of ongoing governance).

### 7. Guardrails

- This skill is prospective — it de-risks decisions not yet locked. Don't use it to audit a decision already acted on.
- Automation dependency risks are especially relevant for Zaradigm: LinkedIn sync, transcript pipeline, morning brief, HubSpot automation are all single points of failure. Flag these explicitly if relevant.
- Don't manufacture risks to look thorough. A short list of real, specific risks is more valuable than a long list of generic ones.
