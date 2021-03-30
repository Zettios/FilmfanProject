from flask import Flask, render_template
from . import app

@app.route('/')
def index():
    print("Route - application: index - app")
    return redirect(url_for('application/films.index'), 308)

@app.route('/contact')
def contact():
    print("Route - application: contact")
    return render_template('application/contact.html')