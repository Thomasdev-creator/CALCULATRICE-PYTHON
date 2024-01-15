'''Dans cet exercice, vous devez créer une fonction qui affiche le nom de l'utilisateur passé en argument.

Par exemple, si j'appelle la fonction en utilisant saluer("Patrick"), le script devra afficher : Bonjour Patrick'''

def affiche_le_nom(nom_utilisateur):
    print("Bonjour", nom_utilisateur)

affiche_le_nom("Patrick")

#Si on définit une valeur par défaut pour un paramètre qui se trouve en première position, vous avez l'obligation de définir une valeur par défaut pour tous les paramètres qui suivent.
'''def multiplicateur_mot(mot, mult=5):
    return mot * mult
 
mot_multiplie = multiplicateur_mot(mot="Bonjour")
print(mot_multiplie)'''

#On doit retourner c pour afficher le résultat de la function addition
'''def addition(a, b):
	c = a + b
	return c
    
resultat = addition(5, 10)
print(resultat)'''