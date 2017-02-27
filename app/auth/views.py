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
        '''
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            fullname=form.first_name.data,
                            password=form.password.data)

        '''
        if request.method == 'GET':
            return render_template('auth/register.html')
        user = User(request.form['username'], request.form['fullname'],
                    request.form['password'], request.form['email'])

        db.session.add(user)
        db.session.commit()
        flash('User successfully registered')
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
