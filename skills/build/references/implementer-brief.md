# Implementer brief format

Write one file and pass its path (`.git/jipda/brief-T<n>.md`; inside `.git` so it is never committed).

```
# T<n>: <task name>
Plan: <plan path>  Spec: <spec path>
Global constraints: <copied verbatim from the plan>

## Task
<the plan's full task text>

## Exchanged with other tasks
<names and formats earlier tasks made; names and formats this task must make>

## Rules
- Write the test first and see it fail before implementing.
- Do not split files or add features outside the plan. If it seems needed, report `concerned`.
- When finished, attach the test command and its result.

## Report format
Status: done | concerned | blocked | needs context
Files changed:
Test command and result:
Concerns or blockers (if any):
```
