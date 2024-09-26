# Jady Lei
# SoftDev Pd 4
# Sep 26 2024 

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
then the render_template function would not be imported, and could
not be used.

Q1:
http://127.0.0.1:5000/my_foist_template

Q2:
the returned website content is an html file. The html files have a
foo and collection variable that the extra arguments in the line
likely fill.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QCC/DISCO:
- can't directly call http://127.0.0.1:5000/templates/model_tmplt.html
- render_template can be given arguments that are used in the html file
- html can take variables and do loops. Most similar to python?
- it's a template so obviously it can be filled in...
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
