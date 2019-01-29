from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from app.model import User


class LoginForm(FlaskForm):
    username = StringField("Username" , validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different user name.')

    def validate_email(self,email):
        email_id = User.query.filter_by(email=email.data).first()
        if email_id is not None:
            raise ValidationError("Please enter a different email address.")

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About_me', validators=[Length(min= 1, max= 160)])
    submit = SubmitField('Submit')

    def __init__(self, org_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args,**kwargs)
        self.org_username = org_username

    def validate_username(self, username):
        if username.data != self.org_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Please use a different user name.')


class PostForm(FlaskForm):
    post = TextAreaField('Say Something', validators=[Length(min=1,max=140),DataRequired()])
    submit = SubmitField('Submit')




