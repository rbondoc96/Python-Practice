#!/usr/bin/env python3

from sys import argv
from os.path import exists


def main():
    from_file, to_file = argv[1:3]
    print(f"Copying from {from_file} to {to_file}")

    with open(from_file, "r") as in_f:
        with open(to_file, "w") as out_f:
            data_in = in_f.read()

            print(f"The input file is {len(data_in)} bytes long.")

            print("Does the output file exist?", exists(to_file))
            print("Ready, hit RETURN to continue, CTRL-C to abort.")
            input("...")

            out_f.write(data_in)

            print("Alright, all done.")


if __name__ == "__main__":
    main()