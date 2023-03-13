from flask import redirect, url_for, render_template, request, flash
from app import app
from app.models import db, Students
from app.forms import Student


@app.route("/")
def index():
    students = Students.query.all()
    return render_template('/index.html', students=students)


@app.route("/<int:student_id>")
def student(student_id):
    student = Students.query.get_or_404(student_id)
    return render_template("/student.html", student=student)


@app.route("/create", methods=['GET', 'POST'])
def create():
    form = Student()
    if form.validate_on_submit():
        if Students.query.filter_by(email=form.email.data).first():
            flash("That email Has an account already.")
            form.process()
        else:
            if request.method == 'POST':
                student = Students(
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    age=int(form.age.data),
                    bio=form.bio.data
                )
                db.session.add(student)
                db.session.commit()
                form.process()
            return redirect(url_for('index'))
    return render_template("/create.html", form=form)


@app.route("/<int:student_id>/edit/", methods=['GET','POST'])
def edit(student_id):
    form = Student()
    student = Students.query.get_or_404(student_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = form.bio.data

        student.firstname = firstname
        student.lastname = lastname
        student.email = email 
        student.age = age
        student.bio = bio

        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('/edit.html', student=student, form = form)


@app.route("/<int:student_id>/delete/", methods=['GET','POST'])
def delete(student_id):
    student = Students.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))



