from config.imports import *
log = setup("UI.JAM")

from ui.imports import *
from ui.assets import button

class InfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Information')
        layout = QVBoxLayout(self)

        message_label = QLabel('This is an informational popup!', self)
        layout.addWidget(message_label)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok, self)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

class Jam:
    def __init__(self,
                 main_window: QMainWindow,
                 size: tuple[int] = (280, 210),
                 position: tuple[int] = (10, 75)):
        log.info("Launching UI.")
        
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
        self.label = QLabel("Jam time, stay tuned for the next update!", self.main_window)
        self.layout.addWidget(self.label)
        ####

        # Adding buttons.
        self.buttons = buttons(self.main_window, self.layout)

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
                 layout: QVBoxLayout) -> None:
        # Assigning variables from arguments.
        self.main_window = main_window
        self.layout = layout
        self.button_assets = button()

        self.help_button = self.helpButton(main_window = self.main_window,
                                           button_assets = self.button_assets,
                                           layout = self.layout)
    
    class helpButton:
        def __init__(self,
                     main_window: QMainWindow,
                     button_assets: button,
                     layout: QVBoxLayout):
            # Assigning variables from arguments.
            self.main_window = main_window
            self.button_assets = button_assets
            self.layout = layout

            # Setting Dimensions.
            self.width, self.height = (30, 30)
            self.x, self.y = (10, 10)

            # Creating button widget.
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(self.func)

            # Assigning dimensions.
            self.button.setGeometry(self.x, self.y,
                                    self.width, self.height)
            
            # Setting icon on the button.
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.help.up)))
            self.button.setIconSize(QSize(self.width, self.height))

            # Setting button style. -> Removing the background.
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

            self.layout.addWidget(self.button, alignment = Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        
        def func(self):
            pass