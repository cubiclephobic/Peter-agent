# customer-segmentation

Define and size attractive customer segments — who buys, why, at what price, and which segments are worth prioritizing. Third skill in the Map stage. Can chain from `market-mapping` or run standalone.

Run as: `/customer-segmentation [business or subject]`

---

## Behavior

### 1. Pull existing segment knowledge

Before building anything new, check what's already documented:
- `wiki/articles/people/avatar-profiles.md` — Zaradigm's 7 ICPs with trigger events, active vs. passive status, and buyer type.
- `wiki/articles/brands/zaradigm.md` — ICP summary, brand positioning.
- HubSpot (if available): pull contact/deal data to check which segments are actually generating revenue vs. just conversations.

Don't reconstruct what's already in the wiki. The task is to sharpen, size, and prioritize — not to re-document what Corinna already knows.

### 2. Segment by need and behavior, not demographics

MBB-grade segmentation splits markets by *why people buy and how they behave* — not just job title or company size. For each potential segment, identify:
- **Core need:** what problem are they specifically trying to solve, and how urgent is it?
- **Trigger event:** what changes in their situation to make them a buyer now?
- **Decision behavior:** who decides, how long does it take, what does it take to close?
- **Revenue economics:** average deal size, repeat purchase likelihood, referral potential.

### 3. Score each segment on attractiveness × fit

- **Attractiveness:** market size, growth, willingness to pay, accessibility.
- **Fit:** how well does Zaradigm (or the client's) current offer, credibility, and capacity actually serve this segment? A segment can be attractive and still be the wrong one to pursue.

### 4. Identify the priority tier

Name the top 1–2 segments: highest attractiveness × highest fit. Name what's been deprioritized and why — so the call is explicit, not accidental.

### 5. Output

**Format (scannable in under five minutes):**

- **Segments mapped:** short list — one line each with core need and trigger event.
- **Attractiveness × fit scores:** brief read on each — not a formal matrix, just honest relative ranking with rationale.
- **Priority tier:** the 1–2 segments worth concentrating on, with one sentence each on why.
- **Deprioritized:** what's being set aside and the reason — makes the trade-off visible.
- **So what:** handoff — what the segmentation implies for offer design, messaging, or `strategic-options`.

### 6. Guardrails

- Do not reduce real people to segment labels in any output that touches HubSpot records or client communications — segmentation is a planning lens, not a relationship frame.
- If the honest answer is "Zaradigm is already over-segmented and trying to serve too many at once," say that. Clarity on who *not* to serve is part of the job.
- This skill defines and prioritizes segments. It does not design the offer or messaging for each — that's `strategic-options` or content work downstream.
