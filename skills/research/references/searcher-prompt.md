# Searcher prompt (shared by external searchers and internal subagents)

```
Research only the one angle below.
Angle: <angle>
Background decision: <decision>

- Prefer primary sources (papers, official docs, repositories). Use summary blogs only as leads to the originals.
- If a name returns nothing, change the wording (maker, language, related project, date) and check official docs, package registries, GitHub, release notes, and recent news before reporting it as not found.
- Attach a source link to every claim. Do not cite links you did not open.
- Result format:
  ## Branches
  - <branch name>: <one line> — [source](url)
  ## Still missing
  - <what you could not find>
- Do not exceed 20 lines.
```
