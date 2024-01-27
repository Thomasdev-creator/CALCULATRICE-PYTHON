from PySide6 import QtWidgets, QtCore
from movie import get_movies
from movie import Movie

# On crée une classe App qui hérite de QWidget
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        self.title_movie = QtWidgets.QLineEdit()
        self.add_movie = QtWidgets.QPushButton("Ajouter un film")
        self.list_movie = QtWidgets.QListWidget()
        self.list_movie.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.delete_movie = QtWidgets.QPushButton("Supprimer le(s)")

        main_layout.addWidget(self.title_movie)
        main_layout.addWidget(self.add_movie)
        main_layout.addWidget(self.list_movie)
        main_layout.addWidget(self.delete_movie)

    def setup_connections(self):
        # On connecte le signal "clicked" du bouton à la fonction
        self.add_movie.clicked.connect(self.add_movie_to_list)
        self.delete_movie.clicked.connect(self.remove_movie)
        # On connecte le signal "returnPressed" du QLineEdit à la fonction
        self.title_movie.returnPressed.connect(self.add_movie_to_list)
    # Fonction pour afficher les films déjà présent dans la liste
    def populate_movies(self):
        # On récupère les films
        movies = get_movies()
        
        # On boucle sur les films
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movie.addItem(lw_item)

    def add_movie_to_list(self):
        #Récupérer le texte dans le lineEdit
        movie_title = self.title_movie.text()
        if not movie_title:
            return False
        #Créer une instance de Movie
        #Ajouter le film dans le fichier json
        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies()
        #Ajouter le film dans la liste widget
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movie.addItem(lw_item)

        self.title_movie.setText("")

    def remove_movie(self):
        for selected_item in self.list_movie.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.list_movie.takeItem(self.list_movie.row(selected_item))
# On lance l'application
app = QtWidgets.QApplication([]) 
# On instancie la classe App
win = App()
# On affiche la fenêtre
win.show()
# On lance l'application
app.exec_()
