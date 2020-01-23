# CircuitPython IO demo #1 - General Purpose I/O
# When badge button a pressed, pin 13 goes high.
# Need to add LED separately
# Copy files onto badge: https://github.com/adafruit/CircuitPython_Badge_README/tree/master/final_versions/HACKADAY_SUPERCON_2019
# Then replace replace contents of code.py with this text

from adafruit_pybadger import PyBadger

pybadger = PyBadger()

import time
import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# For Gemma M0, Trinket M0, Metro M0 Express, ItsyBitsy M0 Express, Itsy M4 Express
switch = DigitalInOut(board.D2)
# switch = DigitalInOut(board.D5)  # For Feather M0 Express, Feather M4 Express
# switch = DigitalInOut(board.D7)  # For Circuit Playground Express
switch.direction = Direction.INPUT
switch.pull = Pull.UP

first_display = True

while True:
    # We could also do "led.value = not switch.value"!
    if pybadger.button.a:
        led.value = True
    else:
        led.value = False

    time.sleep(0.01)  # debounce delay
