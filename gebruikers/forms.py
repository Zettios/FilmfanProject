from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import check_password_hash
from .models import Gebruiker

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    wachtwoord = PasswordField('Wachtwoord', validators=[DataRequired()], render_kw={"placeholder": "Wachtwoord"})
    login = SubmitField('Login')

class RegistreerForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email("Deze e-mail is niet geldig.")], render_kw={"placeholder": "E-mail"})
    gebruikersnaam = StringField('Gebruikersnaam', validators=[DataRequired()], render_kw={"placeholder": "Gebruikersnaam"})
    wachtwoord = PasswordField('Wachtwoord', validators=[DataRequired()], render_kw={"placeholder": "Wachtwoord"})
    wachtwoord_confirmatie = PasswordField('Bevestig wachtwoord',
                                            validators=[DataRequired(), EqualTo('wachtwoord', message='Wachtwoorden moeten gelijk zijn.')], 
                                            render_kw={"placeholder": "Wachtwoord"})
    registreer = SubmitField('Registreer')

    def check_email(self, field):
        if Gebruiker.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres staat al geregistreerd!')

    def check_username(self, field):
        if Gebruiker.query.filter_by(gebruikersnaam=field.data).first():
            raise ValidationError('Deze gebruikersnaam is al vergeven, probeer een ander naam!')