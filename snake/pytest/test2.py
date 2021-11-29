from curses import *
from screen import *

def main(stdscr):
    curs_set(0)
    stdscr = newwin(20, 40, 0, 0)
    # stdscr2 = curses.newwin(7, 8, 7, 8)
    stdscr.timeout(500)
    stdscr.keypad(1)
    start_color()

    init_pair(1, COLOR_BLUE, 0)
    init_pair(2, 0, COLOR_RED)
    # stdscr.attrset(color_pair(1))
    stdscr.border('-', '-', '1', '1')

    y, x = stdscr.getmaxyx()
    key = -1
    phrase = str()
    while key != 27:
        key = stdscr.getch()
        # c_phrase = color(c_fore='YELLOW', c_back='BLUE',
        #                  c_style='BRIGHT', strings=str(phrase)
        #                  )
        phrase = 'HELLO!!\nyou are now sign on\nWELCOME'
        print_screen(stdscr, 'GREEN', 0, str(phrase))
        

        if phrase == 27:
            endwin()

if __name__ == "__main__":
    wrapper(main)
