---
name: plan
description: Splits a spec into task units with the riskiest first. Use before implementing a feature that has a spec but no plan, even if the user did not ask ("start implementing", "write a plan", "구현 들어가", "계획 세워 줘"). Do not use for small work that a few file edits will finish.
---

# plan

Reply and write documents in the user's language.

## Purpose
Turn a spec into task units an implementer can follow alone, so missing work is caught at planning time.

## Input
- Spec path. If absent, the most recent file in `docs/specs/`.
- The repository.

## Output
- `docs/plans/<YYYY-MM-DD>-<topic>.md`
  - Header: one-line goal, 2-3 line approach, spec path, global constraints (spec values verbatim)
  - File structure: files to create or change and what each is responsible for
  - Tasks `T<n>`: files, names and formats exchanged, linked done conditions `D<n>`, steps (test → see it fail → implement → see it pass → commit)

## Steps
0. If `shape` was skipped, scan the existing code first (relevant files, callers, conventions, test commands).
1. Decide file structure first. One responsibility per file; files that change together live together.
2. Split tasks. One task is the smallest unit worth testing and reviewing separately. Put risky or unknown work first.
3. For each task, write the names and formats later tasks rely on (function names, arguments, returns, file paths).
4. Self-check and fix on the spot.
   - Does every spec item have a task?
   - Do names and formats match across tasks?
   - Is the plan not many times longer than the spec (copied code is not a plan)?
   - Does it include affected files (docs, translations, related functions, tests)?
5. List 5 inputs or failures real people will hit that the spec does not mention as "review focus", and assign each to a task's tests.
6. One line for the next step: `review` if expert review is needed, otherwise `build`.

## Do not
- Implement. No function bodies (signatures, tests, and values only).
- Write lines that decide nothing: "handle appropriately", "add error handling", "decide later".
- Use names no task defines.
