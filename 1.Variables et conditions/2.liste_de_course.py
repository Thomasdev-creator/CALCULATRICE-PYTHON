#import de sys pour quitter le programme
import sys
#import du module os et json
import os
import json

#On récupère le dossier actuel avec le chemin complet vers notre script grâce à file
CUR_DIR = os.path.dirname(__file__)
#On concatène le dossier parent avec le fichier liste.json
LISTE_path = os.path.join(CUR_DIR, "liste.json")

'''On vérifie l'existence de la liste sur le disque, puis si l'existe on lit son 
contenue au format json, si il n'existe pas on l'initialise à une liste vide avec else'''

if os.path.exists(LISTE_path):
    with open(LISTE_path, "r") as f:
        LISTE = json.load(f)

else:
    LISTE = []

#Déclaration de la liste qui sera complété par l'utilisateur
#LISTE = []

#Déclaration du menu
MENU = """Choisissez parmi les 5 options suivantes:
1: Ajouter
2: Retirer
3: Afficher
4: Vider
5: Quitter
? Votre choix : """

#Liste de choix
CHOIX = ["1", "2", "3", "4", "5"]

#boucle
while True: 
    user_choice = input(MENU)
    if user_choice not in CHOIX:
        print("Veuillez choisir une option valide ;)")
        continue

#Ajouter
    if user_choice == "1":
        item = input("Entrez un article à la liste de course: ")
        LISTE.append(item)
        print(f"L'élément {item} à bien été ajouté à la liste de course")
#Retirer
    elif user_choice == "2":
        item = input("Entrez le nom de l'article à retirer de la liste de course: ")
        if item in LISTE:
            LISTE.remove(item)
        print("L'article {item} a bien était retirer de la liste de course")
#Afficher
    elif user_choice == "3":
        item = input("Entrez le nom de l'article à afficher: ")
        if LISTE:
            print("Voici le contenu de votre liste:")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément")
#Vider
    elif user_choice == "4":
        item = input("Vider votre liste de course")
        LISTE.clear()
        print("Votre liste de course est vide")
#Quitter
    elif user_choice == "5":
        #Avant de quitter le programme, on va écrire la liste sur le disque, on l'ouvre en mode écriture. On écrit des données à l'intérieur du fichier grâce à la méthode .dump
        with open(LISTE_path, "w") as f:
            json.dump(LISTE, f, indent=4)
        print("A bientôt")
        sys.exit()
    
    print("-" * 50)


            


