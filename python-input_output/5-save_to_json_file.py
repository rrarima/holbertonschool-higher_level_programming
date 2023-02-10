#!/usr/bin/python3
"""Write object to text file in JSON format"""
import json


def save_to_json_file(my_obj, filename):
    """text file in JSON format"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
