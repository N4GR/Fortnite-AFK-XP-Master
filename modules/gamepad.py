from config.imports import *
log = setup("MODULES.GAMEPAD")

class CONTROLLER:
    class DPAD:
        LEFT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
        RIGHT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
        UP = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
        DOWN = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
    
    A = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A
    X = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X
    Y = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y
    B = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B


class GamePad:
    def __init__(self):
        """Class to initialise gamepad and perform presses"""
        self.gamepad = vgamepad.VX360Gamepad()
    
    def Run(self, stop_event: threading.Event):
        self.Wake()

        while not stop_event.is_set():
            x = round(uniform(-1, 1), 1)
            y = round(uniform(-1, 1), 1)

            log.info(f"Moving joystick: x[{x}], y[{y}]")
            self.Joystick(hold_time = randint(1, 10), x = x, y = y)
            # Wait for joysticks to do their actions.
            self.random_sleep(stop_event)
        
        log.info("Stop event detected, exitting gamepad.")

    def Wake(self):
        """Function to press a random button to wake up the device and detect it with game."""

        log.info("Waking up controller.")

        self.gamepad.press_button(button = CONTROLLER.A)
        self.gamepad.update()
        time.sleep(0.5)
        self.gamepad.release_button(button = CONTROLLER.A)
        self.gamepad.update()
        time.sleep(0.5)

    def Press(self, button: CONTROLLER):
    def random_sleep(
            self,
            stop_event: threading.Event,
            random_range: tuple[int, int] = (1, 10)
        ):
        """Function that will sleep for x amount of seconds, checking each second if the stop event is set or not.

        Args:
            stop_event (threading.Event): Threading event that will be set if the program closes.
            random_range (tuple[int, int], optional): A range of x -> x that the program will randomly select a number from. Defaults to (1, 10).
        """
        a, b = random_range
        sleep_time = randint(a, b)
        
        log.info(f"Gamepad sleeping for {sleep_time} seconds.")
        
        for x in range(sleep_time):
            if stop_event.is_set():
                break
            else:
                time.sleep(1)
        """Function that takes a button from CONTROLLER class to press.

        Args:
            button (CONTROLLER): Button from CONTROLLER class.
        """
        
        self.gamepad.press_button(button = button)
        self.gamepad.update()
        time.sleep(1)
        self.gamepad.release_button(button = button)

        return button
    
    def Joystick(self, hold_time: int, x: float, y: float) -> None:
        self.gamepad.left_joystick_float(x_value_float = x, y_value_float = y)
        self.gamepad.right_joystick_float(x_value_float = x, y_value_float = y)

        self.gamepad.update()

        time.sleep(hold_time)
        self.gamepad.reset()