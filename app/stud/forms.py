from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectMultipleField, FormField, DateTimeField
from wtforms.fields import FieldList, DateField, SelectField, TextAreaField
from wtforms.fields import RadioField, IntegerField, SubmitField, HiddenField
#from wtforms.sqlalchemy.fields import QuerySelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email
import wtforms.validators as validators
from app.models import Student
from app.stud import lookup
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from wtforms.ext.sqlalchemy.orm import model_form
from .lookup import *


class ContactForm(FlaskForm):
    id = Student.id
    label = StringField('Enter label :')
    mobile_phone = StringField('Number')
    e_mail = StringField('E-mail')


class AddStudent(FlaskForm):
    id = Student.id
    fullname = StringField('Name :')
    gender = RadioField('Gender', coerce=str, choices=[('Male', 'Male'), ('Female', 'Female')])
    goal = SelectField('Professional Goal :', choices=gen(GOALS)) # Qualification etc
    target = SelectField('Personal aim :', choices=gen(TARGET))  # Skill needing improvment
    occupation = StringField('Occupation :', validators=[DataRequired()])  # Current occupation
    status = SelectField('Student status :', choices=gen(STATUS), validators=[DataRequired()])  # Active Inactive
    lapsedWhy = SelectField('Why they left :', choices=gen(LAPSED))
    address = TextAreaField('Address :')
    dob = DateTimeField('Birthday :', format='%y/%m/%d')
    # contacts = FieldList(FormField(ContactForm))
    days = SelectMultipleField('Days :', choices=gen(DAYS), validators=[DataRequired()])  # 7 digit binary?
    time = IntegerField('Available from :')  # Avail after %%:%% on weekday
    dateEnroll = DateField('Enrolled :')
    dateLastContact = DateField('Last contact :')
    notes = TextAreaField('Notes :')
    mobile = IntegerField("Mobile :")
    email = StringField('Email:', validators=[Email()])
    emer_contact = StringField("Emergency name :")
    emer_mobile = IntegerField("Emergency no. :")
    submit = SubmitField('Submit', validators=[DataRequired()])


class ViewStudent(FlaskForm):
    fullname = StringField('Name :', validators=[DataRequired(), Length(min=4, max=80)])
