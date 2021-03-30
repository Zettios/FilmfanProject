from flask import Blueprint

films_blueprint = Blueprint('films_blueprint', __name__, 
    template_folder='templates',
    static_folder='static')

from .views import *