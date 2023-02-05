#!/usr/bin/python3
"""
Write a function the prints My name is followed by
first then last name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name followed by first and last name"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
