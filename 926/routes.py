from flask import Blueprint
from flask import render_template

from .albums import get_albums


main = Blueprint('routes', __name__)


@main.route('/')
def index_page():
    albums = get_albums()
    return render_template('index.html', albums=albums)
