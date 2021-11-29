#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: sYc
# Date: 2021-02-15 15:59:14
# Version: 0.1
# Description: core program to cacluate snake

import random
from time import sleep
from render import Cursor, Fore, Back, Style


class Snake:
    def __init__(self, window: 'curses._CursesWindow', char: str='#'):
        """

        Args:
            window:
            char:
        """
        self.char = char
        self.scr = window
        self.
        y, x = self.scr.getmaxyx()

        # init snake body
        x1 = random.randint(0, x - 4)
        y1 = random.randint(0, y - 4)
        if random.randint(0, 1):
            x2 = x1 + 1 if random.randint(0, 1) else x1 - 1
            y2 = y1
            x3 = x2 + 1 if x2 > x1 else x2 - 1
            y3 = y2
        else:
            x2 = x1
            y2 = y1 + 1 if random.randint(0, 1) else y1 - 1
            y3 = y2 + 1 if y2 > y1 else y2 - 1
            x3 = x2
        snake = [(y1, x1), (y2, x2), (y3, x3)]

        # init food
        x4 = random.randint(0, x - 1)
        y4 = random.randint(0, y - 1)
        food = [y4, x4]


def snake_block(x_axle, y_axle, block):
    print(Cursor.HID() +
          Cursor.POS(x=x_axle, y=y_axle) +
          Fore.GREEN +
          Back.GREEN +
          str(block)
          )


def start_snake():
    r_num = random.randint(5, 8)
    d_num = r_num % 4
    if d_num == 1:
        return 'R'
    elif d_num == 2:
        return 'D'
    elif d_num == 3:
        return 'L'
    else:
        return 'U'


def adder(x_axle, y_axle, direction):
    sleep(1)
    if direction == 'w':
        y_axle += 1
    if direction == 's':
        y_axle -= 1
    if direction == 'd':
        x_axle += 2
    if direction == 'a':
        x_axle -= 2
    snake_block(x_axle, y_axle, '[]')
