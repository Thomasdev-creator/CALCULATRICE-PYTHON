class Livre:
    def __init__(self, nom, nombre_de_pages, prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix

livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LOTR = Livre("Le seigneur des anneaux", 400, 13.99)

