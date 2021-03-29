import os
from flask import Flask, render_template, url_for, redirect, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional, Length
from models import db, Film

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
db.init_app(app)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'filmfandb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class LoginForm(FlaskForm):
    gebruikersnaam = StringField('Gebruikersnaam', validators=[DataRequired()], render_kw={"placeholder": "Gebruikersnaam"})
    wachtwoord = PasswordField('Wachtwoord', validators=[DataRequired()], render_kw={"placeholder": "Wachtwoord"})
    login = SubmitField('Login')
    registreer = SubmitField('Registreer')

class CommentForm(FlaskForm):
    commentaar = TextAreaField('Commentaar', validators=[DataRequired("Dit veld is verplicht"), Length(min=5, max=200)], render_kw={"placeholder": "Commentaar"})
    # Length werkt wel, maar anders dan DataRequired.
    # De message word door gegeven met <form_naam>.errors
    # Bedoeling om dit in een flash bericht te stoppen
    voegtoe = SubmitField('Voegtoe')

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Route: index")
    films = Film.query.all()
    print(*films, sep='\n')
    return render_template('home.html', len = len(films), Films = films)

@app.route('/film', methods=['GET', 'POST'])
def film():
    print("Route: film")

    commentform = CommentForm()
    
    film_id = request.args.get('film_id')
    current_film = Film.query.get(film_id)

    if request.method == 'POST' and commentform.validate_on_submit():
        # Voeg commentaar toe aan de database
        print(commentform.commentaar.data)
        commentform.commentaar.data = ''
        print("OK")
        return redirect(url_for('film', film_id=current_film.film_id))
    else: 
        if len(commentform.errors.items()) >= 1:
            flash("Het bericht moet tussen 5 en 200 woorden zijn.")

    return render_template('film.html', film_info = current_film, comment_form = commentform)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Route: login")
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.login.data)
        print(form.registreer.data)
        if form.login.data and form.validate_on_submit():
            # Wanneer de login knop wordt in gedrukt, dan wordt gecontroleerd of de gebruiker bestaat.
            # Zo ja: Login
            # Zo nee: Geef error
            return redirect(url_for('index'))

        elif form.registreer.data and form.validate_on_submit():
            # Wanneer de registreer knop wordt in gedrukt, 
            # dan moeten beide velden zijn ingevuld om de gegevens op te slaan 
            # van de nieuwe gebruiker
            return redirect(url_for('account'))

    return render_template('login.html', form=form)

@app.route('/verwijder_account', methods=['GET', 'POST'])
def verwijder_account():
    print("Route: verwijder_account")
    return render_template('verwijder_account.html')

@app.route('/account')
def account():
    print("Route: account")
    return render_template('account.html')

@app.route('/contact')
def contact():
    print("Route: contact")
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)