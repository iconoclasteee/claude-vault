# Skill : resume-session

Produit un résumé structuré de la session de travail en cours.

## Comportement

Rédiger un résumé de la session qui inclut :

1. **Ce qui a été fait** : liste des actions et modifications effectuées
2. **Fichiers modifiés** : liste avec chemin complet
3. **Décisions prises** : choix importants et leur justification
4. **Points en suspens** : ce qui reste à faire ou à décider
5. **Prochaines étapes** : actions recommandées pour la prochaine session

## Format de sortie

```markdown
## Résumé de session — {{date}}

### Réalisé
-

### Fichiers modifiés
-

### Décisions
-

### En suspens
-

### Prochaines étapes
-
```

## Arguments

`$ARGUMENTS` : contexte supplémentaire optionnel à inclure dans le résumé
