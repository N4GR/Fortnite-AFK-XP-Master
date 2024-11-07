from config.imports import *
log = setup("UI.LEGO")

# Python imports.
from random import uniform, randint
import threading

# Local imports.
from modules.gamepad import GamePad, CONTROLLER
from ui.imports import *
from ui.assets import button

class InfoDialog(QDialog):
    def __init__(self, message: str, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Information")
        layout = QVBoxLayout(self)

        message_label = QLabel(message, self)
        layout.addWidget(message_label)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok, self)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

class Lego:
    def __init__(self,
                 main_window: QMainWindow,
                 size: tuple[int] = (280, 210),
                 position: tuple[int] = (10, 75)):
        # Setting arguments to variables.
        self.main_window = main_window
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
        self.buttons = buttons(self.main_window, self.layout, self.widget)

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

class buttons():
    def __init__(self,
                 main_window: QMainWindow,
                 layout: QVBoxLayout,
                 widget: QWidget) -> None:
        # Assigning variables from arguments.
        self.main_window = main_window
        self.layout = layout
        self.widget = widget
        self.button_assets = button()

        self.start_button = self.startButton(main_window = self.main_window,
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
                     button_assets: button,
                     layout: QVBoxLayout,
                     widget: QWidget):
            # Assigning variables from arguments.
            self.main_window = main_window
            self.button_assets = button_assets
            self.layout = layout
            self.widget = widget

            # Setting Dimensions.
            self.width, self.height = (100, 64)
            self.x, self.y = (10, 10)

            # Creating button widget.
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(lambda: Functions.start(self.main_window, self.button, self.button_assets))

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
    
    def start(main_window: QMainWindow, button: QPushButton, button_assets):
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
            print("Starting Lego Fortnite thread.")
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
            thread = threading.Thread(target = pad.Run, args = (stop_event,))
            thread.start()

        else:
            timer.stop()
            label.deleteLater()

            print("Stopping Lego Fortnite thread.")
            is_pressed = False

            stop_event.set()

            # Setting the start button to pause.
            button.setIcon(QIcon(QPixmap.fromImage(button_assets.start.up)))
        