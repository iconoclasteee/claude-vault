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

### 5. Commit automatique immédiat (pas de push)

Juste après l'écriture du fichier, commit **localement** sans push, sur l'hôte où le fichier a été écrit :

- **Si écrit sur le VPS** :
  ```bash
  ssh <vps-host> 'cd ~/ObsidianVaults/Brain && git add -A && git commit -m "journal: session Claude Code YYYY-MM-DD HHhMM — <topic>"'
  ```
- **Si écrit localement sur le Mac** :
  ```bash
  cd ~/ObsidianVaults/Brain && git add -A && git commit -m "journal: session Claude Code YYYY-MM-DD HHhMM — <topic>"
  ```

Si rien à committer ou échec, rapporte mais ne bloque pas.

### 6. Afficher le contenu dans le terminal

Après avoir écrit le fichier et committé, **affiche son contenu complet** dans la conversation pour preview.

### 7. Attendre l'input utilisateur

Termine par :

> **Fichier créé + commité : `<chemin>` (`<hash-court>`)**
> Tu veux ajuster quelque chose ? (ex: "refais plus court", "enlève la section Décisions", "ajoute X"). Sinon, tape "ok" pour pousser sur GitHub.

- Si l'utilisateur demande une modification : **régénère et écrase le fichier** (même chemin), puis **amend** le commit (`git commit -a --amend --no-edit`), réaffiche le nouveau contenu et repose la question.
- Si l'utilisateur confirme (`ok`, `oui`, `go`, `push`, etc.) : passe à l'étape 8.

### 8. Push manuel après confirmation

Sur le même hôte qu'à l'étape 5 :

- **VPS** :
  ```bash
  ssh <vps-host> '~/ObsidianVaults/sync-vault.sh ~/ObsidianVaults/Brain'
  ```
  (le script fait pull --rebase --autostash + push ; peut créer un commit "auto: vps sync …" supplémentaire s'il détecte d'autres changements en attente — c'est normal)
- **Mac** :
  ```bash
  cd ~/ObsidianVaults/Brain && git pull --rebase --autostash origin main && git push origin main
  ```

Affiche le hash court poussé et confirme que `origin/main` est à jour. Si le push échoue, rapporte l'erreur sans bloquer — le cron `sync-vault.sh` du VPS rattrapera dans les 5 min.

## Contraintes strictes

- Une seule note par session — pas de multi-fichiers
- Toujours la session **depuis le début** — pas de tranche
- Respecte le frontmatter Brain (cf. conventions dans `~/ObsidianVaults/Brain/.claude/CLAUDE.md`)
- WikiLinks uniquement pour les liens internes, pas de liens Markdown

$ARGUMENTS
