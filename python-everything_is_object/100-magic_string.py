#!/usr/bin/python3
"""Magic String"""
def magic_string(count=[0]):
    count[0] += 1
    return ", ".join("BestSchool" for _ in range(count[0]))
