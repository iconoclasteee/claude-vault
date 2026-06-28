---
description: "Synthétise la session Claude Code en cours dans le vault Brain (01 Journal/Claude code/)"
argument-hint: "[topic optionnel]"
---

# Synthèse de session Claude Code

Tu dois **synthétiser la session de conversation actuelle**, depuis son tout début — ou depuis le dernier appel à `/log-cc` dans cette session, si la commande a déjà été lancée — et créer une note dans le vault Brain d'Olivier.

## Arguments

- Si l'utilisateur a passé un argument à la commande, il représente le **topic imposé** → utilise-le tel quel comme titre.
- Sinon, **auto-détecte le topic** : un titre synthétique de 3 à 6 mots qui capture l'action principale de la session (exemples : "Setup sync vaults", "Debug cron expired token", "Refacto dossiers PARA").

## Étapes à exécuter

### 1. Déterminer le nom de fichier cible et le contexte machine

- Date : aujourd'hui, format `YYYY-MM-DD`
- Heure : maintenant, format `HHhMM` (exemple : `17h45`)
- Topic : selon la règle ci-dessus
- Caractères invalides dans le topic (`/`, `:`, `\`, `*`, `?`, `"`, `<`, `>`, `|`) → remplace par `-` ou supprime
- **Nom de la machine** : récupère via `hostname -s` (nom court)
- **Répertoire où Claude a été lancé** : récupère via `pwd` (chemin absolu courant)
- **Nom de session Claude** (= exactement ce qu'affiche `claude -r`) : c'est le dernier titre `aiTitle` du journal de session, retrouvé via `$CLAUDE_CODE_SESSION_ID`. ⚠️ Ce fichier vit dans le vault **public** → n'écris **aucun** chemin absolu avec username, UUID ou slug en dur ; utilise les variables :
  ```bash
  SID="$CLAUDE_CODE_SESSION_ID"
  SFILE=$(find "$HOME/.claude/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
  SESSION_NAME=$(grep '"type":"ai-title"' "$SFILE" 2>/dev/null | tail -1 \
    | python3 -c 'import sys,json;print(json.loads(sys.stdin.read()).get("aiTitle",""))' 2>/dev/null)
  [ -z "$SESSION_NAME" ] && SESSION_NAME="session Claude Code"   # repli si pas de titre
  ```
  `$SESSION_NAME` et `$SID` alimenteront le champ `session:` du frontmatter (étape 4).

Chemin final : `~/ObsidianVaults/Brain/01 Journal/Claude code/YYYY-MM-DD HHhMM — <topic>.md`

Si le fichier existe déjà (même minute, collision), ajoute suffixe `-2`, `-3`, etc.

Crée le dossier `~/ObsidianVaults/Brain/01 Journal/Claude code/` s'il n'existe pas (`mkdir -p`).

### 2. Rechercher 1 à 3 WikiLinks pertinents

Scan rapide :
- Liste le contenu de `~/ObsidianVaults/Brain/03 Notes/` et `~/ObsidianVaults/Brain/04 MOC/`
- Identifie 1 à 3 notes dont le titre est sémantiquement proche du topic
- Si aucune note pertinente trouvée, **omet complètement la section "Liens"** du fichier final (ne mets pas de "aucune note pertinente")

### 2bis. Générer les tags contextuels

**Principe central** : un tag est un **filtre de retrieval fonctionnel**. Il doit pouvoir servir à dire « donne-moi tous les logs sur X » où X est un contexte qu'Olivier voudrait réinjecter dans une nouvelle session Claude. Tague le **quoi/pourquoi** (produit, finalité, livrable), pas le **comment** (techno d'exécution).

Règles :

- **`type/fleeting`** : toujours présent (c'est un journal brut, non retravaillé).
- **`domaine/<X>`** : 1 à 3 max. **Domaine fonctionnel pérenne** auquel la session contribue. Ex valides : `domaine/brief-ai`, `domaine/carriere`, `domaine/obsidian`, `domaine/claude-code`, `domaine/design`. **À éviter** : `domaine/git`, `domaine/nginx`, `domaine/devops`, `domaine/web`, `domaine/ia` quand ce sont des moyens et non des fins. **Interdits** : `domaine/meta` (trop générique).
- **`projet/<Y>`** : 0 à 2. **Uniquement les projets pérennes** d'Olivier — sous-dossiers de `~/ObsidianVaults/Brain/11 Projets/` ou repos qu'il maintient (`projet/brain`, `projet/vault-claude`, `projet/briefs-pipeline`). **Jamais** pour un projet one-shot, expérimental, ou éphémère.
- **Mots-clés libres** (sans préfixe) : 0 à 3. Tout ce qui parle fonctionnellement — noms de commandes (`log-cc`), URLs (`brief-ai.orhein.com`), finalités (`demo`, `cv`, `deploiement`), événements (`bpce-lab-ia`). **À éviter** : noms de libs, frameworks, références visuelles internes, technos.

**Test de validation** : si un tag ne te servirait pas pour retrouver ce log depuis une nouvelle session Claude dans 3 mois, jette-le. Mieux vaut 4 tags pertinents que 7 tags descriptifs.

Total visé : 3 à 7 tags.

### 3. Synthétiser la conversation en 8 sections

**Ordre imposé** : Objectif utilisateur → Résumé → Décisions clés → Apprentissages → Problèmes rencontrés → À faire → Commandes importantes → Fichiers touchés.

**Sémantique des sections** :
- **Objectif utilisateur** : le "pourquoi système" que poursuit Olivier à travers cette session — la **vision cible** ou le **résultat désiré** à terme (pas ce qu'on a fait techniquement — ça c'est "Résumé"). 2-5 phrases qui décrivent l'état du monde qu'Olivier veut atteindre. Reformule avec tes mots en t'appuyant sur ce qui a émergé de la conversation (besoins exprimés, contraintes, arbitrages faits). Exemple de style : "Avoir un second brain sur Obsidian accessible depuis Mac, VPS et iPhone ; avoir un vault Claude qui centralise les skills et permet de les découvrir/installer facilement via skill-advisor ; pouvoir journaliser les sessions Claude Code dans Brain."
- **Résumé** : ce qui a été **fait** dans cette session précise (2-5 phrases, ton factuel, pas "Aujourd'hui")
- **Décisions clés** : uniquement les décisions qui ont **infléchi la direction** de la session — changement d'instruction, d'objectif, de périmètre, de priorisation — **prises par Olivier ou arbitrées avec lui**. Les choix d'exécution que l'IA a faits seule en cours de route **n'ont pas leur place ici** (ils relèvent du "Résumé" s'ils comptent). Si aucune décision n'a infléchi la direction, **omets la section**.
- **Apprentissages** : uniquement les **bonnes pratiques réutilisables** — une règle, un piège récurrent, une méthode, une contrainte non-évidente de l'environnement — que l'IA ou Olivier devrait réappliquer dans une future session. Pas les détails d'exécution propres à cette session.
- **Problèmes rencontrés** : uniquement les problèmes dont la **leçon est durable** (piège qui se reproduira, contrainte d'environnement, faux-ami). Un bug ponctuel résolu qui ne se reproduira pas (typo, clé mal normalisée, artefact de copier-coller) **n'a pas sa place ici** : soit sa leçon généralisable remonte dans Apprentissages, soit on l'omet.
- Les 4 autres sections gardent leur sens habituel

**Règles de style :**
- Ton **synthétique**, factuel, professionnel
- **Ne jamais** commencer le résumé par "Aujourd'hui"
- Si une section n'a rien à dire, **omet-la complètement** (pas de placeholder vide). Exception : "Objectif utilisateur" et "Résumé" sont toujours présentes
- Frontmatter obligatoire (cf. template)

**Test de capitalisation (Apprentissages + Problèmes)** : avant d'écrire une puce, demande-toi « dans 3 mois, l'IA ou moi ferions-nous différemment / éviterions-nous une erreur grâce à cette ligne ? ». Si non → jette-la. Mieux vaut **0 puce** qu'une puce de bruit ; ces deux sections s'omettent complètement si rien ne passe le test.

### 4. Écrire le fichier

Utilise ce template exact :

```markdown
---
title: "<topic>"
date: YYYY-MM-DD
tags:
  - type/fleeting
  - domaine/<X>        # 1 à 3 tags domaine, déduits de la session (cf. règles §2bis)
  - projet/<Y>         # 0 à 2 tags projet, uniquement si projet identifiable
  - <mot-cle-libre>    # 0 à 3 mots-clés libres en kebab-case
status: active
session: "<$SESSION_NAME> — YYYY-MM-DD HHhMM (<$CLAUDE_CODE_SESSION_ID>)"   # nom claude -r — date heure (ID technique) ; cf. étape 1
machine: "<hostname court>"
repertoire: "<cwd absolu où Claude a été lancé>"
---

# <topic>

## Objectif utilisateur
<2 à 5 phrases décrivant la vision cible / résultat désiré par Olivier — le "pourquoi système" de la session, pas le "quoi on a fait">

## Résumé
<2 à 5 phrases synthétiques, ton factuel, sans commencer par "Aujourd'hui">

## Décisions clés
- <décision qui a infléchi la direction (instruction/objectif/périmètre/priorité), prise ou arbitrée avec Olivier> parce que <raison> (rejeté <alternative> car <raison>)
- ...

## Apprentissages
- <bonne pratique réutilisable / piège récurrent / méthode — réapplicable en future session>
- ...

## Problèmes rencontrés
- **<problème dont la leçon est durable — piège qui se reproduira, contrainte d'env.>**
  - **Solution** : <ce qui a marché, formulé comme règle réutilisable>
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

### 5. Commit local ciblé (pas de push)

Détecte d'abord si **Obsidian est ouvert** (il gère alors l'auto-sync git du vault — cela conditionne la clôture, étapes 7/8) :
```bash
pgrep -x Obsidian >/dev/null && OBSIDIAN=ouvert || OBSIDIAN=fermé
```

Puis commit **localement** sans push, sur l'hôte où le fichier a été écrit. ⚠️ Ajoute **uniquement LA note** (jamais `git add -A`, qui embarquerait des fichiers sans rapport — ex. `.bak` du vault) :

- **Si écrit localement sur le Mac** :
  ```bash
  cd ~/ObsidianVaults/Brain && git add -- "01 Journal/Claude code/<nom du fichier>.md" && git commit -m "journal: <$SESSION_NAME> — YYYY-MM-DD HHhMM — <topic>"
  ```
- **Si écrit sur le VPS** :
  ```bash
  ssh <vps-host> 'cd ~/ObsidianVaults/Brain && git add -- "01 Journal/Claude code/<nom du fichier>.md" && git commit -m "journal: <$SESSION_NAME> — YYYY-MM-DD HHhMM — <topic>"'
  ```

Si rien à committer ou échec, rapporte mais ne bloque pas.

### 6. Afficher le contenu dans le terminal

Après avoir écrit le fichier et committé, **affiche son contenu complet** dans la conversation pour preview.

### 7. Clôture — selon qu'Obsidian est ouvert ou non

**Le comportement de fin dépend de `$OBSIDIAN` (déterminé à l'étape 5).**

#### Cas A — Obsidian est OUVERT (auto-sync actif → PAS de push manuel)

Le plugin Obsidian Git committe et **pousse automatiquement** en arrière-plan. Ne demande donc **pas** « tape ok pour pousser ». Termine par :

> **Note créée et commitée : `<chemin>` (`<hash-court>`).**
> Obsidian est ouvert → Obsidian Git la **poussera automatiquement** sur GitHub, rien à faire.
> Tu veux ajuster quelque chose ? (ex : « refais plus court », « enlève la section Décisions »).

- Si l'utilisateur demande une modification : **réécris le fichier**, puis fais un **nouveau commit ciblé** (`git add -- "<note>" && git commit -m "…"`) — **jamais d'`amend`** ici (HEAD bouge à cause de l'auto-commit Obsidian, l'amend se collerait sur un commit « vault backup »). Réaffiche et repose la question.
- **Il n'y a pas d'étape 8** dans ce cas.

#### Cas B — Obsidian est FERMÉ (push manuel sur confirmation)

Termine par :

> **Fichier créé + commité : `<chemin>` (`<hash-court>`)**
> Tu veux ajuster quelque chose ? Sinon, tape « ok » pour pousser sur GitHub.

- Si modification demandée : **régénère et écrase le fichier**, puis **amend** (`git commit -a --amend --no-edit`), réaffiche, repose la question.
- Si l'utilisateur confirme (`ok`, `oui`, `go`, `push`…) : passe à l'étape 8.

### 8. Push manuel (uniquement cas B — Obsidian fermé)

Sur le même hôte qu'à l'étape 5 :

- **Mac** :
  ```bash
  cd ~/ObsidianVaults/Brain && git pull --rebase --autostash origin main && git push origin main
  ```
- **VPS** :
  ```bash
  ssh <vps-host> '~/ObsidianVaults/sync-vault.sh ~/ObsidianVaults/Brain'
  ```
  (le script fait pull --rebase --autostash + push ; peut créer un commit "auto: vps sync …" — c'est normal)

Affiche le hash court poussé et confirme que `origin/main` est à jour. Si le push échoue, rapporte l'erreur sans bloquer — le cron `sync-vault.sh` du VPS rattrapera dans les 5 min.

## Contraintes strictes

- Une seule note par session — pas de multi-fichiers
- Toujours la session **depuis le début** — pas de tranche
- Respecte le frontmatter Brain (cf. conventions dans `~/ObsidianVaults/Brain/.claude/CLAUDE.md`)
- WikiLinks uniquement pour les liens internes, pas de liens Markdown

$ARGUMENTS
