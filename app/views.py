from app import app
from flask import url_for, request
import random

@app.route('/')
@app.route('/index')
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
@app.route('/test')
def test():
    user = {'nickname': 'Miguel'}  # fake user
    return '''
        <html>
        <head>
        <title>Home Page</title>
        </head>
        <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
        </body>
        </html>
        '''
