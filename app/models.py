from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, lm
from flask_login import UserMixin


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column("id", db.Integer, primary_key=True)
    fullname = db.Column("Fullname", db.String(64))
    gender = db.Column("Gender", db.String)  # M or F
    goal = db.Column("Goal", db.String)  # Qualification etc
    target = db.Column("Skill Req.", db.String)  # Skill needing improvment
    occupation = db.Column("Occupation", db.String)  # Current occupation
    status = db.Column("Status", db.String)
    lapsedWhy = db.Column("Lapsed", db.String)
    address = db.Column(db.String)
    notes = db.Column(db.String)
    days = db.Column(db.Integer)  # 7 digit binary?
    time = db.Column(db.DateTime)  # Avail after %%:%% on weekday
    timestamp = db.Column(db.DateTime)  # Record created
    dateLastContact = db.Column(db.Date)
    dob = db.Column(db.DateTime)
    dateEnroll = db.Column(db.DateTime())

    def __init__(self, fullname, address, dob, gender, goal, target, occupation,
                 status, days, time, dateEnroll=datetime.now()):
        self.fullname = fullname
        self.gender = gender
        self.goal = goal
        self.target = target
        self.occupation = occupation
        self.address = address
        self.dob = dob
        self.status = status
        self.days = days
        self.time = time
        self.dateEnroll = dateEnroll

    def __repr__(self):
        return "<Student ('%s', '%s', '%s')>" % (self.fullname,
                                                 self.address,
                                                 self.dob)


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(64), index=True, unique=True)
    mobile = db.Column(db.Integer)
    email = db.Column(db.String(120))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self):
        return '<Contact %r>' % (self.label)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column("Email", db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    fullname = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)
    # User account details ... (from Miguel Grinbergs)
    registered_on = db.Column('registered_on', db.DateTime)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    def __init__(self, username, fullname, password, email):
        self.username = username
        self.fullname = fullname
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

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

    # Avatar file location
    def avatar(self, size):
        def avatar(self, size):
            #return '/static/img/avatar/%s.jpg' % self.username.tolower()
            return '/static/img/avatar/default.png'



    def __repr__(self):
        return '<User %r>' % (self.username)


# Set up user_loader
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('User', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % (self.name)


class Post(db.Model):  # Miguel Grinberg
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
