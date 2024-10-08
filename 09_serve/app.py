# Jady Lei
# 63
# SoftDev
# K09 -- Serve
# 2024-09-23
# time spent: 0.5

'''
DISCO:
Plug in 06 function to the helloworld

QCC:
0. 
'''


from flask import Flask

import csv
import random

with open("occupations.csv", newline="") as csvfile:
    #creates a dictionary for every row that can be parsed through
    reader = csv.DictReader(csvfile)
    jobs = []
    percents = []
    for row in reader:
        jobs.append(row['Job Class']), percents.append(float(row['Percentage']))
csvfile.close()
    
def RandomManual():
    # find a valid percentage, subtract percents until random <=0 and we can return the corresponding jobs
    rand = random.random() * percents[-1]
    for i in range(len(percents)):
        rand -= percents[i]
        if rand <= 0:
            return jobs[i]

def htmlOut():
    output = "<head><title>O9_serve</title></head>"
    output += "<body>"
    output += "\t <h1>63</h1>\n"
    output += "\t <p>Period 4</p>\n"
    output += "\t <p>Random: " + RandomManual() + "</p>\n"
    output += "\t <p>List of jobs:</p>\n"
    output += "\t <ul>"
    for job in jobs[:-1]:
        output += "\t \t <li>"
        output += job
        output += "</li> \n"
    output += "\t </ul> \n"
    output += "</body>"
    return output


app = Flask(__name__)        

@app.route("/")                         
def hello_world():
    print(__name__)                  
    return htmlOut()           

app.debug = True # also makes it so I don't have to reload the code every time.
app.run()                                



