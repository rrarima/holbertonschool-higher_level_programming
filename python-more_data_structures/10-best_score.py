#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    high_score = 0
    for key, value in a_dictionary.items():
        if value > high_score:
            high_score = value
    for key, value in a_dictionary.items():
        if value == high_score:
            return key
