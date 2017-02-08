from app import app, db, lm
from flask import url_for, request, render_template, flash, redirect, session, g
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, EditForm  # , PostForm, EmailForm
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


@app.route('/')
@app.route('/index')
def index():
    user = g.user
    posts = [
        {
            'author': {'username': 'Simon'},
            'body': 'This is the CaSE Database Development Page!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', title="login", form=form)
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,
                                           password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user, form.remember_me.data)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/student/add')
@login_required
def addStudent():
    return render_template('/student/add.html', title='Add Student', user=user)


@app.route('/student/edit')
@login_required
def editStudent():
    return render_template('/student/edit.html',
                           title='Edit Student', user=user)


@app.route('/student/list')
@login_required
def listStudents():
    return render_template('/student/list.html',
                           title='List Students', user=user)


@app.route('/student/search')
@login_required
def searchStudent():
    return render_template('/student/search.html', title='Search', user=user)


@app.route('/student/delete')
@login_required
def deleteStudent():
    return render_template('/student/delete.html', title='Delete', user=user)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User %s not found.' % username)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.username)
    if form.validate_on_submit():
        g.user.username = form.username.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    else:
        form.username.data = g.user.username
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error/500.html'), 500
