from os import path
from unittest.mock import patch

import pytest

from homework4.task_2 import count_dots_on_i


@pytest.fixture()
def read_mock_file():
    filename = path.join(path.dirname(__file__), "fixtures/mock.txt")
    with open(filename, 'r') as f:
        text = str(f.readlines())
        return text


def test_url_positive(read_mock_file):
    @patch("homework4.task_2.request_url", return_value=read_mock_file)
    def check(_):
        assert count_dots_on_i(_) == 59
    check()


def test_url_negative(read_mock_file):
    @patch("homework4.task_2.request_url", return_value=read_mock_file)
    def check(_):
        assert not count_dots_on_i(_) == 0
    check()


def test_without_mock():
    assert count_dots_on_i("https://example.com/") == 59


def test_url_error():
    with pytest.raises(ValueError):
        assert count_dots_on_i("https://exasadfsdfmple.com/")
