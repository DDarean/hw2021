"""-  `len(presidents)` will give current amount of rows in presidents
        table in database
 -  `presidents['Yeltsin']` should return single data row
        for president with name Yeltsin
 -  `'Yeltsin' in presidents` should return if president
        with same name exists in table
 -  object implements iteration protocol. i.e. you could use it in for loops::
       for president in presidents:
           print(president['name'])
"""

from os import path

from homework8.task2 import TableData

db_name = path.join(path.dirname(__file__), 'example.sqlite')
table_name = 'presidents'


def test_len():
    test_obj = TableData(db_name, table_name)
    assert len(test_obj) == 3


def test_row_return():
    test_obj = TableData(db_name, table_name)
    assert (test_obj['Yeltsin']) == [('Yeltsin', 999, 'Russia')]


def test_contains_pos():
    test_obj = TableData(db_name, table_name)
    assert 'Yeltsin' in test_obj


def test_contains_neg():
    test_obj = TableData(db_name, table_name)
    assert 'Ne_Yeltsin' not in test_obj


def test_iter_protocol():
    test_obj = TableData(db_name, table_name)
    assert [x['name'] for x in test_obj] == ['Yeltsin', 'Trump',
                                             'Big Man Tyrone']
