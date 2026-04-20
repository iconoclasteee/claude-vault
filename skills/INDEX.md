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

## Collections — Catalogues de référence

### awesome-claude-skills (ComposioHQ)
`collections/awesome-claude-skills/` — 94 skills, 12 catégories

| Catégorie | Skills clés |
|-----------|-------------|
| collaboration-pm | Git, Kanban, Linear, Meeting insights |
| data-analysis | CSV, SQL (MySQL/Postgres), Kaggle |
| development | AWS, Playwright, Claude Code Terminal, TDD, Git worktrees |
| media-content | YouTube transcript, EPUB reader, ElevenLabs |
| security | OWASP, Trail of Bits, Varlock (secrets), Web app testing |
| utility-automation | LinkedIn, File organizer, Invoice organizer |
| writing-research | Article extractor, Brainstorming, Content research writer |

### claude-skills-main (169 skills par rôle métier)
`collections/claude-skills-main/` — Library ultra-spécialisée par rôle

| Domaine | Description |
|---------|-------------|
| c-level-advisor | Advisory C-suite (34 sous-skills) |
| engineering | Workflows ingénierie (21 skills) |
| marketing-skill | Marketing complet (45 skills) |
| product-team | Product management (15 skills) |
| project-management | PM frameworks (11 skills) |

### claude-code-skill-factory (Patterns & Templates)
`collections/claude-code-skill-factory/` — 14 skills générés + exemples

Utiliser pour créer de nouveaux skills : voir `documentation/` et `claude-skills-examples/`

## Comment utiliser un skill de collection

Pour utiliser un skill depuis une collection, référencer son chemin dans le CLAUDE.md du projet :
```
@~/Documents/Obsidian/Claude/skills/collections/awesome-claude-skills/security/owasp/SKILL.md
```
