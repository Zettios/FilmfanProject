from flask import Blueprint

gebruikers_blueprint = Blueprint('gebruikers_blueprint', __name__, 
    template_folder='templates')

from .views import *