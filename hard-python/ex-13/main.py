#!/usr/bin/env python3

from sys import argv


def main():
    script, first, second, third = argv

    print("The script is called", script)

    conf1 = input(f"Your first variable is {first}. Is this correct? ")
    print("Your first variable is:", first)

    conf2 = input(f"Your first variable is {second}. Is this correct? ")
    print("Your second variable is:", second)

    conf3 = input(f"Your first variable is {third}. Is this correct? ")
    print("Your third variable is:", third)

if __name__ == "__main__":
    main()