import sqlite3

db = sqlite3.connect("filmfandb.sqlite")

def sql_table(db):

    db.execute("CREATE TABLE IF NOT EXISTS Individu( \
                        id integer PRIMARY KEY, \
                        voornaam text, \
                        achternaam text, \
                        positierolID integer)")

    db.execute("CREATE TABLE IF NOT EXISTS Positierol( \
                        id integer PRIMARY KEY, \
                        rolnaam text)")

    db.execute("CREATE TABLE IF NOT EXISTS Film( \
                        id integer PRIMARY KEY, \
                        titel text, \
                        individuID integer, \
                        jaar integer, \
                        trailer text)")

    db.execute("INSERT INTO film VALUES (1, 'foo1', 5, 1991, 'https://www.youtube.com/watch?v=ZrdQSAX2kyw&ab_channel=HBOMax')")
    db.execute("INSERT INTO film VALUES (2, 'foo2', 1, 1991, '')")
    db.execute("INSERT INTO film VALUES (3, 'foo3', 90, 1991, '')")
    db.execute("INSERT INTO film VALUES (4, 'foo4', 3, 1991, '')")

    db.execute("CREATE TABLE IF NOT EXISTS Rol( \
                        id integer PRIMARY KEY, \
                        individuID integer, \
                        filmID integer, \
                        vertolkenaam text)")

    db.execute("CREATE TABLE IF NOT EXISTS Gebruiker( \
                        id integer PRIMARY KEY, \
                        gebruikernaam text, \
                        wachtwoord text)")

    db.execute("CREATE TABLE IF NOT EXISTS Citaat( \
                        id integer PRIMARY KEY, \
                        citaat text, \
                        filmID integer)")

    db.execute("CREATE TABLE IF NOT EXISTS Incorrectie( \
                        id integer PRIMARY KEY, \
                        incorrectietekst text, \
                        filmID integer)")

    db.commit()

sql_table(db)

cursor = db.cursor()
cursor.execute("SELECT * FROM film")
for row in cursor:
    print(row)