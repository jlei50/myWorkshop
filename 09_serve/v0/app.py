# Jady Lei
# 63
# SoftDev
# K09 -- Serve
# 2024-09-23
# v0 same as before

from flask import Flask
app = Flask(__name__)          # ...

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ...
    return "No hablo queso!"   # ...

app.run()                      # ...
                
