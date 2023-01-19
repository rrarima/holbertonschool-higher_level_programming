#!/usr/bin/python3
import sys

sum = 0

if __name__ == "__main__":
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
