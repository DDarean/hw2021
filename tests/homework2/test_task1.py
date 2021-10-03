import os

import homework2.task1 as hw

file_path = os.path.join(os.path.dirname(__file__), 'data2.txt')


def test_get_longest_diverse_words():
    assert hw.get_longest_diverse_words(file_path) == \
           ['politisch-strategischen', 'Werkstättenlandschaft',
            'Selbstbezichtigungen']


def test_get_rarest_char():
    assert hw.get_rarest_char(file_path) == ['›', '‹', 'î', '’', '(', ')']


def test_count_punctuation_chars():
    assert hw.count_punctuation_chars(file_path) == [('»', 43),
                                                     ('«', 43),
                                                     ('—', 81),
                                                     (',', 2489),
                                                     ('.', 1614),
                                                     ('-', 1016),
                                                     ('?', 28),
                                                     (';', 72),
                                                     (':', 79),
                                                     ('›', 1),
                                                     ('‹', 1),
                                                     ("'", 3),
                                                     ('’', 1),
                                                     ('(', 1),
                                                     (')', 1)]


def test_count_non_ascii_chars():
    assert hw.count_non_ascii_chars(file_path) == 2971


def test_get_most_common_non_ascii_char():
    assert hw.get_most_common_non_ascii_char(file_path) == 'ä'
