#Les valeurs de a et b ainsi que la valeur retour doivent être de nombre entier
def annotations(a: int = 0, b: int = 2) -> int:
    return a + b

annotations()

#La fonction liste attend une liste avec en retour des nombres entiers
def liste() -> list[int]:
    return [1, 2, 3]

liste()

#Déclaration d'une variable et de son type
a: int = "5" #Détection d'erreur grâce à l'extension pylance avec le paramètre type checking mode sur basic

