from flask import Blueprint

gebruikers = Blueprint('gebruikers', __name__, 
    url_prefix='/gebruikers',
    template_folder='templates')

from .views import *