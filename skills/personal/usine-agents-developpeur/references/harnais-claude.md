# Harnais Claude

Appliquer ces points uniquement lorsque l’environnement Claude les prend en charge.

- Utiliser le mécanisme natif de notification des sous-agents. Ne pas supposer
  qu’une commande externe lancée par un agent se termine avec l’agent.
- Conserver les briefs, résultats structurés et chemins de preuves dans des
  artefacts persistants lorsque le travail doit survivre à une compaction.
- Ne pas faire dépendre le workflow d’un nom de modèle, d’une limite d’abonnement
  ou d’un chemin interne de plugin susceptible de changer.
- Pour un fichier OneDrive, SharePoint ou un document ouvert par un humain,
  vérifier les verrous et risques de synchronisation exigés par le format,
  sauvegarder avant une transformation risquée et regrouper les écritures avant
  de demander la validation humaine.
