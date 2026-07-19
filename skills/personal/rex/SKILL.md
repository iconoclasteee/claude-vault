---
name: rex
description: Conduire un retour d’expérience après un incident notable, en fin de chantier ou lors d’une revue périodique de pratiques de développement. Extraire les faits et leçons généralisables, les confronter au catalogue de l’usine à agents, puis proposer des ajouts, fusions, reformulations, dépréciations ou rejets sans écrire avant validation de l’utilisateur.
---

# REX — développement avec des agents

Localiser la skill `usine-agents-developpeur` disponible dans l’environnement et
lire `references/rex.md`. Si elle est introuvable, signaler le problème et produire
uniquement des propositions sans mise à jour.

## Sources

Analyser :

- la conversation et les artefacts du chantier ;
- les journaux ou mémoires privées explicitement accessibles ;
- le catalogue REX existant.

Ne jamais publier de nom de client, projet privé, chemin personnel, identifiant,
secret ou détail permettant une corrélation.

## Méthode

1. Extraire les observations, corrections et décisions vérifiables.
2. Séparer faits, hypothèses, facteurs contributifs et causes confirmées.
3. Écarter les bugs ponctuels sans enseignement transférable.
4. Dédupliquer contre les entrées existantes.
5. Pour chaque candidat, proposer :
   - déclencheur et exclusions ;
   - statut et confiance ;
   - enseignement ;
   - preuve disponible ;
   - limites et contre-exemples ;
   - provenance privée opaque, si elle existe.
6. Présenter les changements par lot avec recommandation.
7. Ne rien écrire avant validation explicite de l’utilisateur.
8. Après validation, mettre à jour le catalogue et son index éventuel.

Le nombre de mentions ou d’occurrences ne suffit jamais à augmenter la confiance.
Réviser aussi les entrées anciennes : un REX peut être fusionné, déprécié ou rejeté.

## Sortie

Donner :

- le nombre de candidats retenus et écartés ;
- le diff conceptuel proposé ;
- les décisions attendues de l’utilisateur ;
- après écriture autorisée, le bilan des entrées ajoutées, modifiées ou retirées.
