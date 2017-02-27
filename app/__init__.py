from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '{;\x95\xec\x8c_\xc2q\xd9\xefw\xee\xfdB\x830\x9dTC\xa9\x90@\ra'
#app.secret_key = os.urandom(24)

lm = LoginManager()
lm.init_app(app)
lm.session_protection = 'strong'
lm.login_view = 'auth.login'

db = SQLAlchemy(app)
from app import models, views

from .auth import auth as auth_blueprint
from .home import home as home_blueprint
from .stud import stud as stud_blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(stud_blueprint, url_prefix='/stud')

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('mysite/tmp/study.log',
                                       'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: \
                                                %(message)s [in \
                                                %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('study startup')
