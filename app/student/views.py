from app import app
from flask import render_template, g
from flask_login import login_required


@student.route('/add')
@login_required
def addStudent():
    user = g.user
    return render_template('/student/add.html',
                           title='Add Student', user=user)


@student.route('/edit')
@login_required
def editStudent():
    user = g.user
    return render_template('/student/edit.html',
                           title='Edit Student', user=user)


@student.route('/list')
@login_required
def listStudents():
    user = g.user
    return render_template('/student/list.html',
                           title='List Students', user=user)


@student.route('/search')
@login_required
def searchStudent():
    user = g.user
    return render_template('/student/search.html',
                           title='Search', user=user)


@student.route('/delete')
@login_required
def deleteStudent():
    user = g.user
    return render_template('/student/delete.html',
                           title='Delete', user=user)
