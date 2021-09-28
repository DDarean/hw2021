from homework6.task2 import User


def test_get_created_instances_empty():
    assert User.get_created_instances() == 0


def test_get_created_instances_three():
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3


def test_reset_instances_return():
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == user.reset_instances_counter()


def test_reset_instances_result():
    user, _, _ = User(), User(), User()
    user.reset_instances_counter()
    assert user.get_created_instances() == 0
