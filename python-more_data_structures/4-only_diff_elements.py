#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    non_match_a = set(set_1) - set(set_2)
    non_match_b = set(set_2) - set(set_1)
    non_match = list(non_match_a) + list(non_match_b)
    return non_match
