from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, EmailField, PasswordField
from wtforms.validators import input_required, Length


class Loginform(FlaskForm):
    email = EmailField('Email: ', validators=[input_required(), Length(max=50)])
    password = PasswordField('Password: ', validators=[input_required(), Length(max=50)])
    remember = BooleanField('Remember me: ')
    submit = SubmitField('Log In')

class Signupform(FlaskForm):
    email = EmailField('Email: ', validators=[input_required(), Length(max=50)])
    username = StringField('Username: ', validators=[input_required(), Length(max=50)])
    password = PasswordField('Password: ', validators=[input_required(), Length(max=50)])
    submit = SubmitField('Sign Up')