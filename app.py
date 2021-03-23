from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class Film:
    def __init__(self, film_id, titel, regisseur, jaar):
        self.film_id = film_id
        self.titel = titel
        self.regisseur = regisseur
        self.jaar = jaar

film1 = Film(1, "foo1", "bar1", 1991)
film2 = Film(2, "foo2", "bar2", 2055)   
film3 = Film(3, "foo3", "bar3", 2001)   
film4 = Film(4, "foo4", "bar4", 1890)

films = [film1, film2, film3, film4]

@app.route('/')
def index():
    return render_template('home.html', len = len(films), Films = films)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/film')
def film():
    return render_template('film.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)