#!/usr/bin/python3
"""Return True is object inherits class """


def inherits_from(obj, a_class):
    """inherits_from function"""

    if isinstance(obj, a_class) and not issubclass(type(obj), a_class):
        return False
    else:
        return True
