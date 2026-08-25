<!-- Généré par OS-agentic/Socle/bin/install-local-rules. Ne pas éditer directement. -->

# Règles locales — vault Claude public

Ce dépôt est public. Toute création, modification ou validation doit respecter
`SECURITY.md` et les contrôles Git du dépôt.

## Interdictions

- Ne jamais publier de chemin absolu contenant un nom d'utilisateur.
- Ne jamais publier d'adresse email personnelle, hostname, alias SSH ou adresse IP.
- Ne jamais publier de secret, token, mot de passe, clé privée ou contenu de fichier `.env`.
- Ne jamais publier de nom de client privé ni de contenu interne à une mission.

## Substitutions

- Utiliser `~/` pour un chemin sous le répertoire personnel.
- Utiliser `<user>`, `<host>`, `<vps-host>`, `<ip>`, `<email>` et `<TOKEN>` dans les exemples.

## Vérification

- Auditer particulièrement les commandes shell et les ajouts Git avant commit.
- Ajouter uniquement les fichiers concernés ; ne jamais utiliser un ajout global par
  commodité.
- En cas de doute sur le caractère publiable d'une information, ne pas la committer.
- Si un secret a été exposé, le considérer compromis même après réécriture de l'historique
  et demander sa rotation.
