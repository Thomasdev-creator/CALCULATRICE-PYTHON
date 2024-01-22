#Module python
import json
import logging
import os

#Mon module
from constants import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list):
    #Initialistation
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères")
        
        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste")
        
        self.append(element)
        return True

    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f" - {element}")

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        #On vérifie si le chemin exist déjà sinon on créer un noveau dossier
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        #On ouvre le chemin en mode écriture que l'on stocke dans la variable f
        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)

        return True
    
if __name__ == "__main__":
    liste = Liste("courses")
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    liste.sauvegarder()