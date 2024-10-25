# Base imports
from config.imports import *

from ui.imports import *

# Local imports
from config.obj import WINDOW, PROCESS
from ui.assets import panel, button

# Adding window modules
from ui import lego
from ui import jam

class MainWindow(QMainWindow):
    def __init__(self, moveable_y: int):
        """QMainWindow subclass creating the main PyQt6 window thread."""
        super(MainWindow, self).__init__()

        self.moveable_y = moveable_y

        PANEL = panel()

        self.setFixedSize(WINDOW.WIDTH, WINDOW.HEIGHT)
        self.setWindowTitle(WINDOW.TITLE)

        self.setWindowIcon(QIcon(QPixmap.fromImage(PANEL.ICON)))

        label = QLabel(self)
        label.setPixmap(QPixmap.fromImage(PANEL.BACKGROUND))
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
            if event.pos().y() < self.moveable_y:
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
        
        self.main_window = MainWindow(moveable_y = 20)

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

        self.exit = self.exitButton(self.main_window, self.button)
        self.minimise = self.minimiseButton(self.main_window, self.button)
        self.lego = self.legoButton(self.main_window, self.button)
        self.jam = self.jamButton(self.main_window, self.button)

    class exitButton:
        def __init__(self,
                    main_window: QMainWindow,
                    button: button):
            """Exit button that's created to handle the exitting of the program when it's clicked.

            Returns:
                QPushButton: Button created for the exit button.
            """
            self.main_window = main_window
            self.new_window = None
            self.button_assets = button

            # Dimensions
            self.width, self.height = (8, 8)
            self.x, self.y = (275, 15)

            # Creating button widget
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(self.func)
            self.button.pressed.connect(self.pressed)
            self.button.released.connect(self.released)

            self.button.setGeometry(self.x, self.y,
                            self.width, self.height)

            # Setting icon
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.exit.up)))
            self.button.setIconSize(QSize(self.width, self.height))

            # Object styling handling
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")
        
        def pressed(self):
            '''
            Changes the button icon on press.
            '''
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.exit.down)))

        def released(self):
            '''
            Changes the button icon on release.
            '''
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.exit.up)))
        
        def func(self):
            """Function called when the exit button is clicked."""
            sys.exit()

    class minimiseButton:
        def __init__(self,
                    main_window: QMainWindow,
                    button: button):
            """Function to create and set the function for lego.

            Returns:
                QPushButton: Object created for the button.
            """
            self.main_window = main_window
            self.new_window = None
            self.button_assets = button

            # Dimensions
            self.width, self.height = (8, 8)
            self.x, self.y = (260, 15)

            # Creating button widget
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(self.func)
            self.button.pressed.connect(self.pressed)
            self.button.released.connect(self.released)

            self.button.setGeometry(self.x, self.y,
                            self.width, self.height)

            # Setting icon
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.minimise.up)))
            self.button.setIconSize(QSize(self.width, self.height))

            # Object styling handling
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

        def pressed(self):
            '''
            Changes the button icon on press.
            '''
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.minimise.down)))

        def released(self):
            '''
            Changes the button icon on release.
            '''
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.minimise.up)))
        
        def func(self):
            """Functiopn called when the minimise button is pressed."""
            self.main_window.showMinimized()

    class legoButton:
        def __init__(self,
                    main_window: QMainWindow,
                    button: button):
            """Function to create and set the function for lego.

            Returns:
                QPushButton: Object created for the button.
            """
            self.main_window = main_window
            self.new_window = None
            self.button_assets = button

            # Dimensions
            width, height = (81, 32)
            x, y = (10, 30)

            # Creating button widget
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(self.func)
            self.button.pressed.connect(self.pressed)
            #button.released.connect(released)

            self.is_pressed = False

            self.button.setGeometry(x, y,
                            width, height)

            # Setting icon
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.lego.up)))
            self.button.setIconSize(QSize(width, height))

            # Object styling handling
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

        def pressed(self):
            '''
            Changes the button icon on press.
            '''
            if self.is_pressed is False:
                self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.lego.down)))
            else:
                self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.lego.up)))
        
        def func(self):
            if self.is_pressed is False:
                widget = lego.Lego(self.main_window)
                self.new_window = widget.GetWidget()
                self.new_window.show()

                self.is_pressed = True
            else:
                self.new_window.deleteLater()

                self.is_pressed = False

    class jamButton:
        def __init__(self,
                     main_window: QMainWindow,
                     button: button):
            self.main_window = main_window
            self.new_window = None
            self.button_assets = button

            # Dimensions
            width, height = (81, 32)
            x, y = (100, 30)

            # Creating button widget
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(self.func)
            self.button.pressed.connect(self.pressed)
            #button.released.connect(released)

            self.is_pressed = False

            self.button.setGeometry(x, y,
                            width, height)

            # Setting icon
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.jam.up)))
            self.button.setIconSize(QSize(width, height))

            # Object styling handling
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

        def pressed(self):
            '''
            Changes the button icon on press.
            '''
            if self.is_pressed is False:
                self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.jam.down)))
            else:
                self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.jam.up)))
        
        def func(self):
            if self.is_pressed is False:
                widget = jam.Jam(self.main_window)
                self.new_window = widget.GetWidget()
                self.new_window.show()

                self.is_pressed = True
            else:
                self.new_window.deleteLater()

                self.is_pressed = False