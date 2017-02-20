from app import app
from flask import render_template, g
from flask_login import login_required
from . import student
from .forms import AddStudent, ViewStudent
from app.models import User
import sqlite3 as sql


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
   con = sql.connect("app.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from students")

   rows = cur.fetchall();
   return render_template("/student/list.html",rows = rows)


@student.route('/search')
@login_required
def search():
    user = g.user
    return render_template('/student/search.html',
                           title='Search', user=user)


@student.route('/view')
@login_required
def view():
    form = ViewStudent()

    return render_template('/student/view.html', form=form)


@student.route('/delete')
@login_required
def delete():
    user = g.user
    return render_template('/student/delete.html',
                           title='Delete', user=user)
