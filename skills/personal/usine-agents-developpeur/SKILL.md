---
name: usine-agents-developpeur
description: Préparer et encadrer une activité de développement de code confiée à un ou plusieurs sous-agents. Utiliser avant le premier dispatch d’un implémenteur, reviewer ou agent de correction afin de dimensionner l’orchestration par le risque, isoler les ressources, définir les preuves et sélectionner les REX pertinents. Ne pas utiliser pour une simple réponse, analyse ou modification directe sans sous-agent.
---

# Usine à agents — développement

Avant le premier dispatch, produire les cinq sorties ci-dessous. Ne pas recopier
les références entières dans les briefs : n’injecter que les décisions et points
de vigilance applicables.

## 1. Niveau d’orchestration

Lire `references/risque.md` et `references/niveaux.md`.

Choisir `léger`, `standard` ou `renforcé` et justifier le choix en une phrase.
Une dimension élevée interdit le niveau léger, mais n’impose pas à elle seule
le niveau renforcé. Imposer le niveau renforcé en cas de migration destructive,
irréversibilité importante, exposition de secrets ou atteinte possible aux
données réelles.

## 2. Carte des ressources

Lister chaque ressource modifiable, son propriétaire et son mode d’isolation :

- branche et worktree ;
- fichiers ou documents partagés ;
- base et données de test ;
- ports, serveurs et processus ;
- caches, secrets et environnements distants.

Autoriser les écritures parallèles uniquement si toutes les ressources concernées
sont isolées ou fusionnables. Un worktree isole Git, pas les bases, ports, services
ou fichiers externes.

## 3. Contrat de preuves

Lire `references/preuves.md`. Associer à chaque critère d’acceptation et opération
mutante une preuve attendue dans le rapport. Le rapport synthétise et référence
les artefacts ; il ne remplace ni le diff, ni les tests, ni la preuve d’état.

## 4. Points de vigilance

Lire les déclencheurs de `references/rex.md`. Retenir seulement les entrées dont
le déclencheur correspond au contexte et dont aucune exclusion ne s’applique.
Injecter chaque point uniquement dans le brief concerné.

## 5. Point de démonstration

Définir avant de coder :

- ce qui sera observable ;
- où et comment le vérifier ;
- qui donne le verdict produit ;
- ce qui restera volontairement incomplet.

## Exécution

- Préférer les notifications natives des tâches de fond. Ne jamais lancer une
  boucle de polling non bornée ; permettre un contrôle ponctuel ou borné lorsque
  la notification n’est pas garantie ou qu’un processus survit à l’agent.
- Pour chaque processus long, définir qui le démarre, où vont les logs, comment
  récupérer le résultat et comment garantir sa terminaison.
- Utiliser `APPROVED`, `CHANGES REQUIRED` ou `COMMENT` comme verdicts de revue.
- Exiger une re-review après un finding bloquant ou une correction substantielle.
  Permettre au contrôleur de vérifier un correctif mécanique localisé.
- Pour un fichier également manipulé par un humain ou synchronisé par un service,
  lire `references/harnais-claude.md` ou `references/harnais-codex.md` selon
  l’environnement.

## Clôture

Vérifier le diff et les fichiers non suivis, les tests requis, les processus
résiduels et l’état des opérations mutantes. Donner un résumé en langage produit
et indiquer où observer le résultat. Proposer un REX seulement si un enseignement
généralisable a émergé.
