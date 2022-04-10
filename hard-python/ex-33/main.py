#!/usr/bin/env python3


def run(upper_limit, inc=1):
    i = 0
    numbers = []
    inc = max(1, inc)

    while i < upper_limit:
        numbers.append(i)
        i += inc

    return numbers


def run_for(upper_limit, inc=1):
    numbers = []
    inc = max(1, inc)

    for i in range(0, upper_limit):
        if (i * inc) >= upper_limit:
            break
        
        numbers.append(i * inc)

    return numbers


def main():
    limit = 6
    inc = 6

    print(run(limit, inc) == run_for(limit, inc))


if __name__ == "__main__":
    main()