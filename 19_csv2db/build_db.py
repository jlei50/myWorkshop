# Jady Lei
# 45
# SoftDev
# K19 SQL
# 2024-10-18

import csv
import sqlite3 #enable SQLite operations

DB_FILE="discobandit.db"
#open db if exists, otherwise create
db = sqlite3.connect(DB_FILE) 
c = db.cursor() #facilitate db ops

c.execute("DROP TABLE courses")
db.commit()
# c.execute("DROP TABLE students")

command = "CREATE TABLE courses(code, mark, id)"
c.execute(command)
db.commit()
with open("courses.csv", newline="") as csvfile:
    #creates a dictionary for every row that can be parsed through
    coursesRaw = csv.DictReader(csvfile)
    for course in coursesRaw:
        command = f"INSERT INTO courses VALUES ({course['code']}, {course['mark']}, {course['id']})"
        # {course['code']}, {course['mark']}, {course['id']}
#         val = (course['code'], course['mark'], course['id'])
        c.execute(command)
        db.commit()
    
# command = "CREATE TABLE students (name, age, id)"
# c.execute(command)
# with open("students.csv", newline="") as csvfile:
#     #creates a dictionary for every row that can be parsed through
#     studentsRaw = csv.DictReader(csvfile)
#     for student in studentsRaw:
#         command = f"INSERT INTO students (name, age, id) VALUES (%s, %s, %s)"
#         val = (student['name'], student['age'], student['id'])
#         c.execute(command, val)


db.commit() #save changes
db.close()