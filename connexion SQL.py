import pymysql

# établir une connexion
connection = pymysql.connect(host='localhost',
                             user='utilisateur',
                             password='mot_de_passe',
                             db='nom_de_la_base_de_donnees')

# créer un curseur
cursor = connection.cursor()

# exécuter une requête SQL
sql = "SELECT * FROM ma_table"
cursor.execute(sql)

# récupérer les résultats
resultats = cursor.fetchall()

# afficher les résultats
for resultat in resultats:
    print(resultat)

# fermer la connexion
connection.close()

