# Slash commands — claude-vault

## Convention

Toute nouvelle slash command Claude Code créée pour un usage personnel doit vivre ici comme **source de vérité**.

## Pourquoi ici et pas directement dans `~/.claude/commands/` ?

- **Versionné** : historique Git de chaque évolution
- **Backup** : pushé sur GitHub (`iconoclasteee/claude-vault`)
- **Synchronisé sur VPS** : les agents peuvent lire les commandes si besoin
- **Partageable** : repo public, facilement partagé

## Mécanisme

Chaque commande est un fichier markdown ici. Un **symlink** dans `~/.claude/commands/` la rend accessible à Claude Code sur ce Mac :

```bash
ln -s ~/ObsidianVaults/Claude/commands/<name>.md ~/.claude/commands/<name>.md
```

Le symlink est transparent pour Claude Code : `/nom-commande` fonctionne exactement comme si le fichier vivait dans `~/.claude/commands/` directement.

## Commandes actuelles

- [`log-cc.md`](log-cc.md) — synthétise une session Claude Code dans le vault Brain
  - Spec : [`log-cc-spec.md`](log-cc-spec.md)
  - Plan d'implémentation : [`log-cc-plan.md`](log-cc-plan.md)
