import sqlite3

DATABASE = 'database.db'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS offres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    postule TEXT,
    date TEXT,
    entreprise TEXT,
    poste TEXT,
    lien TEXT,
    text TEXT,
    coordonee TEXT
) ;
""")

#data_to_insert = ("alternance", "non", "9/10/2023", "AFTEC GROUPE", "Developpeur Web", "https://fr.indeed.com/?vjk=bcf463224c38909e&advn=464720144577672")
#data_to_insert = ("alternance", "non", "9/10/2023", "Hotel les jardins du marais", "Developpeur Web", "https://fr.indeed.com/?vjk=bf1f9605473175fa")
data_to_insert = ("stage", "non", "11/10/2023", "EDF", "Développeur Informatique", "https://fr.indeed.com/?vjk=65d50a14fb9318d2")

query = "INSERT INTO offres (type, postule, date, entreprise, poste, lien) VALUES (?, ?, ?, ?, ?, ?)"
cursor.execute(query, data_to_insert)
connection.commit()

rows = cursor.execute("SELECT * FROM offres")
for row in rows:
    print(row)


connection.close()
