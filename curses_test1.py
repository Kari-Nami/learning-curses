import curses
from time import sleep


def main(window):

    # curses.curs_set(0)
    # window.nodelay(True)

    x = 5
    y = 10

    while True:
        window.clear()
        window.addstr(y, x, '@')
        window.refresh()

        window_height, window_width = window.getmaxyx()
        window.addstr(0, 0, f'({window_height}, {window_width})   ({y}, {x})')

        pressed_key = window.getch()
        if pressed_key == ord('q'):
            window.addstr(0, 0, 'thank you for playing the game')
            window.refresh()
            sleep(1)
            break
        elif pressed_key == ord('w') and y > 0: y -= 1
        elif pressed_key == ord('r') and y < window_height-1: y += 1
        elif pressed_key == ord('a') and x > 0: x -= 1
        elif pressed_key == ord('s') and x < window_width-3: x += 1


curses.wrapper(main)