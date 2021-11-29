#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: sYc
# Date: 2021-02-15 14:36:43
# Version: 0.1
# Description:

import curses
import time

import screen

stdscr = curses.initscr()


def main(window: "curses._CursesWindows"):
    curses.curs_set(0)
    window.keypad(1)
    window.nodelay(1)

    phrase = "!!!!WELCOME TO SNAKE!!!!\n\na simple tui game by sYc"
    screen.print_screen(window, "blue", "white", phrase)
    window.refresh()

    time.sleep(5)


if __name__ == "__main__":
    curses.wrapper(main)
