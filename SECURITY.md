
# Security policy — public vault hygiene

This repository is intentionally public as a demonstration of a Claude Code setup. The following rules govern what must never reach a commit.

## Forbidden content

The following categories are **never** to be committed to this repository:

- Absolute filesystem paths containing a machine username
- Email addresses of the operator or collaborators
- SSH aliases, resolvable hostnames, public or private IP addresses
- API tokens, passwords, or any form of credential — even expired
- Private key material (SSH, PGP, TLS)
- Contents of `.env` files or equivalents
- Names of private clients or internal projects

## Placeholders to use

When an example requires a value that would otherwise be personal, use a neutral placeholder:

- `~/` for home-relative paths (preferred over any absolute form)
- `<user>` for machine usernames
- `<host>` or `<vps-host>` for SSH aliases and hostnames
- `<ip>` or `<host>` for IP addresses
- `<email>` for email addresses
- `<TOKEN>` for credentials in code samples

## Preventive rules

1. **Think audience**: imagine a recruiter reading this repo. Every line should be usable reference material without revealing who or where.
2. **Audit shell examples carefully**: command blocks are the primary leak vector. Re-read every command line before commit.
3. **Avoid triple correlation**: three weak signals in one file (username hint + handle + hostname fragment) compound into identification. Keep them apart.
4. **When in doubt, abstain**: "I am not sure this is safe to publish" beats committing by reflex.

## Automated safeguards

### Pre-commit hook
A versioned hook at `scripts/hooks/pre-commit` scans staged additions and blocks the commit if any configured pattern matches.

The hook does **not** contain the operator's literal patterns. It reads them from `scripts/hooks/patterns.local`, which is gitignored and lives only on each clone. See `scripts/hooks/README.md` for per-machine setup.

### Gitignore
`.gitignore` excludes files that intrinsically contain personal state:
- macOS Finder metadata
- Obsidian workspace files
- Any symlink whose target would leak a path
- The hook's local patterns file

## Recovery if a leak reaches the remote

1. Stop further commits on the affected branch.
2. Correct the current state with a new commit.
3. Rewrite history with `git filter-repo --replace-text <file> --force` using a local list of values to scrub.
4. Force-push to the remote. Any clone made before this step keeps the leaked content.
5. **Rotate any credential that was exposed**. History rewriting hides the value from the public surface but does not invalidate it — bots may already have harvested it.

## Scope

These rules apply to this repository only. They do not govern private vaults or machine-local configuration, which follow their own conventions.
