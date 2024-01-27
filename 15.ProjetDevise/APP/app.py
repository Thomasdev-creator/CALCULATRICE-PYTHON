from PySide6 import QtWidgets
#Fonctions qui vont nous permettre de créer des interfaces graphiques
import currency_converter
#On créer une classe qui hérite de Qwidget nous permettant de créer notre fenêtre
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #Je crée une instance de la class currency_converter à partir du module currency_converter
        self.c = currency_converter.CurrencyConverter()
        #On crée une instance de la class app à partir de qwidget pour ajouter un titre à notre interface
        self.setWindowTitle("Convertiseur de devises")
        #On appele self.setup_ui()
        self.setup_ui()
        #On appele self.set_default_values()
        self.set_default_values()
        #On appele self.setup_connections()
        # Exemple -----> self.setup_css()
        self.setup_connections()
    
    def setup_ui(self):
        # Créez un widget principal
        main_widget = QtWidgets.QWidget(self)
        
        # Créez un layout horizontal
        self.layout = QtWidgets.QHBoxLayout(main_widget)
        #On créer nos widgets que l'on va ensuite ajouter à notre layout
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")

        #On ajoute nos widgets à notre layout
        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)

        # Définissez le layout du widget principal
        main_widget.setLayout(self.layout)

    def set_default_values(self):
        if self.c.currencies is not None:
            # On ajoute les devises à nos combobox à partir de notre instance c sous forme de liste triée
            self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
            self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        # On définit la devise par défaut
        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")
        # On définit les valeurs min et max
        self.spn_montant.setRange(1, 1000000000)
        self.spn_montantConverti.setRange(1, 1000000000)
        # On définit le montant par défaut
        self.spn_montant.setValue(100)
        self.spn_montantConverti.setValue(100)

    def setup_connections(self):
        #On connecte nos widgets à nos méthodes
        self.cbb_devisesFrom.activated.connect(self.comput)
        self.cbb_devisesTo.activated.connect(self.comput)
        self.spn_montant.valueChanged.connect(self.comput)
        self.btn_inverser.clicked.connect(self.inverser_devise)

    #Exemple ------> def setup_css(self):
        """self.setStyleSheet(
            background-color: rgb(30, 30, 30);
            color: rgb(240, 240, 240);
            border: none;)
        """

    def comput(self):
        #On récupère les valeurs de nos widgets
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        #On utilise la méthode convert() de notre instance c pour convertir notre montant
        #On utilise un try except pour gérer les erreurs
        try:
            resultat = self.c.convert(montant, devise_from, devise_to)
        #On gère l'erreur si la devise n'est pas trouvée
        except currency_converter.currency_converter.RateNotFoundError:
            print("La conversion n'a pas fonctionné")
        else:
            #On affiche le résultat dans notre spinbox
            self.spn_montantConverti.setValue(resultat)

    def inverser_devise(self):
        #On récupère les valeurs de nos widgets
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        #On inverse les valeurs
        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)
        #On appele self.comput()
        self.comput()

#On créer notre application avec Qwidwet
app = QtWidgets.QApplication([])
#On créer notre fenêtre avec une instance à partir de app
win = App()
#Pour afficher notre fenêtre on utilise la méthode show()
win.show()

app.exec_() #On lance notre application

