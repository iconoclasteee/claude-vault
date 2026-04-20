# Workflows — Bonnes pratiques avec Claude Code

## Démarrer une session

1. Claude lit automatiquement `~/.claude/CLAUDE.md` + `CLAUDE.md` au démarrage
2. La mémoire `_claude/memory/MEMORY.md` est chargée dans le contexte
3. Les skills `/slash` sont disponibles immédiatement

## Ajouter une instruction permanente

**Pour ce projet uniquement :** Éditer `CLAUDE.md` (racine du vault)
**Pour tous les projets :** Éditer `_claude/CLAUDE-global.md`

## Créer un nouveau skill /slash

1. Créer `_claude/skills/mon-skill.md`
2. Le skill est immédiatement disponible comme `/mon-skill`
3. Documenter dans `_claude/skills/README.md`

## Sauvegarder quelque chose en mémoire

Dire à Claude : *"Mémorise que..."* ou *"Souviens-toi que..."*
Claude mettra à jour `_claude/memory/MEMORY.md`.

## Consulter ce que Claude sait

Lire `_claude/memory/MEMORY.md` depuis Obsidian ou demander :
*"Qu'est-ce que tu as en mémoire sur ce projet ?"*

## Configurer un hook (action automatique)

Éditer `.claude/settings.json` :

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Fichier modifié : $CLAUDE_TOOL_INPUT'"
          }
        ]
      }
    ]
  }
}
```

Types de hooks disponibles : `PreToolUse`, `PostToolUse`, `Notification`, `Stop`

## Ajouter un serveur MCP

Dans `.claude/settings.json` :

```json
{
  "mcpServers": {
    "nom-serveur": {
      "command": "commande",
      "args": ["arg1"],
      "env": { "VAR": "valeur" }
    }
  }
}
```

## Mettre à jour les instructions globales

Éditer `_claude/CLAUDE-global.md` depuis Obsidian — le changement s'applique
immédiatement à la prochaine session Claude Code (n'importe quel projet).
