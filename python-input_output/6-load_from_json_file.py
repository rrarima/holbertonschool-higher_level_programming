#!/usr/bin/python3
"""Create object from JSON file"""
import json


def load_from_json_file(filename):
    """Create object from JSON file"""
    def load_from_json_file(filename):
        with open(filename) as f:
            return json.load(f)
