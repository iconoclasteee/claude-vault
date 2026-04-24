---
description: "Synthétise la session Claude Code en cours dans le vault Brain (01 Journal/Claude code/)"
argument-hint: "[topic optionnel]"
---

# Synthèse de session Claude Code

Tu dois **synthétiser la session de conversation actuelle** (depuis son tout début) et créer une note dans le vault Brain d'Olivier.

## Arguments

- Si l'utilisateur a passé un argument à la commande, il représente le **topic imposé** → utilise-le tel quel comme titre.
- Sinon, **auto-détecte le topic** : un titre synthétique de 3 à 6 mots qui capture l'action principale de la session (exemples : "Setup sync vaults", "Debug cron expired token", "Refacto dossiers PARA").

## Étapes à exécuter

### 1. Déterminer le nom de fichier cible

- Date : aujourd'hui, format `YYYY-MM-DD`
- Heure : maintenant, format `HHhMM` (exemple : `17h45`)
- Topic : selon la règle ci-dessus
- Caractères invalides dans le topic (`/`, `:`, `\`, `*`, `?`, `"`, `<`, `>`, `|`) → remplace par `-` ou supprime

Chemin final : `~/ObsidianVaults/Brain/01 Journal/Claude code/YYYY-MM-DD HHhMM — <topic>.md`

Si le fichier existe déjà (même minute, collision), ajoute suffixe `-2`, `-3`, etc.

Crée le dossier `~/ObsidianVaults/Brain/01 Journal/Claude code/` s'il n'existe pas (`mkdir -p`).

### 2. Rechercher 1 à 3 WikiLinks pertinents

Scan rapide :
- Liste le contenu de `~/ObsidianVaults/Brain/03 Notes/` et `~/ObsidianVaults/Brain/04 MOC/`
- Identifie 1 à 3 notes dont le titre est sémantiquement proche du topic
- Si aucune note pertinente trouvée, **omet complètement la section "Liens"** du fichier final (ne mets pas de "aucune note pertinente")

### 3. Synthétiser la conversation en 8 sections

**Ordre imposé** : Objectif utilisateur → Résumé → Décisions clés → Apprentissages → Problèmes rencontrés → À faire → Commandes importantes → Fichiers touchés.

**Sémantique des sections** :
- **Objectif utilisateur** : le "pourquoi système" que poursuit Olivier à travers cette session — la **vision cible** ou le **résultat désiré** à terme (pas ce qu'on a fait techniquement — ça c'est "Résumé"). 2-5 phrases qui décrivent l'état du monde qu'Olivier veut atteindre. Reformule avec tes mots en t'appuyant sur ce qui a émergé de la conversation (besoins exprimés, contraintes, arbitrages faits). Exemple de style : "Avoir un second brain sur Obsidian accessible depuis Mac, VPS et iPhone ; avoir un vault Claude qui centralise les skills et permet de les découvrir/installer facilement via skill-advisor ; pouvoir journaliser les sessions Claude Code dans Brain."
- **Résumé** : ce qui a été **fait** dans cette session précise (2-5 phrases, ton factuel, pas "Aujourd'hui")
- Les 6 autres sections gardent leur sens habituel

**Règles de style :**
- Ton **synthétique**, factuel, professionnel
- **Ne jamais** commencer le résumé par "Aujourd'hui"
- Si une section n'a rien à dire, **omet-la complètement** (pas de placeholder vide). Exception : "Objectif utilisateur" et "Résumé" sont toujours présentes
- Frontmatter obligatoire (cf. template)

### 4. Écrire le fichier

Utilise ce template exact :

```markdown
---
title: "<topic>"
date: YYYY-MM-DD
tags:
  - type/fleeting
  - domaine/claude-code
  - domaine/meta
status: active
source: "session Claude Code YYYY-MM-DD HHhMM"
---

# <topic>

## Objectif utilisateur
<2 à 5 phrases décrivant la vision cible / résultat désiré par Olivier — le "pourquoi système" de la session, pas le "quoi on a fait">

## Résumé
<2 à 5 phrases synthétiques, ton factuel, sans commencer par "Aujourd'hui">

## Décisions clés
- <décision> parce que <raison> (rejeté <alternative> car <raison>)
- ...

## Apprentissages
- <ce qu'Olivier a appris, technique ou méthodo>
- ...

## Problèmes rencontrés
- **<description du problème>**
  - **Solution** : <ce qui a marché>
- ...

## À faire
- [ ] <action restante>
- ...

## Commandes importantes
​```bash
<commandes shell ou snippets notables>
​```

## Fichiers touchés
- `<chemin>` — <nature du changement>
- ...

## Liens
- [[<Note existante 1>]] — <pourquoi pertinente>
- [[<Note existante 2>]] — <pourquoi pertinente>
```

### 5. Afficher le contenu dans le terminal

Après avoir écrit le fichier, **affiche son contenu complet** dans la conversation pour preview.

### 6. Attendre l'input utilisateur

Termine par :

> **Fichier créé : `<chemin>`**
> Tu veux ajuster quelque chose ? (ex: "refais plus court", "enlève la section Décisions", "ajoute X"). Sinon, tape "ok" ou rien.

Si l'utilisateur demande une modification, **régénère et écrase le fichier** (même chemin), puis réaffiche le nouveau contenu.

## Contraintes strictes

- Une seule note par session — pas de multi-fichiers
- Toujours la session **depuis le début** — pas de tranche
- Respecte le frontmatter Brain (cf. conventions dans `~/ObsidianVaults/Brain/.claude/CLAUDE.md`)
- WikiLinks uniquement pour les liens internes, pas de liens Markdown

$ARGUMENTS
