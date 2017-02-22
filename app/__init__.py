from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT' # Temporary
# Before deployment generate with :
#import os
#os.urandom(24)

lm = LoginManager()
lm.init_app(app)
lm.session_protection = 'weak'
lm.login_view = 'auth.login'

#CSRF controls ...
#from flask_wtf.csrf import CSRFProtect
#WTF_CSRF_ENABLED=False
#csrf = CSRFProtect(app)
#csrf.init_app(app)


db = SQLAlchemy(app)
from app import models, views

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .stud import stud as stud_blueprint
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
