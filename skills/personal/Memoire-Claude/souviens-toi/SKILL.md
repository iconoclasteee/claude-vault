---
name: souviens-toi
description: Archive une information en mémoire persistante, en demandant d'abord OÙ elle doit être rechargée (ce projet / global machine / un autre projet), et écrit toujours une archive dans Brain/12 Domaines/AI/. À utiliser quand l'utilisateur tape /souviens-toi ou dit "souviens-toi que", "retiens que", "garde en mémoire".
---

# /souviens-toi — Archivage mémoire persistante

## Quand déclencher

- L'utilisateur tape `/souviens-toi <contenu>`
- L'utilisateur dit "souviens-toi que...", "retiens que...", "garde en mémoire..."

## Concept clé — la portée (scope)

La mémoire auto de Claude Code est **scopée par répertoire de lancement** : un fait écrit dans `~/.claude/projects/<slug>/memory/` n'est rechargé que si `claude` est lancé depuis ce répertoire précis. Le seul moyen de rendre un fait **global** (toute la machine) est de l'écrire dans `~/.claude/CLAUDE.md`. Cette skill laisse donc l'utilisateur **choisir la portée**.

## Workflow

1. **Classifier l'info** selon les types du système memory auto :
   - `user` — rôle, préférences, expertise d'Olivier
   - `feedback` — correction ou validation d'une approche
   - `project` — fait daté, décision, deadline
   - `reference` — pointeur externe (Linear, Grafana, etc.)

2. **Récupérer le contexte machine** :
   - **Machine** : `hostname -s` (nom court).
   - **Répertoire de lancement courant** = clé de scope : le `Primary working directory` indiqué au démarrage de la session. **PAS** un simple `pwd`, qui peut avoir dérivé si une commande a fait un `cd`.

3. **Proposer les 3 destinations** et attendre le choix (cf. format en bas) :

   - **1 · Ce projet** → `~/.claude/projects/<slug-courant>/memory/`. Rechargée seulement depuis ce répertoire. Afficher le **basename** + le **chemin complet**.
   - **2 · Global — cette machine** → ajout à `~/.claude/CLAUDE.md`. Rechargée à **chaque** session sur cette machine. Afficher `hostname -s`.
   - **3 · Un autre projet** → liste **dynamique** des autres projets, **triée par récence** (façon `claude -r`), avec le **vrai chemin** ; plus l'option « liste complète » et « ✏️ saisir un chemin absolu » (route fiable à 100 %).

   **Construction de la liste de l'option 3** (dynamique, multi-machine) : pour chaque dossier `~/.claude/projects/*/`, prendre le `.jsonl` le plus récent → son mtime (récence) et son champ `"cwd"` (vrai chemin absolu de lancement). Trier par mtime décroissant, exclure le projet courant, afficher ~6 entrées. Commande de référence (macOS ; sur Linux remplacer `stat -f '%m'` par `stat -c '%Y'`) :
   ```bash
   for p in ~/.claude/projects/*/; do
     l=$(ls -t "$p"*.jsonl 2>/dev/null | head -1); [ -z "$l" ] && continue
     cwd=$(grep -o '"cwd":"[^"]*"' "$l" | head -1 | sed 's/.*"cwd":"//;s/"$//')
     echo "$(stat -f '%m' "$l")|$cwd"
   done | sort -rn | head -6
   ```

4. **Écrire la mémoire selon l'option choisie** :
   - **Option 1 ou 3** : fichier dédié dans `~/.claude/projects/<slug>/memory/` + pointeur dans le `MEMORY.md` **de ce projet**. Frontmatter `name / description / metadata.type`.
     - Le **slug** = chemin absolu cible avec **tout caractère non alphanumérique remplacé par `-`** (ex. `/Users/x/Mon Dossier` → `-Users-x-Mon-Dossier`). Pour l'option 3 par saisie, si le dossier projet n'existe pas encore, créer `~/.claude/projects/<slug>/memory/`.
   - **Option 2 (global)** : ajouter une puce dans `~/.claude/CLAUDE.md`, sous une section dédiée `## Mémoire globale (souviens-toi)` (la créer si absente, en fin de fichier). Format réversible : `- <règle reformulée> _(souviens-toi, YYYY-MM-DD)_`.

5. **Pousser dans le vault Brain** — **toujours**, quelle que soit l'option — dans `~/ObsidianVaults/Brain/12 Domaines/AI/` :
   - Vérifier d'abord s'il existe déjà une note sur le sujet (`ls` + Grep) → si oui, Edit pour appender, sinon Write une nouvelle note
   - Nommage : `YYYY-MM-DD — titre-court.md`
   - Frontmatter Brain obligatoire :
     ```yaml
     ---
     title: "Titre-thèse"
     date: YYYY-MM-DD
     tags:
       - type/permanent        # ou type/fleeting si brouillon
       - domaine/ia            # ou domaine pertinent
     status: active
     source: "session claude code YYYY-MM-DD"
     machine: "<hostname court>"                       # via hostname -s
     repertoire: "<portée choisie>"                    # chemin absolu (opt. 1/3) ou "global — toute la machine" (opt. 2)
     ---
     ```
   - Utiliser `[[WikiLinks]]` vers les notes existantes pertinentes

6. **Confirmer à l'utilisateur** la/les destination(s) exactes : la portée mémoire choisie **et** la note Brain.

## Format de restitution des options (étape 3)

```
🧠 À mémoriser · type `<type>`
« <contenu reformulé> »

Où cette mémoire doit-elle être rechargée automatiquement ?

1 · 📂 Ce projet — répertoire de lancement courant
    <basename> · <chemin complet>
    ↳ rechargée seulement depuis ce répertoire.

2 · 🌐 Global — cette machine
    <hostname -s> · fichier ~/.claude/CLAUDE.md
    ↳ rechargée à CHAQUE session sur cette machine.

3 · 📁 Un autre projet  (triés du plus récent au plus ancien)
    a. <vrai chemin projet 1>
    b. <vrai chemin projet 2>
    …
    f. … (dis « liste complète »)
    g. ✏️ saisir un chemin absolu

ℹ️ Dans tous les cas, une note d'archive est aussi écrite dans Brain/12 Domaines/AI/.

Ton choix ? → 1, 2, ou 3a–3g
```

## Exemples

- `/souviens-toi je préfère Prisma à Drizzle pour l'ORM`
  → type `user`. Probablement **option 2 (global)** car préférence transverse. + note `Brain/12 Domaines/AI/…`
- `/souviens-toi le schéma de ce projet utilise des UUID v7`
  → type `project`. **Option 1 (ce projet)** car spécifique au repo courant. + note Brain
- `/souviens-toi ne pas mocker la base dans les tests`
  → type `feedback`. Demander la portée (souvent global). + note Brain avec le "pourquoi"

## Anti-patterns

- ❌ Écrire la mémoire sans demander la portée (sauf si l'utilisateur l'a déjà précisée dans sa phrase)
- ❌ Utiliser `pwd` au lieu du répertoire de lancement pour le slug de scope
- ❌ Lister l'option 3 en dur — elle doit être recalculée à chaque appel (multi-machine)
- ❌ Archiver du bruit ponctuel (erreurs de debug, état temporaire de session)
- ❌ Créer une note AI/ sans vérifier les doublons
- ❌ Oublier l'archive Brain (toujours présente, quelle que soit l'option)
