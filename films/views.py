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
    editform = EditForm()

    # -- START alle data ophalen --
    film_id = request.args.get('film_id')
    current_film = Film.query.get(film_id)
    regisseur = Regisseur.query.get(current_film.regisseur_id)
    rollen = Rol.query.filter_by(id_film=current_film.id)

    acteurs = []
    for i in range(0, len(rollen.all())):
        acteurs.append(Acteur.query.get(rollen[i].id_acteur))

    commentaar = Comment.query.filter_by(id_film=current_film.id)
    alle_commentaar = []
    for i in range(0, len(commentaar.all())):
        alle_commentaar.append(commentaar[i])

    comments = []
    for i in range(0, len(alle_commentaar)):
        gebruiker = Gebruiker.query.get(alle_commentaar[i].id_gebruiker)
        comments.append([gebruiker.gebruikersnaam, alle_commentaar[i].comment])
    # -- EIND alle data ophalen --

    if request.method == 'POST' and commentform.validate_on_submit():
        if current_user.is_authenticated:
            commentaar = Comment(current_film.id, current_user.id, commentform.commentaar.data)
            db.session.add(commentaar)
            db.session.commit()
            commentform.commentaar.data = ''
            return redirect(url_for('films_blueprint.film', film_id=current_film.id))
        else:
            flash("Je moet ingelogd zijn om commentaar te kunnen plaatsen.")
    else: 
        if len(commentform.errors.items()) >= 1:
            flash("Het bericht moet tussen 5 en 200 woorden zijn.")
    return render_template('films/film.html',   film_info = current_film, regisseur = regisseur, 
                                                rollen = rollen.all(), acteurs = acteurs, comments = comments,
                                                comment_form = commentform, edit_form=editform)