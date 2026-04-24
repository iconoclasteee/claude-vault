# Architecture — Claude Code dans ce vault

## Vue d'ensemble

```
/home/<user>/vaultObsidian/          ← Racine du vault (synchronisé Obsidian)
│
├── CLAUDE.md                        ← Lu automatiquement par Claude Code (projet)
│
├── .claude/                         ← Config Claude Code projet (dossier caché)
│   ├── skills/  →  symlink          ← Pointe vers _claude/skills/
│   └── settings.json                ← Hooks, permissions, MCP projet
│
└── _claude/                         ← Visible dans Obsidian (préfixe _ = premier dans tri)
    ├── CLAUDE-global.md             ← Lu par tous les projets (symlink depuis ~/.claude/CLAUDE.md)
    ├── memory/
    │   └── MEMORY.md                ← Chargé auto dans contexte (symlink depuis ~/.claude/projects/.../memory/)
    ├── skills/                      ← Commandes /slash (symlinké depuis .claude/skills/)
    │   ├── README.md
    │   ├── nouvelle-note.md         ← /nouvelle-note
    │   ├── resume-session.md        ← /resume-session
    │   └── cherche.md               ← /cherche
    └── docs/                        ← Ce dossier — documentation de référence
        ├── architecture.md          ← Ce fichier
        └── workflows.md
```

## Symlinks actifs

| Source (physique) | Destination (symlink) |
|-------------------|----------------------|
| `_claude/skills/` | `.claude/skills/` |
| `_claude/CLAUDE-global.md` | `~/.claude/CLAUDE.md` |
| `_claude/memory/` | `~/.claude/projects/-home-<user>-vaultObsidian/memory/` |

## Ordre de lecture des CLAUDE.md par Claude Code

1. `~/.claude/CLAUDE.md` (global → `_claude/CLAUDE-global.md`)
2. `/home/<user>/vaultObsidian/CLAUDE.md` (projet)
3. CLAUDE.md des sous-dossiers si on travaille dedans

## Fichiers de config clés

| Fichier | Rôle | Portée |
|---------|------|--------|
| `_claude/CLAUDE-global.md` | Instructions comportement Claude | Tous projets |
| `CLAUDE.md` | Contexte et conventions du vault | Ce projet |
| `_claude/memory/MEMORY.md` | Mémoire persistante entre sessions | Ce projet |
| `.claude/settings.json` | Hooks, MCP, permissions | Ce projet |
| `_claude/skills/*.md` | Commandes /slash | Ce projet |
