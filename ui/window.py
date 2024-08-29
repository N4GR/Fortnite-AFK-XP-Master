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

        # Setting window size and title.
        self.setFixedSize(window.width,
                          window.height)
        self.setWindowTitle(window.title)

        # Assigning window Icon.
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(window.icon)))

        # Creating the background for the Window.
        label = QtWidgets.QLabel(self)
        label.setPixmap(QtGui.QPixmap.fromImage(window.background))
        self.setCentralWidget(label)

        # Making the window transparent and frameless to view just the background.
        self.setStyleSheet(r"QMainWindow {background: transparent}")
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    
    def mousePressEvent(self, event):
        """A function used to handle anything when the mouse is pressed.

        Args:
            event (_type_): Event that's being issued.
        """
        if event.button() ==  QtCore.Qt.MouseButton.LeftButton:
            if event.pos().y() < 100:
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

        if (self.offset is not None and
            event.buttons() ==  QtCore.Qt.MouseButton.LeftButton):
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