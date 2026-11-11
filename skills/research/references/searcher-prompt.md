# Searcher prompt (shared by external searchers and internal subagents)

```
Research only the one angle below.
Angle: <angle>
Background decision: <decision>

- Prefer primary sources (papers, official docs, repositories). Use summary blogs only as leads to the originals.
- Attach a source link to every claim. Do not cite links you did not open.
- Result format:
  ## Branches
  - <branch name>: <one line> — [source](url)
  ## Still missing
  - <what you could not find>
- Do not exceed 20 lines.
```
