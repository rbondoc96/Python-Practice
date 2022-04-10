import time
from functools import wraps

def timer(func):
    """Prints the runtime of the decorated function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        delta = end - start

        f_name = func.__name__
        print(f"Finished {f_name!r} in {delta:.4f} secs!")

        return value

    return wrapper


def debug(func):
    """Prints the function signature and return values for the decorated function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        args_repr = [repr(a) for a in args]

        # !r calls repr() on the variable
        kw_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        
        signature = ", ".join(args_repr + kw_repr)
        print(f"Calling {name}({signature})")
        value = func(*args, **kwargs)
        print(f"{name!r} returned {value!r}")

        return value

    return wrapper
    

@debug
def greet(name, age=None):
    if age:
        print(f"Hi {name}! You're {age} years old.")
    else:
        print(f"Hi {name}!")

@timer
def run_around():
    x = 0
    for _ in range(1, 10000):
        x += _


def test_me():
    greet("Michael", 27)
    run_around()


if __name__ == "__main__":
    test_me()