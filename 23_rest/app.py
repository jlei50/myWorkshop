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
import random
app = Flask(__name__)

with open("key_nasa.txt", "r") as file:
    key = file.read()



with urllib.request.urlopen(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=2000&api_key={key}') as response:
   resp = response.read()
   resp = json.loads(resp)
   num_photos = len(resp["photos"])
#    random_nums = random.sample(range(0, ), 4)
   random_nums = [0, int(num_photos * 0.5), int(num_photos * 0.95), num_photos-1]



@app.route("/")
def hello_world():
    return render_template('main.html', # tgere are better ways to do this. make sure to do that next time
    image1 = resp["photos"][random_nums[0]]["img_src"], description1 = "<br>Rover: " + resp["photos"][random_nums[0]]["rover"]["name"] + "<br>Camera: " + resp["photos"][random_nums[0]]["camera"]["full_name"] + "<br>Earth Date: " + resp["photos"][random_nums[0]]["earth_date"],
    image2 = resp["photos"][random_nums[1]]["img_src"], description2 = "<br>Rover: " + resp["photos"][random_nums[1]]["rover"]["name"] + "<br>Camera: " + resp["photos"][random_nums[1]]["camera"]["full_name"] + "<br>Earth Date: " + resp["photos"][random_nums[1]]["earth_date"],
    image3 = resp["photos"][random_nums[2]]["img_src"], description3 = "<br>Rover: " + resp["photos"][random_nums[2]]["rover"]["name"] + "<br>Camera: " + resp["photos"][random_nums[2]]["camera"]["full_name"] + "<br>Earth Date: " + resp["photos"][random_nums[2]]["earth_date"],
    image4 = resp["photos"][random_nums[3]]["img_src"], description4 = "<br>Rover: " + resp["photos"][random_nums[3]]["rover"]["name"] + "<br>Camera: " + resp["photos"][random_nums[3]]["camera"]["full_name"] + "<br>Earth Date: " + resp["photos"][random_nums[3]]["earth_date"])

if __name__ == "__main__":
    app.debug = True
    app.run()