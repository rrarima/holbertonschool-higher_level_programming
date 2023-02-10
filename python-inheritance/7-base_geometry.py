#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Base Geometry"""

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate values"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
