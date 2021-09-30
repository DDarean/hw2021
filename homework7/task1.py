"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

"""str, list, tuple, dict, set, int, bool"""


def find_occurrences(tree: dict, element: Any = None) -> int:
    if element is None:
        raise ValueError('Incorrect request')
    counter = 0
    if isinstance(tree, (str, int, bool)):
        if tree == element:
            return 1
    elif isinstance(tree, dict):
        for k in tree:
            counter += find_occurrences(tree[k], element)
    elif isinstance(tree, (list, tuple, set)):
        for elem in tree:
            counter += find_occurrences(elem, element)
    return counter
