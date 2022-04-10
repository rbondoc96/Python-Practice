#!/usr/bin/env python3


def secret_formula(started):
    beans = started * 500
    jars = beans / 1000
    crates = jars / 100

    return beans, jars, crates


def main():
    print("Let's practice everything")
    print('You\'d need to know \'bout escapes with \\ that do')
    print("\n newlines and \t tabs.")

    poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

    print("".center(20, "-"))
    print(poem)
    print("".center(20, "-"))

    five = 10 - 2 + 3 - 6
    print(f"This should be five: {five}")

    start = 10000
    beans, jars, crates = secret_formula(start)

    print("With a starting point of: {}".format(start))
    print(f"We have {beans} beans, {jars} jars, and {crates} crates")

    start /= 10

    print("We can also do it this way:")
    formula = secret_formula(start)
    print("We'd have {} jars, {} crates, and {} crates".format(*formula))



if __name__ == "__main__":
    main()