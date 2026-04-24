# Git hooks — claude-vault

Hooks versionnés pour éviter qu'un identifiant personnel ne parte sur GitHub public.

## Installation (une fois par clone)

```bash
git config core.hooksPath scripts/hooks
```

C'est tout. Les hooks s'exécuteront désormais automatiquement.

## Hooks présents

### `pre-commit`

Tourne avant chaque commit. Scanne les lignes **ajoutées** (pas celles modifiées par ailleurs) dans les fichiers en cours de commit. Bloque si un pattern de la liste est détecté.

Patterns surveillés (éditables en haut du script) :

- Chemins persos : `<user-mac-path>`, `<user-linux-path>`, `<vps-host>`
- Email : `<email>`
- Tokens : `ghp_...` (GitHub), `sk-ant-...` (Anthropic), `xoxb-...` (Slack), `AKIA...` (AWS)

## Bypasser un bloquage (à éviter)

Si un pattern est légitime et volontaire :

```bash
git commit --no-verify
```

À n'utiliser qu'en connaissance de cause.
