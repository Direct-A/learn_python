#!/usr/bin/env python
# coding:utf-8
# Author: sYc
# Date: 2021-02-13 17:32:49
# Version: 0.2
# Description: print paragraphs on screen for snake game

import curses


def getcolor(color: object) -> int:
    """to simplify usage of curses.COLOR_XXX

    Parameters:
        color: color name or 0, contained: black green blue red yellow white cyan magenta

    Returns:
        0: use default color
    """
    if color == 0:
        return 0
    else:
        color = "COLOR_" + color.upper()
        return getattr(curses, color)


def print_screen(window: "curses._CursesWindow", p_fore: str, p_back: str, phrase: str):
    """print_screen: for print multi-line phrase

    Args:
        window (curses._CursesWindow): a stdscr obj
        p_fore (str): foreground of print phrase
        p_back (str): background of print phrase
        phrase (str): the phrase to print, which can be multi lines, use `\n` to split lines
    """

    # init line & column
    ln, col = window.getmaxyx()

    # locate start point
    ln_count = phrase.count("\n") + 1
    y_axle = (ln - ln_count) // 2

    # convert color to fit curses
    curses.init_pair(1, getcolor(p_fore), getcolor(p_back))

    phrase_cut = phrase.split(sep="\n")
    for phrase in phrase_cut:
        phrase_count = len(phrase)
        x_axle = (col - phrase_count) // 2

        window.addstr(y_axle, x_axle, str(phrase), curses.color_pair(1))
        y_axle += 1

    # restore color_pairs
    curses.start_color()
