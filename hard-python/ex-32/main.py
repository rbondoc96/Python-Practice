#!/usr/bin/env python3

def main():
    counts = [1, 2, 3, 4, 5]
    fruits = ["apples", "oranges", "pears", "apricots"]
    change = [1, "pennies", 2, "dimes", 3, "quarters"]

    # This first kind of for-loop goes through a list
    for n in counts:
        print(f"This is count {n}")
    
    # Same as above
    for fruit in fruits:
        print(f"A fruit of type: {fruit}")

    # Also we can through mixed lists too
    for elem in change:
        print(f"I got {elem}")

    # We can also build lists, first start with an empty one
    elements = range(0, 6)

    # # Then use the range function to do 0 to 5 counts
    # for _ in range(0, 6):
    #     print(f"Adding {_} to the list.")

    #     # append() is a function that lists understand
    #     elements.append(_)

    # Now we can print them out too
    for _ in elements:
        print(f"Element was: {_}")


if __name__ == "__main__":
    main()