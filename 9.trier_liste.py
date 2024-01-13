"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""

#On import pprint pour faire du débug
from pprint import pprint

#J'ouvre ensuite mon fichier puis je le lie et l'affiche en ligne séparé grâce à read et splitlines
with open("User/exemple/documents/prenom.txt", "r") as f:
    lines = f.read().splitlines()

# Affiche un premier résultat --> pprint(lines)

#Je boucle à travers les lignes, j'ajoute ma liste sans les espaces avec extend à prenom = []
prenoms = []

for line in lines:
    prenoms.extend(line.split())

#J'enlève avec la métode strip ce dont je ne souhaite pas
prenom_finals = [prenom.strip(",. ") for prenom in prenoms]
#On ouvre le fichier puis on écrit les prénoms dedans, on applique un passage à la ligne puis on tri par ordre alphabetique
with open("User/exemple/documents/prenom_final.txt", "w") as f:
    f.write("\n".join(sorted(prenom_finals)))



