# Entry point for Student Database

from flask import Flask #, url_for
from flask_sqlalchemy import SQLAlchemy

# OpenID Implementation
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
# END OpenID Implementation

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# app.secret_key = 'This is really unique and secret'

from app import views, models
