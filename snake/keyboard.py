#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: sYc
# Date: 2021-02-15 15:57:26
# Version: 0.1
# Description: keyboard watcher
"""
抄来的，没读懂
"""
import sys
import tty
import termios


def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1B:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5B:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)


import pygame

pygame.init()
