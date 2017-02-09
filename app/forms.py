from flask_wtf import Form

from wtforms.fields import StringField, BooleanField, TextAreaField, DateField, SelectField, TextAreaField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import User, Student, Contact


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


class AddStudent(Form):
    name = StringField('Name :', validators=[DataRequired(), Length(min=4, max=80)])
    address = TextAreaField('Address :', validators=[DataRequired()])
    dob = DateField('Date of Birth :', validators=[DataRequired()])
    gender = RadioField('Male?', choices=[('value','Male'),('value_two','Female')])
    goal = SelectField(' :', validators=[DataRequired()])  # Qualification etc
    target =  SelectField(' :', validators=[DataRequired()]) # Skill needing improvment
    occupation =  SelectField(' :', validators=[DataRequired()]) # Current occupation
    status = SelectField(' :', validators=[DataRequired()]) # Active Inactive
    days = RadioField(' :', validators=[DataRequired()])  # 7 digit binary?
    time = IntegerField(' :', validators=[DataRequired()]) # Avail after %%:%% on weekday
    dateEnroll = DateField(' :', validators=[DataRequired()])
    dateLastContact = DateField(' :', validators=[DataRequired()])
    lapsedWhy = SelectField(' :', validators=[DataRequired()])
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
