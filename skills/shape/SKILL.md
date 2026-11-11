---
name: shape
description: Turns a vague idea into a spec with done conditions through questions. Use when what to build is not decided yet ("I want to build something like...", "help me flesh out this idea", "이런 거 만들고 싶은데", "아이디어 구체화해 줘"). Do not use for changes that are already clear.
---

# shape

Reply and write documents in the user's language.

## Purpose
Turn an idea into one spec that says what gets built, what does not, and when it counts as done. This catches misread requirements and missed edge cases before they become code.

## Input
- The user's idea (one line is enough).
- The repository, if one exists.

## Output
- `docs/specs/<YYYY-MM-DD>-<topic>.md`
  - Goal, non-goals, what counts as failure
  - Done conditions, one per line: `D<n>. <condition> — <how verified>`. Example: `D3. The briefing panel scrolls to the end at 1366×768 — browser check`
  - Separate user decisions `[decision]` from agent judgment `[judgment]`
- Last line: a size call and one line naming the next step.

## Steps
0. **Scan an existing repo first.** Relevant files, callers, naming and folder conventions, test and lint commands. Put this in at most 5 lines at the top of the spec. If the project's `CLAUDE.md` lacks test and lint commands, suggest adding them in one line.
1. Ask one question at a time. Start open; offer short options if the user gets stuck.
2. If the idea is vague, widen then narrow with [ideation.md](references/ideation.md). Do not invent candidates alone.
3. After understanding each part, read it back in 2-3 sentences and ask what is wrong. Mark guesses as guesses.
4. Ask about edge cases early: empty values, boundaries, no permission, network or external service failure, doing it twice.
5. Write the spec and give every done condition a verification method. A condition with no way to verify is not a condition.
6. Call the size in one line (the user can change it).
   - One file, obvious fix → fix it, then `check`
   - Small change → `build` → `check`
   - Project → `review` → `plan` → `review` → `build` → `check`

## Do not
- Write code, design, or split work into tasks (that is `plan`).
- Invoke the next skill yourself. Only name it in one line.
- Bundle several questions in one message.
- Record as `[decision]` anything the user did not say.
- Ask the user what running something would answer. Prototype and show the result instead. Ask the user only about taste and direction.
