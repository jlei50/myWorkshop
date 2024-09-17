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

studentDict = {4: [], 5: []}

for student in students:
    student = student.split("$$$")
    if len(student) > 1:
        studentDict[int(student[0])].append([student[1], student[2]])

randpd = 4
randnum = random.randint(0, len(studentDict[4]))
student = studentDict[4][randnum]
# print(student)
print("period: " + randpd + " name: " + student[0] + " ducky name: " + student[1])