# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, TextField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo, Length

from ..models import User

class RegistrationForm(FlaskForm):
    """
    FlaskForm for users to create new account
    """
    email = StringField('Email', validators=[InputRequired(), Email(), Length(min=6, max=35)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=25)])
    fullname = StringField('Name', validators=[InputRequired(), Length(min=3, max=40)])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    username = TextField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    # remember_me = BooleanField('remember_me', default=False)
    # submit = SubmitField('Login')


    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True
