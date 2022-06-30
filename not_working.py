from collections import OrderedDict
import json

with open("1.json") as json_file:
    d = json.load(json_file)

edition = d['custom_fields']['edition']

print(edition)

d.update(edition)

