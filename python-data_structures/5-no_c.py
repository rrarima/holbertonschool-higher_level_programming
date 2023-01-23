#!/usr/bin/env python3
def no_c(my_string):
    new_char = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_char = new_char + char
    return (new_char)
