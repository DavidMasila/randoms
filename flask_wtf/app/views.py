from app import app
from flask import render_template, url_for, request, redirect
from app.forms import CreateForms

courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]


@app.route("/", methods=["GET","POST"])
def index():
    form = CreateForms()
    return render_template("/index.html", form=form)

@app.route("/courses")
def courses():
    return render_template("/courses.html", courses_list = courses_list)