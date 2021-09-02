"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def fibonacci(n, result) -> bool:
    if n == 0 or n == 1:
        result[n] = n
        return n
    if result[n] != -1:
        return result[n]
    else:
        result[n] = (fibonacci(n - 2, result) + fibonacci(n - 1, result))
        return result[n]


def check_fibonacci(data: Sequence[int]) -> bool:
    sorted_sequence = sorted(data)
    # Check for negative numbers
    if sorted_sequence[0] < 0:
        return False
    # Check that sequence is sorted
    elif data != sorted_sequence:
        return False
    else:
        # Calculate first n Fibonacci numbers
        n = 100
        fibonacci_sequence = [-1] * n
        for i in range(0, n):
            fibonacci(i, fibonacci_sequence)
        # Check if single number is in Fibonacci sequence
        if len(data) == 1:
            return data[0] in fibonacci_sequence
        # Separate check for case with one 1 in the beginning [1, 2, 3, 5...]
        if data[0] == 1 and data[1] == 2:
            sequence_index = 2
        else:
            sequence_index = fibonacci_sequence.index(data[0])
        for i in range(len(data)):
            if fibonacci_sequence[sequence_index + i] == data[i]:
                continue
            else:
                return False
        return True
