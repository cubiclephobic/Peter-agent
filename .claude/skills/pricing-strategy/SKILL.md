# pricing-strategy

Set price points and packaging architecture grounded in buyer value and competitive position — not cost-plus guesswork. Second skill in the Choose stage.

Run as: `/pricing-strategy [offer or subject]`

---

## Behavior

### 1. Establish the offer and context

Name what's being priced: a specific service, a new offer, or a full portfolio pricing review. Check the wiki first:
- `wiki/articles/services/` — current pricing across all Zaradigm and Coachilly offers.
- `wiki/articles/brands/zaradigm.md` — ICP and positioning context.
- HubSpot (if available): pull close rates and average deal sizes by offer to see where pricing is working and where it isn't.

If a `customer-segmentation` or `competitive-intel` output exists in this session, use it — buyer WTP and competitive anchors are inputs, not parallel work.

### 2. Establish value-based anchoring

MBB pricing starts from buyer value, not cost:
- **Economic value:** what is the quantified or estimated value this offer creates for the buyer? (e.g., a workshop that helps a team communicate better → what's that worth in hours recovered, decisions made faster, reduced friction?)
- **Perceived value signals:** what does the buyer use to judge whether the price is fair? Credentials, case studies, comparison to alternatives, framing of ROI.
- **Willingness to pay:** where is the price point where serious buyers stop and curious ones do? If close-rate data from HubSpot is available, use it — don't estimate when the data exists.

### 3. Map the competitive anchor

What are the realistic alternatives the buyer compares this offer to — other coaches, consultants, workshops, doing nothing, hiring internally? What are those alternatives priced at?

For specific competitor pricing: route to the researcher subagent. Don't recall competitor prices from training data.

### 4. Design the architecture

Recommend price points, packaging, and structure:
- **Anchor price:** the high-end option that makes the intended choice feel reasonable.
- **Primary offer:** the price point optimized for close rate × margin.
- **Entry offer:** if applicable — the lowest-friction way to start a relationship, priced to get a yes, not to generate margin.
- **Packaging logic:** what's bundled vs. unbundled, and why. (Bundling raises perceived value; unbundling can increase total revenue per client.)

### 5. Output

**Format (scannable in under five minutes):**

- **Current pricing assessment:** one line — is it working? What does the data say?
- **Value-based anchor:** what the offer is actually worth to the buyer, in plain terms.
- **Competitive frame:** what the buyer compares this to and at what price.
- **Recommended architecture:** anchor / primary / entry — price, what's included, the logic.
- **Expected impact:** close-rate and revenue implications of the change, directional.
- **So what:** handoff — to `business-case-builder` if financial modeling is needed, or to `strategic-options` if pricing is the crux of a larger strategic decision.

### 6. Guardrails

- This skill designs price architecture. It does not write copy or pricing pages — that's content work.
- Never recommend a price change without naming the trade-off (e.g., a higher price that increases margin may reduce volume — be explicit about that).
- Zaradigm and Coachilly pricing must be treated separately. Never blend the two brands' economics in the same analysis.
- If Corinna has already locked a price for an active deal, this skill is prospective only — don't second-guess committed pricing.
