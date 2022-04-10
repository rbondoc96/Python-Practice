#!/usr/bin/env python3

from sys import argv

class FileReader:

    def __init__(self, filepath):
        self.file = open(filepath, "r")
    
    def __del__(self):
        self.file.close()

    def rewind(self):
        self.file.seek(0)

    def print_all(self):
        print(self.file.read())

    def print_a_line(self, line):
        print(f"{line}: {self.file.readline()}", end="")

    def print_self(self):
        print("File:", self.file)
        print("Self:", self)



def main():
    filename = argv[1]
    
    fr = FileReader(filename)

    print("First, let's print the whole file.")
    fr.print_all()
    print("")

    print("Now let's rewind to the start, like a tape.")
    fr.rewind()
    print("")

    print("Let's print three lines")
    cLine = 1
    fr.print_a_line(cLine)

    cLine += 1
    fr.print_a_line(cLine)

    cLine += 1
    fr.print_a_line(cLine)

    print("")
    fr.print_self()


if __name__ == "__main__":
    main()