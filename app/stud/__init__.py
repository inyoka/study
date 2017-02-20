# app/student/__init__.py

from flask import Blueprint

stud = Blueprint('stud', __name__)

from . import views
