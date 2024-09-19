# Jady Lei
# 31
# SoftDev
# K06 -- python csv files
# 2024-09-16
# time spent:
# DISCO: 
# QCC: 
# OPS SUMMARY:

import csv
import random

with open("occupations.csv", newline="") as csvfile:
    #creates a dictionary for every row that can be parsed through
    reader = csv.DictReader(csvfile)
    jobs = []
    percents = []
    for row in reader:
        jobs.append(row['Job Class']), percents.append(float(row['Percentage']))

def ReturnRandom():
# random.choices returns a list, [:-1] to ignore last row, k is returned list size
    return (random.choices(jobs[:-1], weights=percents[:-1], k=1)[0])

print(ReturnRandom())