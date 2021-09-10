"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import defaultdict
from typing import List
from unicodedata import category


def reader(file_path):
    with open(file_path, 'r', encoding='unicode-escape') as f:
        char = True
        while char:
            char = f.read(1).lower()
            if not char:
                break
            yield char


def get_longest_diverse_words(file_path: str) -> List[str]:
    min_length = 0
    counter = defaultdict()
    with open(file_path, 'r', encoding='unicode-escape') as f:
        for line in f:
            for word in line.split():
                if len(word) > min_length:
                    min_length = len(word)
                    counter[word] = len(word)
        return sorted(counter, key=counter.get, reverse=True)[0:10]


def get_rarest_char(file_path: str):
    counter = defaultdict(int)
    for elem in reader(file_path):
        counter[elem] += 1
    rarest = counter[sorted(counter, key=counter.get)[0]]
    rarest_chars = [k for k, v in counter.items() if int(v) == rarest]
    return rarest_chars


def count_punctuation_chars(file_path: str):
    counter = defaultdict(int)
    for elem in reader(file_path):
        counter[elem] += 1
    punctuation_char = [key for key in counter.keys() if
                        category(key).startswith('P')]
    char_counter = [k for k in counter.items() if k[0] in punctuation_char]
    return char_counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    for elem in reader(file_path):
        if len(elem) != len(elem.encode()):
            counter += 1
        else:
            continue
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    counter = defaultdict(int)
    for elem in reader(file_path):
        if len(elem) != len(elem.encode()):
            counter[elem] += 1
        else:
            continue
    return sorted(counter, key=counter.get, reverse=True)[0]
