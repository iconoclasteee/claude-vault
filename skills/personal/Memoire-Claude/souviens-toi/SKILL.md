---
name: souviens-toi
description: Archive une information en mémoire persistante — écrit à la fois dans ~/.claude/memory/ (cache rapide Claude Code) et dans Brain/12 Domaines/AI/ (archive longue du vault). À utiliser quand l'utilisateur tape /souviens-toi ou dit "souviens-toi que", "retiens que", "garde en mémoire".
---

# /souviens-toi — Archivage mémoire persistante

## Quand déclencher

- L'utilisateur tape `/souviens-toi <contenu>`
- L'utilisateur dit "souviens-toi que...", "retiens que...", "garde en mémoire..."

## Workflow

1. **Classifier l'info** selon les types du système memory auto :
   - `user` — rôle, préférences, expertise d'Olivier
   - `feedback` — correction ou validation d'une approche
   - `project` — fait daté, décision, deadline
   - `reference` — pointeur externe (Linear, Grafana, etc.)

2. **Écrire dans `~/.claude/memory/`** via le système memory auto standard (fichier dédié + pointeur dans `MEMORY.md`). Respecter le format frontmatter `name/description/type`.

3. **Pousser dans le vault** dans `~/ObsidianVaults/Brain/12 Domaines/AI/` :
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
     ---
     ```
   - Utiliser `[[WikiLinks]]` vers les notes existantes pertinentes

4. **Confirmer à l'utilisateur** les deux destinations : "Mémorisé dans `~/.claude/memory/<fichier>.md` et dans `Brain/12 Domaines/AI/<fichier>.md`."

## Exemples

- `/souviens-toi je préfère Prisma à Drizzle pour l'ORM`
  → memory type `user` + note `Brain/12 Domaines/AI/2026-04-24 — Préférence ORM Prisma.md`
- `/souviens-toi la deadline du projet Saveurs est le 2026-06-15`
  → memory type `project` + note AI/ liée à `[[Saveurs]]`
- `/souviens-toi ne pas mocker la base dans les tests — on s'est fait avoir au dernier projet`
  → memory type `feedback` + note AI/ avec le "pourquoi"

## Anti-patterns

- ❌ Archiver du bruit ponctuel (erreurs de debug, état temporaire de session)
- ❌ Créer une note AI/ sans vérifier les doublons
- ❌ Frontmatter hors doctrine Brain
- ❌ Oublier de pousser dans l'un des deux systèmes
