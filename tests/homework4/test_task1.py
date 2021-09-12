import pytest
from homework4.task_1 import read_magic_number


@pytest.fixture()
def tmp_file(tmp_path):
    def create_file(text):
        filename = 'test.txt'
        with open(filename, 'w') as f:
            f.write(text)
        return filename
    return create_file


def test_with_correct_value(tmp_file):
    assert read_magic_number(tmp_file('1'))


def test_with_incorrect_value(tmp_file):
    assert not read_magic_number(tmp_file('3'))


def test_with_letter(tmp_file):
    with pytest.raises(ValueError):
        read_magic_number(tmp_file('a'))
