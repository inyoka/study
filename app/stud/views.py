from app import db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from . import stud
from .forms import AddStudent
from app.models import Student
import sqlite3 as sql
from datetime import date
from datetime import datetime


@stud.route('/modify/')
@login_required
def add_modify():
    form = AddStudent()

    return render_template("stud/data.html", action="Add", data_type="a student", form=form)


@stud.route('/modify/<int:student_id>')
@login_required
def edit_modify(student_id):
    student = Student(query.get_or_404(student_id))
    form = AddStudent()

    return render_template("stud/data.html", action="Edit", data_type="student.fullname", form=form)


@stud.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    #id = Student.query.create(id)
    form = AddStudent()

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


@stud.route('/edit/', methods=['GET', 'POST'])
@login_required
def edit():
    student = Student(query.get_or_404(id))
    form = AddStudent(obj=student)
    if form.validate_on_submit():
        form.populate_obj(student)
        '''
        student.fullname = form.fullname.data
        student.gender = form.gender.data
        student.goal = form.goal.data
        student.target = form.target.data
        student.occupation = form.occuptation.data
        student.status = form.status.data
        student.lapsedWhy = form.lapsedWhy.data
        student.address = form.address.data
        student.notes = form.notes.data
        student.days = form.days.data
        student.time = form.time.data
        student.timestamp = form.timestamp.data
        student.dateLastContact = form.dateLastContact.data
        student.dob = form.dob.data
        student.dateEnroll = form.dateEnroll.data

        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('auth.edit'))
    else:
        form.username.data = g.user.username
        form.about_me.data = g.user.about_me
    return render_template('/auth/edit.html', title='Edit Your Profile', form=form)
return render_template('/stud/edit.html',
                       title='Edit Student')
        '''


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
    return render_template("/home/list.html", title="List Students", keys=keys, rows=rows)

@stud.route('/lister')
@login_required
def lister():
    keys = Student.metadata.tables['students'].columns.keys()
    #keys = Student.__table__.columns.keys()
    con = sql.connect("app.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from students ORDER BY id")

    rows = cur.fetchall()
    return render_template("/stud/lister.html", title="List Students", keys=keys, rows=rows)

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
