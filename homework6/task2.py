"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    instances = 0

    def dec_init(*args):
        nonlocal instances
        super(cls, cls).__init__(cls)
        instances += 1

    def get_created_instances(*args):
        return instances

    def reset_instances_counter(*args):
        nonlocal instances
        try:
            return instances
        finally:
            instances = 0

    cls.__init__ = dec_init
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass
