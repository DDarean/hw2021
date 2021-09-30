import pytest

from homework7.task1 import find_occurrences


def test_sample_tree():
    example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            }
        },
        "fourth": "RED",
    }
    assert find_occurrences(example_tree, "RED") == 6


def test_empty_tree():
    tree = {}
    assert find_occurrences(tree, 'any') == 0


def test_no_element():
    tree = {}
    with pytest.raises(ValueError):
        assert find_occurrences(tree)
