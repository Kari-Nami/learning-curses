import curses
from random import randint

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)

    global window, game

    window = stdscr

    curses.init_pair(1, 218, -1)

    cat = '''
 /\\_/\\          z
( o.o )   /\\_/\\z
|u   u|  ( -.- )
`0———0´  O╵0—0╵O
'''
    z = ' /\\_/\\         z   '
    cat_blink = '( -.- )   /\\_/\\z'

    game_w, game_h = 12, 8
    game = curses.newwin(game_h, game_w*2+1, 0, 0)
    game.nodelay(True)
    game.bkgdset(' ', curses.color_pair(1))

    cat_x, cat_y = game_w-(len(cat.splitlines()[3])//2), (game_h//2-len(cat.splitlines())//2)-1

    game.box()
    for i in range(len(cat.splitlines())):
        game.addstr(cat_y+i, cat_x, cat.splitlines()[i])

    window.refresh()
    game.refresh()

    while True:
        game.addstr(cat_y+2, cat_x, cat.splitlines()[2])

        key = game.getch()
        if key == ord('q'):
            return

        game.addstr(cat_y+1, cat_x, z)
        game.refresh()

        curses.napms(500)
        game.addstr(cat_y+1, cat_x, f'{cat.splitlines()[1]}  ')

        chance = randint(0, 5)
        if chance == 1:
            game.addstr(cat_y+2, cat_x, cat_blink)
            game.refresh()

        game.refresh()
        curses.napms(500)

curses.wrapper(main)