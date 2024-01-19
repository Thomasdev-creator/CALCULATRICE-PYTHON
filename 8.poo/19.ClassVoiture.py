#On déclare la classe voiture
class Voiture:
    #Méthonde init pour instancier notre classe
    def __init__(self):
    #On initialise essence à 100l
        self.essence = 100

#Méthode avec self comme argument
def afficher_reservoir(self):
    print(f"La voiture contient {self.essence}L d'essence")

def roule(self, km):
    #Condition
    if self.essence <= 0:
        print("Vous n'avez plus d'essence, faites le plein")
        return
    
    self.essence -= (km * 5) / 100

    if self.essence < 10 :
        print("Vous 'avez presque plus d'essence")
    
    self.afficher_reservoir()

def faire_le_plein(self):
    self.essence = 100
    print("Vous pouvez repartir")

