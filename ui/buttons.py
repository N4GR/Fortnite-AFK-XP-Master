from PyQt6.QtCore import QObject
from imports import *
log = SetupLogging("BUTTONS")

import objects

class buttons:
    def __init__(self, main_window: QtWidgets.QMainWindow) -> None:
        self.main_window = main_window

        # Initialising buttons.
        self.main = self.Main()
        self.main_clicked = False

        #self.fade_button = self.FadeButton(objects.GetAsset("main_default.png"), objects.GetAsset("main_hover.png"))
        #self.fade_button.setGeometry(600, 30, 364, 100)
    
    def LogDebug(self, name: str) -> None:
        log.debug(f"Creating {name} button...")

    def Main(self) -> QtWidgets.QPushButton:
        class HoverFilter(QtCore.QObject):
            def __init__(self, button: QtWidgets.QPushButton):
                super().__init__(button)
                self.button = button
                self.normal_icon = button.icon()

                self.hover_icon = QtGui.QIcon(objects.GetAsset("main_hover.png"))

                self.button.setIcon(self.normal_icon)

            def eventFilter(self,
                            obj: QtCore.QObject,
                            event: QtCore.QEvent):
                if obj == self.button:
                    if event.type() == QtCore.QEvent.Type.Enter:
                        self.button.setIcon(self.hover_icon)

                    elif event.type() == QtCore.QEvent.Type.Leave:
                        self.button.setIcon(self.normal_icon)

                return super().eventFilter(obj, event)
    
        def func():
            """Functiopn called when the Main button is pressed."""
            print("Clicked")

            # Removes the hover-event filter.
            button.removeEventFilter(hover_filter)

            if self.main_clicked is False:
                # Sets the clicked button icon.
                button.setIcon(QtGui.QIcon(objects.GetAsset("main_clicked.png")))

                self.main_clicked = True
            else:
                # Setting icon back to default
                button.setIcon(QtGui.QIcon(objects.GetAsset("main_default.png")))

                # Adds the event filter back.
                button.installEventFilter(hover_filter)

                self.main_clicked = False

            
        self.LogDebug("main")

        # Creating button widget
        button = QtWidgets.QPushButton("", self.main_window)
        
        # Setting button functions
        button.clicked.connect(func)

        button_width = 260
        button_height = 65
        x = 1580
        y = 59
        
        # Setting button icon and size
        button.setIcon(QtGui.QIcon(objects.GetAsset("main_default.png")))
        button.setGeometry(x, y, button_width, button_height)
        button.setIconSize(QtCore.QSize(button_width, button_height))

        # Setting CSS Style
        button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

        # Make the button interactable.
        button.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        # Installing hover event.
        hover_filter = HoverFilter(button)
        button.installEventFilter(hover_filter)

        button.show()

        return button