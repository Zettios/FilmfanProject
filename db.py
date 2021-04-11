from application import db
from films.models import *
from gebruikers.models import *

db.drop_all()
db.create_all()

acteur1 = Acteur("Carice", "van Houten")
acteur2 = Acteur("Roeland", "Fernhout")
acteur3 = Acteur("Linda", "van Dyck")

acteur4 = Acteur("Peter", "Weller")
acteur5 = Acteur("Nancy", "Allen")
acteur6 = Acteur("Don", "O'Herlihy")

acteur7 = Acteur("Ariane", "Schluter")

acteur8 = Acteur("Tom", "Dewispelaere")
acteur9 = Acteur("Alex", "van Warmerdam")

acteur10 = Acteur("Maria", "Teresa Berganza")
acteur11 = Acteur("Johan", "Leysen")
acteur12 = Acteur("Halina", "Reijn")
acteur13 = Acteur("Henri", "Garcin")

db.session.add_all([acteur1, acteur2, acteur3, acteur4,
                    acteur5, acteur6, acteur7, acteur8,
                    acteur9, acteur10, acteur11, acteur12, acteur13])
db.session.commit()

regisseur1 = Regisseur("Martijn", "Koolhoven")
regisseur2 = Regisseur("Paul", "Verhoeven")
regisseur3 = Regisseur("Theo", "van Gogh")
regisseur4 = Regisseur("Alex", "van Warmerdam")

db.session.add_all([regisseur1, regisseur2, regisseur3, regisseur4])
db.session.commit()

film1 = Film("Suzy Q", 1999, regisseur1.id, "https://www.youtube.com/watch?v=ZrdQSAX2kyw&ab_channel=HBOMax")
film2 = Film("RoboCop", 1987, regisseur2.id, "")
film3 = Film("o6", 1994, regisseur3.id, "")
film4 = Film("Schneider vs. Bax", 2015, regisseur4.id, "")
film5 = Film("Grimm ", 2003, regisseur4.id, "")

db.session.add_all([film1, film2, film3, film4, film5])
db.session.commit()

rol1 = Rol(acteur1.id, film1.id, "Suzy")
rol2 = Rol(acteur2.id, film1.id, "Zwier")
rol3 = Rol(acteur3.id, film1.id, "Ruth (Suzy's moeder)")

rol4 = Rol(acteur4.id, film2.id, "Alex J. Murphy/Robocop")
rol5 = Rol(acteur5.id, film2.id, "Anne Lewis")
rol6 = Rol(acteur6.id, film2.id, "De Oude Man")

rol7 = Rol(acteur7.id, film3.id, "Sarah Wever")

rol8 = Rol(acteur8.id, film4.id, "Schneider")
rol9 = Rol(acteur9.id, film4.id, "Ramon Bax")

rol10 = Rol(acteur10.id, film5.id, "Moeder")
rol11 = Rol(acteur11.id, film5.id, "Vader")
rol12 = Rol(acteur12.id, film5.id, "Maria")
rol13 = Rol(acteur13.id, film5.id, "Don Filipe")

db.session.add_all([rol1, rol2, rol3, rol4,
                    rol5, rol6, rol7, rol8,
                    rol9, rol10, rol11, rol12, rol13])
db.session.commit()

user0 = Gebruiker("admin@gmail.com", "Admin", "admin")
user1 = Gebruiker("bobbybobinson@gmail.com", "Bobby", "WW123")
user2 = Gebruiker("boberito@gmail.com", "Bob", "WW1234*")

db.session.add_all([user0, user1, user2])
db.session.commit()

comment1 = Comment(film1.id, user1.id, "Wat een film!!")
comment2 = Comment(film2.id, user1.id, "Wat een film!!")
comment3 = Comment(film3.id, user1.id, "Wat een film!!")
comment4 = Comment(film4.id, user1.id, "Wat een film!!")
comment5 = Comment(film5.id, user1.id, "Wat een film!!")

comment5 = Comment(film2.id, user2.id, "In the close-up of the cocaine dispensing machine, the glass vial rises up to the nozzle only to be dropped a second later causing most of the cocaine to be released into the air.")
comment6 = Comment(film5.id, user2.id, "Could be better.")

db.session.add_all([comment1, comment2, comment3,
                    comment4, comment5, comment6])
db.session.commit()