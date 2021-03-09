from flask import Blueprint, template_rendered, url_for
from flask.templating import render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@main.route('/profile', methods = ['POST', 'GET'])
def profile():
    return 'Profile'