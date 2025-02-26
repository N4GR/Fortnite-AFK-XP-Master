from src.window.imports import *

# Local imports.
from src.window.top_bar import TopBar

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._add_design()
        self.oldPos = None
        
        # Adding background to MainWindow.
        self.background = Background(
            parent = self,
            main_window = self
        )

        # Adding modules to the MainWindow.
        self.topbar = TopBar(self)
        
        # Handing the layout of the MainWindow..
        self.layout_widgets = self._create_layout_widgets()
        self.main_layout = self._create_layout(widgets = self.layout_widgets)
        self.setLayout(self.main_layout)
        
        # Adding size grips to the window.
        self.size_grips = self._create_size_grips()
    
    def _add_design(self):
        """A function to add design to the QWidget, sizing and colour ect."""
        self.setGeometry(
            0, # X
            0, # Y
            800, # Width
            600 # Height
        )
        
        self.setMinimumSize(200, 150) # Minimum size the window can go to.
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    
    def _create_layout_widgets(self) -> list[dict[QWidget, Qt.AlignmentFlag]]:
        """A function containing a manually created list of dictionaries, each having their own widget and alignment flag set to parse to the layout.

        Returns:
            list[dict[QWidget, Qt.AlignmentFlag]]: A list of dictionaries containing "widget", "alignment_flag" to add to the layout.
        """
        layout_widgets = [
            {
                "widget": self.topbar,
                "alignment_flag": Qt.AlignmentFlag.AlignTop
            }
        ]
        
        return layout_widgets
    
    def _create_layout(
            self,
            widgets: list[dict[QWidget, Qt.AlignmentFlag]]
    ) -> QVBoxLayout:
        """A function to create a layout and add widgets to it for the MainWindow object.

        Args:
            widgets (list[dict[QWidget, Qt.AlignmentFlag]]): A list of objects to add to the layout.

        Returns:
            QVBoxLayout: Layout generated from the function.
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        for widget in widgets:
            layout.addWidget(
                widget["widget"],
                alignment = widget["alignment_flag"]
            )
        
        return layout
    
    def _create_size_grips(self) -> list[QSizeGrip]:
        """A function to create size grips that will be used to change the size of the window.

        Returns:
            list[QSizeGrip]: A list of QSizeGrip objects added to the QMainWindow.
        """
        size_grips = []
        
        for i in range(4):
            size_grip = QSizeGrip(self)
            size_grip.setFixedSize(10, 10) # Setting the size of each grip to 10x10 pixels.
            size_grip.setStyleSheet("background-color: transparent") # Making them transparent.
            
            size_grips.append(size_grip)
        
        return size_grips
    
    def mousePressEvent(
            self,
            event: QEvent
    ) -> None:
        """QWidget mousePressEvent connection that will call the function when the mouse is pressed.

        Args:
            event (QEvent): Event returned on the action.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(
            self,
            event: QEvent
    ) -> None:
        """QWidget mouseMoveEvent connection that will call the function when the mouse moves.

        Args:
            event (QEvent): Event returned on the action.
        """
        if self.oldPos:
            delta = event.globalPos() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(
            self,
            event: QEvent
    ) -> None:
        """QWidget mouseReleaseEvent connection that will call the function when the mouse is released.

        Args:
            event (QEvent): Event returned on the action.
        """
        self.oldPos = None
    
    def resizeEvent(
            self,
            event: QEvent
    ) -> None:
        """QWidget resizeEvent connection that will call the function when the window is being resized.

        Args:
            event (QEvent): Event returned on the action.
        """
        super().resizeEvent(event)
        rect = self.rect()
        
        # Top left.
        self.size_grips[0].move(0, 0)
        
        # Top right.
        self.size_grips[1].move(
            rect.right() - self.size_grips[1].width(),
            0
        )
        
        # Bottom right?
        self.size_grips[2].move(
            0,
            rect.bottom() - self.size_grips[2].height()
        )
        
        # Bottom left?
        self.size_grips[3].move(
            rect.right() - self.size_grips[3].width(),
            rect.bottom() - self.size_grips[3].height()
        )
        
        # Make the background move with the window resizing.
        self.background.resize_to_main_window()
    
    def closeEvent(
            self,
            event: QEvent
    ) -> None:
        """A function to handle the closing of the program.

        Args:
            event (QEvent): Event called on the action.
        """
        confirmation_message = QMessageBox.question(
            self, # Parent
            "Exit Confirmation", # Title
            "Are you sure you want to close the program?", # Text
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No # Buttons
        )
        
        if confirmation_message == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

class Background(QWidget):
        def __init__(
                self,
                parent: QWidget,
                main_window: QWidget
        ) -> None:
            """Background QWidget that will fill the background of the TopBar with a solid colour."""
            super().__init__(parent)
            self.main_window = main_window
            
            self._add_design()
            
            self.background_label = self._create_background_label()
            self.main_layout = self._create_layout(widgets = [self.background_label])
            
            self.setLayout(self.main_layout)
        
        def _add_design(self) -> None:
            """Function to add design to the widget - like sizing, colour ect."""
            self.move(0, 0) # Move to 0Y 0X coordinate.
            self.resize_to_main_window() # Resize to fit main window width.
        
        def _create_background_label(self) -> QLabel:
            """A function to create the background label.

            Returns:
                QLabel: Label created from the function.
            """
            label = QLabel()
            label.setStyleSheet("""
                QLabel {
                    background-color: black;
                    border-radius: 20px   
                }
            """) # Setting the colour with a curved border.
            
            return label

        def _create_layout(
                self,
                widgets: list[QWidget]
        ) -> QHBoxLayout:
            """A function that will create a layout and add widgets to it.

            Args:
                widgets (list[QWidget]): List of widgets to add to the layout.

            Returns:
                QHBoxLayout: Layout created containing the widgets added.
            """
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addSpacing(0)
            
            for widget in widgets:
                layout.addWidget(widget)
            
            return layout
        
        def resize_to_main_window(self):
            self.setGeometry(0, 0, self.main_window.width(), self.main_window.height())