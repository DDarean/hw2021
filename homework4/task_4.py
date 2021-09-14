"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers

Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
"""


from typing import List


def fizzbuzz_generator(n: int):
    """
    Auxiliary function provides "FizzBuzz" numbers
    Yields:
        int: next "FizzBuzz" number
    """
    for i in range(1, n**10):
        if i % 3 == 0 and i % 5 == 0:
            yield i


def generate_fizzbuzz_list(n: int):
    """
    Returns list of n "FizzBuzz" numbers (x % 3 == 0 and x % 5 ==0 only)
    :param n: required quantity
    :return: list of FizzBuzz numbers

    >>> generate_fizzbuzz_list(3)
    ['15', '30', '45']
    """
    fizzbuzz_numbers = fizzbuzz_generator(n)
    result = []
    while n:
        result.append(str(next(fizzbuzz_numbers)))
        n -= 1
    return result


def fizzbuzz(n: int) -> List[str]:
    """
    Returns solution for a FizzBuzz task
    :param n: required quantity
    :return: list with numbers replaced with "fizz", "buzz", "fizzbuzz"

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    """
    result = []
    for number in range(1, n + 1):
        result.append(str('fizz' * (not number % 3) + 'buzz' * (not number % 5)
                      or number))
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
