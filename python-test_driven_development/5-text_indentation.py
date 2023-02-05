#!/usr/bin/python3
"""Function that prints text with 2 new lines after each character (.,?,:)"""


def text_indentation(text):
    """Print text with 2 new lines after ., ?,:"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for d in ".?:":
        text = text.replace(d, f"{d}\n\n")
    print(*map(str.strip, text.split('\n')), sep='\n', end="")
