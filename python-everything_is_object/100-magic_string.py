#!/usr/bin/python3
def magic_string(count=[0]):
    count[0] += 1
    return ", ".join("BestSchool" for _ in range(count[0]))
