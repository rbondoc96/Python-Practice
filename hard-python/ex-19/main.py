#!/usr/bin/env python3


def run_me(func, *args):
    if len(args) != 2:
        print("Unable to run function.")
    else:
        func(args[0], args[1])


def tops_and_bottoms(nTops, nBtms):
    print("".center(20, "="))
    print(f"There are {nTops} tops at this party.")
    print(f"There are {nBtms} bottoms at this party.")
    
    if nTops >= nBtms:
        print("Yep, enough for a party.\n")
    else:
        print("Ugh. Too many bottoms.\n")


def main():
    print("Give the function number literals")
    tops_and_bottoms(10, 5)

    print("Let's pass it some variables.")
    nTops = 5
    nBtms = 6
    tops_and_bottoms(nTops, nBtms)

    print("Let's pass it some math expressions")
    tops_and_bottoms(nTops * 2, 3 + 1)

    run_me(tops_and_bottoms, 20, 1)
    

if __name__ == "__main__":
    main()