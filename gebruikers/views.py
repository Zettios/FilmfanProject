from flask import Flask, render_template, url_for, redirect, request, flash
from application import db
from .forms import *
from .models import *
from . import gebruikers

@gebruikers.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('films.index'))

        elif form.registreer.data and form.validate_on_submit():
            # Wanneer de registreer knop wordt in gedrukt, 
            # dan moeten beide velden zijn ingevuld om de gegevens op te slaan 
            # van de nieuwe gebruiker
            return redirect(url_for('gebruikers.account'))

    return render_template('gebruikers/login.html', form=form)

@gebruikers.route('/account')
def account():
    print("Route: account")
    return render_template('gebruikers/account.html')

@gebruikers.route('/verwijder_account', methods=['GET', 'POST'])
def verwijder_account():
    print("Route: verwijder_account")
    return render_template('gebruikers/verwijder_account.html')

