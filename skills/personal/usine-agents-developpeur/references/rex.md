# Catalogue REX — développement avec des agents

Les REX éclairent la décision ; ils ne s’appliquent jamais automatiquement.
La provenance détaillée reste dans la mémoire privée. Ce fichier public ne contient
que des distillats génériques et, si disponible, un identifiant privé opaque.

Statuts : `candidate`, `validated`, `deprecated`, `rejected`.
Confiance : `faible`, `moyenne`, `élevée`.

## REX-001 — Isoler les suites de tests mutantes

- **Déclencheur :** plusieurs suites peuvent modifier les mêmes données.
- **Exclusions :** suites en lecture seule ou exécution strictement séquentielle.
- **Statut :** validated
- **Confiance :** élevée
- **Enseignement :** isoler par base, schéma, transaction, namespace ou
  séquencement explicite.
- **Preuve attendue :** exécutions concurrentes répétées sans interférence.

## REX-002 — Vérifier l’état produit

- **Déclencheur :** migration, seed, import, déploiement ou script d’administration.
- **Exclusions :** opération purement calculatoire sans effet externe.
- **Statut :** validated
- **Confiance :** élevée
- **Enseignement :** contrôler l’état métier obtenu en plus du succès technique.
- **Preuve attendue :** version, comptage, échantillon ou ressource réellement servie.

## REX-003 — Contrôler la structure avant de conclure à une absence métier

- **Déclencheur :** extraction depuis un classeur, CSV ou document semi-structuré.
- **Exclusions :** format contractuel validé automatiquement par un schéma.
- **Statut :** validated
- **Confiance :** moyenne
- **Enseignement :** vérifier en-têtes, version, marqueurs conventionnels et cellules
  sources avant de qualifier un trou de données.

## REX-004 — Gérer le cycle de vie des processus longs

- **Déclencheur :** serveur de développement, navigateur E2E, watcher ou tâche de fond.
- **Exclusions :** commande synchrone courte dont la terminaison est garantie.
- **Statut :** candidate
- **Confiance :** moyenne
- **Enseignement :** attribuer un propriétaire, un canal de résultat, des logs bornés
  et une procédure de terminaison.
- **Limite :** les processus résiduels peuvent être un facteur contributif sans être
  la cause unique d’un incident.

## REX-005 — Ne pas confondre revue statique et validation produit

- **Déclencheur :** fonctionnalité UI avec volume ou interaction significatifs.
- **Exclusions :** changement interne sans effet perceptible.
- **Statut :** validated
- **Confiance :** moyenne
- **Enseignement :** compléter la revue du code par une interaction représentative
  et un passage produit au jalon convenu.

## REX-006 — Réserver « cause racine » aux causes confirmées

- **Déclencheur :** diagnostic d’un incident potentiellement multifactoriel.
- **Exclusions :** aucune.
- **Statut :** validated
- **Confiance :** moyenne
- **Enseignement :** distinguer observation, hypothèse, facteur contributif et cause
  confirmée par reproduction ou expérience comparative.

## REX-007 — Le coût de coordination peut dépasser le risque couvert

- **Déclencheur :** le workflow prévoit plusieurs agents, revues, re-revues ou
  handoffs pour des tâches locales ou facilement réversibles.
- **Exclusions :** sécurité, migration destructive, données sensibles, logique métier
  critique ou exigence réglementaire justifiant cette séparation.
- **Statut :** candidate
- **Confiance :** moyenne
- **Enseignement :** avant d’exécuter un pipeline proposé, comparer son coût de
  coordination aux risques concrets qu’il couvre et proposer une version plus simple.
- **Signal observable :** davantage de relances, rapports, attentes et reprises
  d’état que de modifications ou de validations utiles.
- **Limite :** le nombre d’étapes ne suffit pas à conclure ; une tâche courte peut
  néanmoins exiger une séparation forte des responsabilités.

## Maintenance

Lors d’un REX :

1. Extraire incidents, corrections et décisions observables.
2. Séparer faits, hypothèses, causes confirmées et décisions.
3. Rechercher les entrées existantes apparentées.
4. Évaluer portée, preuve, limites, contre-exemples et conséquences hors contexte.
5. Présenter les propositions par lot avec une recommandation motivée.
6. Après validation, ajouter, fusionner, reformuler, déprécier ou rejeter.
7. Ne jamais augmenter la confiance sur le seul nombre de mentions.
8. Réexaminer les entrées anciennes, absolues, contradictoires ou obsolètes.
9. Conserver la provenance sensible dans un espace privé.
10. Consigner la date, la décision et la raison de chaque évolution.

Au-delà d’environ quinze entrées actives, déclencher une revue de structure sans
supprimer une distinction utile uniquement pour respecter ce seuil.
