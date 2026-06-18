# run-test-cases

Run a set of test prompts against a named subagent, capture inputs/outputs/traces under `evals/`, and log a daily summary.

## Trigger

`/run-test-cases [agent-name]`

## Steps

1. **Collect test cases.**
   - Create `evals/cases/[agent-name]/` if it doesn't already exist.
   - Ask the user to write a prompt for the `[agent-name]` subagent. Wait for their answer.
   - Ask for a second prompt. Wait for their answer.
   - Save both as a numbered list to `evals/cases/[agent-name]/test-cases.md`:
     ```
     # Test Cases: [agent-name]

     1. [exact prompt text]
     2. [exact prompt text]
     ```
     If the file already exists, append new numbered entries continuing from the last number rather than overwriting.

2. **Resolve the subagent type.**
   - Read the contents of `.claude/agents/` to see what agent definitions actually exist. Do not hardcode any agent name list.
   - If a file named `[agent-name].md` exists there, that is the subagent definition to run from (its frontmatter `name`, `description`, `tools`, and `model`, plus its full body of instructions, define how the subagent must behave).
   - If no matching file exists, stop and tell the user no agent definition was found for that name in `.claude/agents/`, and ask them to confirm the agent name or create the definition first.

3. **Run the test cases.**
   - In a single message, spawn one subagent per test case added in this session, all in parallel, using the Agent tool with `subagent_type` set to `[agent-name]`.
   - Pass each prompt's exact text, unmodified, plus this appended line:
     `Return your full response as plain text. Do not commit files, push to git, or write to Notion unless that action is the explicit subject of the prompt.`
   - The agent's own instruction body (from `.claude/agents/[agent-name].md`) governs its behavior — do not add extra instructions beyond the appended line above.

4. **Save run artifacts.**
   - Create `evals/runs/[agent-name]/[YYYY-MM-DD]/` using today's date (create the dated folder fresh each run; if it already exists for today, add new test-case files alongside existing ones rather than overwriting).
   - For each test case N, write:
     - `test-case-[N]-input.md` — the exact prompt sent
     - `test-case-[N]-output.md` — the full, unedited agent response
     - `test-case-[N]-trace.md` — a numbered list of the key decisions and tool calls the subagent made, written immediately while the run is still in context (don't reconstruct this later from memory)

5. **Update the daily log.**
   - Create `logs/[agent-name]/` if it doesn't exist.
   - Append one entry per test case to `logs/[agent-name]/[YYYY-MM-DD].md` (one file per agent per day; append, never overwrite):
     ```
     ## Run - [HH:MM UTC] (test-case-[N])
     **Input:** [exact prompt sent]
     **Output summary:** [1-2 sentence summary of what the agent returned]
     **Trace:** evals/runs/[agent-name]/[YYYY-MM-DD]/test-case-[N]-trace.md
     ```

6. **Merge to main.**
   - Commit the new/updated skill case file, run artifacts, and log entries.
   - Merge all changes to `main` and push.

7. **Report.**
   - Print exactly: `Ran [N] test cases for [agent-name]. Results saved to evals/runs/[agent-name]/[date]/. Log appended to logs/[agent-name]/[date].md.`

## Tool/Connector Dependencies

- Agent tool (to spawn the subagent under test)
- Read / Glob (to inspect `.claude/agents/`)
- Write / Edit (to create case files, run artifacts, and logs)
- Bash + git (to commit, merge, and push)

## Output Format

- `evals/cases/[agent-name]/test-cases.md` — numbered prompt list
- `evals/runs/[agent-name]/[date]/test-case-[N]-{input,output,trace}.md` — per-run artifacts
- `logs/[agent-name]/[date].md` — daily appended log
- Final terminal message per step 7

## Guardrails

- Never hardcode a fixed list of agent names — always resolve against the live contents of `.claude/agents/`.
- Never run a test case against an agent name with no matching definition in `.claude/agents/`.
- Never let the spawned subagent commit, push, or write to Notion unless that is the explicit subject of the test prompt itself.
- Never overwrite existing `test-cases.md`, run folders, or daily logs — always append/extend.
- Never edit or summarize the subagent's output before saving it — `test-case-[N]-output.md` must be the full, verbatim response.
