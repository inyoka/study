# Entry point for Student Database

from flask import Flask #, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# app.secret_key = 'This is really unique and secret'

from app import views, models
