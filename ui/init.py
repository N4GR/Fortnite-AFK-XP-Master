# Base imports
from config.imports import *

# Third party libraries
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QErrorMessage, QMessageBox, QInputDialog, QApplication, QWidget, QScrollArea, QGridLayout, QToolButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QFontDatabase, QFont, QMovie
from PyQt6.QtCore import QSize, Qt, QPoint, QThread

# Local imports
from config.obj import WINDOW, PROCESS
from ui.assets import panel, button

class MainWindow(QMainWindow):
    def __init__(self):
        """QMainWindow subclass creating the main PyQt6 window thread."""
        super(MainWindow, self).__init__()

        PANEL = panel()

        self.setFixedSize(WINDOW.WIDTH, WINDOW.HEIGHT)
        self.setWindowTitle(WINDOW.TITLE)

        self.setWindowIcon(QIcon(QPixmap.fromImage(PANEL.ICON)))

        label = QLabel(self)
        #label.setPixmap(QPixmap.fromImage(PANEL_ASSETS.background))
        self.setCentralWidget(label)

        self.setStyleSheet(r"QMainWindow {background: transparent}")
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
        )
        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    
    def mousePressEvent(self, event):
        """A function used to handle anything when the mouse is pressed.

        Args:
            event (_type_): Event that's being issued.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            if event.pos().y() < 50:
                self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """A function used to handle anything when the mouse is moved.

        Args:
            event (_type_): Event that's being issued.
        """
        try:
            if self.offset is not None:
                pass
        except AttributeError:
            self.offset = None

        if self.offset is not None and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """A function used to handle anythign when the mouse is released.

        Args:
            event (_type_): Event that's being issued.
        """
        self.offset = None
        super().mouseReleaseEvent(event)

class ui():
    def __init__(self) -> None:
        '''Main menu creation class for the main UI which can be re-created.

        Usage:
            ui(new = False): This will re-create the main UI without closing the Application.
        '''
        self.main_app = self.createApp()
        
        self.main_window = MainWindow()

        # Initialise buttons.
        self.buttons = buttons(self.main_window)

        self.main_window.show()

        self.createExit()
    
    def createApp(self) -> QApplication:
        """Function to create a QApplication.

        Returns:
            QApplication: Object made when the application is generated.
        """
        main_app = QApplication(sys.argv)

        return main_app
    
    def createExit(self):
        """A function that exits the main application."""
        sys.exit(self.main_app.exec())

class buttons():
    def __init__(self, main_window: MainWindow) -> None:
        '''Buttons class containing and initilising all buttons related to the main ui.
        
        Attributes:
            exit [QPushButton]: Exit push button of the main UI.
            minimise [QPushButton]: Minimise push button of the main UI.
        '''
        self.main_window = main_window

        self.button = button()

        self.exit = self.exitButton()
        self.minimise = self.minimiseButton()
        
    def exitButton(self) -> QPushButton:
        """Exit button that's created to handle the exitting of the program when it's clicked.

        Returns:
            QPushButton: Button created for the exit button.
        """
        def pressed():
            '''
            Changes the button icon on press.
            '''
            button.setIcon(QIcon(QPixmap.fromImage(self.button.exit.down)))

        def released():
            '''
            Changes the button icon on release.
            '''
            button.setIcon(QIcon(QPixmap.fromImage(self.button.exit.up)))
        
        def func():
            """Function called when the exit button is clicked."""
            sys.exit()

        # Creating button widget
        button = QPushButton("", self.main_window)
        button.clicked.connect(func)
        button.pressed.connect(pressed)
        button.released.connect(released)
        button.setGeometry(285, 10,
                           8, 8)

        # Setting icon
        button.setIcon(QIcon(QPixmap.fromImage(self.button.exit.up)))
        button.setIconSize(QSize(8, 8))

        # Object styling handling
        button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

        return button
    
    def minimiseButton(self) -> QPushButton:
        """Function to create and set any function for minimising.

        Returns:
            QPushButton: Object created for the button.
        """
        def pressed():
            '''
            Changes the button icon on press.
            '''
            button.setIcon(QIcon(QPixmap.fromImage(self.button.minimise.down)))

        def released():
            '''
            Changes the button icon on release.
            '''
            button.setIcon(QIcon(QPixmap.fromImage(self.button.minimise.up)))
        
        def func():
            """Functiopn called when the minimise button is pressed."""
            self.main_window.showMinimized()

        # Creating button widget
        button = QPushButton("", self.main_window)
        button.clicked.connect(func)
        button.pressed.connect(pressed)
        button.released.connect(released)
        button.setGeometry(270, 10,
                           8, 8)

        # Setting icon
        button.setIcon(QIcon(QPixmap.fromImage(self.button.minimise.up)))
        button.setIconSize(QSize(8, 8))

        # Object styling handling
        button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

        return button
