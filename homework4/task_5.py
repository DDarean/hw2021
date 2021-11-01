"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the
implementation in this video https://www.youtube.com/watch?v=NSzsYWckGd4.
"""


def fizzbuzz_gen_replace(n):
    """Implementation from video

    >>> fizzbuzz_gen_replace(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', \
11, 'Fizz', 13, 14, 'FizzBuzz']
    """
    result = [i for i in range(1, n + 1)]
    for i in range(2, n, 3):
        result[i] = 'Fizz'
    for i in range(4, n, 5):
        result[i] = 'Buzz'
    for i in range(14, n, 15):
        result[i] = 'FizzBuzz'
    return result  # yield for generator


def fizzbuzz_omg():
    """out of contest..."""
    n = 1
    while True:
        yield 0 + n
        yield 1 + n
        yield 'Fizz'
        yield 3 + n
        yield 'Buzz'
        yield 'Fizz'
        yield 6 + n
        yield 7 + n
        yield 'Fizz'
        yield 'Buzz'
        yield 10 + n
        yield 'Fizz'
        yield 12 + n
        yield 13 + n
        yield 'FizzBuzz'
        n = 16


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    gen = fizzbuzz_omg()
    res = []
    for num in range(20):
        res.append(next(gen))
    print(res)
