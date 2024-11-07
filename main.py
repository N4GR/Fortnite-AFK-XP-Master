from config.imports import *
log = setup("MAIN")

# Local imports.
from modules.gamepad import GamePad, CONTROLLER
from config.obj import PROCESS
import ui.init

class GameModes:
    def __init__(self):
        self.pad = GamePad()

    def Lego(self):
        while True:
            x = round(uniform(-1, 1), 1)
            y = round(uniform(-1, 1), 1)

            log.info(f"Moving joystick: x[{x}], y[{y}]")
            self.pad.Joystick(hold_time = 1, x = x, y = y)

if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(PROCESS.ID)

    log.info("Launching...")

    ui.init.ui()