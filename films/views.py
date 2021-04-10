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
                                                comment_form = commentform)
                                
@films_blueprint.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():

    editform = EditForm()

    film_id = request.args.get('id')
    current_film = Film.query.get(film_id)

    if request.method == 'POST' and editform.validate_on_submit():
        if editform.verander.data:
            print('ok')
            current_film.trailer = editform.trailer_link.data
            current_film.titel = editform.titel.data
            current_film.jaar = editform.jaar.data
            current_film.regisseur_id = editform.regisseurs.data + 1
            print(editform.regisseurs.data)

            db.session.add(current_film)
            db.session.commit()

            return redirect(url_for('films_blueprint.edit', id=film_id))

    alle_regisseurs = Regisseur.query.all()
    regisseurs = []

    for i in range(0, len(alle_regisseurs)):
        regisseurs.append((str(i), str(alle_regisseurs[i])))

    editform.regisseurs.default = current_film.regisseur_id - 1
    editform.process()

    editform.trailer_link.data = current_film.trailer
    editform.titel.data = current_film.titel
    editform.jaar.data = current_film.jaar
    editform.regisseurs.choices = regisseurs

    rollen = Rol.query.filter_by(id_film=current_film.id)
    acteurs = []
    for i in range(0, len(rollen.all())):
        acteurs.append(Acteur.query.get(rollen[i].id_acteur))

    return render_template('films/edit.html',   editform=editform, current_film=current_film, 
                                                rollen = rollen.all(), acteurs = acteurs)

@films_blueprint.route('/acteur_toevoegen', methods=['GET', 'POST'])
@login_required
def acteur_toevoegen():
    acteurtoevoegenform = ActeurToevoegenForm()

    film_id = request.args.get('id')

    if request.method == 'POST' and acteurtoevoegenform.validate_on_submit():
        print("post") 
        acteur = Acteur(acteurtoevoegenform.voornaam.data, acteurtoevoegenform.achternaam.data)
        db.session.add(acteur)
        db.session.commit()

        return redirect(url_for('films_blueprint.edit', id=film_id))

    return render_template('films/acteur_toevoegen.html', form=acteurtoevoegenform, id=film_id)

@films_blueprint.route('/rol_toevoegen', methods=['GET', 'POST'])
@login_required
def rol_toevoegen():
    roltoevoegenform = RolToevoegenForm()

    film_id = request.args.get('id')
    acteurs = Acteur.query.all()
    acteurs_arr = []

    for i in range(0, len(acteurs)):
        acteurs_arr.append((str(i), str(acteurs[i].voornaam + " " + acteurs[i].achternaam)))
    print(acteurs_arr)

    roltoevoegenform.acteurs.choices = acteurs_arr

    if request.method == 'POST' and roltoevoegenform.validate_on_submit():
        print("post") 
        rol = Rol(roltoevoegenform.acteurs.data + 1, film_id, roltoevoegenform.personage.data)
        db.session.add(rol)
        db.session.commit()

        return redirect(url_for('films_blueprint.edit', id=film_id))

    return render_template('films/rol_toevoegen.html', form=roltoevoegenform, id=film_id)
