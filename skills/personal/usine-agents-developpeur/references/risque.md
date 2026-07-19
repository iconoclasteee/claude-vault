# Évaluation du risque

Évaluer chaque dimension comme faible, moyenne ou élevée.

| Dimension | Question |
|---|---|
| Impact métier | Une erreur fausse-t-elle une décision, un calcul ou une restitution ? |
| Données | Des données sensibles, réelles ou difficiles à reconstruire sont-elles modifiées ? |
| Sécurité | Authentification, autorisation, secrets ou isolation sont-ils concernés ? |
| Réversibilité | Peut-on revenir en arrière simplement et sans perte ? |
| Étendue | Combien de composants, couches ou consommateurs sont touchés ? |
| Incertitude | Le comportement attendu et les technologies sont-ils bien compris ? |
| Observabilité | Une erreur sera-t-elle rapidement visible ? |
| Couverture | Les tests existants détecteraient-ils une régression ? |

Une dimension élevée interdit le niveau léger et exige une justification du
niveau retenu. La catégorie apparente — UI, CRUD, ETL ou migration — ne détermine
pas le risque.
