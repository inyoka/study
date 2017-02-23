import datetime
from app import db, lm
from sqlalchemy.sql import func

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(64))
    address = db.Column(db.String)
    timestamp = db.Column(db.DateTime)  # Record created
    dob = db.Column(db.DateTime(timezone=True), onupdate=func.now())  # Calculate age
    gender = db.Column(db.String)  # M or F
    goal = db.Column(db.String)  # Qualification etc
    target = db.Column(db.String)  # Skill needing improvment
    occupation = db.Column(db.String)  # Current occupation
    status = db.Column(db.String)
    days = db.Column(db.Integer)  # 7 digit binary?
    time = db.Column(db.Integer)  # Avail after %%:%% on weekday
    dateEnroll = db.Column(db.DateTime(timezone=True), server_default=func.now())

    dateLastContact = db.Column(db.Date)
    lapsedWhy = db.Column(db.String)
    notes = db.Column(db.String)

    def __init__(self, fullname, address, dob, gender, goal, target, occupation, status, days, time, dateEnroll=datetime.date.today()):
        self.fullname = fullname
        self.address = address
        self.dob = dob
        self.gender = gender
        self.goal = goal
        self.target = target
        self.occupation = occupation
        self.status = status
        self.days = days
        self.time = time
        self.dateEnroll = dateEnroll

    def __repr__(self):
        return "<Student ('%s', '%s', '%s', '%s')>" % (self.fullname, self.address, self.dob)


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(64), index=True, unique=True)
    mobile = db.Column(db.Integer)
    email = db.Column(db.String(120))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self):
        return '<Contact %r>' % (self.label)
