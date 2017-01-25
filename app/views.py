from app import app, db, lm, oid
from flask import url_for, request, render_template, flash, redirect, session, url_for, g
from flask_login import login_user, logout_user, current_user, login_required
import random
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def hello_person():
    user = {'nickname': 'Iain'}  # fake user
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/greet')
def greeting():
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
    return render_template('test.html', title='Test', user=user)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/greet', methods=['POST'])
def greet():
    greeting = random.choice(["Hiya", "Hallo", "Hola", "Ola", "Salut", "Privet",
                              "Konnichiwa", "Ni hao"])
    return """
<p>%s, %s!</p>
<p><a href="%s">Back to start</a></p>
""" % (greeting, request.form["person"], url_for('hello_person'))
