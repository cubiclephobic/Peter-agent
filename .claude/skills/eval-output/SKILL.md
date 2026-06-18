# eval-output

Score an agent's most recent test-case outputs against its rubric, log results to `evals/evaluations.md`, queue any fixes needed to reliably hit Score 5, and link the diagram to the results.

## Trigger

`Run eval-output for [agent-name]`

## Steps

1. **Load the rubric.**
   - Read `evals/rubrics/[agent-name].md`.
   - Extract the dimension names from the first column of the rubric table, skipping the header row and the `---` separator row.

2. **Load the most recent outputs.**
   - List the date-named folders (`YYYY-MM-DD`) under `evals/runs/[agent-name]/` and pick the most recent one.
   - Read every file matching `test-case-[N]-output.md` in that folder.

3. **Score each output.**
   - Build the judge prompt as two parts, in this fixed order, so the first part is byte-for-byte identical across every test case and every run for this agent (enables prompt caching):
     - **Part A — Judge Instructions (stable, cacheable).** Assemble once per skill run, verbatim:
       1. Role line: "You are scoring a single agent output against a fixed rubric. Score strictly from the rubric text below — do not invent criteria."
       2. The full rubric table from `evals/rubrics/[agent-name].md`, pasted in as-is (all dimensions, all Score 1/3/5 descriptions, in file order).
       3. Fixed scoring instructions (verbatim every time):
          "For each dimension above, output a score from 1-5 and exactly one sentence of explanation grounded in evidence from the output text below.
          Overall status: PASS if every dimension scores 3 or higher, otherwise FAIL.
          Watch flag: mark any dimension scoring below 5 as a watch item, even when overall status is PASS — a high average must never hide one weak dimension.
          Return your scoring in this exact format: one line per dimension as `Dimension: score - explanation`, then `Overall: status`, then `Watch: [dimension names below 5, or None]`."
     - **Part B — Output to score (variable).** Append after a fixed delimiter line (`---OUTPUT TO SCORE---`): the test case number and the full content of that one `test-case-[N]-output.md` file. Nothing else goes in this part.
   - Do not paraphrase, reorder, or reformat Part A between test cases or between runs — reuse the same assembled string and only swap out Part B. If the rubric file changes, Part A changes for all subsequent runs, but must still stay fixed within a single run.
   - Parse the judge's response into per-dimension scores/explanations, Overall status, and Watch list per the format specified in Part A.

4. **Ensure `evals/evaluations.md` exists.**
   - If it doesn't exist, create it with:
     - A header comment explaining the file's purpose (running log of rubric-scored agent outputs, plus a queue of fixes needed to close score gaps).
     - A `## Review Queue` section at the bottom with this table header:
       `| Date | Agent | Test Case | Dimension | Score | Fix Type | Risk | Suggested Change | My Change | Action | Batch |`

5. **Ensure the agent's section exists.**
   - If no `## [agent-name]` section exists in `evals/evaluations.md`, append one (above the `## Review Queue` section) with a table header:
     `| Date | Test Case | [dimension 1] | [dimension 2] | ... | Overall | Status | Batch |`
     using the exact dimension names extracted in step 1, in rubric order.

6. **Determine the batch value.**
   - Scan the `## Review Queue` table for the most recent row (by Date, then table order) where `Action` is `Applied`.
   - If found, use that row's `Batch` value for all new scoring rows in this run.
   - If none found, leave `Batch` blank for all new scoring rows.

7. **Append scoring rows.**
   - For each scored output, append one row to the agent's `## [agent-name]` table: today's date, the test case number, each dimension's score in rubric order, the Overall (average of all dimension scores, rounded to one decimal), Status (`PASS`/`FAIL`), and the Batch value from step 6.

8. **Queue fixes for sub-5 dimensions.**
   - Collect every dimension that scored below 5 across this run's outputs.
   - Deduplicate by (agent, dimension) — if the same dimension scored below 5 on multiple test cases, keep only the most recent test case's instance.
   - Skip any (agent, dimension) pair that already has a row in the Review Queue with a non-empty `Action`.
   - For each remaining dimension:
     - Read that dimension's Score 5 description from the rubric.
     - Identify the specific file and section in the codebase that would need to change for the agent to reliably hit Score 5 on that dimension (e.g., a specific instruction block in `.claude/agents/[agent-name].md`, a step in a related skill, the rubric wording itself, or a tool/MCP config).
     - Assign **Fix Type**: `Skill`, `CLAUDE.md`, `Rubric`, `Tool Config`, or `Prompt`.
     - Assign **Risk**: `Low` if the fix is a skill addition or prompt-only change; `High` if it touches `CLAUDE.md`, the rubric, or tool/MCP config.
     - Append a row to `## Review Queue`: Date (today), Agent, Test Case, Dimension, Score, Fix Type, Risk, Suggested Change (the specific file/section + what to change), `My Change` (blank), Action (blank if High risk, `Approved` if Low risk), Batch (blank).
   - Sort the full Review Queue table so High-risk rows appear before Low-risk rows (stable sort otherwise — don't reorder existing rows relative to each other beyond the risk grouping).

9. **Link the diagram.**
   - Open `diagrams/agent-system.md` and find the Agents table row where the `Agent` column matches `[agent-name]`.
   - If the `Evaluations` cell is empty, replace it with `[evals](../evals/evaluations.md#[agent-name])`.
   - If it already contains a link, leave it unchanged.

10. **Commit and push.**
    - Commit the updated `evals/evaluations.md` and `diagrams/agent-system.md`.
    - Push to the current branch (do not merge to main unless explicitly asked).

## Tool/Connector Dependencies

- Read / Glob (rubric, run folders, output files, evaluations.md, diagram)
- Write / Edit (evaluations.md, diagram)
- Bash + git (commit, push)
- LLM judging happens in-context — no external judge API required

## Output Format

- `evals/evaluations.md` — updated with new rows in `## [agent-name]` and any new rows in `## Review Queue`
- `diagrams/agent-system.md` — Evaluations cell populated for `[agent-name]` if it was empty
- A short inline summary: scores per dimension per test case, overall status, and how many Review Queue rows were added

## Guardrails

- Writes only to the agent's own `## [agent-name]` section in `evals/evaluations.md` — never edits another agent's section or reorders its rows.
- Never overwrites existing scoring rows — always appends.
- Never sets `Action` to `Approved` on a High-risk row, and never leaves a Low-risk row's `Action` blank.
- Never skips the watch flag — a dimension below 5 must surface even if the overall status is `PASS`.
- Never modifies a Review Queue row that already has a non-empty `Action` for the same (Agent + Dimension).
- Never merges to `main` as part of this skill — only commits and pushes to the current branch.
