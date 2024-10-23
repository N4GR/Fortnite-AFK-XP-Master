from imports import *

# Local imports.
from gamepad import GamePad, CONTROLLER

from random import uniform

if __name__ == "__main__":
    pad = GamePad()

    while True:
        pad.Joystick(hold_time = 1, x = round(uniform(-1, 1), 1), y = round(uniform(-1, 1), 1))