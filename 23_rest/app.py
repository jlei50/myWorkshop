# Jady Lei
# Team: 45
# SoftDev Pd 4
# Sep 30 2024 

"""
QCC/DISCO:
 - in notes
"""

from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)

with open("key_nasa.txt", "r") as file:
    raw = file.read()
    key = str(raw)[:-2]
    print(key)

with urllib.request.urlopen(f'https://api.nasa.gov/insight_weather/?api_key={key}&feedtype=json&ver=1.0') as response:
   JSO = response.read()

@app.route("/")
def hello_world():
    return "JSO"

# ~~ back to app stuff

# @app.route("/wdywtbwygp") 
# def test_tmplt():
# #     return render_template( 'tablified.html', foo= ReturnRandom(), coll = full)

if __name__ == "__main__":
    app.debug = True
    app.run()