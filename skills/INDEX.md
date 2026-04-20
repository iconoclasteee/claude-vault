---
title: "Index des skills Claude"
date: 2026-04-20
tags:
  - type/reference
  - domaine/ia
status: active
source: ""
---

# Index des skills Claude

## Personal — Skills actifs

| Skill | Fichier | Description |
|-------|---------|-------------|
| **Skill Advisor** ⭐ | [[skills/personal/skill-advisor/SKILL]] | Trouve et déclare les skills adaptés à un projet — chargé globalement |
| Recherche vault | [[skills/personal/obsidian/cherche]] | Cherche dans le vault Brain via Grep |
| Nouvelle note | [[skills/personal/obsidian/nouvelle-note]] | Crée une note Brain avec frontmatter standard |
| Résumé session | [[skills/personal/obsidian/resume-session]] | Génère un résumé structuré de session |
| Content extraction | [[skills/personal/content-extraction/SKILL]] | Transforme du contenu long-form en formats multi-plateformes |
| Business case | [[skills/personal/business-case/SKILL]] | Framework de business case avec rigueur financière |
| PPTX | [[skills/personal/pptx/SKILL]] | Génère des présentations PowerPoint via pptxgenjs |

## Obsidian Skills — dans Brain vault

> Ces skills sont chargés automatiquement quand Claude Code est lancé depuis `~/Documents/Obsidian/Brain/`

| Skill | Rôle |
|-------|------|
| obsidian-markdown | Syntaxe Obsidian exacte (WikiLinks, callouts, frontmatter) |
| obsidian-cli | Contrôle de l'app Obsidian ouverte |
| obsidian-bases | Vues dynamiques .base |
| json-canvas | Fichiers .canvas valides |
| defuddle | Extraction d'articles web en Markdown |

## Collections — Catalogues de référence fusionnés

> Organisés par domaine fonctionnel. Non chargés automatiquement — référencer le chemin complet dans CLAUDE.md du projet.

### development/ — Dev, Ingénierie, Sécurité
- `dev-tools/` — 21 skills : AWS, Azure DevOps, Playwright, Claude Code Terminal, TDD, Git worktrees, UI/UX guide
- `security/` — 8 skills : OWASP, Trail of Bits, Varlock (secrets), Web app testing, FFuf
- `engineering/` — 19 skills : workflows ingénierie (claude-skills-main)
- `engineering-team/` — 19 skills : workflows équipe ingénierie (claude-skills-main)
- `agents/` — patterns d'agents IA

### business/ — Stratégie, Management, Finance
- `collaboration-pm/` — 12 skills : Git, Kanban, Linear, Meeting insights, PM frameworks
- `c-level-advisor/` — 28 skills : advisory C-suite complet
- `product-team/` — 8 skills : product management
- `project-management/` — 6 skills : PM frameworks
- `business-growth/` — 4 skills : stratégie croissance
- `finance/` — 1 skill : finance

### marketing-content/ — Marketing, Création de contenu, Médias
- `marketing-skill/` — 40 skills : marketing complet (claude-skills-main)
- `media-content/` — 11 skills : YouTube, EPUB, ElevenLabs, vidéo
- `writing-research/` — 6 skills : article extractor, brainstorming, content research

### data/ — Analyse de données, Recherche
- `data-analysis/` — 10 skills : CSV, SQL (MySQL/Postgres/MSSQL), Kaggle, Octav API
- `science-research/` — 4 skills : deep research, materials simulation

### productivity/ — Productivité, Automatisation, Documents
- `utility-automation/` — 5 skills : LinkedIn, file organizer, invoice organizer
- `documents/` — 2 skills : extraction doc, Reveal.js presentations
- `learning-knowledge/` — 1 skill : Ship-Learn-Next

### claude-config/ — Configuration et extension de Claude Code
- `skills/` — hook-factory, agent-factory, slash-command-factory, prompt-factory, agnix (validation), skill-improver, skill-security-auditor, designing-workflow-skills
- `agents/` — agent-designer, self-improving-agent (+ promote)
- `mcp/` — mcp-developer, mcp-server-builder
- `plugins/` — plugin-authoring, codex-cli-bridge

### specialized/ — Domaines spécialisés
- `bundles/` — 5 bundles curatés : agentbay-skills, clawfu-skills, devmarketing-skills, openpaw, wondelai-skills
- `ra-qm-team/` — 11 skills : Regulatory & Quality Management
- `standards/` — 5 skills : standards et guidelines
- `health-life-sciences/` — 2 skills : health ally, DNA genome analysis

### claude-code-skill-factory (Patterns & Templates)
`collections/claude-code-skill-factory/` — 14 skills générés + exemples

Utiliser pour créer de nouveaux skills : voir `documentation/` et `claude-skills-examples/`

## Comment utiliser un skill de collection

Pour utiliser un skill depuis une collection, référencer son chemin dans le CLAUDE.md du projet :
```
@~/Documents/Obsidian/Claude/skills/collections/development/security/owasp/SKILL.md
```
