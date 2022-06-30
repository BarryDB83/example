from collections import OrderedDict
import json

def ordered(d, key_order):
   
    return OrderedDict([(key, d[key]) for key in key_order])

desired_key_order = ("name", "description", "image", "attributes")

with open("1.json") as json_file:
    d = json.load(json_file)

result = ordered(d, desired_key_order)

f = open("new.json", "a")

f.write(json.dumps(result, indent=4))

f.close()