"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
...
Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(mcs, name, bases, attr):
        new_instance = super().__new__(mcs, name, bases, attr)
        for attr_name, value in attr.items():
            if attr_name.startswith(f'_{name}'):
                try:
                    for attribute in value:
                        setattr(new_instance, attribute, attribute)
                except TypeError:
                    raise TypeError
        return new_instance
