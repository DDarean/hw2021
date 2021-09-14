from homework4.task_3 import my_precious_logger


def test_logger_positive(capsys):
    test_string = 'error_test'
    my_precious_logger(test_string)
    out, err = capsys.readouterr()
    assert err == 'error_test\n'
    assert out == ''


def test_logger_negative(capsys):
    test_string = 'something_good'
    my_precious_logger(test_string)
    out, err = capsys.readouterr()
    assert not err == 'something_good\n'
    assert out == 'something_good\n'
