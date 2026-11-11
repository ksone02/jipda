---
name: guard
description: Turns on or off a hook that asks for confirmation before dangerous commands (pushing to production branches, rm -rf, reading secrets). Use only for "block dangerous commands", "turn guard off", "guard status", "위험한 명령 막아 줘", "guard 꺼 줘", "guard 상태 알려 줘". Do not use for other permission or settings topics.
---

# guard

Reply in the user's language.

## Purpose
Prevent accidental changes to production servers, bots handling real money, and secrets. Off by default.

## Input
- One of `on`, `off`, `status`.

## Output
- State file `${JIPDA_GUARD_FILE:-$HOME/.claude/jipda-guard.on}` (present means on). The hook reads the same variable.
- Report: current state and the commands it asks about.

## Steps
1. `on`: `touch "${JIPDA_GUARD_FILE:-$HOME/.claude/jipda-guard.on}"`
2. `off`: `rm -f "${JIPDA_GUARD_FILE:-$HOME/.claude/jipda-guard.on}"`
3. `status`: check whether the file exists; if it does, guard is on.
4. In every case, read the `RISKY` list in [guard.py](../../hooks/guard.py) and show one line per item.
5. When on, Claude Code asks before those commands run. It asks; it does not block.

## Do not
- Fully block commands or change other hook settings.
- Turn it off unasked.
