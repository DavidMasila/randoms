from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField, EmailField, TextAreaField
from wtforms.validators import InputRequired, Length

class Student(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired(), Length(max=50)])
    lastname = StringField("Last Name", validators=[InputRequired(), Length(max=50)])
    email = EmailField("Email", validators=[InputRequired(), Length(min=10,max=100)])
    age = IntegerField("Age", validators=[InputRequired()])
    bio = TextAreaField("Bio", validators=[InputRequired()])
    add = SubmitField('Submit', render_kw={'class':'btn btn-primary mt-3'})
