#!/usr/bin/python3
import sys
def print_argv(argv):
    argument = len(argv) - 1
    if argument == 0:
        print("{:d} argument:".format(argument))
        return
    else:
        if argument == 1:
            print("{:d} argument: ".format(argument))
        else:
            print("{:d} arguments:".format(argument))
        i = 1
        while i <= argument:
            print("{:d}: {:s}".format(i, argv[i]))
            i = i + 1

if __name__ == "__main__":
        print_argv(sys.argv)
