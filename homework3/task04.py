"""
Write a function that detects if a number is
                Armstrong number in functionally style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions
"""
import math


def find_num_len(n):
    num_length = int(math.log10(n)) + 1
    return num_length


def break_number(num, length):
    return [num // 10**power for power in range(0, length)]


def return_last_digit(x):
    return x % 10


def is_armstrong(number: int) -> bool:
    # return sum([int(x)**len(str(number)) for x in str(number)]) == number
    num_len = find_num_len(number)
    return sum([return_last_digit(x)**num_len
                for x in break_number(number, num_len)]) == number
