---
description: "Promeut un keeper (code ou livrable) en projet formalisé : fiche dans Brain/11 Projets + rangement ~/dev si code"
argument-hint: "[nom-du-projet optionnel]"
---

# /formalise-projet — Promouvoir un keeper en projet

Transforme un artefact durable né d'une session (script, commande, outil, OU analyse / rapport
/ pptx / excel) en **projet formalisé et retrouvable**. Couche d'index universelle :
`Brain/11 Projets/`. Le code vit en plus dans `~/dev/`.

## 1. Identifier l'artefact
- Argument fourni → c'est le nom du projet.
- Sinon, déduis le(s) keeper(s) de la session courante (et de la dernière note /log-cc si utile).
  Plusieurs candidats → demande lequel.
- Détermine le **médium** : CODE vs LIVRABLE (doc).

## 2. Nom + anti-doublon
- Nom court en kebab-case.
- Vérifie l'existant : `~/ObsidianVaults/Brain/11 Projets/<nom>/` et/ou `~/dev/<nom>/`.
  Si présent → **mise à jour**, jamais duplication.

## 3a. Si CODE → ranger dans ~/dev
- Code éparpillé (dans `~`, `_lab`, Downloads…) → crée `~/dev/<nom>/`, déplace-le, écris un
  `README.md` qui **commence par le POURQUOI** (besoin, problème, alternatives écartées — puisés
  dans la session).
- Puis **versionne et fais un premier commit** :
  ```bash
  cd ~/dev/<nom> && git init -q && printf '.DS_Store\n' >> .gitignore \
    && git add -A && git commit -q -m "init: <nom> — <pitch en une ligne>"
  ```
- Effets de bord environnement (`.zshrc`, cron, hooks) → documente-les dans le README.

## 3b. Si LIVRABLE → laisser en place
- Le fichier reste dans son dossier naturel (OneDrive/Dropbox). On capture juste son chemin et
  son pourquoi dans la fiche.

## 4. Fiche projet dans Brain/11 Projets (TOUJOURS — c'est le cœur)
`~/ObsidianVaults/Brain/11 Projets/<nom>/<nom>.md` (crée le dossier si besoin).
Frontmatter Brain standard (title, date, tags `type/permanent` + `domaine/…` + `projet/<nom>`,
status, source). Corps :
- **## Pourquoi** — le besoin / problème (le plus important, tant que c'est frais)
- **## Artefacts** — liens/chemins : code (`~/dev/<nom>`) et/ou livrables (chemin OneDrive)
- **## État** — où ça en est
- **## Prochaines étapes** — `[ ] …`
- WikiLinks vers notes / MOC pertinents.

## 5. Confirmer
Résume : fiche créée (chemin), code rangé + commité le cas échéant, ce qui reste.

## Sécurité
Ce fichier-commande vit dans le vault **public** → aucun chemin absolu avec username ni nom de
client en dur ici. La fiche `11 Projets` (vault **privé** Brain) peut, elle, contenir ces détails.

$ARGUMENTS
