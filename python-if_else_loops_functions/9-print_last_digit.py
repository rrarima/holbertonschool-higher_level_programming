#!/usr/bin/python3
def print_last_digit(number):
    last_digit_number = abs(number) % 10
    if number < 0:
        print("{:d}".format(last_digit_number), end='')
        return last_digit_number
    else:
        print("{:d}".format(last_digit_number), end='')
        return last_digit_number
