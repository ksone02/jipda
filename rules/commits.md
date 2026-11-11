# Commits

One commit holds one thing: one feature, one fix, or one document.

- **Feature:** the code and its tests.
- **Fix:** one change request, one bug, or one review finding group, with its test. A structure change counts as a fix.
- **Document:** one README, guide, spec, or plan, on its own and never mixed with code.
- Progress-log lines and QA result cells are records. They go in the commit they describe.
- Stage files by path. Do not use `git add -A` or `git add .`.
- Before committing, read `git diff --cached --stat`. If it holds two things, split it.
- Commit only when a skill's steps or the user call for it. Never push unasked.
