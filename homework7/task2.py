"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

import re


def backspace_compare(first: str, second: str):
    pattern = r'.{1}#{1}'
    while re.findall(pattern, first.lower()):
        first = re.sub(pattern, '', first.lower())
    while re.findall(pattern, second.lower()):
        second = re.sub(pattern, '', second.lower())
    return first == second
