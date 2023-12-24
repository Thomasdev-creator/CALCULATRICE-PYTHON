#utilisateur = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""for i in utilisateur:
    if i <= 10:
        print(f"Utilisateur {i}")
"""

#Afficher utilisateur de 1 à 10

"""for i in range(10):
    print(f"Utilisateur {i + 1}")
"""

#Afficher le mot Python est l'inverser

"""mot = "Python"

for i in reversed(mot):
    print(i)
"""

#Sortir d'une boucle infini

"""continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")
"""

#Raccourcir le code

"""
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [ i for i in nombres if i % 2 == 0]

print(nombres_pairs)

# ---------------------------------------------------- #

nombres = range(-10, 10)
nombres_positifs = [ i for i in nombres if i >= 0]

print(nombres_positifs)

# ---------------------------------------------------- #

nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]

print(nombres_doubles)

# ---------------------------------------------------- #

nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]

print(nombres_inverses)
"""