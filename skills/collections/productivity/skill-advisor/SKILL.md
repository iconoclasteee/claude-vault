---
name: skill-advisor
description: Search skills across all sources (local library + skilluse repos), read their content, install them in a project, and optionally copy them to the personal library
version: "2.0.0"
author: Olivier
---

# Skill Advisor

Find, read, install, and save Claude skills from all available sources.

## Triggers

- "trouve-moi un skill pour X"
- "quels skills pour X ?"
- "cherche un skill qui fait X"
- "ajoute le skill X à ce projet"
- "aide-moi à choisir des skills"

---

## Process

### Step 1 — Understand the need
If the goal isn't clear, ask: "Pour quel besoin ou tâche ?"

---

### Step 2 — Search all sources in parallel

Search simultaneously across all three sources:

**Source A — Local library** (`~/Documents/Obsidian/Claude/skills/`)
- Read `INDEX.md` for quick overview
- Grep `collections/` for SKILL.md files matching keywords

**Source B — skilluse: vault perso** (`iconoclasteee/claude-vault`)
```bash
skilluse repo use iconoclasteee/claude-vault
skilluse search <keyword>
```

**Source C — skilluse: Anthropic official** (`anthropics/skills`)
```bash
skilluse repo use anthropics/skills
skilluse search <keyword>
```

---

### Step 3 — Present results grouped by source

```
── Source : vault perso (iconoclasteee/claude-vault) ──
  [1] skill-advisor      — Navigate la librairie de skills
  [2] business-case      — Framework de business case

── Source : Anthropic officiel ──
  [3] webapp-testing     — Tests d'applications web
  [4] pdf                — Traitement de fichiers PDF

── Source : librairie locale ──
  [5] owasp              — Security audit OWASP
      ~/Documents/Obsidian/Claude/skills/collections/development/security/owasp/SKILL.md
```

Ask: "Tu veux lire le contenu d'un skill avant de choisir ? (indique le numéro)"

---

### Step 4 — Read skill on request

If the user wants to read a skill before deciding:

- **From skilluse source:** run `skilluse info <name>` then read the full SKILL.md from its local install path or GitHub raw URL
- **From local library:** read the SKILL.md file directly

Display the full content so the user can evaluate it.

---

### Step 5 — Install in current project

Once the user has chosen, ask:
> "Je l'installe dans ce projet (`--local`) ou globalement (tous les projets) ?"

**Option A — via skilluse** (for skills from skilluse sources):
```bash
skilluse install <name> --local    # project only: ./.claude/skills/
skilluse install <name>            # global: ~/.claude/skills/
```

**Option B — via CLAUDE.md reference** (for local library skills):
Add to project `CLAUDE.md`:
```
@~/Documents/Obsidian/Claude/skills/collections/<path>/SKILL.md
@~/Documents/Obsidian/Claude/skills/collections/<path>/references/<file>.md
```

Always include `references/` files that the SKILL.md cites (check for `references/` folder).

Confirm: "Skill actif. Il sera chargé à la prochaine session Claude Code dans ce projet."

---

### Step 6 — Copy to personal library (automatic)

After every install, always copy the skill to the personal library without asking.

1. Create folder: `~/Documents/Obsidian/Claude/skills/personal/<skill-name>/`
2. Copy SKILL.md (and references/ if any) into it
3. Commit and push:
```bash
cd ~/Documents/Obsidian/Claude
git add skills/personal/<skill-name>/
git commit -m "feat: add <skill-name> to personal skills"
git push
```
4. Confirm: "Copié dans `skills/personal/<skill-name>/` et pushé sur GitHub."

---

## Rules

- Never install or copy a skill without user confirmation
- Always show content when asked — don't summarize, show the full SKILL.md
- Use `~/` paths (not `/Users/<user>/`) in CLAUDE.md entries
- If a skill has a `references/` folder, list those files and ask which to include
- If no match found in any source, say so — don't invent
- After copying to personal/, the skill becomes available via `skilluse search` automatically (public repo)
