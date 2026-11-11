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
- `features.md` in the folder named after the spec, if it exists. It overrides the spec on behavior.
- The repository.

## Output
- `docs/plans/<YYYY-MM-DD>-<topic>.md`
  - Header: one-line goal, 2-3 line approach, spec path, global constraints (spec values verbatim)
  - File structure: files to create or change and what each is responsible for
  - Stages: for each, what the user can see when it ends and the command to run it
  - Tasks `T<n>` under each stage: files, names and formats exchanged, linked done conditions `D<n>` and rules `R<n>`, screen IDs `S<n>` for UI tasks, steps (test → see it fail → implement → see it pass → commit)

## Steps
0. If `features.md` has an open question blocking a P0 or P1 feature, stop and list those questions. If the spec marks a no-product demand test with no result, ask once whether to run it or skip it, and record the answer in the spec. If `shape` was skipped, scan the existing code first (relevant files, callers, conventions, test commands).
1. Decide file structure first. One responsibility per file; files that change together live together.
2. Split tasks and group them into stages: proof of the riskiest technical assumptions, then the smallest P0 version a person can run end to end, then P1, then P2. Small work is one stage. One task is the smallest unit worth testing and reviewing separately. In a new project, T1 creates the repository, fixes the stack, and writes the test, data-preparation, and screen-capture commands into `features.md`. A web app uses `measure.py` for screen capture. Any other command must run once here before it is written down.
3. For each task, write the names and formats later tasks rely on (function names, arguments, returns, file paths).
4. Self-check and fix on the spot.
   - Does every spec item, and every rule of a non-excluded feature, have a task?
   - Do names and formats match across tasks?
   - Is the plan not many times longer than the spec (copied code is not a plan)?
   - Does it include affected files (docs, translations, related functions, tests)?
5. List 5 inputs or failures real people will hit that the spec does not mention as "review focus", and assign each to a task's tests.
6. One line for the next step: `build`. Name `review` first only when a decision is hard to reverse, such as payments, personal data, or data deletion.

## Do not
- Implement. No function bodies (signatures, tests, and values only).
- Write lines that decide nothing: "handle appropriately", "add error handling", "decide later".
- Use names no task defines.
