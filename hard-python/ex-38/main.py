#!/usr/bin/env python3

def main():
    ten_things = "Apples Oranges Crows Telephone Light Sugar"

    print("Wait there are not 10 things in that list. Let's fix that.")

    stuff = ten_things.split()
    more_stuff = ["Day", "Night", "Song", "Frisbee",
        "Corn", "Banana", "Girl", "Boy",
    ]

    while len(stuff) != 10:
        next_one = more_stuff.pop()
        print("Adding", next_one)
        stuff.append(next_one)
        print(f"There are {len(stuff)} items now.")

    print("There we go:", stuff)

    print("Let's do some things with stuff.")

    print(stuff[1])
    print(stuff[-1])
    print(stuff.pop())
    print(" ".join(stuff))
    print("#".join(stuff[3:5]))

    # PDF page 170
    print("Only evens")
    print(stuff[0::2])

    print("Only odds")
    print(stuff[1::2])

    print("A copy of my stuff")
    print(stuff.copy())

    print("Whoa, another copy!")
    print(stuff[:])

    print("Wait, I want them lined up with their order (1-ordering)")
    for (index, item) in enumerate(stuff):
        print(f"{index+1}:", item)

    print("Let's make a new list with the map() function.")
    # map() applies a given function and applys it to item item
    # in the iterable passed to it
    my_list = list(map(lambda x: x**2, range(10)))
    for item in my_list:
        print(item)

    print("Let's make the same list using list comprehensions.")
    same_list = [x**2 for x in range(10)]
    for item in same_list:
        print(item)
        


if __name__ == "__main__":
    main()