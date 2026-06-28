# narrative-builder

Turn analysis into a structured story that earns the audience's agreement before they've read the last page. Uses the Pyramid Principle — answer first, then structure the support top-down. Second skill in the Communicate stage.

Run as: `/narrative-builder [analysis or recommendation to communicate]`

---

## Behavior

### 1. Establish the audience and the ask

Who is this narrative for, and what do you need them to think, feel, or do after hearing it? The answer shapes everything:
- An executive sponsor needs a clear recommendation and confidence it's right.
- A skeptical committee needs the evidence before the recommendation lands.
- A client needs to understand why this matters to them before they'll care about the recommendation.

Pull from `stakeholder-alignment` if run this session — the audience profile and alignment gap already identified there are the inputs, not a fresh derivation.

### 2. Structure the narrative using the Pyramid Principle

**Answer first — always.** Lead with the conclusion. The audience should know what you're recommending in the first 30 seconds — before the evidence, before the analysis.

Structure:
- **Governing thought:** one sentence — the recommendation or key message.
- **Key arguments (3 max):** the three strongest reasons the governing thought is true. Each argument must independently support the governing thought, not set up the next argument.
- **Support under each argument:** data, evidence, examples — as much as needed, but only what actually supports the argument above it. Nothing that's interesting but doesn't support the case.

**What not to do:**
- Don't build to the conclusion (suspense structure). Executives read the first slide and decide; they don't wait for the reveal.
- Don't include analysis that doesn't support an argument. "Context" that doesn't change the recommendation is filler.
- Don't use more than three top-level arguments. If there are more, find the common thread and make them sub-points.

### 3. Anticipate the hostile questions

For each key argument: what's the sharpest objection a skeptic would raise? Name it and address it inside the narrative — don't wait to be asked. This is what separates a convincing narrative from one that gets torn apart in Q&A.

### 4. Hand off to draft-writer

Once the structure is locked — governing thought, 3 arguments, support for each, hostile Q&A addressed — pass to `/draft-writer` for the actual prose, then `/personal-tone` for voice, then `/qa-check` for final review. The narrative-builder defines the architecture; the downstream skills produce the language.

### 5. Output

**Format:**

- **Audience and ask:** one line each.
- **Governing thought:** the answer, in one sentence.
- **Argument 1 / 2 / 3:** each with 2–3 supporting points and the hostile question addressed.
- **Structure ready for draft-writer:** clear enough that the next skill can produce prose without re-deriving the logic.

### 6. Guardrails

- Answer first. Every time. Even when the answer is uncomfortable.
- Never include analysis in the narrative that doesn't support an argument. Interesting ≠ relevant.
- Apply Zaradigm voice rules to any structure that will become client-facing content: no em-dashes, no banned words, no rhetorical questions as hooks. (Voice application happens in `personal-tone`, but flag conflicts at the structure stage.)
- This skill produces a content structure, not finished prose. Don't deliver a draft — deliver architecture clear enough that `/draft-writer` can execute it.
