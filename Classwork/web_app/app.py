#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set a secret key to use when validating form data
app.config["SECRET_KEY"] = "secret"

#define a constant value for url
URL = "http://127.0.0.1:5000/api/students/all"
#function to request student data from the api
#input is url
#output is JSON student data
def get_student_data(url):
    #make a request
    response = requests.get(url)
    #covert format to JSON
    response_json = response.json()
    return response_json

def get_unique_majors():
    

    student_list = get_student_data(URL)

    unique_majors = []
    for student in student_list:
        if student["major"] not in unique_majors:
            unique_majors.append(student["major"])
        else:
            continue
    unique_majors.sort()
    return unique_majors
#create a route for the site index page that will display all student data
@app.route("/", methods=['GET'])
def index():
    #get the student data
    #make a request to the student data api url
    url = "http://127.0.0.1:5000/api/students/all"

    student_data = get_student_data(url)

    #send the student data to the index.html page
    return render_template('index.html', student_data=student_data)

@app.route('/majors', methods=['GET'])
def majors():
    #write code that gets a unique list of majors from students data
    major_list = get_unique_majors()
    #get student data from the api: list of student dictionaries
    return render_template('majors.html', major_list = major_list)
@app.route('/majors', methods=['POST'])
def majors_post():
    major_list = get_unique_majors()
    result_list = []
    #get the form data that was submmitted
    major = request.form.get('major')
    #validate the form data. If invalid show error
    if not major:
        flash("You must select a major")
    else:
        #find students with the selected major and return to the majors.html page
        #get the student data
        url = "http://127.0.0.1:5000/api/students/all"
        student_list = get_student_data(URL)
        
        #loop through list of students. If student major equals major place students in result list
        for student in student_list:
            if student['major'] == major:
                result_list.append(student)
            else:
                continue
        #send the results list to the majors.html page

    return render_template('majors.html', major_list=major_list, result_list=result_list )
app.run(port=5005)