from app import app
from flask import render_template, g
from flask_login import login_required
from . import student
from .forms import AddStudent


@student.route('/add')
@login_required
def add():
    form = AddStudent()
    user = g.user
    return render_template('/student/add.html',
                           title='Add Student', form=form, user=user)


@student.route('/edit')
@login_required
def edit():
    user = g.user
    return render_template('/student/edit.html',
                           title='Edit Student', user=user)


@student.route('/list')
@login_required
def list():
    user = g.user
    return render_template('/student/list.html',
                           title='List Students', user=user)


@student.route('/search')
@login_required
def search():
    user = g.user
    return render_template('/student/search.html',
                           title='Search', user=user)


@student.route('/delete')
@login_required
def delete():
    user = g.user
    return render_template('/student/delete.html',
                           title='Delete', user=user)
