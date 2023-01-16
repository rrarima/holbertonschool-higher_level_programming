#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(num):
    last_digit_unsigned = abs(num) % 10
    return -last_digit_unsigned if (num < 0) else last_digit_unsigned


last = last_digit(number)

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
if last == 0:
    print(f"Last digit of {number} is {last} and is 0")
else:
    if last < 6 and last != 0:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
