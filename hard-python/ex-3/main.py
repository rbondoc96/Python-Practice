#!/usr/bin/env python3

def main():
    print("I will now count my chickens")

    # Calculates 30/6 first. Equiv: 25 + (30 / 6)
    print("Hens", 25 + 30 / 6)

    # Calculates 25 * 3 first, then % 4, then 100 - ANS
    # Equiv: 100 - ((25 * 3) % 4)
    print("Roosters" , 100 - 25 * 3 % 4)
    print("")

    # Calculates 4 % 2 first, then 1 / 4, then left to right
    # Equiv: 3 + 2 + 1 - 5 + (4 % 2) - (1 / 4) + 6
    print("Now I will count the eggs:")
    ans = 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
    print(ans)
    print("Or more accurately:", int(ans), "eggs")
    print("")

    # Calculates both sides of "<" first, then does the comparison
    print("Is it true that 3 + 2 < 5 - 7?:", 3 + 2 < 5 - 7)
    print("What is 3 + 2?", 3 + 2)
    print("What is 5 - 7?", 5 - 7)
    print("Oh, that's why it's False")
    print("")

    print("How about some more?")
    print("Is it greater?", 5 > 2)
    print("Is it greater or equal?", 5 >= 2)
    print("Is it less or equal?", 5 <= 2)


def main_fp():
    pass


if __name__ == "__main__":
    main()
    # main_fp()