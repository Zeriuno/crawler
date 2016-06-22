import mysql.connector 

#connexion MySQL
conn = mysql.connector.connect(host="localhost",user="root",password="XXX", database="test1")
cursor = conn.cursor()
conn.close()

#insérer des données dans la table 

user = ("olivier", "34")
cursor.execute("""INSERT INTO users (name, age) VALUES(%s, %s)""", user)

user = {"name": "olivier", "age" : "34"}
cursor.execute("""INSERT INTO users (name, age) VALUES(%(name)s, %(age)s)""", user)