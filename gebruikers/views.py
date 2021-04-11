from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from application import db, login_manager, bcrypt
from .forms import *
from .models import *
from . import gebruikers_blueprint
from films.models import Comment

@gebruikers_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Gebruiker.query.filter_by(email=form.email.data).first()
        if user == None or user.check_password(form.wachtwoord.data) == False:
            form.email.errors.append("Deze gebruiker bestaat niet of het ingevoerde wachtwoord is incorrect.")
            return render_template('gebruikers/login.html', form=form)
        login_user(user)
        url = request.args.get('next')
        if not url or url[0] != '/':
            url = url_for('films_blueprint.index')
        return redirect(url)

    return render_template('gebruikers/login.html', form=form)

@gebruikers_blueprint.route('/verander_wachtwoord', methods=['GET', 'POST'])
def verander_wachtwoord():
    form = VeranderWachtwoordForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Gebruiker.query.filter_by(id=current_user.id).first()
        if user.check_password(form.oude_wachtwoord.data) == False:
            form.oude_wachtwoord.errors.append("Het oude wachtwoord is niet hetzelfde.")
            return render_template('gebruikers/verander_wachtwoord.html', form=form)

        if form.nieuwe_wachtwoord.data == form.nieuwe_wachtwoord_check.data:
            user.wachtwoord = bcrypt.generate_password_hash(form.nieuwe_wachtwoord.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('gebruikers_blueprint.account'))

    return render_template('gebruikers/verander_wachtwoord.html', form=form)

@gebruikers_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    form = LogoutForm()
    if request.method == 'POST' and form.validate_on_submit():
        if form.logout.data:
            logout_user()
            return redirect(url_for('films_blueprint.index'), 308)
        if form.ga_terug.data:
            return redirect(url_for('films_blueprint.index'), 308)
    return render_template('gebruikers/logout.html', form=form)

@gebruikers_blueprint.route('/registreer_gebruiker', methods=['GET', 'POST'])
def registreer_gebruiker():
    form = RegistreerForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Gebruiker(form.email.data, form.gebruikersnaam.data, form.wachtwoord.data)
        try:
            form.check_email(form.email)
            form.check_username(form.gebruikersnaam)
        except:
            form.email.errors.append("Deze e-mail en/of gebruikersnaam zijn al in gebruik.")
            return render_template('gebruikers/registreer_gebruiker.html', form=form)
        db.session.add(user)
        db.session.commit()
        user = Gebruiker.query.filter_by(email=form.email.data).first()
        login_user(user)
        url = request.args.get('next')
        if not url or url[0] != '/':
            url = url_for('gebruikers_blueprint.account')
        return redirect(url)
    return render_template('gebruikers/registreer_gebruiker.html', form=form)

@gebruikers_blueprint.route('/account')
@login_required
def account():
    fake_password = "*****"
    return render_template('gebruikers/account.html', fake_password=fake_password)

@gebruikers_blueprint.route('/verwijder_account', methods=['GET', 'POST'])
def verwijder_account():
    form = VerwijderForm()
    if request.method == 'POST' and form.validate_on_submit():
        gebruiker = Gebruiker.load_user(current_user.id)
        comments = Comment.query.filter_by(id_gebruiker=current_user.id).delete()
        db.session.delete(gebruiker)
        db.session.commit()
        logout_user
        return redirect(url_for('films_blueprint.index'), 308)
    
    return render_template('gebruikers/verwijder_account.html', form=form)

