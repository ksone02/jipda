# Debugging techniques

## Root-cause tracing
- Do not stop at the line that errored. Trace back through callers to where the bad value was first created.
- Print the value at each step to confirm "correct up to here" and narrow the range.
- Fix where it first goes wrong. A guard below it is not a root-cause fix.

## Defense in depth
- After fixing the cause, add one check at each boundary the same bad value could re-enter (input handlers, external call results, just before saving).
- Give each check a one-line comment saying what it stops.

## Wait on conditions, not time
- `sleep` is a common cause of flaky tests. Wait on a condition ("until the element is visible", "until the file exists") with an upper time limit.

## Finding the test that pollutes others
- If a test passes alone and fails with others, bisect the tests running before it to find the culprit.
- The culprit is usually global state, leftover files, or unfixed time and seeds.
