#!/usr/bin/env python3

def main():
    print("How old are you?: ", end="")
    age = input()
    print("How tall are you?:", end=" ")
    height = input()
    print("How much do you weight?", end=" ")
    weight = input()

    print(f"So, you're {age} old, {height} tall and {weight} heavy.")
    print("%r" % height)


if __name__ == "__main__":
    main()