
# Flask SQLAlchemy

Practice code for database management using SQLAlchemy and postgresql




### Commands Run on Terminal

Here is a bunch of code run on the flask shell to add values to our db table

from app.models import db, Students

student1 = Students(firstname='john', lastname='doe', email='jobdoe@example.com', age=23, bio='Biology student')
student1 = Students(firstname='david', lastname='masila', email='myself@example.com', age=25, bio='Chemistry student')
student1 = Students(firstname='you', lastname='yourself', email='youme@example.com', age=19, bio='Marine Biology student')

students = [student1, student2, student3]

db.session.add_all(students) -> When adding all as a list use .add(student) for single record
db.session.commit() -> Commit changes to the database 

user1 = db.session.query(Students).filter_by(firstname='john').first() -> Gets the first element
db.session.query(Students).filter_by(firstname='john').all()-> Self explanatory 
db.session.query(Students).filter(Students.firstname == 'john').first() -> Use either 

user1[0].firstname
>> Will give you the value in firstname from db -> Same criterion for the rest. 

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
