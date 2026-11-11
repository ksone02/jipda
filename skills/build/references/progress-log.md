# Progress log format

`docs/progress/<YYYY-MM-DD>-<topic>.md`

```
# Progress log — plan: <plan path>
T1 | in progress | a1b2c3d | -
T1 | review round 1 | a1b2c3d | Tier 1: 2, Tier 2: 1
T1: complete (a1b2c3d..e4f5a6b, review clean)
T2: complete (e4f5a6b..c7d8e9f, 1 parked)
Parked: T2 <finding> — <reason>
Decision: T3 <what differed from the plan> — <why> — <cost if wrong>
```

- Log each task in the same commit as the task (do not defer it).
- `Decision:` lines are every choice that differs from the plan. Show them together at the end.
