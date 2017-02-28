# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError,\
    TextField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Email, EqualTo, Length
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired()])
    fullname = StringField('Name', validators=[InputRequired()])
    password = PasswordField('Password',
                             validators=[InputRequired(), EqualTo('confirm')])
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
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Login')


class EditForm(FlaskForm):
    username = StringField('Username : ', validators=[InputRequired()])
    about_me = TextAreaField('About you : ',
                             validators=[Length(min=0, max=140)])
