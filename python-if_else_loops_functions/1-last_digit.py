#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(num):
    last_digit_unsigned = abs(num) % 10
    return -last_digit_unsigned if (num < 0) else last_digit_unsigned


last_d = last_digit(number)

if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
if last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
if last_d < 6 and not 0:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
