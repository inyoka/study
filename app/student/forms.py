from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, SelectMultipleField, FormField, FieldList, TextAreaField, DateField, SelectField, TextAreaField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import Student
from app import lookup

class ContactForm(Form):
    id = Student.id
    mobile_phone = StringField('Number')
    e_mail = StringField('E-mail')

class AddStudent(Form):
    name = StringField('Name :', validators=[DataRequired(), Length(min=4, max=80)])
    address = TextAreaField('Address :', validators=[DataRequired()])
    dob = DateField('Date of Birth :', validators=[DataRequired()])
    gender = RadioField('Male?', choices=[('0','Male'),('1','Female')])
    contacts = FieldList(FormField(ContactForm))
    goal = SelectField('Goal :', choices=lookup.GOAL, validators=[DataRequired()])  # Qualification etc
    target =  SelectField('Target  :', choices=lookup.TARGET, validators=[DataRequired()]) # Skill needing improvment
    occupation =  SelectField('Occupation :', validators=[DataRequired()]) # Current occupation
    status = SelectField('Student status :', choices=[('0','Pending'),('1','Active'), ('2','Inactive')], validators=[DataRequired()]) # Active Inactive
    days = SelectMultipleField('Days available :', choices=lookup.DAYS, validators=[DataRequired()])  # 7 digit binary?
    time = IntegerField('Available from :', validators=[DataRequired()]) # Avail after %%:%% on weekday
    dateEnroll = DateField('Date enrolled :', format='%Y-%m-%d', validators=[DataRequired()])
    dateLastContact = DateField('Last contact :', format='%Y-%m-%d', validators=[DataRequired()])
    lapsedWhy = SelectField('Why they left :')
    notes = TextAreaField('Notes :', validators=[DataRequired()])
    submit = SubmitField('Submit')
