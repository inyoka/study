# app/auth/iews.py
from flask import url_for, render_template, flash, redirect, g
from flask_login import login_user, logout_user, login_required

from app.auth.forms import LoginForm, RegistrationForm, EditForm
from app.auth import auth
from app import db
from app.models import User
import sqlite3 as sql


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.errors)

    if form.is_submitted():
        print("submitted")

    if form.validate():
        print("valid")

    print(form.errors)
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    fullname=form.fullname.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Successfully registered, please login.')

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(
                form.password.data):

            login_user(user, form.remember_me.data)
            flash('Logged in successfully')

            if user.is_admin:
                return redirect(url_for('home.index'))
            else:
                return redirect(url_for('home.index'))
        else:
            flash('Invalid email or password.')

    return render_template('auth/login.html', form=form, title='Login')


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
    return render_template("/home/list.html", title="List Authenticated Users",
                           keys=keys, rows=rows)


@auth.route('/<username>')
@login_required
def view(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User %s not found.' % username)
        return redirect(url_for('home.index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('/auth/view.html',
                           user=user,
                           posts=posts)


@auth.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.username)
    if form.validate_on_submit():
        g.user.username = form.username.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('auth.edit'))
    else:
        form.username.data = g.user.username
        form.about_me.data = g.user.about_me
    return render_template('/auth/edit.html', form=form)
