from os import path

from homework9.task3 import universal_file_counter


def test_4_files():
    assert universal_file_counter(path.dirname(__file__), 'txt') == 14


def test_extension():
    assert universal_file_counter(path.dirname(__file__), 'txt') < \
           universal_file_counter(path.dirname(__file__))


def test_with_tokenizer():
    assert universal_file_counter(path.dirname(__file__),
                                  'txt', tokenizer=str.split) == 15
