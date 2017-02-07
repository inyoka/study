from app import app
from flask import render_template, g
from flask_login import login_required


@app.route('/student/add')
@login_required
def addStudent():
    user = g.user
    return render_template('/student/add.html',
                           title='Add Student', user=user)


@app.route('/student/edit')
@login_required
def editStudent():
    user = g.user
    return render_template('/student/edit.html',
                           title='Edit Student', user=user)


@app.route('/student/list')
@login_required
def listStudents():
    user = g.user
    return render_template('/student/list.html',
                           title='List Students', user=user)


@app.route('/student/search')
@login_required
def searchStudent():
    user = g.user
    return render_template('/student/search.html',
                           title='Search', user=user)


@app.route('/student/delete')
@login_required
def deleteStudent():
    user = g.user
    return render_template('/student/delete.html',
                           title='Delete', user=user)
