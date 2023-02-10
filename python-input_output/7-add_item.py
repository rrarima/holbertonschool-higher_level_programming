#!/usr/bin/python3
"""Add all argument ti a python list and save them to a file"""


import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
add_item = "add_item.json"

if os.path.isfile(add_item):
    obj = load_from_json_file(add_item)
else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, filename)
