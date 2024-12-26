from config.imports import *
log = setup("UI.LEGO")

# Python imports.
from random import uniform, randint
import threading

# Local imports.
from modules.gamepad import GamePad
from ui.imports import *
from ui.assets import button

from ui.obj import (
    InfoDialog
)

class Lego:
    def __init__(self,
                 main_window: QMainWindow,
                 jam_button: QPushButton,
                 lego_button: QPushButton,
                 size: tuple[int] = (280, 210),
                 position: tuple[int] = (10, 75)):
        log.info("Launching UI.")

        # Setting arguments to variables.
        self.main_window = main_window
        self.jam_button = jam_button
        self.lego_button = lego_button
        self.width, self.height = size
        self.x, self.y = position

        # Creating the widget and layout.
        self.widget = QWidget(parent = self.main_window)
        self.layout = QVBoxLayout()

        # Add stuff to layout
        #
        #
        #self.label = QLabel("Lego!", self.main_window)
        #self.layout.addWidget(self.label)

        # Adding buttons.
        self.buttons = buttons(self.main_window, self.jam_button, self.lego_button, self.layout, self.widget)

        # Setting layout to widget.
        self.widget.setLayout(self.layout)

        # Making the background of the window transparent.
        self.widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Setting size of widget and its position.
        self.widget.setGeometry(self.x, self.y,
                                self.width, self.height)
        self.widget.setStyleSheet("background-color: lightgray; border: 1px solid black;")

    def GetWidget(self):
        return self.widget
    
    def get_stop_event(self):
        global stop_event
        
        return stop_event

class buttons():
    def __init__(self,
                 main_window: QMainWindow,
                 jam_button: QPushButton,
                 lego_button: QPushButton,
                 layout: QVBoxLayout,
                 widget: QWidget) -> None:
        # Assigning variables from arguments.
        self.main_window = main_window
        self.jam_button = jam_button
        self.lego_button = lego_button
        self.layout = layout
        self.widget = widget
        self.button_assets = button()

        self.start_button = self.startButton(main_window = self.main_window,
                                             jam_button = self.jam_button,
                                             lego_button = self.lego_button,
                                             button_assets = self.button_assets,
                                             layout = self.layout,
                                             widget = self.widget)

        self.help_button = self.helpButton(main_window = self.main_window,
                                           button_assets = self.button_assets,
                                           layout = self.layout,
                                           widget = self.widget)

    class startButton:
        def __init__(self,
                     main_window: QMainWindow,
                     jam_button: QPushButton,
                     lego_button: QPushButton,
                     button_assets: button,
                     layout: QVBoxLayout,
                     widget: QWidget):
            # Assigning variables from arguments.
            self.main_window = main_window
            self.button_assets = button_assets
            self.layout = layout
            self.widget = widget
            self.jam_button = jam_button
            self.lego_button = lego_button

            # Setting Dimensions.
            self.width, self.height = (100, 64)
            self.x, self.y = (10, 10)

            # Creating button widget.
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(lambda: Functions.start(self.main_window, self.button, self.button_assets, self.jam_button, self.lego_button))

            # Assigning dimensions.
            self.button.setGeometry(self.x, self.y,
                                    self.width, self.height)
            
            # Setting icon on the button.
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.start.up)))
            self.button.setIconSize(QSize(self.width, self.height))

            # Setting button style. -> Removing the background.
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

            self.layout.addWidget(self.button, alignment = Qt.AlignmentFlag.AlignCenter)

    class helpButton:
        def __init__(self,
                     main_window: QMainWindow,
                     button_assets: button,
                     layout: QVBoxLayout,
                     widget: QWidget):
            # Assigning variables from arguments.
            self.main_window = main_window
            self.button_assets = button_assets
            self.layout = layout
            self.widget = widget

            # Setting Dimensions.
            self.width, self.height = (30, 30)
            self.x, self.y = (10, 10)

            # Creating button widget.
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(lambda: Functions.help(self.main_window))

            # Assigning dimensions.
            self.button.setGeometry(self.x, self.y,
                                    self.width, self.height)
            
            # Setting icon on the button.
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.help.up)))
            self.button.setIconSize(QSize(self.width, self.height))

            # Setting button style. -> Removing the background.
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

            self.layout.addWidget(self.button, alignment = Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        def makeLambda(self, func):
            '''Basic function to return a lambda for buttons
            
            Return:
                lambda func(self.main_menu)
            '''
            return lambda: func(self.main_window, self.button, self.button_assets)

# Creating all the necessary variables for the start globals.
is_pressed : bool = False
stop_event : threading.Event = None
thread : threading.Thread = None
seconds_elapsed : int = 0
timer : QTimer = None
label : QLabel = None
class Functions:
    def help(main_window: QMainWindow):
        message = "Howdy, partna!\n1. Launch into a Lego Fortnite world.\n2. Press start and click into the game.\n\nDone!"

        dialog = InfoDialog(message = message,
                            parent = main_window)
        dialog.exec()
    
    def start(
            main_window: QMainWindow,
            button: QPushButton,
            button_assets: button,
            jam_button: QPushButton,
            lego_button: QPushButton
        ):
        
        global is_pressed
        global stop_event
        global thread
        global seconds_elapsed
        global timer
        global label

        def startTimer(timer):
            timer.start(1000)
        
        def updateTimer(label):
            global is_pressed
            if is_pressed is True:
                global seconds_elapsed
                seconds_elapsed += 1
                hours, remainder = divmod(seconds_elapsed, 3600)
                minutes, seconds = divmod(remainder, 60)
                label.setText(f"{hours}:{minutes:02d}:{seconds:02d}")
        
        # Creating the Gamepad object.
        pad = GamePad()

        # Do this on the first run.
        if is_pressed is False:
            log.info("Launching lego fortnite thread.")

            # Disabling jam button
            log.info("Disabling jam button.")
            jam_button.setDisabled(True)

            # Disabling Lego button
            log.info("Disabling lego button.")
            lego_button.setDisabled(True)

            is_pressed = True
            seconds_elapsed = 0

            #####
            label = QLabel("0:00:00", main_window)
            label.setStyleSheet("font-size: 30px;")

            label.setGeometry(105, 150, 100, 100)

            label.show()

            # Creating and setting timer.
            timer = QTimer(main_window)
            timer.timeout.connect(lambda: updateTimer(label))

            startTimer(timer)

            # Setting the start button to pause.
            button.setIcon(QIcon(QPixmap.fromImage(button_assets.pause.up)))

            # Creating the stop event.
            stop_event = threading.Event()

            # Start the thread.
            thread = threading.Thread(target = pad.run_lego, args = (stop_event,))
            thread.start()

        else:
            timer.stop()
            label.deleteLater()

            log.info("Stopping lego fortnite thread.")
            is_pressed = False

            # Enabling jam button again.
            log.info("Enabling jam button.")
            jam_button.setEnabled(True)

            # Enabling lego button
            log.info("Enabling lego button.")
            lego_button.setEnabled(True)

            stop_event.set()

            log.info("Lego fortnite thread stopped.")

            # Setting the start button to pause.
            button.setIcon(QIcon(QPixmap.fromImage(button_assets.start.up)))
        