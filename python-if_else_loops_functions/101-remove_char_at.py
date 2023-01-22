#!/usr/bin/python3
def remove_char_at(str, n):
    rem_str = ""
    for i in range(0, len(str)):
        if i != n:
            rem_str = rem_str + str[i]
    return (rem_str)
