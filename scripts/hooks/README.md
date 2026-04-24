# Git hooks — public vault

Versioned hooks to prevent personal identifiers from reaching this public repository.

## Per-machine setup (one time per clone)

```bash
cp scripts/hooks/patterns.example scripts/hooks/patterns.local
# edit scripts/hooks/patterns.local with your actual sensitive values
git config core.hooksPath scripts/hooks
```

`patterns.local` is gitignored, so your literal values stay on your machine.

## Hooks present

### `pre-commit`
Runs before each commit. Scans **added** lines in staged files against the patterns from `patterns.local`. Blocks the commit on any match. Skips itself (files under `scripts/hooks/`).

If `patterns.local` is missing, the hook prints a setup reminder and exits 0 — it does not block commits when misconfigured.

## Pattern file format

- One extended regex per line
- Lines starting with `#` or empty lines are ignored
- Patterns are matched against `^+.*PATTERN` in the staged diff (i.e. new lines only)

## Bypassing the hook

```bash
git commit --no-verify
```

Use only when a pattern match is a legitimate false positive and you've verified the diff manually.
