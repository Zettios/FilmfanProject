from flask import Flask, render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user
from . import app
from application import db, login_manager

@app.route('/')
def index():
    print("Route - application: index - app")
    return redirect(url_for('films.index'), 308)

@app.route('/contact')
def contact():
    print("Route - application: contact")
    return render_template('application/contact.html')