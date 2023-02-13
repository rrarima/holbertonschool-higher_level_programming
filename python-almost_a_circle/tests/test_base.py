#!/usr/bin/python3
"""Base Class"""


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
