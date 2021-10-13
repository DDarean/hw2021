from os import path

from homework9.task1 import merge_sorted_files


def test_two_files():
    names = ['text1.txt', 'text2.txt']
    files = [path.join(path.dirname(__file__), file_name)
             for file_name in names]
    assert merge_sorted_files(files) == [1, 2, 3, 4, 5, 6]


def test_file_with_wrong_char():
    names = ['text1.txt', 'text2.txt', 'text3.txt']
    files = [path.join(path.dirname(__file__), file_name)
             for file_name in names]
    assert merge_sorted_files(files) == [1, 2, 3, 3, 4, 5, 5, 6]
