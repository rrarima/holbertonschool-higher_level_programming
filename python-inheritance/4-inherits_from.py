#!/usr/bin/python3
"""Return True is object inherits class """


def inherits_from(obj, a_class):
    """inherits_from function"""
        return(issubclass(type(obj), a_class) and type(obj) != a_class)
