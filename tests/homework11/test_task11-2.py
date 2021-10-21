from homework11.task2 import Order


def test_first_discount_method():
    def morning_discount(price):
        discount_value = 0.5
        return price - price * discount_value

    morning_order = Order(100, morning_discount)
    assert morning_order.final_price() == 50.0


def test_second_discount_method():
    def night_discount(price):
        discount_value = 0.95
        return price - price * discount_value

    night_order = Order(100, night_discount)
    assert night_order.final_price() == 5.0


def test_no_discount():
    regular_order = Order(100)
    assert regular_order.final_price() == 100
