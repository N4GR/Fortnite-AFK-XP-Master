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
        
        # Creates the main window, adding 20 as the movable area from top.
        self.main_window = MainWindow(moveable_y = 20)

        # Initialise buttons.
        self.buttons = buttons(main_window = self.main_window)

        # Shows the main window.
        self.main_window.show()

        # Creates the exit function.
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

# Variable for assigning the current open window to.
open_window : QWidget = None
class buttons():
    def __init__(self,
                 main_window: MainWindow) -> None:
        '''Buttons class containing and initilising all buttons related to the main ui.
        
        Attributes:
            exit [QPushButton]: Exit push button of the main UI.
            minimise [QPushButton]: Minimise push button of the main UI.
        '''
        # Assigning default arguments to variables.
        self.main_window = main_window

        # Initialising layouts.
        self.titlebarlayout = self.ButtonLayout(self.main_window, position = (240, 0), size = (50, 40))
        self.modulelayout = self.ButtonLayout(self.main_window, position = (0, 0), size = (200, 100))

        # Assigning button assets.
        self.button_assets = button()

        # Adding the buttons.
        self.minimise = self.minimiseButton(self.main_window,
                                            self.button_assets,
                                            self.titlebarlayout)
        
        self.exit = self.exitButton(self.main_window,
                                    self.button_assets,
                                    self.titlebarlayout)

        self.lego = self.legoButton(self.main_window,
                                    self.button_assets,
                                    self.modulelayout)
        
        self.jam = self.jamButton(self.main_window,
                                  self.button_assets,
                                  self.modulelayout)
    
    class ButtonLayout:
        def __init__(self, main_window: QMainWindow, position: tuple[int], size: tuple[int]):
            self.main_window = main_window
            self.x, self.y = position
            self.width, self.height = size
            
            self.layout = QHBoxLayout()
            self.widget = QWidget(parent = self.main_window)

            self.widget.setGeometry(self.x, self.y, self.width, self.height)

            self.widget.setLayout(self.layout)

    class exitButton:
        def __init__(self,
                    main_window: QMainWindow,
                    button_assets: button,
                    layout: QHBoxLayout):
            """Exit button that's created to handle the exitting of the program when it's clicked.

            Returns:
                QPushButton: Button created for the exit button.
            """
            self.main_window = main_window
            self.new_window = None
            self.button_assets = button_assets
            self.layout = layout.layout

            # Dimensions
            self.width, self.height = (10, 10)
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

            # Adding the widget to the layout.
            self.layout.addWidget(self.button)
        
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
                    button_assets: button,
                    layout: QHBoxLayout):
            """Function to create and set the function for lego.

            Returns:
                QPushButton: Object created for the button.
            """
            self.main_window = main_window
            self.new_window = None
            self.button_assets = button_assets
            self.layout = layout.layout

            # Dimensions
            self.width, self.height = (10, 10)
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

            # Adding the widget to the layout.
            self.layout.addWidget(self.button)

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
                    button_assets: button,
                    layout: QHBoxLayout):
            """Function to create and set the function for lego.

            Returns:
                QPushButton: Object created for the button.
            """
            self.main_window = main_window
            self.new_window = None
            self.button_assets = button_assets
            self.layout = layout.layout

            # Assigns variable to see if window is open.
            self.is_open = False

            # Dimensions
            width, height = (81, 32)
            x, y = (10, 30)

            # Creating button widget
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(self.func)
            self.button.pressed.connect(self.pressed)
            self.button.released.connect(self.released)

            self.button.setGeometry(x, y,
                            width, height)

            # Setting icon
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.lego.up)))
            self.button.setIconSize(QSize(width, height))

            # Object styling handling
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

            # Adding the widget to the layout.
            self.layout.addWidget(self.button)

        def pressed(self):
            '''
            Changes the button icon on press.
            '''
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.lego.down)))
        
        def released(self):
            '''
            Changes the button icon on release.
            '''
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.lego.up)))
        
        def func(self):
            global open_window

            # Checks if there's an object in open_window, if there is then that means the other module is open; let's close it.
            if open_window:
                open_window.deleteLater()
                open_window = None

            self.new_window = lego.Lego(self.main_window)
            self.new_window = self.new_window.GetWidget()
            self.new_window.show()

            # Assigning open_window to global variable
            open_window = self.new_window

    class jamButton:
        def __init__(self,
                     main_window: QMainWindow,
                     button_assets: button,
                     layout: QHBoxLayout):
            self.main_window = main_window
            self.new_window = None
            self.button_assets = button_assets
            self.layout = layout.layout
            
            # Assigns variable to see if window is open.
            self.is_open = False

            # Dimensions
            width, height = (81, 32)
            x, y = (100, 30)

            # Creating button widget
            self.button = QPushButton("", self.main_window)
            self.button.clicked.connect(self.func)
            self.button.pressed.connect(self.pressed)
            self.button.released.connect(self.released)

            self.button.setGeometry(x, y,
                            width, height)

            # Setting icon
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.jam.up)))
            self.button.setIconSize(QSize(width, height))

            # Object styling handling
            self.button.setStyleSheet("QPushButton {background-color: transparent; border: 0px}")

            # Adding the widget to the layout.
            self.layout.addWidget(self.button)

        def pressed(self):
            '''
            Changes the button icon on press.
            '''
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.jam.down)))
        
        def released(self):
            '''
            Changes the button icon on release.
            '''
            self.button.setIcon(QIcon(QPixmap.fromImage(self.button_assets.jam.up)))
        
        def func(self):
            global open_window

            # Checks if there's an object in open_window, if there is then that means the other module is open; let's close it.
            if open_window:
                open_window.deleteLater()
                open_window = None

            self.new_window = jam.Jam(self.main_window)
            self.new_window = self.new_window.GetWidget()
            self.new_window.show()
            self.is_open = True

            # Assigning open_window to global variable
            open_window = self.new_window