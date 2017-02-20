from app import app
from flask import render_template
from flask_login import login_required
from . import stud
from .forms import AddStudent, ViewStudent
from app.models import User, Student
import sqlite3 as sql


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%b %d, %Y'
    return native.strftime(format)
    

@stud.route('/add')
@login_required
def add():
    student = Student
    form = AddStudent()
    if form.validate_on_submit():
        student.timestamp = datetime.utcnow()
        student.name = form.name.data
        student.address = form.address.data
        student.dob = form.dob.data
        student.gender = form.gender.data
        student.goal = form.goal.data
        student.target = form.target.data
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
        form.occupation.data = student.occupation
        form.status.data = student.status
        form.days.data = student.days
        form.time.data = student.time
        form.dateEnroll.data = student.dateEnroll
        form.dateLastContact.data = student.dateLastContact
        form.lapsedWhy.data = student.lapsedWhy
        form.notes.data = student.notes


    return render_template('/stud/add.html',
                           title='Add Student', form=form)


@stud.route('/edit')
@login_required
def edit():
    return render_template('/stud/edit.html',
                           title='Edit Student')


@stud.route('/list')
@login_required
def list():
   con = sql.connect("app.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from students")

   rows = cur.fetchall();
   return render_template("/stud/list.html",rows = rows)


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
