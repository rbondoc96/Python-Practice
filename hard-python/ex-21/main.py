#!/usr/bin/env python3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def remainder(x, y):
    return x % y


def main():
    print("add(5, 3)", add(5, 3))
    print("subtract(5, 3)", subtract(5, 3))
    print("multiply(5, 3)", multiply(5, 3))
    print("divide(5, 4)", divide(5, 4))
    print("remainder(5, 4)", remainder(5, 4))
    print("power(2, 3)", power(2, 3))

    # The innermost function call is first
    # d = divide(50, 2)             25.0
    # then, m = multiply(4, d)      4 * 25.0 = 100.0
    # then, s = subtract(90, m)     90 - 100.0 = -10.0
    # lastly, a = add(35, s)        35 + -10.0 = 25.0
    what = add(35, subtract(90, multiply(4, divide(50, 2))))
    print("what:", what)

    # 49 + 1 / 26 - 1
    q = divide(add(49, 1), subtract(26, 1))
    print("q:", q)


if __name__ == "__main__":
    main()