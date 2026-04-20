---
name: skill-advisor
description: Navigate the Claude skills library, recommend relevant skills for a project, and declare them in the project CLAUDE.md
version: "1.0.0"
author: Olivier
---

# Skill Advisor

Navigate the personal Claude skills library, recommend the right skills for a project need, and add them to the project's CLAUDE.md.

## Triggers

Invoke this skill when the user says things like:
- "trouve-moi un skill pour X"
- "quels skills j'ai pour X ?"
- "ajoute le skill X à ce projet"
- "aide-moi à choisir des skills"
- "what skills do I have for X"

## Library location

The skills library is at `~/Documents/Obsidian/Claude/skills/`.

Structure:
```
skills/
├── INDEX.md                    ← start here for quick overview
├── personal/                   ← Olivier's active custom skills
└── collections/                ← reference catalogs (not auto-loaded)
    ├── development/            dev-tools, security, engineering, engineering-team, agents
    ├── business/               collaboration-pm, c-level-advisor, product-team, project-management, business-growth, finance
    ├── marketing-content/      marketing-skill, media-content, writing-research
    ├── data/                   data-analysis, science-research
    ├── productivity/           documents, learning-knowledge, utility-automation
    └── specialized/            bundles, ra-qm-team, standards, health-life-sciences
```

## Process

### Step 1 — Understand the need
If the user hasn't stated a clear goal, ask one question: "Pour quel besoin ou tâche ?"

### Step 2 — Search the library
1. Read `~/Documents/Obsidian/Claude/skills/INDEX.md` for a quick overview
2. Use Grep on `~/Documents/Obsidian/Claude/skills/collections/` to find SKILL.md files matching keywords from the user's need
3. Read the frontmatter (`name`, `description`) of candidate SKILL.md files to confirm relevance

### Step 3 — Present recommendations
For each recommended skill, show:
```
Skill   : <name>
Chemin  : ~/Documents/Obsidian/Claude/skills/collections/<path>/SKILL.md
Rôle    : <description from frontmatter>
Refs    : <list references/ files if folder exists, else "aucune">
```

Ask: "Tu veux que j'ajoute ces skills au CLAUDE.md du projet ?"

### Step 4 — Declare in project CLAUDE.md
With user approval:

1. Find the project CLAUDE.md: look for `CLAUDE.md` in the current working directory, then parent directories up to `~/`.
2. Add `@` references **after existing lines**, one per skill + one per reference file needed:
```
@~/Documents/Obsidian/Claude/skills/collections/<path>/SKILL.md
@~/Documents/Obsidian/Claude/skills/collections/<path>/references/<file>.md
```
3. Confirm: "Ajouté dans `<path>/CLAUDE.md`. Le skill sera actif à la prochaine session Claude Code."

## Rules

- Never add a skill without user confirmation
- Always include relevant `references/` files when the SKILL.md cites them
- Use absolute paths with `~/` prefix (not expanded `/Users/...`) in CLAUDE.md entries
- If no skill matches, say so clearly — don't invent one
