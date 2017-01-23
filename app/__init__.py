# Entry point for Student Database

from flask import Flask, request, url_for

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'
from app import views
