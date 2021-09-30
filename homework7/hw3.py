"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    flat = ''.join([char for row in board for char in row])
    flat = flat.replace('-', '0').replace('o', '1').replace('x', '5')
    try:
        flat = [int(x) for x in flat]
    except ValueError:
        raise ValueError('Wrong board')

    unfinished_flag = 0
    if 0 in flat:
        unfinished_flag = 1

    win_variants = [flat[:3], flat[3:6], flat[6:9],  # rows
                    flat[::3], flat[1::3], flat[2::3],  # columns
                    flat[::4], flat[2::2][:3]]  # diagonals

    for var in win_variants:
        if sum(var) == 3:
            return 'o'
        elif sum(var) == 15:
            return 'x'
        else:
            if unfinished_flag:
                return 'unfinished'
            else:
                return 'draw'
