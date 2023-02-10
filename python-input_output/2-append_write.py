#!/usr/bin/python3
"""Append string at th end of text"""


def append_write(filename="", text=""):
    """Append text"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
