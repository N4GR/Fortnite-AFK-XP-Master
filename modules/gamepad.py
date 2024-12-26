from config.imports import *
log = setup("MODULES.GAMEPAD")

class Controller:
    def __init__(self, gamepad: vgamepad.VX360Gamepad):
        self.dpad = self.DPad()
        self.face = self.Face()
        self.joystick = self.JoyStick(gamepad)
    
    class DPad:
        def __init__(self):
            self.left = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
            self.right = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
            self.up = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
            self.down = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
    
    class Face:
        def __init__(self):
            self.a = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A
            self.x = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X
            self.y = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y
            self.b = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B
    
    class JoyStick:
        def __init__(self, gamepad: vgamepad.VX360Gamepad):
            self.left = gamepad.left_joystick_float
            self.right = gamepad.right_joystick_float


class GamePad:
    def __init__(self):
        """Class to initialise gamepad and perform presses"""
        self.gamepad = vgamepad.VX360Gamepad()
        self.controller = Controller(self.gamepad)
    
    def run_lego(self, stop_event: threading.Event):
        self.wake()

        while not stop_event.is_set():
            x = round(uniform(-1, 1), 1)
            y = round(uniform(-1, 1), 1)

            log.info(f"Moving joystick: x[{x}], y[{y}]")
            
            # Run joysticks.
            self.joystick(
                x = round(uniform(-1, 1), 1),
                y = round(uniform(-1, 1), 1),
                joystick = self.controller.joystick.left
            )
            
            self.joystick(
                x = round(uniform(-1, 1), 1),
                y = round(uniform(-1, 1), 1),
                joystick = self.controller.joystick.right
            )
            
            # Wait for joysticks to do their actions.
            self.random_sleep(stop_event)
            self.random_sleep(stop_event, random_range = (1, 5))
            
            # Release joysticks.
            self.release_joystick(self.controller.joystick.left)
            self.release_joystick(self.controller.joystick.right)
        
        log.info("Stop event detected, exitting gamepad.")

    def wake(self):
        """Function to press a random button to wake up the device and detect it with game."""

        log.info("Waking up controller.")

        self.gamepad.press_button(button = self.controller.face.a)
        self.gamepad.update()
        time.sleep(0.5)
        self.gamepad.release_button(button = self.controller.face.a)
        self.gamepad.update()
        time.sleep(0.5)

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

    def press(self, button: Controller.Face):
        """Function that takes a button from CONTROLLER class to press.

        Args:
            button (CONTROLLER): Button from CONTROLLER class.
        """
        
        self.gamepad.press_button(button = button)
        self.gamepad.update()
        time.sleep(1)
        self.gamepad.release_button(button = button)

        return button
    
    def joystick(self, x: float, y: float, joystick: Controller.JoyStick) -> Controller.JoyStick:
        joystick(x_value_float = x, y_value_float = y)
        self.gamepad.update()
        
        return joystick
    
    
    def release_joystick(self, joystick: Controller.JoyStick) -> Controller.JoyStick:
        self.gamepad.reset()
        
        return joystick
    
    def hold_button(self, button: Controller.Face):
        self.gamepad.press_button(button = button)
        self.gamepad.update()
        
        return button
    
    def release_button(self, button: Controller.Face):
        self.gamepad.release_button(button = button)
        
        return button