#!/usr/bin/env python3


def print_two(*args):
    arg1, arg2 = args

    print(f"arg1: {arg1} | arg2: {arg2}")


def print_two_again(arg1, arg2):

    print_two(arg1, arg2)


def print_kwargs(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}", end=" | ")
    
    print("")


def print_one(arg):
    print(f"arg: {arg}")


def print_none():
    print("No args here.")


def main():
    print_two("Rodrigo", "Bondoc")
    print_two_again("Rodrigo", "Bondoc")
    print_kwargs(fName="Rodrigo", lName="Bondoc", suffix="IV")
    print_one("Rodrigo Bondoc")
    print_none()


if __name__ == "__main__":
    main()