#!/usr/bin/python3
"""Function that prints square with #"""


def print_square(size):
    """Prints square with #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
