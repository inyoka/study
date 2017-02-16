# app/auth/views.py
from flask import url_for, request, render_template, flash, redirect, session, g

#from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User


'''
@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    user = User(request.form['username'], request.form['password'], request.form['email'], request.form['name'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('auth.login'))
'''
@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an user to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                            username=form.username.data,
                            name=form.name.data,
                            password=form.password.data)

        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering. Please login below ...')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


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
        flash('Username is invalid', 'error')
        return redirect(url_for('auth.login'))
    elif not user.verify_password(form.password.data):
            flash('Password is invalid', 'error')
            return redirect(url_for('auth.login'))
    login_user(registered_user, form.remember_me.data)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('home.index'))


'''
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        # check whether user exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            # log user in
            login_user(user)

            # redirect to the dashboard page after login
            return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')
'''

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))

'''
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))

'''
