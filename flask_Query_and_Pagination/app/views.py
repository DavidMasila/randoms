from app import app
from flask import render_template, redirect, request, url_for
from app.forms import InputForm
from app.models import db, Employee
from flask_paginate import Pagination, get_page_parameter


@app.route("/")
def index():
    page = request.args.get(get_page_parameter(), default=1, type=int)
    employees = Employee.query.order_by(
        Employee.firstname).paginate(page=page, per_page=2)
    # pagination = Pagination(
    #     page=page, per_page=2, total=Employee.query.count(), css_framework='bootstrap5')
    return render_template('index.html', employees=employees)


@app.route("/add_employee", methods=['GET', 'POST'])
def add_employee():
    form = InputForm()
    if form.validate_on_submit():
        employee = Employee(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            age=form.age.data,
            hire_date=form.hire_date.data,
            active=form.active.data
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('/form.html', form=form)
