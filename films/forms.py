from flask import Flask
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional, Length

class CommentForm(FlaskForm):
    commentaar = TextAreaField('Commentaar', validators=[DataRequired("Dit veld is verplicht"), Length(min=5, max=200)], render_kw={"placeholder": "Commentaar"})
    # Length werkt wel, maar anders dan DataRequired.
    # De message word door gegeven met <form_naam>.errors
    # Bedoeling om dit in een flash bericht te stoppen
    voegtoe = SubmitField('Voegtoe')