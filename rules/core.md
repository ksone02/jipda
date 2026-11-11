# Core principles

Short principles skills point to. Standing principles are in [always.md](always.md).

## Do only what was asked
- Finish the scope given. You may name the next step in one line but do not start it.

## Bugs start with a reproducer
- Before fixing, build a check that goes red only on this bug (failing test, script, browser action). See the `diagnose` skill.

## Question the premise
- Write the one sentence all failed fixes believed. Pick one observation that would differ if it were false, and make it.

## Explain the number
- Decide what result would change the decision and how big noise is before measuring.
- Say what limits the value (disk, network, the measuring tool itself).
- Rule out one by one that the number measures something else (errors, cache, code not run, a default baseline).

## Confirm with official docs
- Do not write version-dependent facts from memory. Check official docs or source and cite them.

## Check instead of asking
- For forks that running settles (behavior, speed, look), build a small prototype and show the result. Ask the user only about taste and direction.

## Read-only investigation
- For "how does this work" and "why is it built this way", answer from files and lines without changing code.
