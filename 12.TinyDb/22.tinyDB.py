from tinydb import TinyDB

"""Création d'une base de donnée en mémoire
from tinydb.storages import MemoryStorage
db = TinyDB(storage = MemoryStorage)
"""
#Stockage de mes données dans un fichier json
db = TinyDB('data.json', indent=4)

"""Créer plusieurs tables dans mon fichier json
users = db.table("users")
roles = db.table("roles")

users.insert(...)

roles.insert(...)
"""

#On insert des données dans notre fichier json
#db.insert({"name": "Patrick", "score": 0})
#La méthode insert_multiple avec l'ajout d'un dictionnaire
db.insert_multiple([
    {"name": "Patrick", "score": 0},
    {"name": "Julie", "score": 5}
])

#Mettre à jour notre bdd
db.update({"score: 10"}, where("name") == "Patrick")

#Met à jour ou créer une donnée si elle n'existe pas
db.upsert()

#Supprime toute la bdd
#db.truncate()

#Supprimer des données
db.remove()

#On utilise query
User = Query()
#search pour chercher dans notre bdd
patrick = db.search(User.name == "Patrick")
#get pour obtenir une donnée unique
patrick_unique = db.get(User.name == "Patrick")

high_scores = db.search(where("name") == "Patrick")

print(len(db))
#méthode contains pour une donnée existante
print(db.contains(User.name == "Patrick"))
print(db.count(User.name == "Patrick"))




