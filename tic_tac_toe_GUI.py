#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 22:32:41 2025

@author: Dhananjoy Bhuyan
"""

import tkinter as tk
from tkinter import messagebox
from random import choice


root = tk.Tk()
root.title("Tic Tac Toe")

symbol = "X"
bot_symbol = "O"

grid = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None]*3 for _ in range(3)]


def win(player):
    for i in range(3):
        if all(grid[i][j] == player for j in range(3)) or \
           all(grid[j][i] == player for j in range(3)):
            return True
    if all(grid[i][i] == player for i in range(3)) or \
       all(grid[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_tie():
    return all(grid[i][j] != "" for i in range(3) for j in range(3))


def reset_game():
    for i in range(3):
        for j in range(3):
            grid[i][j] = ""
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"


def end_game(message):
    if messagebox.askyesno("Game Over", f"{message}\n\nPlay again?"):
        reset_game()
    else:
        root.destroy()


def computer_move():
    empty = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == ""]

    def try_win(p):
        for i, j in empty:
            grid[i][j] = p
            if win(p):
                grid[i][j] = ""
                return i, j
            grid[i][j] = ""
        return None

    move = try_win(bot_symbol)
    if not move:
        move = try_win(symbol)
    if not move:
        if grid[1][1] == "":
            move = (1, 1)
        else:
            corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
            av_corners = [pos for pos in corners if pos in empty]
            move = choice(av_corners) if av_corners else choice(empty)
    if (grid[0][0] == symbol and grid[2][2] == symbol) or (grid[2][0] == symbol and grid[0][2] == symbol):
        is_second_move = True
        for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if grid[r][c] != "":
                is_second_move = False
        if is_second_move:
            move = choice([(0, 1), (1, 0), (1, 2), (2, 1)])

    else:
        if grid[1][0] == symbol and grid[2][1] == symbol:
            if grid[2][0] == "":
                move = (2, 0)
        elif grid[1][0] == symbol and grid[0][1] == symbol:
            if grid[0][0] == "":
                move = (0, 0)
        elif grid[1][2] == symbol and grid[2][1] == symbol:
            if grid[2][2] == '':
                move = (2, 2)
        elif grid[1][2] == symbol and grid[0][1] == symbol:
            if grid[0][2] == '':
                move = (0, 2)

    i, j = move
    grid[i][j] = bot_symbol
    buttons[i][j]["text"] = bot_symbol
    buttons[i][j]["state"] = "disabled"

    if win(bot_symbol):
        end_game("You lost.")
    elif check_tie():
        end_game("It's a tie!")


def on_click(i, j):
    if grid[i][j] == "":
        grid[i][j] = symbol
        buttons[i][j]["text"] = symbol
        buttons[i][j]["state"] = "disabled"

        if win(symbol):
            end_game("You won!")
        elif check_tie():
            end_game("It's a tie!")
        else:
            root.after(300, computer_move)


# Create buttons
for i in range(3):
    for j in range(3):
        b = tk.Button(root, text="", font=("Arial", 24), width=9, height=4,
                      command=lambda i=i, j=j: on_click(i, j))
        b.grid(row=i, column=j)
        buttons[i][j] = b

root.mainloop()
