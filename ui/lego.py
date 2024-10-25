from ui.imports import *

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

        # Setting layout to widget.
        self.widget.setLayout(self.layout)

        # Setting size of widget and its position.
        self.widget.setGeometry(self.x, self.y,
                                self.width, self.height)
        self.widget.setStyleSheet("background-color: lightgray; border: 1px solid black;")
    
    def GetWidget(self):
        return self.widget