from application import db, login_manager, bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from films.models import *

class Gebruiker(db.Model, UserMixin):

    __tablename__ = 'Gebruikers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True, index=True)
    gebruikersnaam = db.Column(db.Text, nullable=False, unique=True, index=True)
    wachtwoord = db.Column(db.Text, nullable=False)

    comment = db.relationship('Comment', backref='comment_gebruiker', lazy='dynamic')

    def __init__(self, email, gebruikersnaam, wachtwoord):
        self.email = email
        self.gebruikersnaam = gebruikersnaam
        self.wachtwoord = bcrypt.generate_password_hash(wachtwoord).decode('utf-8')
    
    def check_password(self, wachtwoord):
        return bcrypt.check_password_hash(self.wachtwoord_hash, wachtwoord)

    @login_manager.user_loader
    def load_user(id):
        return Gebruiker.query.get(id)

    def __repr__(self):
        return f"Email: {self.email} / Gebruikersnaam: {self.gebruikersnaam} / Wachtwoord: {self.wachtwoord}"