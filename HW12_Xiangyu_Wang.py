"""SSW810 HomeWork Week 12
    Xiangyu Wang"""

from flask import Flask, render_template, request
import sqlite3
DB_FILE = '810_startup.db'   # Global constant

app = Flask(__name__)


@app.route('/instructors')
def show_instructors_courses():
    """display a summary of each Instructor with her CWID, Name, Department, Course, and the number of students in
    the course. """

    query = """SELECT instructors.CWID, instructors.Name, instructors.Dept, grades.Course, count(*) as 'Students'
                From instructors join grades on instructors.CWID = grades.InstructorCWID group by course,CWID"""  # Sqlite commend
    db = sqlite3.connect(DB_FILE)  # Connecting to database file
    results = db.execute(query)  # Get results

    rows = [{'cwid': cwid, 'name': name, 'department': department, 'course': course, 'students': students} for
            cwid, name, department, course, students in results]  # convert information we need into JSON format
    db.close()  # Close database file

    return render_template('show_instructor_courses.html',
                           title="Stevens Repository",
                           table_title="Courses and student counts",
                           rows=rows)  # Pass information to Jinja format


app.run(debug=True)
