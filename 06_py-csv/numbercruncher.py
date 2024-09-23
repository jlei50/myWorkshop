# Jady Lei
# 31
# SoftDev
# K06 -- python csv files
# 2024-09-16
# time spent:
# DISCO: We use DictReader to read a csv file into a list? of dictionaries. We then iterate through it to extract values.
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

def RandomManual():
    # find a valid percentage, subtract percents until random <=0 and we can return the corresponding jobs
    rand = random.random() * percents[-1]
    for i in range(len(percents)):
        rand -= percents[i]
        if rand <= 0:
            return jobs[i]
    

print(ReturnRandom())
print(RandomManual())