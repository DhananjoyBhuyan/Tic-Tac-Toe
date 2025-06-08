#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 22:32:41 2025

@author: Dhananjoy Bhuyan
"""
from random import choice

grid = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

move_map = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2)}


def print_grid():
    global grid

    print('---------')
    for i in grid:
        print(" | ".join(i))
        print('---------')


def get_symbol():
    while 1:
        symbol = input("Which symbol will you choose? (X/O): ").upper().strip()
        if symbol not in ['X', 'O']:
            print("You should've entered either X or O.")
        else:
            if symbol == 'X':
                return 'X', 'O'
            else:
                return 'O', 'X'


def win(symbol: str):
    global grid

    for i in grid:
        if ''.join(i) == symbol*3:
            return True
    for i in zip(*grid):
        if ''.join(list(i)) == symbol*3:
            return True
    if ''.join([grid[i][i] for i in range(3)]) == symbol*3:
        return True
    elif ''.join([grid[i][2 - i] for i in range(3)]) == symbol*3:
        return True
    return False


symbol, bot_symbol = get_symbol()


def computer_move():
    global grid
    global bot_symbol
    global symbol

    empty_cells = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] in '123456789':
                empty_cells.append((i, j))

    def find_winning_move(symbol: str):
        for i, j in empty_cells:
            old = grid[i][j]
            grid[i][j] = symbol
            if win(symbol):
                grid[i][j] = old
                return i, j
            else:
                grid[i][j] = old
        return None

    mv = find_winning_move(bot_symbol)
    if mv:
        return mv
    else:
        block_user = find_winning_move(symbol)
        if block_user:
            return block_user

    if grid[1][1] == "5":
        return (1, 1)
    if (grid[0][0] == symbol and grid[2][2] == symbol) or (grid[2][0] == symbol and grid[0][2] == symbol):
        is_second_move = True
        for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if grid[r][c] not in "123456789":
                is_second_move = False
        if is_second_move:
            return choice([(0, 1), (1, 0), (1, 2), (2, 1)])
    else:
        if grid[1][0] == symbol and grid[2][1] == symbol:
            if grid[2][0] == "7":
                return (2, 0)
        elif grid[1][0] == symbol and grid[0][1] == symbol:
            if grid[0][0] == "1":
                return (0, 0)
        elif grid[1][2] == symbol and grid[2][1] == symbol:
            if grid[2][2] == '9':
                return (2, 2)
        elif grid[1][2] == symbol and grid[0][1] == symbol:
            if grid[0][2] == '3':
                return (0, 2)
    corners = [(0, 0), (2, 2), (0, 2), (2, 0)]
    available_corners = [i for i in corners if i in empty_cells]
    if available_corners:
        return choice(available_corners)

    if grid[1][1] == '5':
        return (1, 1)
    else:
        return choice(empty_cells)


while 1:

    print_grid()

    try:
        move = move_map[input("Enter cell number(1-9): ").strip()]
    except KeyError:
        print("Invalid input!!")
        continue

    if grid[move[0]][move[1]] in '123456789':
        grid[move[0]][move[1]] = symbol
    else:
        print("Nope, that spot is taken. Try another.")
        continue

    if win(symbol):
        print_grid()
        print("You won!!")
        break

    if all(j not in "123456789" for i in grid for j in i):
        print_grid()
        print("It's a tie!!!")
        break

    row, col = computer_move()
    grid[row][col] = bot_symbol

    if win(bot_symbol):
        print_grid()
        print("You lost.")
        break

    if all(j not in "123456789" for i in grid for j in i):
        print_grid()
        print("It's a tie!!!")
        break
