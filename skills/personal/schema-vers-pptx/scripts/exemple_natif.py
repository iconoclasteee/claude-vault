# -*- coding: utf-8 -*-
"""Exemple minimal de génération native : deux blocs, une flèche, un panneau.

À copier comme point de départ pour un nouveau schéma. Le contenu et la mise en page
sont spécifiques à chaque schéma ; seule la plomberie (pptx_kit) se réutilise.

    python exemple_natif.py
"""
from pptx_kit import Toile

INK, MUTED, DARK, ACCENT = "22303F", "5F6F7E", "12406F", "1B5C96"
BLEU = dict(fond="EEF4FA", ligne="A9C5DF", rappel="7D9CBB", titre=DARK, filet="C2D7E9")
NAVY = dict(fond=DARK, ligne=None, rappel="9DB9D4", titre="FFFFFF", filet="3D6F9F")

t = Toile()                       # 1520 × 855 unités, diapo 16:9
M, BW, BH, BY = 32, 264, 200, 200

t.texte(t.diapo, M, 60, "Un titre de schéma", 25, DARK, gras=True, largeur=1200)
t.filet(t.diapo, M, 80, t.unites - M, DARK, 2)

for i, (rappel, titre, lignes, style) in enumerate([
        ("ÉTAPE 1", "Collecte", [[("30 éléments en ", 0), ("8 familles", 1), (".", 0)],
                                 [("Rien n'est pondéré à ce stade.", 0)]], BLEU),
        ("ÉTAPE 2", "Résultat", [[("Moyenne pondérée", 1), (" des familles.", 0)],
                                 [("Sortie : un score sur 100.", 0)]], NAVY)]):
    x = M + i * (BW + 29)
    g = t.groupe()                                   # 1 groupe = 1 objet déplaçable
    t.bloc(g, x, BY, BW, BH, style["fond"], style["ligne"])
    t.texte(g, x + 18, BY + 26, rappel, 10, style["rappel"], gras=True, spc=1.4)
    t.texte(g, x + 18, BY + 50, titre, 20, style["titre"], gras=True)
    t.filet(g, x + 18, BY + 64, x + BW - 18, style["filet"])
    corps = {False: INK if style is BLEU else "E8F0F8",
             True: ACCENT if style is BLEU else "FFFFFF"}
    for k, ligne in enumerate(lignes):
        t.texte(g, x + 18, BY + 90 + k * 17.5, ligne, 12.4, corps, largeur=BW)
    if i == 0:
        t.pastille(g, x + BW - 18, BY, "Calculé")
        t.fleche(t.diapo, x + BW + 6, BY + BH / 2)

g = t.groupe()
t.bloc(g, M, BY + BH + 30, 2 * BW + 29, 110, "F2F5F8", "D8DEE5")
t.texte(g, M + 18, BY + BH + 52, "ÉTAPE 1", 10, "7D9CBB", gras=True, spc=1.4)
t.texte(g, M + 18, BY + BH + 72, "PARAMÈTRES", 10.5, DARK, gras=True, spc=1.3)
t.texte(g, M + 18, BY + BH + 100, "Une ligne de détail.", 11.5, MUTED, largeur=400)

print(t.enregistre("exemple.pptx"))
