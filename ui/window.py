from imports import *
log = SetupLogging("WINDOW ")

# Local imports
import objects

# Initialising Main PyQt6 class
class FNMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """QMainWindow subclass creating the main PyQt6 window thread."""
        super(FNMainWindow, self).__init__()
        log.debug("Getting FNMainWindow object...")

        # Initialising required objects.
        window = objects.Window()

        # Get the primary screen
        primary_screen = QtWidgets.QApplication.primaryScreen()

        # Get the geometry of the primary screen
        screen_geometry = primary_screen.geometry()

        # Get the device pixel ratio (scaling factor)
        device_pixel_ratio = primary_screen.devicePixelRatio()
        
        # Calculate the physical width and height
        screen_width = int(screen_geometry.width() * device_pixel_ratio)
        screen_height = int(screen_geometry.height() * device_pixel_ratio)

        # Setting window size and title.
        self.setFixedSize(screen_width, screen_height)
        self.setWindowTitle(window.title)

        # Assigning window Icon.
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(window.icon)))

        # Creating the background for the Window.
        label = QtWidgets.QLabel(self)
        label.setPixmap(QtGui.QPixmap.fromImage(window.background))
        self.setCentralWidget(label)

        # Making the window transparent and frameless to view just the background.
        self.setStyleSheet(r"QMainWindow {background: transparent}")

        # Set the window to stay on top, be frameless, and transparent to input.
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowTransparentForInput)

        # Set the background to be transparent.
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)