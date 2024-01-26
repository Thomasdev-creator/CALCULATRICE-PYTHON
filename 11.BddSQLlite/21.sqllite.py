import sqlite3

#On créer une connexion à notre base de donnée, elle n'exite pas encore donc python va la créer automatiquement dans le même répertoire
connexion = sqlite3.connect("database.db")

#On récupère notre curseur pour exécuter nos reqûte sql
c = connexion.cursor()

#On execute notre requête SQL avec la méthode execute sur notre variable c
#Puis on créer notre table avec du code sql
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
          prenom text,
          nom text
          salaire int
)
""")

#On créer un dictionnaire que l'on stocke dans notre variable d
d = {"prenom": "Paul", "nom": "Dupont"}
#On ajoute en employé à la table employees, on lui passe en argument le prénom et le nom ainsi que le dictionnaire
c.execute("INSERT INTO employees VALUES(:prenom, :nom)", d)

#On sélectionne tout les employés de la table employees
c.execute("SELECT * FROM employees")
#On utilise la méthode fetchall pour afficher tout les employées
donnees = c.fetchall()
print(donnees)
#On utilise la méthode fethone pour afficher un seul employé
premier = c.fetchone()
print(premier)

#On met à jour le salaire de la table employees
c.execute("UPDATE employees SET salaire=:salaire WHERE prenom=:prenom AND nom=: nom", d)

#On supprime un employé ayant comme prénom Paul
c.execute("DELETE FROM employees WHERE prenom= 'Paul'")

#On ajoute nos modification à la base de donnée
connexion.commit()

#On arrête la connexion avec la méthode close
connexion.close()