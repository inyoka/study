from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, SelectMultipleField, FormField, FieldList, TextAreaField, DateField, SelectField, TextAreaField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import Student
from app import lookup

class ContactForm(FlaskForm):
    id = Student.id
    mobile_phone = StringField('Number')
    e_mail = StringField('E-mail')

class AddStudent(FlaskForm):
    name = StringField('Name :', validators=[DataRequired(), Length(min=4, max=80)])
    address = TextAreaField('Address :', validators=[DataRequired()])
    dob = DateField('Date of Birth :', validators=[DataRequired()])
    gender = RadioField('Male?', choices=[('Male','Male'),('Female','Female')])
    contacts = FieldList(FormField(ContactForm))
    goal = SelectField('Goal :', choices=lookup.GOAL, validators=[DataRequired()])  # Qualification etc
    target =  SelectField('Target  :', choices=lookup.TARGET, validators=[DataRequired()]) # Skill needing improvment
    occupation =  SelectField('Occupation :', validators=[DataRequired()]) # Current occupation
    status = SelectField('Student status :', choices=[('Pending','Pending'),('Active','Active'), ('Inactive','Inactive')], validators=[DataRequired()]) # Active Inactive
    days = SelectMultipleField('Days available :', choices=lookup.DAYS, validators=[DataRequired()])  # 7 digit binary?
    time = IntegerField('Available from :', validators=[DataRequired()]) # Avail after %%:%% on weekday
    dateEnroll = DateField('Date enrolled :', format='%Y-%m-%d', validators=[DataRequired()])
    dateLastContact = DateField('Last contact :', format='%Y-%m-%d', validators=[DataRequired()])
    lapsedWhy = SelectField('Why they left :')
    notes = TextAreaField('Notes :', validators=[DataRequired()])

class ViewStudent(FlaskForm):
    name = StringField('Name :', validators=[DataRequired(), Length(min=4, max=80)])
