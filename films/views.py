from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from application import db, login_manager
from .forms import *
from .models import *
from gebruikers.models import *
from . import films_blueprint

@films_blueprint.route('/', methods=['GET', 'POST'])
def index():
    films = Film.query.all()
    regisseurs = Regisseur.query.all()
    print(*films, sep='\n')
    return render_template('films/home.html', len = len(films), Films = films, Regisseurs = regisseurs)

@films_blueprint.route('/film', methods=['GET', 'POST'])
def film():
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
            current_film.trailer = editform.trailer_link.data
            current_film.titel = editform.titel.data
            current_film.jaar = editform.jaar.data

            split = editform.regisseurs.data.split(" ", 1)
            voornaam = split[0]
            achternaam = split[1]
            regisseur = Regisseur.query.filter_by(voornaam=voornaam, achternaam=achternaam).first()
            current_film.regisseur_id = regisseur.id

            db.session.add(current_film)
            db.session.commit()

            return redirect(url_for('films_blueprint.edit', id=film_id))

    alle_regisseurs = Regisseur.query.all()
    regisseurs = []
    index = 0

    for i in range(0, len(alle_regisseurs)):
        regisseurs.append(alle_regisseurs[i])
        if alle_regisseurs[i].id == current_film.regisseur_id:
            index = str(alle_regisseurs[i].voornaam + " " + alle_regisseurs[i].achternaam)

    editform.regisseurs.choices = regisseurs
    editform.regisseurs.default = index
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

@films_blueprint.route('/film_verwijderen', methods=['GET', 'POST'])
@login_required
def film_verwijderen():
    return render_template('films/film_verwijderen.html', id=film_id)

@films_blueprint.route('/acteur_toevoegen', methods=['GET', 'POST'])
@login_required
def acteur_toevoegen():
    acteurtoevoegenform = ActeurToevoegenForm()

    film_id = request.args.get('id')

    if request.method == 'POST' and acteurtoevoegenform.validate_on_submit():
        acteur = Acteur(acteurtoevoegenform.voornaam.data, acteurtoevoegenform.achternaam.data)
        db.session.add(acteur)
        db.session.commit()

        return redirect(url_for('films_blueprint.edit', id=film_id))

    return render_template('films/acteur_toevoegen.html', form=acteurtoevoegenform, id=film_id)

@films_blueprint.route('/acteur_verwijderen', methods=['GET', 'POST'])
@login_required
def acteur_verwijderen():
    acteurverwijderform = ActeurVerwijderForm()
    film_id = request.args.get('id')

    if request.method == 'POST' and acteurverwijderform.validate_on_submit():
        split = acteurverwijderform.acteurs.data.split(" ", 1)
        voornaam = split[0]
        achternaam = split[1]
        acteur = Acteur.query.filter_by(voornaam=voornaam, achternaam=achternaam).first()
 
        Rol.query.filter_by(id_acteur=acteur.id).delete()
        db.session.commit()
        db.session.delete(acteur)
        db.session.commit()

        return redirect(url_for('films_blueprint.edit', id=film_id))

    acteurs = Acteur.query.all()
    acteurs_arr = []
    for i in range(0, len(acteurs)):
        acteurs_arr.append((str(acteurs[i].voornaam + " " + acteurs[i].achternaam)))

    acteurverwijderform.acteurs.choices = acteurs_arr

    return render_template('films/acteur_verwijderen.html', form=acteurverwijderform, id=film_id)

@films_blueprint.route('/rol_toevoegen', methods=['GET', 'POST'])
@login_required
def rol_toevoegen():
    roltoevoegenform = RolToevoegenForm()

    film_id = request.args.get('id')
    acteurs = Acteur.query.all()
    acteurs_arr = []

    for i in range(0, len(acteurs)):
        acteurs_arr.append((str(acteurs[i].voornaam + " " + acteurs[i].achternaam)))

    roltoevoegenform.acteurs.choices = acteurs_arr

    if request.method == 'POST' and roltoevoegenform.validate_on_submit():
        split = roltoevoegenform.acteurs.data.split(" ", 1)
        voornaam = split[0]
        achternaam = split[1]
        acteur = Acteur.query.filter_by(voornaam=voornaam, achternaam=achternaam).first()

        rol = Rol(acteur.id, film_id, roltoevoegenform.personage.data)
        db.session.add(rol)
        db.session.commit()

        return redirect(url_for('films_blueprint.edit', id=film_id))

    return render_template('films/rol_toevoegen.html', form=roltoevoegenform, id=film_id)

@films_blueprint.route('/rol_veranderen', methods=['GET', 'POST'])
@login_required
def rol_veranderen():
    rolveranderform = RolVeranderenForm()

    film_id = request.args.get('id')
    rol_id = request.args.get('rol_id')
    acteur_id = request.args.get('acteur_id')

    acteurs = Acteur.query.all()
    rol = Rol.query.filter_by(id=rol_id).first()
    acteur = Acteur.query.filter_by(id=acteur_id).first()
    acteur_default = str(acteur.voornaam + " " + acteur.achternaam)

    acteurs_arr = []

    for i in range(0, len(acteurs)):
        acteurs_arr.append((str(acteurs[i].voornaam + " " + acteurs[i].achternaam)))

    if request.method == 'POST' and rolveranderform.validate_on_submit():
        split = rolveranderform.acteurs.data.split(" ", 1)
        voornaam = split[0]
        achternaam = split[1]
        acteur = Acteur.query.filter_by(voornaam=voornaam, achternaam=achternaam).first()

        rol.id_acteur = acteur.id
        rol.id_film = film_id
        rol.naam_personage = rolveranderform.personage.data
        db.session.add(rol)
        db.session.commit()
        return redirect(url_for('films_blueprint.edit', id=film_id))

    rolveranderform.acteurs.default = acteur_default
    rolveranderform.process()
    rolveranderform.personage.data = rol.naam_personage
    rolveranderform.acteurs.choices = acteurs_arr

    return render_template('films/rol_veranderen.html', veranderform=rolveranderform, id=film_id)

@films_blueprint.route('/rol_verwijderen', methods=['GET', 'POST'])
@login_required
def rol_verwijderen():
    rolverwijderform = RolVerwijderForm()
    film_id = request.args.get('id')
    
    rollen = Rol.query.filter_by(id_film=film_id)
    rollen_arr = []

    for i in range(0, len(rollen.all())):
        rollen_arr.append((rollen.all()[i].naam_personage))

    rolverwijderform.personage.choices = rollen_arr

    if request.method == 'POST' and rolverwijderform.validate_on_submit():
        rol = Rol.query.filter_by(naam_personage=rolverwijderform.personage.data).first()
        db.session.delete(rol)
        db.session.commit()
        return redirect(url_for('films_blueprint.edit', id=film_id))

    return render_template('films/rol_verwijderen.html', form=rolverwijderform, id=film_id)