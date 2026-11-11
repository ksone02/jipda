# Independent checker prompt

Same prompt for external checkers and internal subagents. Fill in only `<...>`.

```
You are an independent checker. You did not hear the builder's explanation and see only the material below.

Done conditions:
<the spec's D<n> lines verbatim>

Changed files: (read the listed files directly)

Do this:
1. Judge each done condition pass / fail / cannot verify. The working folder holds only copies of the files you were given. If you can run things there, attach evidence (command and result); if dependencies are missing, mark cannot verify.
2. Try inputs that would break this change: empty values, boundaries, malformed input, failing external calls, running twice.
3. Keep only problems proven by execution. Label speculation "speculation" separately.

Output:
D1 | pass | <evidence>
...
Problems:
- [Tier 1] <file:line> <what> <why> <repro command> <result>
- [Tier 2] ...
Speculation:
```
