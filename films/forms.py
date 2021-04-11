from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional, Length

class FilmToevoegenForm(FlaskForm):
    trailer_link = StringField('Trailer', validators=[DataRequired()])
    titel = StringField('Titel', validators=[DataRequired()])
    jaar = IntegerField('Jaar', validators=[DataRequired()])
    regisseurs = SelectField("Regisseurs", validate_choice=False)
    voegtoe = SubmitField("Voegtoe")

class EditForm(FlaskForm):
    trailer_link = StringField('Trailer', validators=[DataRequired()])
    titel = StringField('Titel', validators=[DataRequired()])
    jaar = IntegerField('Jaar', validators=[DataRequired()])
    regisseurs = SelectField("Regisseurs", validate_choice=False)
    verander = SubmitField("Verander")
   
class CommentForm(FlaskForm):
    commentaar = TextAreaField('Commentaar', validators=[DataRequired("Dit veld is verplicht"), Length(min=5, max=200)], render_kw={"placeholder": "Commentaar"})
    # Length werkt wel, maar anders dan DataRequired.
    # De message word door gegeven met <form_naam>.errors
    # Bedoeling om dit in een flash bericht te stoppen
    voegtoe = SubmitField('Voegtoe')

class VerwijderFilmForm(FlaskForm):
    verwijder = SubmitField("Verwijder")

class ActeurToevoegenForm(FlaskForm):
    voornaam = StringField('Voornaam', validators=[DataRequired()])
    achternaam = StringField('Achternaam', validators=[DataRequired()])
    toevoegen = SubmitField("Toevoegen")

class ActeurVerwijderForm(FlaskForm):
    acteurs = SelectField("Acteurs", validate_choice=False)
    verwijder = SubmitField("Verwijder")

class RolToevoegenForm(FlaskForm):
    personage = StringField('Personage', validators=[DataRequired()])
    acteurs = SelectField("Acteurs", validate_choice=False)
    toevoegen = SubmitField("Toevoegen")

class RolVeranderenForm(FlaskForm):
    personage = StringField('Personage', validators=[DataRequired()])
    acteurs = SelectField("Acteurs", validate_choice=False)
    verander = SubmitField("Pas aan")

class RolVerwijderForm(FlaskForm):
    personage = SelectField('Personage', validators=[DataRequired()])
    verwijder = SubmitField("Verwijder")