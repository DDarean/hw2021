from homework5.task2 import custom_sum


def test_custom_list():
    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


def test_custom_sum():
    assert custom_sum(1, 2, 3, 4) == 10


def test_doc_print():
    assert custom_sum.__doc__ == 'This function can sum any ' \
                                 'objects which have __add___'


def test_name_print():
    assert custom_sum.__name__ == 'custom_sum'


def test_without_print():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
