---
name: handoff
description: Pauses work safely, resumes it in a later session, and records user decisions. Use for "wrap up here", "let's continue", "record this decision", "여기까지 정리해 줘", "이어서 하자", "이 결정 기록해 줘". Do not use for ordinary progress reports mid-session.
---

# handoff

Reply and write documents in the user's language.

## Purpose
Keep work and decisions from vanishing when context fills up or sessions change. On resume, reconfirm the previous session's "done".

## Input
- One of `pause`, `resume`, `decide <decision>`.

## Output
- Resume note `docs/progress/HANDOFF.md`. Sections in this order: `## Goal`, `## In progress`, `## Verified`, `## Current state`, `## Next`, `## Key files`, `## Decisions`.
- Decision log `docs/decisions.md`. Line format `- YYYY-MM-DD | decision | reason | alternatives`. If a team decision document exists, write there.

## Steps
**pause**
1. Finish or revert the current small step. Do not start new work; stop delegated work (background commands, running agents).
2. Do nothing hard to reverse (push, PR).
3. Preserve changed files. Default is one `wip:` commit. If the project's `CLAUDE.md` forbids commits, use `git diff > docs/progress/wip.patch` instead.
4. Write the resume note. Under "Verified", list only commands actually run and their results.

**resume**
1. Read the resume note and progress logs (`docs/progress/`).
2. Compare against reality with `git log`, `git status`, `git diff`. If they differ from the note, trust git.
3. Reconfirm what the note calls verified against real output (rerun tests).
4. State where you are continuing and what remains in one line, then continue.

**decide**
1. Record one user decision as one line in the decision log, with the reason and alternatives considered.

## Do not
- Record as a decision anything the user did not decide.
- Write unverified work under "Verified".
- Push or delete branches in order to stop.
