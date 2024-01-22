import json

#On stock le fichier json dans la variable fichier
fichier = "settings.json"

#On lit le fichier json
with open(fichier, "r") as f:
    settings = json.load(f)

#On écrit dans le fichier json
with open(fichier, "w") as f:
    json.dump(settings, f, indent=4)