from app import db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from . import stud
from .forms import AddStudent
from app.models import Student
import sqlite3 as sql
from datetime import date
from datetime import datetime


@stud.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    #id = Student.query.create(id)
    form = AddStudent()

    if form.is_submitted():
        print(form.errors)
        print("submitted")

    if form.validate():
        print(form.errors)
        print("valid")
    else:
        flash("Form not valid")
        print(form.errors)

    #if form.validate_on_submit():
    if form.submit.data and form.validate_on_submit():
        student = Student(fullname=form.fullname.data,
                          timestamp=datetime.utcnow(),
                          address=form.address.data,
                          dob=form.dob.data,
                          gender=form.gender.data,
                          goal=form.goal.data,
                          target=form.target.data,
                          occupation=form.occupation.data,
                          status=form.status.data,
                          days=form.days.data,
                          time=form.time.data,
                          dateEnroll=form.dateEnroll.data,
                          dateLastContact=form.dateLastContact.data,
                          lapsedWhy=form.lapsedWhy.data,
                          notes=form.notes.data)
        try:
            db.session.add(student)
            db.session.commit()
            flash('Your changes have been most likely been saved!?!')
        except:
            flash('Error writing reocrd.')
            return redirect(url_for('stud.add'))
    return render_template('/stud/add.html',
                           title='Add Student', form=form)


@stud.route('/edit')
@login_required
def edit(id):
    return render_template('/stud/edit.html',
                           title='Edit Student')



@stud.route('/list')
@login_required
def list():
    keys = Student.metadata.tables['students'].columns.keys()
    #keys = Student.__table__.columns.keys()
    con = sql.connect("app.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from students ORDER BY id")

    rows = cur.fetchall()
    return render_template("/list.html", keys=keys, rows=rows)


@stud.route('/search')
@login_required
def search():
    return render_template('/stud/search.html',
                           title='Search')


@stud.route('/view')
@login_required
def view():
    form = ViewStudent()

    return render_template('/stud/view.html', form=form)


@stud.route('/delete')
@login_required
def delete():

    return render_template('/stud/delete.html',
                           title='Delete')
