from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from app.model import User
from flask_babel import lazy_gettext as _l
from flask_babel import _



class LoginForm(FlaskForm):
    username = StringField(_l("Username") , validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    remember_me = BooleanField(_l("Remember me"))
    submit = SubmitField(_l('Sign in'))


class RegistrationForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    password2 = PasswordField(_l('Repeat Password'),validators=[DataRequired(), EqualTo('password')])
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different user name.'))

    def validate_email(self,email):
        email_id = User.query.filter_by(email=email.data).first()
        if email_id is not None:
            raise ValidationError(_("Please enter a different email address."))

class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About_me'), validators=[Length(min= 1, max= 160)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, org_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args,**kwargs)
        self.org_username = org_username

    def validate_username(self, username):
        if username.data != self.org_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different user name.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say Something'), validators=[Length(min=1,max=140),DataRequired()])
    submit = SubmitField(_l('Submit'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    password2 = PasswordField(_l("'Repeat Password'"), validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField(_l('Request Password Reset'))





