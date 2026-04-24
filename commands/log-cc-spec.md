# Spec — Slash command `/log-cc`

**Status** : design validated 2026-04-24 — implementation en cours
**Auteur** : brainstorming Olivier / Claude

## 🎯 Objectif

Permettre à Olivier de **synthétiser une session Claude Code** dans son second brain (vault Brain) en une seule commande, avec preview en terminal et possibilité de régénérer à la demande.

## 📦 Livrables

1. **Slash command** `~/.claude/commands/log-cc.md` → symlink vers la source
2. **Source de vérité** `~/ObsidianVaults/Claude/commands/log-cc.md`
3. **README** `~/ObsidianVaults/Claude/commands/README.md` décrivant la convention "toute slash command vit dans claude-vault comme source de vérité"
4. **Correction** de `~/ObsidianVaults/Claude/CLAUDE.md` (chemins Brain obsolètes)

## 🕹️ Usage

```
/log-cc                  # topic auto-détecté par Claude
/log-cc <topic custom>   # topic imposé par l'utilisateur
```

Exemple :
```
/log-cc Setup sync vaults
```

## 🔄 Flow d'exécution

1. Claude lit les instructions du fichier `log-cc.md`
2. Claude synthétise la **conversation actuelle depuis le début** en 7 sections, dans l'ordre :
   - **Résumé** (ton synthétique, pas "aujourd'hui")
   - **Décisions clés**
   - **Apprentissages**
   - **Problèmes + solutions**
   - **À faire**
   - **Commandes importantes**
   - **Fichiers touchés**
3. Claude détermine le topic :
   - Si argument passé : le prend tel quel
   - Sinon : auto-détection = un titre synthétique de 3 à 6 mots qui capture l'action principale de la session (ex: "Setup sync vaults", "Debug cron expired token", "Refacto dossiers PARA")
4. Claude scanne `~/ObsidianVaults/Brain/03 Notes/` et `~/ObsidianVaults/Brain/04 MOC/` pour trouver 1 à 3 notes existantes pertinentes au topic, à lier via `[[WikiLinks]]`
5. Claude écrit le fichier dans `~/ObsidianVaults/Brain/01 Journal/Claude code/YYYY-MM-DD HHhMM — <topic>.md` (crée le dossier si absent)
6. Claude affiche le contenu complet dans le terminal pour preview
7. Olivier peut répondre :
   - **"ok"** ou rien → on s'arrête
   - **"refais plus court"**, **"enlève la section Décisions"**, **"ajoute X"** → Claude régénère et écrase le fichier

## 📝 Format du fichier de sortie

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
[Ton synthétique, 2-5 phrases. Pas "aujourd'hui"]

## Décisions clés
- ...

## Apprentissages
- ...

## Problèmes rencontrés
- **Problème** : ...
  - **Solution** : ...

## À faire
- [ ] ...

## Commandes importantes
\`\`\`bash
...
\`\`\`

## Fichiers touchés
- `chemin` — nature du changement

## Liens
- [[Note 1]] — pourquoi pertinente
- [[Note 2]] — pourquoi pertinente
```

## 🧩 Règles / edge cases

| Cas | Règle |
|---|---|
| Section vide (rien à dire) | Claude omet la section (pas de placeholder type "*(rien)*") |
| Dossier `01 Journal/Claude code/` absent | Claude le crée |
| Fichier cible existe déjà (même minute) | Claude ajoute suffixe `-2`, `-3`, etc. |
| Aucune note Brain pertinente trouvée | Claude omet la section "Liens" |
| Argument topic contient des caractères invalides pour nom de fichier (`/`, `:`, etc.) | Claude remplace par `-` ou supprime |

## 🏗️ Architecture

### Source de vérité unique via symlink

```
~/.claude/commands/log-cc.md  ─→ symlink vers ─→  ~/ObsidianVaults/Claude/commands/log-cc.md
```

**Bénéfices** :
- 1 seul fichier à maintenir
- Versioné Git (dans claude-vault)
- Sync automatique GitHub + VPS via l'architecture existante
- L'historique Git = historique d'évolution de la commande

### Convention pour les futures commandes/skills

Toute nouvelle slash command doit vivre dans `~/ObsidianVaults/Claude/commands/` comme source de vérité. Le symlink vers `~/.claude/commands/` est créé au moment du déploiement. Idem pour les skills dans `skills/personal/`.

## ⚠️ Risques identifiés et parades

| Risque | Parade |
|---|---|
| Le vault Claude disparaît / est déplacé | Symlink cassé. Regénérer le symlink vers le nouveau chemin |
| Synthèse de mauvaise qualité | Pattern "write + preview + regenerate" : Olivier peut demander des corrections avant de fermer la session |
| Session très longue (500+ messages) | La synthèse reste possible mais risque d'être dense. Pas de mitigation dans la v1 (YAGNI) |
| Fichier pollué par une mauvaise synthèse commise par Git avant correction | Le plugin Obsidian Git commit toutes les 10 min. Fenêtre courte. Olivier régénère dans les secondes, pas minutes. Acceptable |

## ✅ Validation post-implémentation

- [ ] `ls -la ~/.claude/commands/log-cc.md` → montre un symlink vers le vault Claude
- [ ] Lancer `/log-cc` dans une session → crée bien un fichier dans `Brain/01 Journal/Claude code/`
- [ ] Preview s'affiche dans le terminal
- [ ] "refais plus court" → régénère et écrase le fichier
- [ ] Fichier synchronisé sur GitHub (via plugin Obsidian Git)
- [ ] Fichier sync sur VPS (via cron `sync-vault.sh`)

## 🚫 Hors scope (YAGNI)

- Synthèse d'une tranche précise (ex: "les 30 derniers messages") → v2 si besoin
- Auto-déclenchement via hook SessionEnd → non voulu (user voulait manuel)
- Multi-fichiers (par thème) → non voulu (une session = un fichier)
- Intégration dans le graphe Obsidian au-delà des WikiLinks manuels → natif à Obsidian, rien à faire
