"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def fibonacci_generator(n=100000):
    n_first = 0
    n_last = 1
    for i in range(n-2):
        if i == 0 or i == 1:
            yield i
        result = n_first + n_last
        yield result
        n_first, n_last = n_last, result


def check_fibonacci(data: Sequence[int]) -> bool:
    sorted_sequence = sorted(data)
    # Check for negative numbers
    if sorted_sequence[0] < 0:
        return False
    # Check that sequence is sorted
    elif data != sorted_sequence:
        return False
    else:
        # Calculate Fibonacci generator
        gen = fibonacci_generator()
        number = next(gen)
        # Searching first element of array if Fibonacci sequence
        while data[0] != number:
            if number > data[0]:
                return False
            number = next(gen)
        # Separate check for case with one 1 in the beginning [1, 2, 3, 5...]
        if data[0] == 1 and data[1] == 2:
            number = next(gen)
        # Element-wise comparison
        for i in data:
            if i != number:
                return False
            else:
                number = next(gen)
        return True
