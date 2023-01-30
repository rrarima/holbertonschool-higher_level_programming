#!/usr/bin/python3
"""Square class define a square"""


class Square:
    """ Class that defines a square """

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
