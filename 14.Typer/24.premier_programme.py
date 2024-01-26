import typer

#On peut passer des arguments à notre fonction main
def main(extension: str):
    """
    Affiche les fichiers trouvés avec l'extension données.
    """
    #Affiche des informations
    typer.echo(f"Recherche des fichiers avec l'extension {extension}")

extension = typer.prompt("Quelle extension recherchez vous")
print(extension)
#On indiquer ce que l'on souhaite executer dans notre script
typer.run(main)

