from flask import redirect, url_for, request, render_template
from app import app
from app.models import Students, db
from app.forms import Student

@app.route("/")
def index():
    students =  Students.query.all()
    return render_template('/index.html', students = students)

@app.route("/<int:student_id>")
def student(student_id):
    student =  Students.query.get_or_404(student_id)
    return render_template("/student.html", student=student)

@app.route("/create", methods=['GET','POST'])
def create():
    form =  Student()
    if form.validate_on_submit():
        student = Students(
            firstname = form.firstname.data,
            lastname = form.lastname.data,
            email = form.email.data,
            age = int(form.age.data),
            bio = form.bio.data
        )
        db.session.add(student)
        db.session.commit()
        form.process()
        return redirect(url_for('index'))
    return render_template("/create.html", form = form)