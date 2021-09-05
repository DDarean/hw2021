"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}
    from_cache_flag = 0  # for tests

    def calculate(*args):
        nonlocal from_cache_flag
        if args in cache_storage:
            from_cache_flag = 1
            return cache_storage[args], from_cache_flag
        else:
            from_cache_flag = 0
            cache_storage[args] = func(*args)
            return func(*args), from_cache_flag
    return calculate
