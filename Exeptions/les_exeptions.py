fichier = input("Entrez un fichier à ouvrir: ")

try:
    f = open(fichier, "r")
    print(f.read())
except FileNotFoundError:
    print("Impossible d'ouvrir le fichier")
except UnicodeDecodeError:
    print("Le fichier est introuvable")
else:
    f.close()