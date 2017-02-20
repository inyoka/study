from app import app
from flask import render_template, g
from flask_login import login_required
from . import stud
from .forms import AddStudent, ViewStudent
from app.models import User, Student
import sqlite3 as sql


@stud.route('/add')
@login_required
def add():
    form = AddStudent()
    if form.validate_on_submit():
        student.timestamp = datetime.utcnow()
        student.name = form.name.data
        student.address = form.address.data
        student.dob = form.dob.data
        student.gender = form.gender.data
        student.goal = form.goal.data
        student.target = form.target.data
        student.education = form.education.data
        student.occupation = form.occupation.data
        student.status = form.status.data
        student.days = form.days.data
        student.time = form.time.data
        student.dateEnroll = form.dateEnroll.data
        student.dateLastContact = form.dateLastContact.data
        student.lapsedWhy = form.lapsedWhy.data
        student.notes = form.notes.data
        db.session.add(student)
        db.session.commit()
        flash('Your changes have been most likely been saved!?!')
        return redirect(url_for('edit'))
    else:
        form.name.data = student.name
        form.address.data = student.address
        form.dob.data = student.dob
        form.gender.data = student.gender
        form.goal.data = student.goal
        form.target.data = student.target
        form.education.data = student.education
        form.occupation.data = student.occupation
        form.status.data = student.status
        form.days.data = student.days
        form.time.data = student.time
        form.dateEnroll.data = student.dateEnroll
        form.dateLastContact.data = student.dateLastContact
        form.lapsedWhy.data = student.lapsedWhy
        form.notes.data = student.notes


    return render_template('/student/add.html',
                           title='Add Student', form=form, user=user)


@stud.route('/edit')
@login_required
def edit():
    user = g.user
    return render_template('/student/edit.html',
                           title='Edit Student', user=user)


@stud.route('/list')
@login_required
def list():
   con = sql.connect("app.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from students")

   rows = cur.fetchall();
   return render_template("/student/list.html",rows = rows)


@stud.route('/search')
@login_required
def search():
    user = g.user
    return render_template('/student/search.html',
                           title='Search', user=user)


@stud.route('/view')
@login_required
def view():
    form = ViewStudent()

    return render_template('/student/view.html', form=form)


@stud.route('/delete')
@login_required
def delete():
    user = g.user
    return render_template('/student/delete.html',
                           title='Delete', user=user)
