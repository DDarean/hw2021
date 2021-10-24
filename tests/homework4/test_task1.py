import tempfile

import pytest

from homework4.task_1 import read_magic_number

"""
@pytest.fixture()
def tmp_file(tmp_path):
    def create_file(text):
        filename = 'test.txt'
        with open(filename, 'w') as f:
            f.write(text)
        return filename
    return create_file
"""


def test_with_correct_value():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write('1')
        f.flush()
        assert read_magic_number(f.name)


def test_with_incorrect_value():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write('3')
        f.flush()
        assert not read_magic_number(f.name)


def test_with_letter():
    with pytest.raises(ValueError):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write('a')
            f.flush()
            assert not read_magic_number(f.name)
