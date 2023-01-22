#!/usr/bin/python3
print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
    *(chr(122 - ch) if ch % 2 == 0 else chr(90 - ch) for ch in range(26))
))
