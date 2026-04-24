---
name: rappelle-toi
description: Recharge du contexte depuis le vault Brain dans la session courante. Trois modes — sans argument (liste à choisir), mot-clé (recherche + choix), chemin(s) (lecture directe). À utiliser quand l'utilisateur tape /rappelle-toi ou dit "rappelle-toi", "recharge", "relis".
---

# /rappelle-toi — Hydratation de contexte depuis le vault

## Quand déclencher

- L'utilisateur tape `/rappelle-toi [args]`
- L'utilisateur dit "rappelle-toi...", "recharge...", "relis la note...", "ressort le MOC..."

## Modes d'invocation

### Mode 1 — Sans argument
`/rappelle-toi`
→ Lister :
- Les 5 derniers fichiers modifiés de `Brain/01 Journal/Claude code/` (tri par date décroissante)
- Tous les MOC existants dans `Brain/04 MOC/`

Présenter sous forme de liste numérotée. Demander : "Lequel / lesquels charger ?"

### Mode 2 — Mot-clé
`/rappelle-toi <mot-clé>`
→ Grep (case-insensitive) dans cet ordre de priorité :
1. `Brain/01 Journal/Claude code/`
2. `Brain/12 Domaines/AI/`
3. `Brain/04 MOC/`
4. `Brain/11 Projets/`
5. `Brain/03 Notes/`

Remonter les 5 meilleurs matchs (par pertinence : nombre d'occurrences, position dans le titre, récence). Demander lesquels charger.

### Mode 3 — Chemin(s)
`/rappelle-toi <chemin1> [<chemin2>...]`
→ Lire directement les fichiers spécifiés. Support multi-fichiers séparés par espace.
Les chemins peuvent être relatifs à `Brain/` ou absolus.

## Règles de chargement

- **Cap : 3 fichiers max par appel**. Au-delà, demander à l'utilisateur de restreindre.
- **Annoncer ce qui est chargé** avant de poursuivre : "J'ai rechargé : [[IA]] (MOC, 42 lignes) et [[2026-04-23 — Session Next.js]] (journal, 120 lignes)."
- **Extraction intelligente** pour les fichiers > 200 lignes : lire la totalité, mais ne recracher dans le chat que les passages liés au mot-clé ou au contexte de la conversation. Garder le reste en contexte pour questions ultérieures.
- **Wikilinks transitifs** : si une note chargée référence `[[X]]` et que X semble critique à la question en cours, signaler "la note référence aussi [[X]] — tu veux que je la charge aussi ?"

## Exemples

- `/rappelle-toi`
  → "Derniers journaux Claude code : [1] 2026-04-24 11h54 — Setup sync vaults... [2] ... MOC disponibles : [A] IA.md, [B] Projets.md ... Quels éléments ?"

- `/rappelle-toi prisma`
  → Grep trouve 3 notes : `AI/2026-04-24 — Préférence ORM Prisma.md`, `11 Projets/Saveurs/schema.md`, `01 Journal/Claude code/2026-04-20 — migration prisma.md`. "3 matchs, lesquels ?"

- `/rappelle-toi "04 MOC/IA.md" "11 Projets/Saveurs/README.md"`
  → Charge les deux, annonce le chargement, répond à la question suivante avec ce contexte.

## Anti-patterns

- ❌ Charger > 3 fichiers sans demander
- ❌ Recracher le contenu intégral dans le chat — résumer / extraire
- ❌ Ne pas annoncer ce qui a été chargé (l'utilisateur doit savoir ce qui est entré en contexte)
- ❌ Ignorer les wikilinks sortants pertinents
