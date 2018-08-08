from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, BooleanField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from user_db.models import User

# validators

EMAIL = Email()
DATA_REQUIRED = DataRequired()


class SignUpForm(FlaskForm):
    username = StringField(label='Username', validators=[DATA_REQUIRED, Length(min=2, max=16)])
    email = StringField(label='Email', validators=[DATA_REQUIRED, Length(max=50), EMAIL])
    password = PasswordField(label='Password', validators=[DATA_REQUIRED, Length(max=32)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DATA_REQUIRED, EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class SignInForm(FlaskForm):
    email = StringField(label='Email', validators=[DATA_REQUIRED, Length(max=50), EMAIL])
    password = PasswordField(label='Password', validators=[DATA_REQUIRED, Length(max=32)])
    remember_me = BooleanField(label='Stay signed in')
    submit = SubmitField('Sign In')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                print ValidationError('That email is taken. Please choose a different one.')
