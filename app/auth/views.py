# app/auth/old-views.py
from app import db, lm
from flask import url_for, request, render_template, flash, redirect, g
from flask_login import login_user, logout_user, current_user
from app.forms import LoginForm
from app.models import User
from datetime import datetime
from . import auth


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@auth.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('auth/login.html', title="login", form=form)
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,
                                           password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('auth.login'))
    login_user(registered_user, form.remember_me.data)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('home.index'))
'''
# NEW ...
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('home.dashboard'))
        elif registered_user is None:
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid email or password.')
    return render_template('auth/login.html', form=form, title='Login')
'''

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    user = User(request.form['username'], request.form['name'],
                request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))
