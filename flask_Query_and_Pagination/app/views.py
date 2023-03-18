from app import app
from flask import render_template, redirect, request, url_for
from app.forms import InputForm
from app.models import db, Employee
from datetime import date


@app.route("/")
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route("/add_employee", methods=['GET', 'POST'])
def add_employee():
    form = InputForm()
    if form.validate_on_submit():
        employee = Employee(
            firstname = form.firstname.data,
            lastname = form.lastname.data,
            email = form.email.data,
            age = form.age.data,
            hire_date = form.hire_date.data,
            active = form.active.data
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('/form.html', form=form)
