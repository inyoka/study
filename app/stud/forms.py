from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectMultipleField, FormField, DateTimeField
from wtforms.fields import FieldList, DateField, SelectField, TextAreaField
from wtforms.fields import RadioField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length
import wtforms.validators as validators
from app.models import Student
from app import lookup
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from wtforms.ext.sqlalchemy.orm import model_form


class ContactForm(FlaskForm):
    id = Student.id
    mobile_phone = StringField('Number')
    e_mail = StringField('E-mail')


class AddStudent(FlaskForm):
    id = Student.id
    fullname = StringField('Name :')
    gender = RadioField('Gender', coerce=str, choices=[('Male', 'Male'), ('Female', 'Female')])
    goal = SelectField('Professional Goal :', choices=[('none', 'None'), ('TOEFL', 'TOEFL'),('IELTS','IELTS'),('iGCSE','iGCSE'),('A-Levels','A-Levels'),('Professional','Professional Development'),('Personal','Personal Development'),('Overseas','Overseas Study')])  # Qualification etc
    target = SelectField('Personal aim :', choices=[('none', 'None'), ('spoken', 'Spoken'), ('grammar','Grammar'), ('reading','Reading'), ('listening','Listening'), ('writing','Writing'), ('exam','Exam'), ('conversation','Conversation')])  # Skill needing improvment
    occupation = StringField('Occupation :', validators=[DataRequired()])  # Current occupation
    status = SelectField('Student status :', choices=[('Pending', 'Pending'),('Active', 'Active'),('Inactive', 'Inactive')], validators=[DataRequired()])  # Active Inactive
    lapsedWhy = SelectField('Why they left :', choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Inactive', 'Inactive')])
    address = TextAreaField('Address :')
    dob = DateTimeField('Birthday :', format='%y/%m/%d')
    # contacts = FieldList(FormField(ContactForm))
    days = SelectMultipleField('Days :', choices=[('Sunday', 'Sunday'),('Monday', 'Monday'),('Tuesday', 'Tuesday'),('Wednesday', 'Wednesday'),('Thursday', 'Thursday'),('Friday', 'Friday'),('Saturday', 'Saturday')], validators=[DataRequired()])  # 7 digit binary?
    time = IntegerField('Available from :')  # Avail after %%:%% on weekday
    dateEnroll = DateField('Enrolled :')
    dateLastContact = DateField('Last contact :')
    notes = TextAreaField('Notes :')
    submit = SubmitField('submit', validators=[DataRequired()])


class ViewStudent(FlaskForm):
    fullname = StringField('Name :', validators=[DataRequired(), Length(min=4, max=80)])
