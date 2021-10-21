import pytest

from homework11.task1 import SimplifiedEnum


def test_attributes():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == 'RED'


def test_attributes_wrong_type():
    with pytest.raises(TypeError):
        class SizesEnum(metaclass=SimplifiedEnum):
            __a = [0]
