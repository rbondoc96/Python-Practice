#!/usr/bin/env python3

from sys import argv

def main():
    input_encoding, error = argv[1:3]

    langf = open("languages.txt", "r")
    print_file(langf, input_encoding, error)


def print_file(_file, encoding, errors):
    line = _file.readline()

    if line:
        print_line(line, encoding, errors)
        return print_file(_file, encoding, errors)


def print_line(line, encoding, errors):
    lang = line.strip()
    raw_bytes = lang.encode(encoding, errors=errors)
    proc_str = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", proc_str)


if __name__ == "__main__":
    main()