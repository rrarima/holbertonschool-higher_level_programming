#!/usr/bin/python3
"""Return True is object is exactly an instance of the specified class"""


def is_kind_of_class(obj, a_class):
    """is_same_function"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
