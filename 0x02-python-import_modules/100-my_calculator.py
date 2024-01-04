#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, ops, b = map(int, args)

    if ops not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    for op in ops:
        result = operators[op](a, b)
        print("{} {} {} = {}".format(a, op, b, result))
