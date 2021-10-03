from homework3.task03 import Filter, make_filter


def test_filter_class():
    positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0,
                            lambda a: isinstance(a, int)])
    assert positive_even.apply(range(7)) == [2, 4, 6]


def test_initial():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly",
        }
    ]

    assert (make_filter(name='polly', type='bird').apply(sample_data)
            == [sample_data[1]])


def test_wrong_name():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly2",
        }
    ]

    assert make_filter(name='polly', type='bird').apply(sample_data) == []


def test_wrong_type():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird2",
            "name": "polly",
        }
    ]

    assert make_filter(name='polly', type='bird').apply(sample_data) == []


def test_new_key():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly",
            "new": 1
        }
    ]

    assert (make_filter(name='polly', type='bird', new=1).apply(sample_data)
            == [sample_data[1]])
