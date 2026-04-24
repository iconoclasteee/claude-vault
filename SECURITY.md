# Règles d'écriture sécurisée — Vault Claude public

## Contexte

Le repo `iconoclasteee/claude-vault` est **public sur GitHub**. Tout contenu committé peut être lu, indexé, cloné, mis en cache par des outils tiers. Le repo est volontairement public (vitrine de compétence Claude Code). Cela impose une discipline d'écriture stricte.

## Règles absolues — NE JAMAIS écrire ces patterns

### Identifiants personnels
- Chemin absolu Mac : `<user-mac-path>/` → utiliser `~/` (préféré) ou `/Users/<user>/` (placeholder)
- Chemin absolu VPS : `<user-linux-path>/` → utiliser `~/` ou `/home/<user>/`
- Username macOS nu (`<user>`) en dehors d'un chemin
- Email : `<email>` → utiliser `<email>`
- Prénom + nom complet associé à une machine/serveur

### Infrastructure
- Alias SSH : `<vps-host>` → utiliser `<vps-host>`
- IPs publiques ou privées (`10.x.x.x`, `192.168.x.x`, IPs de prod)
- Hostnames résolvables par DNS
- Ports internes non-publics
- Empreintes SSH / clés publiques serveur

### Secrets — absolument jamais, même expirés
- Tokens API : GitHub `ghp_*` `ghs_*` `gho_*`, Anthropic `sk-ant-*`, Slack `xoxb-*` `xoxp-*`, AWS `AKIA*`
- Mots de passe, même en exemple de test
- Clés privées : SSH (`BEGIN OPENSSH PRIVATE KEY`), PGP, TLS
- Contenu de fichiers `.env`, `.secrets/`, `.credentials.json`

### Données sensibles par contexte
- Noms de clients / projets privés
- Chemins de fichiers sur serveurs non-publics
- Adresses postales, numéros de téléphone
- Infos financières

## Règles préventives — à appliquer AVANT écriture

1. **Pense à l'audience** : imagine un recruteur qui parcourt ton GitHub. Ce que tu écris est-il valorisant pour lui **sans rien révéler** ?
2. **Préfère les placeholders** : `~/` avant `<user-mac-path>/`, `<vps-host>` avant `<vps-host>`, `<user>` avant `<user>` ou `ubuntu`
3. **Les exemples de commande sont le vecteur principal de fuite** : relis toutes les commandes shell avant commit
4. **Évite les triples corrélations** : username + email + hostname dans un même fichier = identification certaine, même si chaque élément pris isolément semble anodin
5. **En cas de doute, abstiens-toi** : "je ne suis pas sûr que cette info doit être publique" > la committer par réflexe

## Garde-fous automatiques en place

### `scripts/hooks/pre-commit`
Hook git versionné qui bloque les commits contenant les patterns critiques. Activation par clone :
```bash
git config core.hooksPath scripts/hooks
```
Les patterns exacts sont listés en haut de `scripts/hooks/pre-commit`. Tenir cette liste à jour.

### `.gitignore`
Ignorer les fichiers contenant intrinsèquement des infos privées :
- `.DS_Store` (métadonnées Finder)
- `memory` (symlink vers `~/.claude/memory/` privé)
- Workspace Obsidian
- Tout fichier `.local.*`, `.secrets*`

## Procédure en cas de fuite accidentelle

Si un identifiant personnel est committé et pushé :

1. **Arrêter** : ne pas enchaîner d'autres commits
2. **Corriger HEAD** : edit + `git commit --amend` ou nouveau commit
3. **Nettoyer l'historique** : `git filter-repo --replace-text /path/to/replacements.txt --force`
4. **Force push** : `git push --force origin main`
5. **Noter** : ajouter le pattern à `scripts/hooks/pre-commit` si ce n'était pas couvert

Les tokens / secrets doivent en plus être **rotés côté provider** — le filter-repo ne les rend pas invalides, il les cache seulement.

## À qui s'appliquent ces règles

- À **Claude** quand il crée ou édite un fichier dans `~/ObsidianVaults/Claude/` (Mac) ou `~/vaults/Claude/` (VPS)
- À **Olivier** quand il édite à la main
- Au plugin **obsidian-git** dont les auto-commits sont soumis au pre-commit hook

Ces règles ne s'appliquent **pas** à `~/ObsidianVaults/Brain/` (vault privé, repo séparé, pas public) ni à `~/.claude/memory/` (hors vault).
