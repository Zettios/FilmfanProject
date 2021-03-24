from flask import Flask, render_template, url_for, redirect, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class LoginForm(FlaskForm):

    gebruikersnaam = StringField('Gebruikersnaam', validators=[DataRequired()], render_kw={"placeholder": "Gebruikersnaam"})
    wachtwoord = PasswordField('Wachtwoord', validators=[DataRequired()], render_kw={"placeholder": "Wachtwoord"})
    login = SubmitField('Login')
    registreer = SubmitField('Registreer')

class Film:
    def __init__(self, film_id, titel, regisseur, jaar, trailer):
        self.film_id = film_id
        self.titel = titel
        self.regisseur = regisseur
        self.jaar = jaar
        self.trailer = trailer

    def __repr__(self):
        return  "ID: " +  str(self.film_id) + ", titel: " +  str(self.titel) + \
                ", regisseur: " +  str(self.regisseur) + ", jaar: " +  str(self.jaar)
    
    def getID(self):
        return self.film_id

film1 = Film(1, "foo1", "bar1", 1991, "https://www.youtube.com/watch?v=ZrdQSAX2kyw&ab_channel=HBOMax")
film2 = Film(2, "foo2", "bar2", 2055, "")
film3 = Film(3, "foo3", "bar3", 2001, "")
film4 = Film(4, "foo4", "bar4", 1890, "")

films = [film1, film2, film3, film4]

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html', len = len(films), Films = films)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        print(form.login.data)
        print(form.registreer.data)
        if form.login.data:
            # Wanneer de login knop wordt in gedrukt, dan wordt gecontroleerd of de gebruiker bestaat.
            # Zo ja: Login
            # Zo nee: Geef error
            return redirect(url_for('index'))

        elif form.registreer.data:
            # Wanneer de registreer knop wordt in gedrukt, 
            # dan moeten beide velden zijn ingevuld om de gegevens op te slaan 
            # van de nieuwe gebruiker
            return redirect(url_for('registreer'))

    return render_template('login.html', form=form)

@app.route('/registreer', methods=['GET', 'POST'])
def registreer():
    return render_template('registreer.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/film', methods=['GET', 'POST'])
def film():

    film = request.args.get('film')
    current_film = films[int(film) - 1]
    print(current_film)

    return render_template('film.html', film_info = current_film)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)