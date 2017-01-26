# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'
from app import views

@app.route('/')
def hello_person():
    return """
        <h1>CaSE Online Database Development</h1>
        <p>Hello Iain!  Please check back here periodically for developments.  Much </p>
        <p>of the work will be in the background, but I will let you know when things </p>
        <p>start to change on here.</p>
        <hr>
        <p>Test sending, processing and recieving data...</p>
        <p>Who do you want me to say "Hi" to with a random greating?</p>
        <form method="POST" action="%s"><input name="person" /><input type="submit" value="Go!" /></form>
        """ % (url_for('greet'),)

@app.route('/greet', methods=['POST'])
def greet():
    greeting = random.choice(["Hiya", "Hallo", "Hola", "Ola", "Salut", "Privet", "Konnichiwa", "Ni hao"])
    return """
        <p>%s, %s!</p>
        <p><a href="%s">Back to start</a></p>
        """ % (greeting, request.form["person"], url_for('hello_person'))
