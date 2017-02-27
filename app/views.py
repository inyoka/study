from app import app, db, lm
from flask import url_for, request, render_template, flash, redirect, session, g
from flask_login import login_user, logout_user, current_user, login_required
from app.auth.forms import LoginForm, EditForm # , PostForm, EmailForm
from app.models import User
from datetime import datetime


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()



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


@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='Forbidden'), 403


@app.errorhandler(404)
def not_found_error(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error/500.html'), 500
