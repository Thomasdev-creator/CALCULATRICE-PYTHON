#Import du module Pathlib (gère les chemins de fichiers et de dossiers)
from pathlib import Path

#Déclaration d'un dictionnaire qui mapp les extensions
dirs = {
        ".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".pdf": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques"
}

#Je récupère le chemin vers mon dossier de tri, le chemin utilisateur avec home puis je concatène avec le slash
tri_dir = Path.home() / "tri"
#Je récupère ensuite tout les fichiers contenu dans ce dossier
#J'utilise iterdir pour récupérer tout les fichiers et dossiers à l'intérieur d'un dossier
#Je fais une compréhension de liste et utilise isfile pour ne récupérer que les fichiers
#On obtien ainsi une lite de fichiers
files =  [f for f in tri_dir.iterdir() if f.is_file()]
#On boucle ensuite sur cette liste de fichier
for f in files:
#On récupère et concatene les fichiers trouvés sinon on les places dans autres
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
#On créer les dossiers de sorti pour ranger nos fichiers
    output_dir.mkdir(exist_ok=True)
#On utilise rename pour déplacer notre fichier d'origine de f que l'on replace dans output_dir puis on récupère son nom
    f.rename(output_dir / f.name)




