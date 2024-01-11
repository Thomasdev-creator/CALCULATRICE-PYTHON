#import de sys pour quitter le programme
import sys

#Déclaration de la liste qui sera complété par l'utilisateur
LISTE = []

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
        item = input("Quitter le programme")
        sys.exit()
    
    print("-" * 50)


            


