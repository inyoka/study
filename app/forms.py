from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, FormField, FieldList, TextAreaField, DateField, SelectField, TextAreaField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import User, Student, Contact
from app import lookup


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    username = StringField('User.username', validators = [DataRequired()])
    about_me = TextAreaField('User.about_me', validators = [Length(min=0, max=140)])

    def __init__(self, original_username, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_username = original_username

    def validate(self):
        if not Form.validate(self): #Normal flask's built in check.
            return False
        if self.username.data == self.original_username: #If it's just the same, no worries
            return True
        user = User.query.filter_by(username=self.username.data).first() #Check database now for
        #the username guy wants
        if user != None: #If result returns non-none, already in use.
            self.username.errors.append('This username is already in use. Please choose another one.')
            return False
        return True

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
    status = SelectField('Student status :', validators=[DataRequired()]) # Active Inactive
    days = RadioField('Days available :', choices=lookup.DAYS, validators=[DataRequired()])  # 7 digit binary?
    time = IntegerField('Available from :', validators=[DataRequired()]) # Avail after %%:%% on weekday
    dateEnroll = DateField('Date enrolled :', format='%Y-%m-%d', validators=[DataRequired()])
    dateLastContact = DateField('Last contact :', format='%Y-%m-%d', validators=[DataRequired()])
    lapsedWhy = SelectField('Why they left :')
    notes = TextAreaField('Notes :', validators=[DataRequired()])
    submit = SubmitField('Submit')


'''
class AddContact(Form):
'''
'''
class EmailForm(Form):
    email = StringField('email', validators= [DataRequired()])
'''
'''
class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])
'''
