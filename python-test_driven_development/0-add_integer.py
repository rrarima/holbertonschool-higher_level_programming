#!/usr/bin/python3
"""A function that adds 2 integers"""


def add_integer(a, b=98):
    """Adding edge cases"""

    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integert")
    elif type(b) != int:
        raise TypeError("b must be an integert")
    else:
        return a + b
