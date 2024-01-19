#Variable qui permet d'accèder à des dossiers dans les quel python va chercher pour des modules 
#On import sys pour l'afficher puis pprint pour que la liste soit plus lisible

import sys
from pprint import pprint
pprint(sys.path)