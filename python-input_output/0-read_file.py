#!/usr/bin/python3
"""Read text file using UTF8"""

def read_file(filename=""):
    """Read text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
