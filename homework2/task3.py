"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    length = [len(x) for x in args]
    flat_list = [x for y in args for x in y]
    pointer = 0
    comb_list = []
    for array_size in length:
        base = flat_list[pointer:array_size]
        last = flat_list[0:pointer] + flat_list[array_size:]
        for first_elem in base:
            for second_element in last:
                comb_list.append([first_elem] + [second_element])
        pointer += array_size
    return comb_list
