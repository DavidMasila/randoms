from app import app
from flask import render_template, url_for, request, redirect, flash
from app.forms import CreateForms

courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
}]


@app.route("/", methods=["GET", "POST"])
def index():
    form = CreateForms()
    if form.validate_on_submit():

        flash("new course added successfully")
        isAvailable = ''
        if form.available.data == 'True':
            isAvailable = 'Yes'
        else:
            isAvailable = 'No'

        courses_list.append({
            'title': request.form.get('title'),
            'description': request.form['description'],
            'price': form.price.data,
            'level': form.level.data,
            'available': isAvailable
        })
        return redirect(url_for('courses'))
    return render_template("/index.html", form=form)


@app.route("/courses")
def courses():
    return render_template("/courses.html", courses_list=courses_list)
