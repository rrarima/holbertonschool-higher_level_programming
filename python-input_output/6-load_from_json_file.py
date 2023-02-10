#!/usr/bin/python3
"""Create object from JSON file"""
import json


def load_from_json_file(filename):
    """Create object from JSON file"""
    def load_from_json_file(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.loads(f)
