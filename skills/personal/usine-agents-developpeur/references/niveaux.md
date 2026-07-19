# Niveaux d’orchestration

## Léger

Pour une modification locale, réversible et à faible impact :

- exécution directe ou un implémenteur ;
- tests ciblés et inspection du diff ;
- aperçu si le résultat est visible ;
- pas de reviewer séparé par défaut.

## Standard

Pour plusieurs fichiers ou couches, ou un impact notable :

- brief avec critères d’acceptation ;
- un implémenteur ;
- tests ciblés et non-régression pertinente ;
- revue indépendante ;
- vérification des corrections ;
- démonstration du résultat.

## Renforcé

Pour la sécurité, les opérations difficilement réversibles, les calculs métier
critiques, les exports contractuels ou les changements transverses :

- plan validé avant implémentation ;
- stratégie de retour arrière ;
- implémentation et revue indépendantes ;
- vérification des invariants métier et de sécurité ;
- répétition du chemin critique sur un état représentatif ;
- re-review des corrections bloquantes ;
- validation humaine avant mise en production.

Réévaluer le niveau si de nouveaux risques apparaissent.
