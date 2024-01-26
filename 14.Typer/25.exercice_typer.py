#On import typer
#Permet d'utiliser le paramètre optional
#Utilisation de pathlib pour les chemins
import typer
from typing import Optional
from pathlib import Path

#On créer une instance de typer
app = typer.Typer()
"""Extension de fichier que l'on souhaite récupérer en paramètre,
puis le dossier dans lequel on souhaite chercher (paramètre optionnel)
On utilise typer.argument puis none pour indiquer qu'on peut ne rien passer en argument, puis on indique l'aide
Puis l'option delete par default à False que l'on peut passer à True
"""

#On crée ensuite des commandes
@app.command('run')
def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher"),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés")):
    """Affiche les fichiers avec l'extension donnée
    """
    #Si le nom de dossier est à None on récupère le dossier courant
    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()

    #Si le dossier n'existe pas, puis on affiche le message en rouge
    if not directory.exists():
        typer.secho(f"Le dossier '{directory}' n'existe pas.", fg=typer.colors.RED)
    #On utilise typer.Exit pour sortir de notre script
        raise typer.Exit()
    
    #Si le fichier existe on va cherher de manière récursive avec rglob, puis on cherche tout les fichiers selon l'extension
    files = directory.rglob(f"*{extension}")
    if delete:
        #On demande à l'utilisateur si il veut vraiment supprimer tout les fichiers trouvés
        #On passe abort à True si l'utilisateur ne souhaite pas aller plus loin
        typer.confirm("Voulez vous vraiment supprimer les fichiers séléctionné ?", abort=True)
        #On boucle sur les fichiers puis on utilise la méthode unlick de Pathlib pour supprimer un fichier
        for file in files:
            file.unlick()
            typer.secho(f"Suppression du fichier {file}", fg=typer.colors.RED)
        
    else:
        typer.secho(f"Fichier trouvé avec l'extension {extension}:", bg=typer.colors.BLUE, fg=typer.colors.BRIGHT_WHITE)
        for file in files:
            typer.echo(files)

@app.command()
def search(extension: str):
    """Chercher les fichiers avec l'extension donnée
    """
    main(extension=extension, directory=None, delete=False)

@app.command()
def delete(extension: str):
    """Supprimer les fichiers avec l'extension donnée
    """
    main(extension=extension, directory=None, delete=True)
#Execute seulement le script lorsque l'on execute main
if __name__ == "__main__":
    #On exécute notre instance app
    app()