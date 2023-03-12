from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, RadioField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length


# Class to create the form
class CreateForms(FlaskForm):
    title = StringField('Title', validators=[
                        InputRequired(), Length(min=10, max=100)])
    description = TextAreaField('Description', validators=[
                                InputRequired(), Length(max=500)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level', validators=[InputRequired()], choices=[
                       'Beginner', 'Intermediate', 'advanced'], render_kw={'class': 'no-bullet'})
    available = BooleanField('Available', default='checked')
    add = SubmitField('Add')
