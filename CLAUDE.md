# Contexte global — Olivier

## Vault Claude PUBLIC — règles de sécurité

Ce dossier est **versionné dans un repo GitHub public**. Toute création ou édition de fichier ici DOIT respecter les règles de [SECURITY.md](SECURITY.md), chargé ci-dessous.

Réflexe : aucun identifiant personnel (chemin absolu contenant un username, email, hostname, alias SSH, IP, token). Utiliser les placeholders `~/`, `<user>`, `<vps-host>`, `<email>`. En cas de doute, ne pas committer.

@SECURITY.md

## Profil
- Vibe coder qui utilise Claude Code au quotidien
- Mac + iPhone, travaille principalement en français
- Projets : développement web (Next.js, TypeScript, Prisma, PostgreSQL)

## Vault Brain
- Chemin : ~/ObsidianVaults/Brain/
- Second brain personnel (PARA + Zettelkasten + MOC)
- Toute note créée dans Brain doit avoir le frontmatter standard (title, date, tags, status, source)
- Utiliser les WikiLinks [[Note]] pour relier les notes entre elles
- Les nouvelles captures vont dans Brain/00 Inbox/ par défaut
- Structure : `0X` pour les flux Zettelkasten (00 Inbox, 01 Journal, 02 Briefs, 03 Notes, 04 MOC), `1X` pour PARA (11 Projets, 12 Domaines, 13 Ressources, 14 Archive). Voir `Brain/README.md` pour la doctrine complète.

## Conventions
- Langue : français sauf si explicitement demandé en anglais
- Frontmatter : toujours présent sur les notes créées dans Brain
- WikiLinks : toujours préférés aux liens Markdown pour les notes internes
- Tags : format type/xxx et domaine/xxx

## Skills disponibles (chargés depuis Brain/.claude/)
- obsidian-markdown : syntaxe Obsidian exacte
- obsidian-cli : interaction avec l'app Obsidian ouverte
- obsidian-bases : vues dynamiques .base
- json-canvas : fichiers canvas valides
- defuddle : extraction propre d'articles web
