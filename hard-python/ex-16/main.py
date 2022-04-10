#!/usr/bin/env python3

from sys import argv

def main():
    filename = argv[1]

    print(f"We're going to erase {filename}")
    print("If you don't want that, hit CTRL-C (^C)")
    print("If you do want that, hit RETURN")

    input("?")

    print(f"Opening {filename}...")

    # "r+" is read & write
    # "w" is write, but truncates the file first
    # "a" is append
    with open(filename, "r+") as target:

        #  Not needed with "w" flag, as it truncates the file first
        #  (sets to 0 bytes)
        # print("Trunacting the file. Goodbye!")
        # target.truncate()

        print("Now I'm going to ask you for three lines...")
        line1 = input("line 1: ")
        line2 = input("line 2: ")
        line3 = input("line 3: ")

        print("I'm going to write these to the file.")

        target.write(f"{line1}\n{line2}\n{line3}")

        print("And finally, we close it.")

if __name__ == "__main__":
    main()