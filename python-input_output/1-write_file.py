#!/usr/bin/python3
"""Write to text file"""


def write_file(filename="", text=""):
    """Write to text"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
