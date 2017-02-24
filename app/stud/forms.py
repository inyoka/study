from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectMultipleField, FormField
from wtforms.fields import FieldList, DateField, SelectField, TextAreaField
from wtforms.fields import RadioField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length
import wtforms.validators as validators
from app.models import Student
from app import lookup
from flask_wtf import Form
from wtforms.widgets import TextArea


class ContactForm(FlaskForm):
    id = Student.id
    mobile_phone = StringField('Number')
    e_mail = StringField('E-mail')


class AddStudent(FlaskForm):
    id = Student.id
    fullname = StringField('Name :', validators=[Length(min=4, max=80)])
    address = TextAreaField('Address :')
    dob = DateField('Date of Birth :')
    gender = SelectField('Gender', choices=lookup.GENDER, validators=[validators.optional()])
    # contacts = FieldList(FormField(ContactForm))
    goal = SelectField('Goal :', choices=lookup.GOAL)  # Qualification etc
    target = SelectField('Target  :', choices=lookup.TARGET)  # Skill needing improvment
    occupation = SelectField('Occupation :', validators=[DataRequired()])  # Current occupation
    status = SelectField('Student status :', choices=lookup.STATUS, validators=[DataRequired()])  # Active Inactive
    days = SelectMultipleField('Days available :', choices=lookup.DAYS, validators=[DataRequired()])  # 7 digit binary?
    time = IntegerField('Available from :')  # Avail after %%:%% on weekday
    dateEnroll = DateField('Date enrolled :', format='%Y-%m-%d')
    dateLastContact = DateField('Last contact :', format='%Y-%m-%d')
    lapsedWhy = SelectField('Why they left :', choices=lookup.LAPSED)
    notes = TextAreaField('Notes :')
    submit = SubmitField('submit', validators=[DataRequired()])


class ViewStudent(FlaskForm):
    fullname = StringField('Name :', validators=[DataRequired(), Length(min=4, max=80)])
