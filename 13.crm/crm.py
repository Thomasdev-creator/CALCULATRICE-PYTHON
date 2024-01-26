import re
import string
from tinydb import TinyDB
from pathlib import Path

class User:

    DB = TinyDB(Path(__file__).resolve().parent / "db.json", indent =4)

    #Initialisation de la classe avec plusieurs utilisateurs
    def __init__(self, first_name: str, last_name: str, phone_number: str="", address: str=""):
                self.first_name = first_name
                self.last_name = last_name
                self.phone_number = phone_number
                self.address = address
    #----------------------------------------------
                
    #Méthode repr qui permet d'avoir une représentation de la classe
    def __repr__(self):
           return f"User({self.first_name}, {self.last_name})"
    
    #Définit une présentation avec un retour à la ligne dans le terminale
    def __str__(self):
           return f"{self.full_name}\n{self.last_name}\n{self.phone_number}\n{self.address}"
    
    #----------------------------------------------

    #On défini une propriété
    @property
    def full_name(self):
           return f"{self.first_name} {self.last_name}"
    
    #----------------------------------------------
    
    #Permet de vérifier toute les conditions d'un seul coup
    def _checks(self):
           self._check_names()
           self._check_phone_number()
    
    #Vérification -> On créer une méthode qui ne peut pas être utiliser directement avec le tiret du bas
    #On imort regex puis on utilise la méthode sub pour supprimer toutes les occurences passé dans la liste
    def _check_phone_number(self):
            phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
            #On lève une erreur si le numéro de téléphone est inférieur à une longeur de dix et que ce n'est pas un type int
            if len(phone_number) < 10 or not phone_number.isdigit():
              raise ValueError(f"Le numéro de téléphone {self.phone_number} est invalide") 
            print(phone_number)

    #On vérifie que le nom est prénom de l'utilisateur ne sont pas vides
    def _check_names(self):
            if not (self.first_name and self.last_name):
                  raise ValueError("Le nom est prénom ne peuvent pas être vides.")
           
    #On stocke dans une variable toutes les caractères spéciaux
            special_caracters = string.punctuation + string.digits
            print(special_caracters)
    #On créer une boucle que vérifie que des caractères spéciaux ne sont pas présent dans le nom
            for caracteres in self.first_name + self.last_name:
                   if caracteres in special_caracters:
                          raise ValueError(f"Nom invalide {self.full_name}.")
                   
    #----------------------------------------------       

    #Sauvegarde les données après vérification          
    def save(self, validate_data: bool=False) -> int:
           if validate_data:
                self._checks()
            
                #Inser toutes les données des attributs
                return User.DB.insert(self.__dict__)

    #----------------------------------------------
            
if __name__ == "__main__":
        from faker import Faker
        fake = Faker(locale="fr_FR")

        #On créer une boucle de dix itération en utilisant faker pour créer des utilisateurs factice
        for _ in range(10):
            user = User(first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        phone_number=fake.phone_number(),
                        address=fake.address())
            print(user.save())
            #On ajoute une séparation de dix tiret entre chaque utilisateur
            print("-" * 10)
            #print(repr(user)) permet d'utiliser la méthode __repr__
            #user._check_phone_number()