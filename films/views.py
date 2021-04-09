from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from application import db, login_manager
from .forms import *
from .models import *
from gebruikers.models import *
from . import films_blueprint

@films_blueprint.route('/', methods=['GET', 'POST'])
def index():
    print("Route - films: index")

    films = Film.query.all()
    regisseurs = Regisseur.query.all()
    print(*films, sep='\n')
    return render_template('films/home.html', len = len(films), Films = films, Regisseurs = regisseurs)

@films_blueprint.route('/film', methods=['GET', 'POST'])
def film():
    print("Route - films: film")

    commentform = CommentForm()
    film_id = request.args.get('film_id')
    print(film_id)
    current_film = Film.query.get(film_id)
    if request.method == 'POST' and commentform.validate_on_submit():
        # Voeg commentaar toe aan de database
        print(commentform.commentaar.data)
        commentform.commentaar.data = ''
        print("OK")
        return redirect(url_for('films_blueprint.film', film_id=current_film.id))
    else: 
        if len(commentform.errors.items()) >= 1:
            flash("Het bericht moet tussen 5 en 200 woorden zijn.")
    return render_template('films/film.html', film_info = current_film, comment_form = commentform)