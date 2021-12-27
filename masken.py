from microbit import *
import music

# pins
Buzzer_pin = pin0
CrashSensor_pin = pin1

# set up crash sensor
CrashSensor_pin.set_pull(CrashSensor_pin.PULL_UP)

while True:
    # if crash sensor is pressed, play a note, if not stop the music
    if CrashSensor_pin.read_digital() == 1:
        display.set_pixel(0, 0, 0)
        music.stop()

    else:
        display.set_pixel(0, 0, 9)
        music.play("c4:3")

