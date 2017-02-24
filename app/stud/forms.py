from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectMultipleField, FormField, DateTimeField
from wtforms.fields import FieldList, DateField, SelectField, TextAreaField
from wtforms.fields import RadioField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length
import wtforms.validators as validators
from app.models import Student
from app import lookup
from flask_wtf import Form
from wtforms.widgets import TextArea
from wtforms.ext.sqlalchemy.orm import model_form


class ContactForm(Form):
    id = Student.id
    mobile_phone = StringField('Number')
    e_mail = StringField('E-mail')


class AddStudent(Form):

    id = Student.id
    fullname = StringField('Name :', validators=[Length(min=4, max=80)])
    gender = RadioField('Gender', coerce=str, choices=[('Male', 'Male'), ('Female', 'Female')], validators=[validators.optional()])
    goal = SelectField('Goal :', choices=[('none', 'None'), ('TOEFL', 'TOEFL'),('IELTS','IELTS'),('iGCSE','iGCSE'),('A-Levels','A-Levels'),('Professional','Professional Development'),('Personal','Personal Development'),('Overseas','Overseas Study')])  # Qualification etc
    target = SelectField('Target  :', choices=[('none', 'None'), ('spoken', 'Spoken'), ('grammar','Grammar'), ('reading','Reading'), ('listening','Listening'), ('writing','Writing'), ('exam','Exam'), ('conversation','Conversation')])  # Skill needing improvment
    occupation = StringField('Occupation :', validators=[DataRequired()])  # Current occupation
    status = SelectField('Student status :', choices=[('Pending', 'Pending'),('Active', 'Active'),('Inactive', 'Inactive')], validators=[DataRequired()])  # Active Inactive
    lapsedWhy = SelectField('Why they left :', choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Inactive', 'Inactive')])
    address = TextAreaField('Address :')
    dob = DateTimeField('Date of Birth :', format='%y/%m/%d')
    # contacts = FieldList(FormField(ContactForm))
    days = SelectMultipleField('Days available :', choices=[('Sunday', 'Sunday'),('Monday', 'Monday'),('Tuesday', 'Tuesday'),('Wednesday', 'Wednesday'),('Thursday', 'Thursday'),('Friday', 'Friday'),('Saturday', 'Saturday')], validators=[DataRequired()])  # 7 digit binary?
    time = IntegerField('Available from :')  # Avail after %%:%% on weekday
    dateEnroll = DateField('Date enrolled :', format='%Y-%m-%d')
    dateLastContact = DateField('Last contact :', format='%Y-%m-%d')
    notes = TextAreaField('Notes :')
    submit = SubmitField('submit', validators=[DataRequired()])


class ViewStudent(Form):
    fullname = StringField('Name :', validators=[DataRequired(), Length(min=4, max=80)])
