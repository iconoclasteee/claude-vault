# Skills — Commandes /slash personnalisées

> Les fichiers dans ce dossier deviennent des commandes `/nom-fichier` dans Claude Code.
> Ce dossier est symlinké depuis `.claude/skills/` et donc actif automatiquement.

## Comment utiliser un skill

Dans Claude Code, taper `/nom-du-fichier` (sans l'extension `.md`).
Ex: `/nouvelle-note` lance le skill `nouvelle-note.md`.

## Comment créer un skill

1. Créer un fichier `mon-skill.md` dans ce dossier
2. Le fichier est un prompt qui sera exécuté par Claude
3. Utiliser `$ARGUMENTS` pour récupérer les arguments passés à la commande

## Skills disponibles

| Commande | Description |
|----------|-------------|
| `/nouvelle-note` | Créer une nouvelle note Obsidian structurée |
| `/resume-session` | Résumer ce qui a été fait dans la session |
| `/cherche` | Rechercher dans les notes du vault |

## Template de skill

```markdown
# Skill : nom-du-skill

## Description
Ce que fait ce skill en une phrase.

## Comportement
Instructions détaillées pour Claude...

## Arguments
$ARGUMENTS : description de ce qui peut être passé en argument

## Exemple
/nom-du-skill argument optionnel
```
