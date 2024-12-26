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

class jam_reel:
    # First number = x
    # Second number = y
    up = (0, 1)
    top_right = (1, 1)
    right = (1, 0)
    bottom_right = (1, -1)
    bottom = (0, -1)
    bottom_left = (-1, -1)
    left = (-1, 0)
    top_left = (-1, 1)
    
    reels = [
        up, top_right, right,
        bottom_right, bottom,
        bottom_left, left,
        top_right
    ]

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
            self.random_sleep(stop_event, random_range = (1, 5))
            
            # Release joysticks.
            self.release_joystick(self.controller.joystick.left)
            self.release_joystick(self.controller.joystick.right)
        
        log.info("Stop event detected, exitting gamepad.")
    
    def run_jam(self, stop_event: threading.Event):
        self.wake()
        
        while not stop_event.is_set():
            # Hold button to open jam loops.
            held_button = self.hold_button(self.controller.dpad.down)
            
            # Wait for loops to open.
            self.random_sleep(stop_event, random_range = (1, 1))
            
            # Switch instrument.
            self.press(self.controller.face.y)
            
            x, y = choice(jam_reel.reels)
            
            # Change song.
            held_joystick = self.joystick(x = x, y = y, joystick = self.controller.joystick.right)
            
            # Wait for song to be selected.
            self.random_sleep(stop_event, random_range = (1, 2))
            
            # Stop joystick movement.
            self.release_joystick(held_joystick)
            
            # Close jam loops.
            self.release_button(held_button)
            
            # Wait for next song to be played.
            self.random_sleep(stop_event, random_range = (10, 20))
        
        log.info("Stop event for jam detected, exitting gamepad.")

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
        
        log.info(f"Sleeping for {sleep_time} seconds.")
        
        for x in range(sleep_time):
            if stop_event.is_set():
                break
            else:
                time.sleep(1)
            
            if x + 1 == sleep_time:
                log.info("Sleep achieved.")

    def press(self, button: Controller.Face):
        """Function that takes a button from CONTROLLER class to press.

        Args:
            button (CONTROLLER): Button from CONTROLLER class.
        """
        
        self.gamepad.press_button(button = button)
        self.gamepad.update()

        return button
    
    def joystick(self, x: float, y: float, joystick: Controller.JoyStick) -> Controller.JoyStick:
        joystick(x_value_float = x, y_value_float = y)
        self.gamepad.update()
        
        return joystick
    
    def release_joystick(self, joystick: Controller.JoyStick) -> Controller.JoyStick:
        self.gamepad.reset()
        self.gamepad.update()
        
        return joystick
    
    def hold_button(self, button: Controller.Face):
        self.gamepad.press_button(button = button)
        self.gamepad.update()
        
        return button
    
    def release_button(self, button: Controller.Face):
        self.gamepad.release_button(button = button)
        self.gamepad.update()
        
        return button