# Jady Lei
# 31
# SoftDev
# October 8 2024

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session, redirect
import os


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

app.secret_key = os.urandom(32)

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if 'username' in session:
        rp = "<p>Logged in as " + session['username'] + "</p>"
        rp += "<br><form action='/logout'>"
        rp += "<input type='submit' value='logout?'>"
        rp += "</form>"
    else:
        rp = "Login?"
        rp += "<h3>Enter your username below to proceed.</h3>"
        rp += "<form action='/auth'>"
        rp += "<input type='submit' value='==>'>"
        rp += "</form>"
    return render_template( 'login.html', foo = rp )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect("http://127.0.0.1:5000/")
    return render_template( 'response.html' )

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect("http://127.0.0.1:5000/")
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()