from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    gebruikersnaam = StringField('Gebruikersnaam', validators=[DataRequired()], render_kw={"placeholder": "Gebruikersnaam"})
    wachtwoord = PasswordField('Wachtwoord', validators=[DataRequired()], render_kw={"placeholder": "Wachtwoord"})
    login = SubmitField('Login')
    registreer = SubmitField('Registreer')