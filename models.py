import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Koppelt de Flask-applicatie met de database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'filmfandb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Film(db.Model):

    __tablename__ = 'Film'

    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.Text)
    jaar = db.Column(db.Integer)
    regisseur_id = db.Column(db.Integer)
    trailer = db.Column(db.Text)

    def __init__(self, titel, jaar, regisseur_id, trailer):
        self.titel = titel
        self.jaar = jaar
        self.regisseur_id = regisseur_id
        self.trailer = trailer

    def __repr__(self):
        return f"Titel: {self.titel}. Jaar {self.jaar}. Regisseur id: {self.regisseur_id}. Trailer link: {self.trailer}."

db.create_all()

film1 = Film("foo1", 1991, "bar1", "https://www.youtube.com/watch?v=ZrdQSAX2kyw&ab_channel=HBOMax")
film2 = Film("foo2", 2055, "bar2", "")
film3 = Film("foo3", 2001, "bar3", "")
film4 = Film("foo4", 1890, "bar4", "")

db.session.add_all([film1, film2, film3, film4])
db.session.commit()