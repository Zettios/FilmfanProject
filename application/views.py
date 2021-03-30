from flask import Flask, render_template
from . import app

@app.route('/')
def index():
    print("Route: index - app")
    return redirect(url_for('application/films.index'), 308)

@app.route('/contact')
def contact():
    print("Route: contact")
    return render_template('application/contact.html')