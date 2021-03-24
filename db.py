import sqlite3

con = sqlite3.connect("filmfandb.sqlite")

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE Individu(id integer PRIMARY KEY, voornaam text, achternaam text, positierolID integer)")
    cursorObj.execute("CREATE TABLE Positierol(id integer PRIMARY KEY, rolnaam text)")
    cursorObj.execute("CREATE TABLE Film(id integer PRIMARY KEY, titel text, individuID integer, release integer)")
    cursorObj.execute("CREATE TABLE Rol(id integer PRIMARY KEY, individuID integer, filmID integer, vertolkenaam text)")
    cursorObj.execute("CREATE TABLE Gebruiker(id integer PRIMARY KEY, gebruikernaam text, wachtwoord text)")
    cursorObj.execute("CREATE TABLE Citaat(id integer PRIMARY KEY, citaat text, filmID integer)")
    cursorObj.execute("CREATE TABLE Incorrectie(id integer PRIMARY KEY, incorrectietekst text, filmID integer)")

    con.commit()

sql_table(con)