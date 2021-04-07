from application import db

class Gebruiker(db.Model):

    __tablename__ = 'Gebruiker'

    id = db.Column(db.Integer, primary_key=True)
    gebruikersnaam = db.Column(db.Text)
    wachtwoord = db.Column(db.Text)

    def __init__(self, gebruikersnaam, wachtwoord):
        self.gebruikersnaam = gebruikersnaam
        self.wachtwoord = wachtwoord

    def __repr__(self):
        return f"Gebruikersnaam: {self.gebruikersnaam}. Wachtwoord {self.wachtwoord}."