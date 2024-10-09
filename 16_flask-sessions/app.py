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
from flask import make_response

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    
    return render_template( 'login.html' )


@app.route("/auth", methods=['POST'])
def authenticate():
    user = request.form['username']
    resp = make_response(render_template( 'response.html' , foo = request.form['username']))
    resp.set_cookie('userID', user)
    return resp

@app.route("/logout", methods=['GET'])
def logout():
    name = request.cookies.get('userID')
    return render_template( 'logout.html' , foo = name)
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()