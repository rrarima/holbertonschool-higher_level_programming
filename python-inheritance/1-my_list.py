#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """Sort list"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
