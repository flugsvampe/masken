from microbit import *
import time
import random

game_running = True
mask_x = 0
mask_y = 2
direction_x = 1
direction_y = 0
apple_x = None
apple_y = None
round = 0
shut_of_pixel = \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mask_length = 1


def apple_ny_position():
    ny_x = random.randint(0, 4)
    ny_y = random.randint(0, 4)
    if (ny_x == mask_x or ny_y == mask_y):
        return apple_ny_position()
    if (display.get_pixel(ny_x, ny_y) != 0):
        return apple_ny_position()
    return [ny_x, ny_y]

def gameover():
    global game_running
    game_running = False
    for light in range(9, -1, -1):
        for x in range(0, 5):
            for y in range(0, 5):
                if (light == 9):
                    display.set_pixel(x, y, light)
                else:
                    if (y == 0 or (y == 1 and x != 1 and x != 3) or y == 2 or
                        (y == 3 and (x == 0 or x == 4)) or
                            (y == 4 and x != 0 and x != 4)):
                        display.set_pixel(x, y, light)
        time.sleep(0.05)
    time.sleep(1)
    for light in range(9, -1, -1):
        for x in range(0, 5):
            for y in range(0, 5):
                old_light = display.get_pixel(x, y)
                if (old_light != 0):
                    display.set_pixel(x, y, light)
        time.sleep(0.05)

while game_running:

    round = round + 1

    if (apple_x is None or apple_y is None):
        pos = apple_ny_position()
        apple_x = pos[0]
        apple_y = pos[1]

    a_presses = button_a.get_presses()
    b_presses = button_b.get_presses()

    if (mask_length > 1):
        display.set_pixel(mask_x, mask_y, 5)
    for x in range(0, 5):
        for y in range(0, 5):
            if (shut_of_pixel[y * 5 + x] == round):
                display.set_pixel(x, y, 0)

    mask_x = mask_x + direction_x
    mask_y = mask_y + direction_y

    if (mask_x == apple_x and mask_y == apple_y):
        apple_x = None
        apple_y = None
        mask_length = mask_length + 1
        for pixel in range(0, 25):
            if (shut_of_pixel[pixel] > round):
                shut_of_pixel[pixel] = shut_of_pixel[pixel] + 1

    if (mask_x >= 5):
        gameover()
        mask_x = 0

    if (game_running and mask_x < 0):
        gameover()
        mask_x = 4

    if (game_running and mask_y >= 5):
        gameover()
        mask_y = 0

    if (game_running and mask_y < 0):
        gameover()
        mask_y = 4

    if (game_running and display.get_pixel(mask_x, mask_y) != 0):
        gameover()

    if (game_running):
        display.set_pixel(mask_x, mask_y, 9)
        shut_of_pixel[mask_y * 5 + mask_x] = round + mask_length

        for light in range(1, 10):
            if (apple_x is not None and apple_y is not None):
                display.set_pixel(apple_x, apple_y, light)
            time.sleep(0.025)
        for light in range(8, -1, -1):
            if (apple_x is not None and apple_y is not None):
                display.set_pixel(apple_x, apple_y, light)
            time.sleep(0.025)

        if (a_presses != button_a.get_presses()):
            if (direction_y == 0):
                if (direction_x == 1):
                    direction_y = -1
                else:
                    direction_y = 1
                direction_x = 0
            else:
                if (direction_y == 1):
                    direction_x = 1
                else:
                    direction_x = -1
                direction_y = 0

        if (b_presses != button_b.get_presses()):
            if (direction_y == 0):
                if (direction_x == 1):
                    direction_y = 1
                else:
                    direction_y = -1
                direction_x = 0
            else:
                if (direction_y == 1):
                    direction_x = -1
                else:
                    direction_x = 1
                direction_y = 0

