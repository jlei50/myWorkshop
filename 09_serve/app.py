# Jady Lei
# 63
# SoftDev
# K09 -- Serve
# 2024-09-23
# time spent: 0.5

'''
DISCO:
Flask creates the website that runs the hello_world so we can see the "No hable queso!". It needs the virtual machine to run.

QCC:
0. creating a flask object with a name? like java?
1. Root Directory? or to seperate directories in a path
2. probably the shell? I don't see anything that could be __name__ in the website or terminal.
3. a name, it might be the website name or something that shows up in the terminal when ran.
4. it appears on the website
5. java!?!?! function from an object?
 ...

INVESTIGATIVE APPROACH:
Demoer showed that the scary looking terminal output is a link that works (:
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



