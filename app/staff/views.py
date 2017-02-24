# app/staff/old-views.py
from app import db, lm
from flask import url_for, request, render_template, flash, redirect, g
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm
from app.models import User
from datetime import datetime
from . import staff
import sqlite3 as sql



@staff.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('staff/login.html', title="login", form=form)
    user = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=user).first()
    if registered_user is None:
        flash('Username is invalid', 'error')
        return redirect(url_for('staff.login'))
    login_user(registered_user, form.remember_me.data)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('home.index'))


@staff.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('staff/register.html')
    user = User(request.form['username'], request.form['fullname'],
                request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('staff.login'))


@staff.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@staff.route('/list')
@login_required
def list():
    con = sql.connect("app.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from users ORDER BY id")

    rows = cur.fetchall()
    return render_template("/staff/list.html", rows=rows)
