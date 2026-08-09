---
name: schema-vers-pptx
description: Utiliser quand un schéma doit arriver dans PowerPoint en formes éditables — conversion d'un SVG existant ou dessin natif — ou quand un PPTX généré sort avec du texte noir illisible sur fond sombre, des textes qui débordent de leur bloc, des retours à la ligne parasites, une ombre portée non voulue, ou des dizaines de formes libres impossibles à déplacer.
---

# Schéma vers PowerPoint

Amener un schéma vers PowerPoint en **formes natives éditables**, jamais en image.
Outils dans `scripts/`, à côté de ce fichier : `svg_vers_pptx.py` (conversion),
`pptx_kit.py` (dessin natif), `exemple_natif.py` (point de départ).

## Environnement — à faire avant tout

`pip install` sur le Python système **échoue** sur macOS/Homebrew (PEP 668,
`externally-managed-environment`). Il faut un venv, et l'appeler par son chemin
absolu — `python` n'existe pas toujours, seulement `python3` :

```bash
python3 -m venv ~/.venvs/svg2pptx
~/.venvs/svg2pptx/bin/pip install svg2pptx python-pptx lxml
```

LibreOffice (`soffice` dans le PATH) est requis pour le PDF de contrôle.

## Choisir le chemin

| | Conversion depuis SVG | Dessin natif |
|---|---|---|
| Coût | une commande | un script par schéma, ~300 lignes |
| Formes | libres, non groupées | un groupe par bloc |
| Interlettrage | perdu | conservé |

**Conversion par défaut.** Le natif se justifie quand quelqu'un reprendra la mise en
page à la souris : déplacer un bloc parmi 137 formes libres est pénible, parmi 15
groupes c'est un clic.

```bash
~/.venvs/svg2pptx/bin/python <dossier-de-cette-skill>/scripts/svg_vers_pptx.py \
    mon-schema.svg --pdf
```
`--pdf` écrit le PDF de contrôle **à côté du PPTX**, sans redirection possible : dans
un dossier de l'utilisateur, prévenir ou nettoyer ensuite.

## Lire la sortie du script

`47/47 lignes recolorées, 1 débordement(s) rentré(s)`

- **`N/M`** : `M` = lignes à styles multiples trouvées dans le SVG, `N` = celles
  retrouvées et réparées dans le PPTX. **`N = M` est le seul résultat acceptable** ;
  un écart signale des lignes restées en noir, le script le dit alors explicitement.
- **débordements rentrés** : informatif, aucune action. Zones de texte estimées trop
  larges par svg2pptx, rognées au bord de la diapo.
- **`⚠ ligne ambiguë`** : deux lignes de même texte à la même abscisse. Les couleurs
  peuvent être inverties entre les deux — vérifier ces lignes précises au rendu.

## Les pièges — aucun ne lève d'erreur

| Piège | Symptôme au rendu | Traitement |
|---|---|---|
| `<tspan>` ignorés par svg2pptx | texte à styles multiples entièrement noir ; sur fond sombre, illisible | le script relit le SVG et reconstruit les runs |
| Corps de police 4/3 trop grands | textes débordant des blocs, chevauchements, retours à la ligne | facteur 0,75 sur chaque run |
| Pile de polices CSS transmise telle quelle | PowerPoint ne trouve pas `Inter, 'Segoe UI', …`, retombe sur son thème | un nom de police unique et réel |
| `<a:effectRef>` du thème | ombre portée non voulue ; `shadow.inherit = False` **ne suffit pas** | neutraliser aussi `effectRef` |
| SVG large sur diapo 16:9 | bande blanche en bas | centrage vertical |

## Vérifier — l'étape qu'on ne saute pas

Un script qui annonce « 47/47 » ne dit rien du rendu : il ignore ce que le schéma est
censé montrer. Les pièges les plus coûteux ci-dessus ont été trouvés à l'œil.

**Produire le PDF (`--pdf`) et le lire avec l'outil Read**, qui rend les pages de PDF
directement — pas besoin de rasteriser, ni de passer par `qlmanage` (qui sort une
vignette carrée recadrée, inutilisable).

À constater, dans cet ordre :
1. **Un bloc à fond sombre garde-t-il son texte clair ?** C'est le piège n°1 en action.
   S'il n'y a aucun fond sombre dans le schéma, le dire — le piège n'était pas atteignable.
2. Aucun texte ne déborde de son bloc, aucun retour à la ligne parasite.
3. Aucune ombre portée sur les blocs.
4. Les couleurs des fonds sont celles du SVG.
5. **Attendu, pas un défaut** : l'interlettrage des petites capitales a disparu, et la
   police est substituée.

LibreOffice n'est qu'un contrôle intermédiaire. Pour un livrable qui circule, ouvrir
dans PowerPoint avant diffusion — les métriques de police diffèrent.

## Générer un SVG destiné à être converti

- couleur explicite sur **chaque** `<tspan>`, jamais héritée du `<text>` parent ;
- aucune information portée par l'interlettrage — il ne survit pas ;
- un `<text>` par ligne, `x` explicite, pas de retour à la ligne implicite ;
- éviter deux lignes de texte identique à la même abscisse (ambiguïté de réparation) ;
- un `<g>` par bloc logique si le groupement compte.
