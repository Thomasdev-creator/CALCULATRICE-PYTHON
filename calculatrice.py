"""
#nombre_a = int(input("Entrez un nombre: "))
#nombre_b = int(input("Entrez un autre nombre: "))
#resultat = (nombre_a + nombre_b)
#print(resultat)

#On décalre deux variables
a = b = ""

#On boucle tant a et b ne sont pas des entiers
while not(a.isdigit() and b.isdigit()):

#On demande avec input un nombre à l'utilisateur
    a = input("Entrez un nombre: ")
    b = input("Entrez un nombre: ")

#Conditions, on affiche une phrase si l'utilisateur n'entre pas des lettres
    if not(a.isdigit() and b.isdigit()):
        print("Veuillez entrer des nombres valides")

#On affiche le résultat de l'addition
resultat = f"Le résultat de l'addition de {a} + {b} est égale à {int(a) + int(b)}"
print(resultat)
"""