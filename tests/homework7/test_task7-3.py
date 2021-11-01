import pytest

from homework7.task3 import tic_tac_toe_checker


def test_unfinished():
    board = [
     ['-', '-', 'o'],
     ['-', 'x', 'o'],
     ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'unfinished'


def test_draw():
    board = [
        ['o', 'x', 'o'],
        ['x', 'x', 'o'],
        ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'draw'


def test_x_wins():
    board = [
        ['-', '-', 'x'],
        ['x', 'x', 'o'],
        ['x', 'o', 'o']]
    assert tic_tac_toe_checker(board) == 'x wins!'


def test_o_wins():
    board = [
        ['-', '-', 'o'],
        ['x', 'x', 'o'],
        ['x', 'o', 'o']]
    assert tic_tac_toe_checker(board) == 'o wins!'


def test_wrong_board():
    board = [
        ['-', 'y', 'o'],
        ['x', 'x', 'o'],
        ['x', 'o', 'o']]
    with pytest.raises(ValueError):
        assert tic_tac_toe_checker(board)
