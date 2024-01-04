#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = args[2]
    a = int(args[1])
    b = int(args[3])

    if ops not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = operators[ops](a, b)
    print("{} {} {} = {}".format(a, ops, b, result))
