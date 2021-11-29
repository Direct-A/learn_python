#!/usr/bin/env python
# coding:utf-8
# Author: sYc
# Date: 2021-02-11 13:08:25
# Version: 0.1
# Description: Print colorful in terminal
#              a expand of moudle colorama

from colorama import init
from colorama.ansi import (
    CSI,
    set_title,
    clear_screen,
    clear_line,
    Fore,
    Back,
    Style,
    Cursor,
    AnsiCodes,
    AnsiFore,
    AnsiBack,
    AnsiStyle,
    AnsiCursor,
)

"""
init
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
Cursor: UP, DOWN, FORWARD, BACK, POS
set_title, clear_screen, clear_line
"""
init(autoreset=True)


class Style2(AnsiStyle):
    HLIGHT = 1  # 设置高亮度
    ULINE = 4  # 下划线
    FLASH = 5  # 闪烁
    REVERSE = 7  # 反显
    F_TO_B = 8  # 消隐


class Cursor2(AnsiCursor):
    def SAVE(self):
        return CSI + "s"  # 保存光标位置

    def RTURN(self):
        return CSI + "u"  # 恢复光标位置

    def HID(self):
        return CSI + "?25l"  # 隐藏光标

    def SHOW(self):
        return CSI + "?25h"  # 显示光标


Style = Style2()
Cursor = Cursor2()
CLR = clear_line(mode=2)
CLS = clear_screen(mode=2)


def color(c_fore="RESET", c_back="RESET", c_style="NORMAL", strings=""):
    return "{}{}{}{}".format(
        getattr(Style, c_style), getattr(Fore, c_fore), getattr(Back, c_back), strings
    )
