from flask import Flask, render_template, url_for, redirect, request, flash
from application import db
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
    return render_template('gebruikers/registreer_gebruiker.html', form=form)

@gebruikers_blueprint.route('/account')
def account():
    print("Route - gebruiker: account")
    return render_template('gebruikers/account.html')

@gebruikers_blueprint.route('/verwijder_account', methods=['GET', 'POST'])
def verwijder_account():
    print("Route - gebruiker: verwijder_account")
    return render_template('gebruikers/verwijder_account.html')

