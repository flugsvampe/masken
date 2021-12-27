from microbit import *
import time

mask_x = 0
mask_y = 2
direction_x = 1
direction_y = 0

while True:

    a_presses = button_a.get_presses()
    b_presses = button_b.get_presses()

    display.set_pixel(mask_x, mask_y, 0)
    mask_x = mask_x + direction_x
    mask_y = mask_y + direction_y

    if (mask_x >= 5):
        mask_x = 0

    if (mask_x < 0):
        mask_x = 4

    if (mask_y >= 5):
        mask_y = 0

    if (mask_y < 0):
        mask_y = 4

    display.set_pixel(mask_x, mask_y, 9)

    time.sleep(0.5)

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

