from functools import wraps

# This decorator will wrap a function, modifying its behavior
def decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")

    return wrapper


def pass_me():
    print("pass_me!")


@decorator
def decorate_me():
    print("decorate_me!")


@decorator
def decorate_me_too():
    print("decorate_me_too!")


def decorator_with_args(func):
    def wrapper_with_args(*args, **kwargs):
        print("Calling function with args.")
        func(*args, **kwargs)

    return wrapper_with_args


@decorator_with_args
def give_me_name(name):
    print(name)


def decorator_with_ret(func):

    # This decorator lets info for func() be preserved when using
    # shell commands such as help(func)
    # Without it, help(func) outputs info about wrapper_with_ret()
    @wraps(func)
    def wrapper_with_ret(*args, **kwargs):
        print("I will give you something")
        func(*args, **kwargs)

        return "Here it is!"

    return wrapper_with_ret


@decorator_with_ret
def give_me_drink(drink):
    print(f"Thanks for the {drink}!")


def main():
    foo = decorator(pass_me)
    foo()

    decorate_me()
    decorate_me_too()

    give_me_name("Rodrigo")
    ret = give_me_drink("Vodka")
    print("I got this from decorator_with_ret:", ret)

    # outputs info about the wrapper function, not give_me_name
    # help(give_me_name)

    # outputs info about give_me_drink!
    # help(give_me_drink)


if __name__ == "__main__":
    main()