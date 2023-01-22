#!/usr/bin/python3
for ch in range(26):
    if ch % 2 == 0:
        print(chr(122 - ch), end="")
    else:
        print(chr(90 - ch), end="")
