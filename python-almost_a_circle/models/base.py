#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Base class init"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Define init"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string format"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
