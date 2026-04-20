# Skill : nouvelle-note

Crée une nouvelle note Obsidian bien structurée dans le vault.

## Comportement

1. Demander à l'utilisateur le titre si `$ARGUMENTS` est vide
2. Déterminer le dossier approprié selon le type de note
3. Créer la note avec un frontmatter YAML complet
4. Utiliser la syntaxe Obsidian (wikilinks, tags avec #)

## Template à utiliser

```markdown
---
title: "{{titre}}"
date: {{date-aujourd-hui}}
tags: []
status: draft
---

# {{titre}}

## Contexte

## Notes

## Liens
-
```

## Arguments

`$ARGUMENTS` : titre de la note (optionnel, demandé si absent)
