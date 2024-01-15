from pathlib import Path

chemin = ("Exemple/exemple")
 
d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}
#Je boucle grâce à items sur mes clés et valeurs que je récupère dans les variables dossier_principal et sous_dossier
for dossier_principal, sous_dossier in d.items():
#On boucle à travers les valeurs
    for dossier in sous_dossier:
#On créer un chemin puis on concatène
        chemin_dossier = Path(chemin) / dossier_principal / dossier
#On créer ensuite les dossiers à l'aide de mkdir (parents pour créer une structure de dossier)
        chemin_dossier.mkdir(exist_ok=True, parents=True)
