from flask import render_template
from flask_login import login_required
from . import home
from app.models import User


@home.route('/')
@home.route('/index')
def index():
    return render_template('home/index.html', title="Welcome")
