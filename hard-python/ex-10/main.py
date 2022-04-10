#!/usr/bin/env python3

def main():
    tabby = "\tI'm tabbed in."
    persian = "I'm split \non a line."
    backslash_cat = "I'm \\ a \\ cat."

    fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass"""

    print(tabby)
    print(persian)
    print(backslash_cat)
    print(fat_cat)

if __name__ == "__main__":
    main()