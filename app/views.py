from app import app
from flask import url_for, request, render_template, flash, redirect
import random
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def hello_person():
    user = {'nickname': 'Iain'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Iain'},
            'body': 'Beautiful day in CaSE 2!'
        },
        {
            'author': {'nickname': 'Simon'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/greet', methods=['POST'])
def greet():
    greeting = random.choice(["Hiya", "Hallo", "Hola", "Ola", "Salut", "Privet",
                              "Konnichiwa", "Ni hao"])
    return """
        <p>%s, %s!</p>
        <p><a href="%s">Back to start</a></p>
        """ % (greeting, request.form["person"], url_for('hello_person'))
