from flask import Blueprint
from flask import render_template


main = Blueprint('routes', __name__)


@main.route('/')
def index_page():
    return render_template('index.html')
