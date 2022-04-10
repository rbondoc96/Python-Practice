#!/usr/bin/env python3

class Person:
    name = "Adam"

    def __repr__(self):
        return f"Hello {Person.name}"

def main():
    name = "Zed A. Shaw"
    age = 35
    height = 74  # inches
    weight = 180  # lbs
    eyes = "Blue"
    teeth = "White"
    hair = "Brown"

    person = Person()
    print(repr(person))
    # %r calles the repr() function on an object
    print("String: %r" % person)

    print("Let's talk about %s" % name)
    print(f"He's {height} inches, or {height * 2.54} cm tall")
    print("He's %d pounds or %.2f kg heavy" % (weight, weight * 0.453592))
    print("Actually, that's not too heavy.")
    print(f"He's got {eyes} eyes and {hair} hair.")
    # print("He's got %s eyes and %s hair." % (eyes, hair))
    print("His teeth are usually %s depending on the coffee." % teeth)

    print("If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight))


if __name__ == "__main__":
    main()