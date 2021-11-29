import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, wrapper
from random import randint

# 封装后可以交给wrapper()
# win = curses.newwin(20, 60, 0, 0)

def main(stdscr):
    stdscr.border(0)
    stdscr.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    stdscr.nodelay(1)
    # 不需要refresh的关键
    stdscr.timeout(200)


    y, x = stdscr.getmaxyx()

    # Initializing values
    key = KEY_RIGHT
    score = 0

    # Initial snake co-ordinates
    snake = [[4,4], [4,3], [4,2], [4,1]]
    # First food co-ordinates
    food = [9, 8]

    # Prints the food
    stdscr.addch(food[0], food[1], '*')

    # While Esc key is not pressed
    while key != 27:
        # 绘制边框
        # stdscr.border(0)
        # Printing 'Score' and
        stdscr.addstr(0, 2, 'Score : ' + str(score) + ' ')
        # 'SNAKE' strings
        stdscr.addstr(0, 27, ' SNAKE ')

        # Previous key pressed
        # 在获取输入时refresh
        prevKey = key
        event = stdscr.getch()
        # 无输入，非阻塞输入返回-1
        key = key if event == -1 else event

        # Increases the speed of Snake as its length increases
        # 非阻塞输入，无输入时返回-1
        # stdscr.timeout(round(150 - (len(snake)/5 + len(snake)/10) % 120))

        # If SPACE BAR is pressed, wait for another
        if key == ord(' '):
            # one (Pause/Resume)
            key = -1
            while key != ord(' '):
                key = stdscr.getch()
            key = prevKey
            continue

        # If an invalid key is pressed
        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
            key = prevKey

        # If snake crosses the boundaries, make it enter from the other side
        # 没搞明白，这居然能实现
        if snake[0][0] == 0:
            snake[0][0] = y-2
        if snake[0][1] == 0:
            snake[0][1] = x-2
        
        if snake[0][0] == y-1:
            snake[0][0] = 1
        if snake[0][1] == x-1:
            snake[0][1] = 1
        stdscr.refresh()

        # Exit if snake crosses the boundaries (Uncomment to enable)
        # if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

        # If snake runs over itself
        if snake[0] in snake[1:]:
            if key == prevKey:
                break

        stdscr.refresh()
        # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
        # This is taken care of later at [1].
        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                        snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # When snake eats the food
        if snake[0] == food:
            food = []
            score += 1
            while food == []:
                # Calculating next food's coordinates
                food = [randint(1, 18), randint(1, 58)]
                if food in snake:
                    food = []
            stdscr.addch(food[0], food[1], '*')
        else:
            # [1] If it does not eat the food, length decreases
            last = snake.pop()
            stdscr.addch(last[0], last[1], ' ')
        stdscr.addstr(snake[0][0], snake[0][1], '#')

    curses.endwin()

wrapper(main)

# print("\nScore - " + str(score))
# print("http://bitemelater.in\n")
