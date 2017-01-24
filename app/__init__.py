# Entry point for Student Database

from flask import Flask, url_for

app = Flask(__name__)
app.config.from_object('config')
# app.secret_key = 'This is really unique and secret'

from app import views
