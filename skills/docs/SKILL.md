---
name: docs
description: Reads the code to confirm facts, then writes repository docs or fixes where docs drift from code. Use for "document this", "write a README", "update the docs", "문서화해 줘", "README 써 줘", "문서 최신화해 줘". Do not use when the user names claude.ai docs or Notion.
---

# docs

Reply and write documents in the user's language, or match the repository's existing documentation language.

## Purpose
Leave docs in the repo that readers can use right away and that do not drift from code. Runs in two modes: write and audit (`--audit`).

## Input
- Write: a feature, module, or project. If absent, ask once what to document.
- Audit: `--audit` and a base branch. If absent, compare with the default branch.

## Output
- Write: edits to existing docs or Markdown files in `docs/`. Follow existing folders and formats.
- Audit: fixed list, question list, missing-docs list.

## Steps

### Write
1. **Read everything first.** README, CLAUDE.md, config files, the full implementation, tests, and code using the target. Do not write from signatures alone.
2. **Pick doc types.** Write only what the target needs. Confirm the list first if there are more than 5.
   - Reference: every command, option, default, and constraint. Always taken from code. Write this first, since it sets the vocabulary.
   - How-to: steps, prerequisites, verification, and common failures for one job.
   - Explanation: why it is built this way. Start from the problem and state what was given up. If the reason cannot be found, leave it blank rather than inventing one.
   - Tutorial: one example a newcomer can follow to something working.
3. **Write, then edit by the rules.** Follow [writing-ko.md](../../rules/writing-ko.md) or [writing-en.md](../../rules/writing-en.md).
4. **Run it before finishing.** Actually run the commands and examples and match the results. Mark anything you cannot run with `not run` in place. Check that paths and links exist.

### Audit (`--audit`)
1. **Collect what changed.** From `git diff <base>...HEAD`, extract new, renamed, or removed commands, options, env vars, APIs, and skills.
2. **Compare with docs.** Table it.

   ```
   Item | Code location (file:line) | Doc location | Status (ok/wrong/missing)
   ```
3. **Fix factual errors right away.** Only things code settles: paths, commands, numbers, option names, broken links.
4. **Number the rest and ask together.** Explanation direction, content removal, large rewrites. Without an answer, do not change them.
5. **Report missing docs as a list only.** Do not write them. Name write mode in one line if needed.

## Do not
- Commit, push, or bump versions.
- Delete or rewrite existing CHANGELOG entries.
- Do decision records (`handoff decide`) or spec and plan review (`review`).
- Present behavior or reasons you could not confirm in code as fact.
- Leave unrun examples looking run.
- Copy keys, personal information, or raw data values into docs.
