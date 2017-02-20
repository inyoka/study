from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, lm


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True)
    password = db.Column(db.String(10))
    registered_on = db.Column('registered_on', db.DateTime)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, name, password, email):
        self.username = username
        self.name = name
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

    def avatar(self, size):
        return '/static/img/avatar/' + (self.username) + '.jpg'

    # Password settings from scotch.io flask crud web app part 1
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def make_unique_username(username):
        if User.query.filter_by(username=username).first() is None:
            return username
        version = 2
        while True:
            new_username = username + str(version)
            if User.query.filter_by(username=new_username).first() is None:
                break
            version += 1
        return new_username


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Departments(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('User', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)  # Record created
    name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String)
    dob = db.Column(db.Date)  # Calculate age
    gender = db.Column(db.Boolean, default=False, index=True)  # M or F
    goal = db.Column(db.String)  # Qualification etc
    target = db.Column(db.String)  # Skill needing improvment
    occupation = db.Column(db.String)  # Current occupation
    status = db.Column(db.Integer)
    days = db.Column(db.Integer)  # 7 digit binary?
    time = db.Column(db.Integer)  # Avail after %%:%% on weekday
    dateEnroll = db.Column(db.Date)
    dateLastContact = db.Column(db.Date)
    lapsedWhy = db.Column(db.String)
    notes = db.Column(db.String)

    def __init__(self, name, address, dob, gender, goal, target, occupation, status, days, time, dateEnroll):
        self.name = name
        self.address = address
        self.dob = dob
        self.gender = gender
        self.goal = goal
        self.target = target
        self.occupation = occupation
        self.status = status
        self.days = days
        self.time = time
        self.dateEnroll = datetime.utcnow()

    def __repr__(self):
        return "<Student ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.name, self.address, self.dob, self.gender, self.goal, self.target, self.occupation, self.status, self.days, self.time, self.dateEnroll)



class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(64), index=True, unique=True)
    mobile = db.Column(db.Integer)
    email = db.Column(db.String(120))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self):
        return '<Contact %r>' % (self.label)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % (self.name)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
