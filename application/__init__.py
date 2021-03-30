import os
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'filmfandb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from films import films_blueprint
app.register_blueprint(films_blueprint)

from gebruikers import gebruikers_blueprint
app.register_blueprint(gebruikers_blueprint)

from .views import *