#!/usr/bin/python3

import calculator_1
import sys

if __name__ == "__main__":
    unkown_op = "Unknown operator. Available operators: +, -, * and /"

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1:]
    a = int(a)
    b = int(b)

    if operator == "+":
        result = calculator_1.add(a, b)
    elif operator == "-":
        result = calculator_1.sub(a, b)
    elif operator == "*":
        result = calculator_1.mul(a, b)
    elif operator == "/":
        result = calculator_1.div(a, b)
    else:
        print(unkown_op)
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
    sys.exit(0)
