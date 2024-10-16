# Jady Lei
# 45
# SoftDev
# 2024-10-16

from flask import Flask, render_template
app = Flask(__name__)          

@app.route("/")                
def hello_world():
    print(__name__)            
    return render_template('index.html')  

app.debug = True  
app.run() 
                