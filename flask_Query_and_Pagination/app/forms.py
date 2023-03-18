from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, EmailField, DateField, SubmitField
from wtforms.validators import InputRequired, Length
from wtforms.widgets import CheckboxInput


class InputForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired(), Length(max=100)])
    lastname = StringField('Last Name', validators=[InputRequired(), Length(max=100)])
    email = EmailField('Email', validators=[InputRequired(), Length(max=100)])
    age = IntegerField('Age', validators=[InputRequired()])
    hire_date = DateField('Hire Date', validators=[InputRequired()])
    active = BooleanField('Active: ')
    submit = SubmitField('Submit')