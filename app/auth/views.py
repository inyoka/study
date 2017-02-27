# app/auth/old-views.py
from app import db, lm
from flask import url_for, request, render_template, flash, redirect, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegistrationForm
from app.models import User
from datetime import datetime
from . import auth
import sqlite3 as sql





@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                            username=form.username.data,
                            fullname=form.fullname.data,
                            password=form.password.data)

        # add employee to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')



@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if request.method == 'GET':
        return render_template('auth/login.html', title="login", form=form)
    user = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=user).first()
    if registered_user is None:
        flash('Username is invalid', 'error')
        return redirect(url_for('auth.login'))
    login_user(registered_user, form.remember_me.data)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('home.index'))
    '''

    form = LoginForm()
    if form.validate_on_submit():
        login_user(user)
        session['remember_me'] = form.remember_me.data  # Does user want remembering?

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('home.index'))
    return render_template('auth/login.html', title='Sign-In', form=form)
    '''

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@auth.route('/list')
@login_required
def list():
    keys = User.__table__.columns.keys()
    con = sql.connect("app.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from users ORDER BY id")

    rows = cur.fetchall()
    return render_template("/list.html",title="List Authenticated Users", keys=keys, rows=rows)
