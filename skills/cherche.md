# Skill : cherche

Recherche dans les notes du vault Obsidian.

## Comportement

1. Utiliser l'outil Grep pour chercher `$ARGUMENTS` dans tous les `.md` du vault
2. Exclure les dossiers `_claude/` et `.obsidian/`
3. Présenter les résultats groupés par fichier
4. Pour chaque résultat : nom de fichier, numéro de ligne, ligne correspondante
5. Proposer d'ouvrir le fichier le plus pertinent si un seul résultat clair

## Arguments

`$ARGUMENTS` : terme ou phrase à rechercher (obligatoire)

## Exemple

```
/cherche gestion de projet
```
