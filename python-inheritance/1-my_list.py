#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """Sort list"""

    def print_sorted(self):
        return super(MyList, self.sort())
