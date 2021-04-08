from application import db
from films.models import *

class Gebruiker(db.Model):

    __tablename__ = 'Gebruikers'

    id = db.Column(db.Integer, primary_key=True)
    gebruikersnaam = db.Column(db.Text)
    wachtwoord = db.Column(db.Text)

    comment = db.relationship('Comment', backref='comment_gebruiker', lazy='dynamic')

    def __init__(self, gebruikersnaam, wachtwoord):
        self.gebruikersnaam = gebruikersnaam
        self.wachtwoord = wachtwoord

    def __repr__(self):
        return f"Gebruikersnaam: {self.gebruikersnaam}. Wachtwoord {self.wachtwoord}."