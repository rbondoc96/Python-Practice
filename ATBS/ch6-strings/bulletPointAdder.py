#!/usr/bin/env python3

import pyperclip

def main():
    text = pyperclip.paste()

    lines = text.split("\n")

    lines = ["* " + line for line in lines]

    pyperclip.copy("\n".join(lines))

if __name__ == "__main__":
    main()    

    