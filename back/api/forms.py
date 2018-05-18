from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# validators
EMAIL = Email()
DATA_REQUIRED = DataRequired()


class SignUpForm(FlaskForm):
    username = StringField(label='Username', validators=[DATA_REQUIRED, Length(min=2, max=16)])
    email = StringField(label='Email', validators=[DATA_REQUIRED, Length(max=50), EMAIL])
    password = PasswordField(label='Password', validators=[DATA_REQUIRED, Length(max=32)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DATA_REQUIRED, EqualTo('password')])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField(label='Email', validators=[DATA_REQUIRED, Length(max=50), EMAIL])
    password = PasswordField(label='Password', validators=[DATA_REQUIRED, Length(max=32)])
    remember_me = BooleanField(label='Stay signed in')
    submit = SubmitField('Sign In')
