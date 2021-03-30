from flask import Blueprint

films = Blueprint('films', __name__, 
    url_prefix='/films',
    template_folder='templates')

from .views import *