import json
from datetime import datetime
json_file = open('settings.json')
data = json.load(json_file)
#print(data)
xyz = {
    "width": 1200,
    "height": 700 
       }
f = open("hit.json", "w")
f.write(str(xyz))
f.close()

#open and read the file after the appending:
f = open("hit.json", "r")
print(f.read())