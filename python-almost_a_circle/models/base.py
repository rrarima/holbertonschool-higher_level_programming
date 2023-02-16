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
        """Return JSON string format"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Return JSON list of objects"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dict_list = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Return JSON dict"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return instance with all attributes set"""
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
