# Jady Lei
# SoftDev Pd 4
# Sep 25 2024

# DEMO
# basics of /static folder
import random
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

'''
@app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
   # return render_template('fixie.html')
    return str(random.random())
'''
# overwrites the foo.html in static


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

