import sqlite3

# Chemin vers votre fichier de base de données
db_file = 'user.db'

# Charger le contenu du fichier SQL
with open('bdd/users.sql', 'r') as file:
    sql_script = file.read()

# Créer une connexion à la base de données
conn = sqlite3.connect(db_file)

# Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécuter le script SQL
cursor.executescript(sql_script)

# Valider et enregistrer les modifications
conn.commit()

# Fermer la connexion
conn.close()

