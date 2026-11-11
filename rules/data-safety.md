# External send rules

If external tools are enabled, send only questions, code, specs, and public documents.

- Files sent must go through `scripts/safe_files.py` (or `scripts/ext.py`, which uses it). Excluded: everything under `data/`, `raw/`, `output(s)/`, `results/`, `.env*`, data extensions (csv, parquet, xlsx, etc.), files over 1MB, binaries, symlinks, files containing key-like strings.
- External tools run in a temp folder holding only copies of the filtered files. The rest of the repository is invisible to them.
- If the project's `CLAUDE.md`, `AGENTS.md`, or memory says "no external AI" or "no upload", do not use external models at all and go internal.
- Do not put data values (rows, raw figures, personal information) in search queries. Ask only about concepts and methods.
- If files were excluded, say so in one line in the result. Do not ask the user each time.
