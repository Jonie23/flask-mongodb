from flask import render_template, request, json, Response
from application import app, db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/courses')
def courses():
    courseInfo = [
        {
            "courseID": "1111",
            "title": "Python for Data Science",
            "description": "Intro to Data Science with Python",
            "duration": "9 months",
            "term": "Cohort 3"
        },
        {
            "courseID": "2222",
            "title": "FullStack Web",
            "description": "Fullstack Web Development with Python & JavaScript",
            "duration": "9 months",
            "term": "Cohort 3"
        },
        {
            "courseID": "3333",
            "title": "Jamstack",
            "description": "React, Vue, MongoDB",
            "duration": "6 months",
            "term": "Cohort 1"
        },
        {
            "courseID": "4444",
            "title": "HTML & CSS",
            "description": "Intro to Web Development",
            "duration": "3 months",
            "term": "Cohort 5"
        }
    ]
    return render_template('courses.html', courseInfo=courseInfo)

    # print(courseInfo)

# create a class of users to connect to the database


class User(db.Document):
    userID = db.StringField(unique=True, sparse=True)
    firstName = db.StringField(max_length=60)
    lastName = db.StringField(max_length=60)
    email = db.StringField(max_length=60)
    password = db.StringField(max_length=30)

# create a route to display the users details
@app.route('/user')
def user():
    User(userID='001', firstName='Jones', lastName='Quartey',
         email='quarteyjonie18@gmail.com', password='123').save()

    User(userID='002', firstName='James', lastName='Quartey',
         email='jamesquartey@gmail.com', password='456').save()

    User(userID='003', firstName='Hilda', lastName='Laryea',
         email='hildalaryea@gmail.com', password='789').save()

    users = User.objects.all()
    return render_template('user.html', users=users)
