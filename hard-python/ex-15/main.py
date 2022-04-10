#!/usr/bin/env python3

from sys import argv

def main():
    filename = argv[1]

    # Opens a file using the file() type, returns a faile object
    txt = open(filename)

    print(f"Here's your file {filename}")

    # read() will read until EOF, since no parameter is given
    print(txt.read())

    # close() closes the file from further I/O operations
    txt.close()

    print("Type the filename again.")
    file_again = input("> ")

    txt_again = open(file_again)

    # read(3) will read at most 3 bytes
    print(txt_again.read(3))
    txt.close()

def main2():
    filename = argv[1]

    # close() is automatically called after this block
    with open(filename) as txt:
        print(f"Here's your file {filename}")
        print(txt.read())

    print("Type the filename again.")
    file_again = input("> ")

    with open(file_again) as txt_again:
        print(txt_again.read())

if __name__ == "__main__":
    main2()