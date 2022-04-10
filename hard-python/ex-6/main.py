#!/usr/bin/env python3

def main():
    x = "There are %d types of people." % 10
    binary = "binary"
    do_not = "don't"
    y = f"Those who know {binary} and those who {do_not}"

    print(x)
    print(y)

    print("I said: %r." % x)
    print("I also said: '%s'." % y)

    hilarious = False
    joke_eval = "Isn't that joke so funny?! %r"
    joke_eval2 = "Isn't that joke so funny?! {}"

    print(joke_eval % hilarious)
    print(joke_eval2.format(hilarious))

    w = "This is the left side of ..."
    e = "a string with a right side"

    print(w + e)

if __name__ == "__main__":
    main()