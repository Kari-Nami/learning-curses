import curses
from time import sleep
from random import randint

def main(stdscr):
    global window, start_x, start_y, board_height, board_width, character_x, character_y

    window = stdscr
    curses.curs_set(0)
    window.keypad(True)

    start_x, start_y = 2, 2
    board_width, board_height = 16, 8

    character_x = start_x + board_width//2
    character_y = start_y + board_height//2

    character = 'x'
    apple = '@'
    super_apple = '$'
    score = 0

    apple_x, apple_y = generate_apple()

    super_apple_probability = 2
    super_apple_x, super_apple_y = 0, 0
    super_apple_chance = 0

    while True:
        window.clear()

        print_board()

        window.addch(apple_y, apple_x, apple)

        if super_apple_chance == 1:
            window.addstr(super_apple_y, super_apple_x, super_apple)

        window.addstr(character_y, character_x, character)
        window.refresh()

        window.addstr(0, 0, f"({character_x}, {character_y}) Score: {score}")

        global pressed_key
        pressed_key = window.getch()

        if pressed_key == ord('q'):
            window.addstr(0, 0, 'thank you for playing the game')
            window.refresh()
            sleep(1)
            break

        move()

        if character_x == apple_x and character_y == apple_y:
            apple_x, apple_y = generate_apple()
            super_apple_chance = randint(1, super_apple_probability)
            if super_apple_chance == 1:
                super_apple_x, super_apple_y = generate_apple()

            score += 1

        if character_x == super_apple_x and character_y == super_apple_y:
            apple_x, apple_y = generate_apple()
            score += 10
            super_apple_chance = 0
            super_apple_x = super_apple_y = 0

def print_board():
    window.addstr(start_y, start_x, f"+{'-' * board_width}+")
    window.addstr(start_y + 1 + board_height, start_x, f"+{'-' * board_width}+")
    for row in range(1, board_height + 1):
        window.addstr(start_y + row, start_x, f"|")
        window.addstr(start_y + row, start_x + board_width + 1, f"|")

def move():
    global character_x, character_y

    if (pressed_key == ord('w') or pressed_key == curses.KEY_UP) and character_y > start_y + 1:
        character_y -= 1
    elif (pressed_key == ord('r') or pressed_key == curses.KEY_DOWN) and character_y < start_y + board_height:
        character_y += 1
    elif (pressed_key == ord('a') or pressed_key == curses.KEY_LEFT) and character_x > start_x + 1:
        character_x -= 1
    elif (pressed_key == ord('s') or pressed_key == curses.KEY_RIGHT) and character_x < start_x + board_width:
        character_x += 1

def generate_apple():
    x = randint(start_x + 1, board_width + start_x)
    y = randint(start_y + 1, board_height + start_y)

    return x, y


curses.wrapper(main)