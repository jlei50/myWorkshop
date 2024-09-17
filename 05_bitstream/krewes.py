# Jady Lei
# 45
# SoftDev
# K05 -- Random from Bitstream
# 2024-09-17
# time spent:
# DISCO: 
# QCC: 
# OPS SUMMARY:

import random

f = open("krewes.txt", "r")
raw = f.read()
students = raw.split("@@@")

studentDict = {4: list(), 5: list()}

for student in students:
    student = student.split("$$$")
    student[0] = int(student[0])
    studentDict[student[0]].append(list(student[1], student[2]))


randnum = randrange(studentDict[4])
student = studentDict[4][randnum]
print("period: " + student[0] + " name: " + student[1] + " ducky name: " + student[2])