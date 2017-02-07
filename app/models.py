from app import db
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

    def avatar(self, size):
        return '/static/img/avatar/' + (self.username) + '.jpg'

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


class Student(db.Model):
    __tablename__='students'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)  # Record created
    name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String)
    dob = db.Column(db.DateTime)  # Calculate age
    gender = db.Column(db.Boolean, default=False, index=True) # M or F
    goal = db.Column(db.String)  # Qualification etc
    target = db.Column(db.String) # Skill needing improvment
    education = db.Column(db.String) # Level of Education
    occupation = db.Column(db.String) # Current occupation
    status = db.Column(db.Integer)
    days = db.Column(db.Integer)  # 7 digit binary?
    time = db.Column(db.Integer) # Avail after %%:%% on weekday
    dateEnroll = db.Column(db.DateTime)
    dateLastContact = db.Column(db.DateTime)
    lapsedWhy = db.Column(db.String)
    notes = db.Column(db.String)


class Contact(db.Model):
    __tablename__='contacts'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(64), index=True, unique=True)
    mobile = db.Column(db.Integer)
    email = db.Column(db.String(120))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self):
        return '<Contact %r>' % (self.label)


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % (self.name)


class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
