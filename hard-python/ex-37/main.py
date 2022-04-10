#!/usr/bin/env python3

def assert_something(boolean, msg):
    assert boolean, msg


def except_something(exc=True):
    if exc:
        raise Exception


def call_for_global(X):
    global GLOBAL_X
    GLOBAL_X = X


def also_change_global(X):
    print("Changing global")
    GLOBAL_X = X


def main():
    # Assertions are good for debugging in DEV, not PROD
    assert_something(True, "This shouldn't fail.")
    # assert_something(False, "This should fail.")

    list0 = [1, 2, 3]
    dict0 = {
        "hi": {
            1: 2,
            "hm": "okay"
        },
        "bye": ":("
    }

    print(list0, len(list0))
    print(dict0, len(dict0))
    
    # Can delete list and dict elements
    del list0[1]
    del dict0["hi"]

    # Run below string as Python code
    exec("print('hi')")

    print(list0, len(list0))
    print(dict0, len(dict0))

    exec_me = lambda s: exec(s)
    square_me = lambda n: n**2
    exec_me("print('I\\'m from a lambda function')")
    print("square_me(4):", square_me(4))


    try:
        except_something()
    except Exception:
        print("The exception was raised")
    finally:
        print("finally, I still run")

    try:
        except_something(False)
    except Exception:
        print("The exception was raised")
    finally:
        print("No exception, I still ran")        

    call_for_global("hi")
    print("Global", GLOBAL_X)
    call_for_global("changed")
    print("Global", GLOBAL_X)

    also_change_global("Surprise, this doesn't change.")
    print("Global", GLOBAL_X)

    # GLOBAL_X = "This results in an UnboundLocalError"
    # M: 'local variable "GLOBAL_X" referenced before assignment

    byte_a = b"\x00\x03"    # Byte literal, immutable
    empty_bytes = bytes(4)  # Empty bytes with length 4
    byte_b = bytearray(b"\x03\x00") # Mutable bytes object
    byte_b[0] = 255     # Can use like a list
    byte_b.append(1)    # Has list-like functions
    print(byte_b)

    quotient = 2 / 4
    print("2/4:", quotient)
    floor_me = 2 // 4
    print("2//4:", floor_me)


if __name__ == "__main__":
    main()