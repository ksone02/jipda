---
name: shape
description: Turns a vague idea into a spec with done conditions. Shows a first-draft hypothesis, then applies the planning and strategy tools the situation calls for. Use when what to build is not decided yet ("I want to build something like...", "help me flesh out this idea", "plan this product", "이런 거 만들고 싶은데", "아이디어 구체화해 줘", "기획해 줘"). Do not use for changes that are already clear.
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
0. **Scan an existing repo first.** Relevant files, callers, naming and folder conventions, test and lint commands. Put this in at most 5 lines at the top of the spec.
1. **Show a draft first.** Before asking anything, write your best guess in 3-5 lines: who it is for, when they need it, the problem, the likely answer. Mark it as a guess and ask what is wrong. Reacting to a draft is easier than answering an empty question.
2. **Pick the tools yourself.** Read [toolkit.md](references/toolkit.md), name what is blocking the idea, and pick only tools that could change a decision. Keep each to one table or list. Stop when the next tool would not change anything. Order them: understand the problem, generate options, choose, then stress-test. Say the plan in one line and start; the user can redirect it. If the idea is already clear, skip to step 4.
3. **Run each chosen tool.** Read only that tool's file, fill it from what you know and what the user says, and show one table or list. Ask what is wrong before the next tool. Mark assumptions. Need outside facts or competitors? Name `research --competitive` in one line. A tool that changed no decision is dropped from the spec.
4. **Ask about edge cases.** Empty values, boundaries, no permission, network or external service failure, doing it twice.
5. **Write the spec** in the [one-page form](references/decide.md), then give every done condition a verification method. A condition with no way to verify is not a condition.
6. **Call the size in one line** (the user can change it).
   - One file, obvious fix → fix it, then `check`
   - Small change → `build` → `check`
   - Project → `review` → `plan` → `review` → `build` → `check`

## Do not
- Write code, design, or split work into tasks (that is `plan`).
- Invoke the next skill yourself. Only name it in one line.
- Bundle several questions in one message.
- Ask the user which tool or framework to use. Ask only about the idea, one question at a time.
- Run every tool, or fill a framework just to fill it.
- Record as `[decision]` anything the user did not say.
- Ask the user what running something would answer. Prototype and show the result instead. Ask the user only about taste and direction.
