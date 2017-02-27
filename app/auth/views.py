# app/auth/old-views.py
from app import db
from flask import url_for, request, render_template, flash, redirect
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from app.models import User
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

        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if request.method == 'GET':
        return render_template('auth/login.html', title="login", form=form)
    user = request.form['username']
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
    return render_template("/home/list.html", title="List Authenticated Users",
                           keys=keys, rows=rows)


@app.route('/profile/<username>')
@login_required
def viewProfile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User %s not found.' % username)
        return redirect(url_for('home.index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('/profile/view.html',
                           user=user,
                           posts=posts)


@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def editProfile():
    form = EditForm(g.user.username)
    if form.validate_on_submit():
        g.user.username = form.username.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('editProfile'))
    else:
        form.username.data = g.user.username
        form.about_me.data = g.user.about_me
    return render_template('/profile/edit.html', form=form)
