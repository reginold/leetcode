import functools


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("my_decorator1 - 1")
        func(*args, **kwargs)
        print("my_decorator1 - 2")

    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("my_decorator2 - 1")
        func(*args, **kwargs)
        print("my_decorator2 - 2")

    return wrapper


def my_decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("my_decorator3 - 1")
        func(*args, **kwargs)
        print("my_decorator3 - 2")

    return wrapper


@my_decorator1
@my_decorator2
@my_decorator3
def greet(message):
    print(message)


greet("hello world")
