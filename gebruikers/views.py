from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from application import db, bcrypt
from .forms import *
from .models import *
from . import gebruikers_blueprint

@gebruikers_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    print("Route - gebruiker: login")
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.login.data)
        if form.login.data:
            # Wanneer de login knop wordt in gedrukt, dan wordt gecontroleerd of de gebruiker bestaat.
            # Zo ja: Login
            # Zo nee: Geef error
            return redirect(url_for('films_blueprint.index'))

    return render_template('gebruikers/login.html', form=form)

@gebruikers_blueprint.route('/registreer_gebruiker', methods=['GET', 'POST'])
def registreer_gebruiker():
    print("Route - gebruiker: registreer_gebruiker")
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
def account():
    print("Route - gebruiker: account")

    email = current_user.email
    gebruikersnaam = current_user.gebruikersnaam
    wachtwoord = current_user.wachtwoord

    return render_template('gebruikers/account.html', email=email, gebruikersnaam=gebruikersnaam, wachtwoord=wachtwoord)

@gebruikers_blueprint.route('/verwijder_account', methods=['GET', 'POST'])
def verwijder_account():
    print("Route - gebruiker: verwijder_account")
    return render_template('gebruikers/verwijder_account.html')

