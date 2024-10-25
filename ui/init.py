# Base imports
from config.imports import *

# Third party libraries
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QErrorMessage, QMessageBox, QInputDialog, QApplication, QWidget, QScrollArea, QGridLayout, QToolButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QFontDatabase, QFont, QMovie
from PyQt6.QtCore import QSize, Qt, QPoint, QThread

# Local imports
from config.obj import WINDOW, PROCESS
from ui.assets import panel

class MainWindow(QMainWindow):
    def __init__(self):
        """QMainWindow subclass creating the main PyQt6 window thread."""
        super(MainWindow, self).__init__()

        PANEL = panel()

        self.setFixedSize(WINDOW.WIDTH, WINDOW.HEIGHT)
        self.setWindowTitle("Fortnite AFK Master")

        self.setWindowIcon(QIcon(QPixmap.fromImage(PANEL.ICON)))

        label = QLabel(self)
        #label.setPixmap(QPixmap.fromImage(PANEL_ASSETS.background))
        self.setCentralWidget(label)

        self.setStyleSheet(r"QMainWindow {background: transparent}")
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
        )
        
        #self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    
    def mousePressEvent(self, event):
        """A function used to handle anything when the mouse is pressed.

        Args:
            event (_type_): Event that's being issued.
        """
        if event.button() == Qt.MouseButton.LeftButton:
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

if __name__ == "__main__":
    ui()