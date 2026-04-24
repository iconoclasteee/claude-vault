# /log-cc Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Déployer le slash command `/log-cc` qui synthétise une session Claude Code dans le vault Brain, avec source de vérité versionnée dans claude-vault et exécution via symlink.

**Architecture:** Fichier markdown d'instructions qui vit dans `claude-vault/commands/`, exposé à Claude Code via un symlink dans `~/.claude/commands/`. Une page README dans `commands/` formalise la convention. Correction en bonus du `CLAUDE.md` du vault Claude (chemins obsolètes vers iCloud).

**Tech Stack:** Markdown (slash command Claude Code), ln (symlink), git.

---

## File Structure

| Chemin | Type | Rôle |
|---|---|---|
| `~/ObsidianVaults/Claude/commands/README.md` | créer | Convention : toute slash command vit ici |
| `~/ObsidianVaults/Claude/commands/log-cc.md` | créer | Source de vérité de la commande (ce que Claude Code exécute) |
| `~/.claude/commands/log-cc.md` | créer (symlink) | Pointe vers la source dans claude-vault |
| `~/ObsidianVaults/Claude/CLAUDE.md` | modifier | Corriger chemins obsolètes `~/Documents/Obsidian/Brain/` → `~/ObsidianVaults/Brain/`, et `Brain/Inbox/` → `Brain/00 Inbox/` |

---

## Task 1 : Créer README.md de la convention `commands/`

**Files:**
- Create: `~/ObsidianVaults/Claude/commands/README.md`

- [ ] **Step 1: Écrire le fichier**

Contenu exact à mettre dans `~/ObsidianVaults/Claude/commands/README.md` :

```markdown
# Slash commands — claude-vault

## Convention

Toute nouvelle slash command Claude Code créée pour un usage personnel doit vivre ici comme **source de vérité**.

## Pourquoi ici et pas directement dans `~/.claude/commands/` ?

- **Versionné** : historique Git de chaque évolution
- **Backup** : pushé sur GitHub (`iconoclasteee/claude-vault`)
- **Synchronisé sur VPS** : les agents peuvent lire les commandes si besoin
- **Partageable** : repo public, facilement partagé

## Mécanisme

Chaque commande est un fichier markdown ici. Un **symlink** dans `~/.claude/commands/` la rend accessible à Claude Code sur ce Mac :

\`\`\`bash
ln -s ~/ObsidianVaults/Claude/commands/<name>.md ~/.claude/commands/<name>.md
\`\`\`

Le symlink est transparent pour Claude Code : `/nom-commande` fonctionne exactement comme si le fichier vivait dans `~/.claude/commands/` directement.

## Commandes actuelles

- [`log-cc.md`](log-cc.md) — synthétise une session Claude Code dans le vault Brain
  - Spec : [`log-cc-spec.md`](log-cc-spec.md)
  - Plan d'implémentation : [`log-cc-plan.md`](log-cc-plan.md)
```

- [ ] **Step 2: Vérifier le contenu**

```bash
cat ~/ObsidianVaults/Claude/commands/README.md | head -5
```
Expected : les 5 premières lignes du contenu ci-dessus.

---

## Task 2 : Créer le fichier de commande `log-cc.md`

**Files:**
- Create: `~/ObsidianVaults/Claude/commands/log-cc.md`

Ce fichier est lu par Claude Code quand l'utilisateur tape `/log-cc`. Son contenu est un **prompt** que Claude exécute.

- [ ] **Step 1: Écrire le fichier**

Contenu exact à mettre dans `~/ObsidianVaults/Claude/commands/log-cc.md` :

````markdown
---
description: "Synthétise la session Claude Code en cours dans le vault Brain (01 Journal/Claude code/)"
argument-hint: "[topic optionnel]"
---

# Synthèse de session Claude Code

Tu dois **synthétiser la session de conversation actuelle** (depuis son tout début) et créer une note dans le vault Brain d'Olivier.

## Arguments

- Si l'utilisateur a passé un argument à la commande (`$ARGUMENTS`), il représente le **topic imposé** → utilise-le tel quel comme titre.
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

### 3. Synthétiser la conversation en 7 sections

**Ordre imposé** : Résumé → Décisions clés → Apprentissages → Problèmes rencontrés → À faire → Commandes importantes → Fichiers touchés.

**Règles de style :**
- Ton **synthétique**, factuel, professionnel
- **Ne jamais** commencer le résumé par "Aujourd'hui"
- Si une section n'a rien à dire, **omet-la complètement** (pas de placeholder vide)
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
````

- [ ] **Step 2: Vérifier le contenu**

```bash
head -3 ~/ObsidianVaults/Claude/commands/log-cc.md
```
Expected : la ligne `---` puis `description:` puis `argument-hint:`.

---

## Task 3 : Créer le symlink `~/.claude/commands/log-cc.md`

**Files:**
- Create: `~/.claude/commands/log-cc.md` (symlink)

- [ ] **Step 1: Vérifier que `~/.claude/commands/` existe**

```bash
ls -la ~/.claude/commands/ 2>/dev/null || mkdir -p ~/.claude/commands/
```

- [ ] **Step 2: Créer le symlink**

```bash
ln -s ~/ObsidianVaults/Claude/commands/log-cc.md ~/.claude/commands/log-cc.md
```

- [ ] **Step 3: Vérifier le symlink**

```bash
ls -la ~/.claude/commands/log-cc.md
```

Expected : ligne commençant par `lrwxr-xr-x` et finissant par `-> /Users/<user>/ObsidianVaults/Claude/commands/log-cc.md`

- [ ] **Step 4: Vérifier que Claude Code peut lire le fichier via le symlink**

```bash
readlink ~/.claude/commands/log-cc.md
head -3 ~/.claude/commands/log-cc.md
```

Expected :
- `readlink` retourne `/Users/<user>/ObsidianVaults/Claude/commands/log-cc.md`
- `head` montre le frontmatter `description:` et `argument-hint:`

---

## Task 4 : Corriger `~/ObsidianVaults/Claude/CLAUDE.md` (chemins obsolètes)

**Files:**
- Modify: `~/ObsidianVaults/Claude/CLAUDE.md`

- [ ] **Step 1: Lire le fichier actuel**

```bash
cat ~/ObsidianVaults/Claude/CLAUDE.md
```

- [ ] **Step 2: Remplacer les chemins obsolètes**

Remplacements à faire :
- `~/Documents/Obsidian/Brain/` → `~/ObsidianVaults/Brain/`
- `Brain/Inbox/` → `Brain/00 Inbox/`
- Si présent : `Brain/Notes/` → `Brain/03 Notes/`
- Si présent : toute autre ref à un ancien chemin

Utilise l'outil Edit pour faire ces substitutions ciblées.

- [ ] **Step 3: Vérifier qu'aucun chemin obsolète ne subsiste**

```bash
grep -E "Documents/Obsidian|Brain/Inbox[^0]|Brain/Notes[^0]|Brain/MOC[^0]|Brain/Briefs[^0]|Brain/Journal[^0]|Brain/01 Projets|Brain/02 Domaines|Brain/03 Ressources|Brain/04 Archive" ~/ObsidianVaults/Claude/CLAUDE.md || echo "✓ aucun chemin obsolète"
```

Expected : `✓ aucun chemin obsolète`

---

## Task 5 : Git commit + push (claude-vault)

**Files:**
- Commit all changes in `~/ObsidianVaults/Claude/`

- [ ] **Step 1: Vérifier les changements**

```bash
cd ~/ObsidianVaults/Claude && git status --short
```

Expected : 3 fichiers
- `A commands/README.md`
- `A commands/log-cc.md`
- `M CLAUDE.md`

(Note : `log-cc-plan.md` et `log-cc-spec.md` sont déjà commités précédemment.)

- [ ] **Step 2: Stage + commit**

```bash
cd ~/ObsidianVaults/Claude && \
  git add commands/README.md commands/log-cc.md CLAUDE.md && \
  git commit -m "feat: slash command /log-cc + correction chemins CLAUDE.md"
```

- [ ] **Step 3: Push**

```bash
cd ~/ObsidianVaults/Claude && git push
```

Expected : push OK, hash de nouveau commit visible.

- [ ] **Step 4: Vérifier la propagation VPS**

```bash
ssh <vps-host> '~/vaults/sync-vault.sh ~/vaults/Claude 2>&1 | tail -3'
```

Expected : `Updating <old>..<new> Fast-forward` dans la sortie.

---

## Task 6 : Test end-to-end manuel (validation post-implémentation)

**Files:** aucun (test d'usage)

- [ ] **Step 1: Relancer Claude Code dans un terminal neuf**

Ouvrir un nouveau terminal ou redémarrer la session Claude Code en cours pour que le slash command soit détecté.

- [ ] **Step 2: Tester la commande minimale**

Dans Claude Code, taper :
```
/log-cc test implementation log-cc
```

Attendu :
- Claude détecte la commande
- Exécute les instructions du fichier
- Crée un fichier dans `~/ObsidianVaults/Brain/01 Journal/Claude code/`
- Affiche le contenu dans le terminal
- Termine par la phrase "Tu veux ajuster quelque chose ?"

- [ ] **Step 3: Vérifier le fichier créé**

```bash
ls -la ~/ObsidianVaults/Brain/01\ Journal/Claude\ code/
```

Expected : 1 fichier du jour avec le topic "test implementation log-cc".

- [ ] **Step 4: Tester la régénération**

Dans Claude Code, répondre :
```
refais plus court, juste 2 lignes de résumé
```

Expected : Claude régénère le fichier, le réaffiche. Le fichier cible est écrasé (même chemin).

- [ ] **Step 5: Vérifier la sync Git**

Attendre ~10 min OU déclencher manuellement via command palette Obsidian : "Obsidian Git: Commit-and-sync".

```bash
ssh <vps-host> 'ls /home/<user>/vaults/Brain/01\ Journal/Claude\ code/ 2>&1'
```

Expected : le fichier test arrive côté VPS dans les ~5 min suivantes (via le cron).

- [ ] **Step 6: Nettoyage du test**

Supprimer le fichier test dans Obsidian (ou `rm` en ligne de commande), laisser la prochaine sync propager la suppression.

---

## Self-review (déjà effectué lors de l'écriture)

- ✅ Couverture spec : tous les livrables de la spec sont dans des tasks (README, log-cc.md, symlink, CLAUDE.md, commit)
- ✅ Pas de placeholder : tout le contenu est explicite
- ✅ Cohérence des types : `log-cc.md` référencé aux mêmes chemins partout
- ✅ Chaque task fait 2-5 min d'actions concrètes
- ✅ Commandes exactes avec expected output
