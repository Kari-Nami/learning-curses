import curses
from time import sleep

def main(window):
    window = window

    board_h, board_w = 16, 16
    player = '██'
    player_x, player_y = board_w-1, board_h//2

    body = '##'
    snake_length = 1
    current_rotation = -1  # 0 = u, 1 = r, 2 = d, 3 = l

    window.refresh()

    board = curses.newwin(board_h, board_w*2, 1, 0)
    curses.curs_set(0)
    # board.nodelay(True)
    board.keypad(True)
    board.box()

    board.refresh()
    while True:
        window.addstr(0, 0, f'rotation: {current_rotation} ')

        board.addstr(player_y, player_x, player)
        window.refresh()
        board.refresh()

        key = board.getch()

        board.addstr(player_y, player_x, '  ')

        if key == ord('q'):
            return

        elif key == ord('w') and player_y>1:
            current_rotation = 0
            player_y -= 1

        elif key == ord('s') and player_x<board_w*2-3:
            current_rotation = 1
            player_x += 2

        elif key == ord('r') and player_y<board_h-2:
            current_rotation = 2
            player_y += 1

        elif key == ord('a') and player_x>1:
            current_rotation = 3
            player_x -= 2

        # if current_rotation != -1:
        #     if current_rotation == 0 and player_y>1: player_y -= 1








curses.wrapper(main)