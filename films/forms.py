from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional, Length

class EditForm(FlaskForm):
    trailer_link = StringField('Trailer', validators=[DataRequired()])
    titel = StringField('Titel', validators=[DataRequired()])
    jaar = StringField('Jaar', validators=[DataRequired()])
    regisseurs = SelectField("Regisseurs", coerce=int, validate_choice=False)
    verander = SubmitField("Verander")

    acteur_toevoegen = SubmitField('Voeg een acteur toe.')
    acteur_verwijderen = SubmitField('Verwijder een acteur.')

    rol_toevoegen = SubmitField('Voeg een rol toe.')
    rol_verwijderen = SubmitField('Verwijder een rol.')
   

class CommentForm(FlaskForm):
    commentaar = TextAreaField('Commentaar', validators=[DataRequired("Dit veld is verplicht"), Length(min=5, max=200)], render_kw={"placeholder": "Commentaar"})
    # Length werkt wel, maar anders dan DataRequired.
    # De message word door gegeven met <form_naam>.errors
    # Bedoeling om dit in een flash bericht te stoppen
    voegtoe = SubmitField('Voegtoe')