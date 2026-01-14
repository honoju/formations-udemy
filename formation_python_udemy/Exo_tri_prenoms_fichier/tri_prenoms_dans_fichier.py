"""
Ce qui est fait:
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""

from pathlib import Path
import re

NOM_FICHIER = "prenoms.txt"
NOM_FICHIER_TRIE = "prenoms_tries.txt"
DOSSIER_COURANT = Path.cwd()
fichier = DOSSIER_COURANT / NOM_FICHIER
fichier_trie = DOSSIER_COURANT / NOM_FICHIER_TRIE

''' With regex (more generic)'''
# with fichier.open("r", encoding="utf-8") as f:
#     texte = f.read()
#     prenoms = re.findall(r'[^\W\d_]+(?:-[^\W\d_]+)*', texte)
#     prenoms.sort()

# with fichier_trie.open("w", encoding="utf-8") as f_trie:
#     for prenom in prenoms:
#         f_trie.write(prenom + '\n')


''' Instructor code (less generic, more pythonic, more use of text functions)'''
with fichier.open("r", encoding="utf-8") as f:
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_tries = [prenom.strip(", ") for prenom in prenoms]

with fichier_trie.open("w", encoding="utf-8") as f_trie:
    f_trie.write("\n".join(sorted(prenoms_tries)))