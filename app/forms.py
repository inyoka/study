from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, SelectMultipleField, FormField, FieldList, TextAreaField, DateField, SelectField, TextAreaField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import User, Student, Contact
from app import lookup


class LoginForm(FlaskForm):
    remember_me = BooleanField('remember_me', default=False)


class EditForm(FlaskForm):
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
