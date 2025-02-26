from src.window.imports import *

# Creating global placeholders.
main_window: QWidget = None

class TopBar(QWidget):
    def __init__(
            self,
            main_window: QWidget
    ) -> None:
        super().__init__()
        self.main_window = main_window
        
        self._add_design()
    
        self.background_widget = Background(
            parent = self,
            main_window = self.main_window
        )
        
        self.button_widget = Buttons(
            parent = self,
            main_window = self.main_window,
            width = 96,
            height = self.height()
        )
        self.button_widget.raise_() # Ensures button is always at the top.
    
    def _add_design(self):
        self.setFixedHeight(50)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    
    def resizeEvent(
            self,
            event: QEvent
    ) -> None:
        """Resizes widgets within the topbar to scale automatically with the main window.

        Args:
            event (_type_): _description_
        """
        self.background_widget.resize_to_main_window()
        self.button_widget.anchor_to_right()
        
        super().resizeEvent(event)
        
class Buttons(QWidget):
    def __init__(
            self,
            parent: QWidget,
            main_window: QWidget,
            width: int,
            height: int
    ) -> None:
        """Buttons object that will hold the buttons and functions of the TopBar.

        Args:
            parent (QWidget): Parent to the buttons.
            main_window: QWidget
            width (int): Width of the buttons layout.
            height (int): Height of the buttons layout.
        """
        super().__init__(parent)
        self.main_window = main_window
        
        self._add_design(width, height)
        
        self.minimise_button = self.MinimiseButton(self.main_window)
        self.close_button = self.CloseButton(self.main_window)
        
        self.main_layout = self._create_layout(widgets = [self.minimise_button, self.close_button])
        self.setLayout(self.main_layout)
    
    def _add_design(
            self,
            width: int,
            height: int
    ) -> None:
        """A function to set the design to a QWidget, sizing and colour ect.

        Args:
            width (int): Width of the buttons widget in pixels.
            height (int): Height of the buttons widget in pixels.
        """
        self.setFixedSize(width, height)
        
        self.anchor_to_right()
    
    def _create_layout(
            self,
            widgets: list[QWidget]
    ) -> QHBoxLayout:
        """A function to create and add widgets to a layout.

        Args:
            widgets (list[QWidget]): Widgets to add to the layout.

        Returns:
            QHBoxLayout: Layout created from the function.
        """
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addSpacing(0)
        
        for widget in widgets:
            layout.addWidget(widget)
        
        return layout

    def anchor_to_right(self):
        """A function to anchor the buttons widget to the right of the main window."""
        main_window_geometry = self.main_window.geometry()
        
        # Calculating the X position to move the widget to the right.
        x_position = (main_window_geometry.width() - self.width()) - 10 # Offset by 10 pixels
        
        # Move the widget to the calculated position (the right.)
        self.move(x_position, 0)

    class CloseButton(QPushButton):
        def __init__(
                self,
                main_window: QWidget
        ) -> None:
            """CloseButton (QPushButton) object that will handle the closing of the main window through a button.

            Args:
                main_window (QWidget): The MainWindow QWidget.
            """
            super().__init__()
            self.main_window = main_window
            
            self._add_design()
            self._add_connections()
        
        def _add_design(self):
            """Function to add design to the button, colouring and sizing, ect."""
            self.setFixedSize(40, 40)
            
            self.setText("X")
        
        def _add_connections(self):
            """A function that will initialise all connections to the button with functions."""
            self.clicked.connect(self._on_click) # Send close event on button click.
        
        def _on_click(self):
            """A function connected to the click function that will call a close event to the main window."""
            print("Exit clicked!")
            
            self.main_window.close() # Closes the MainWindow.
    
    class MinimiseButton(QPushButton):
        def __init__(
                self,
                main_window: QWidget
        ) -> None:
            """MinimiseButton (QPushButton) object that will handle the minimising of the main window through a button.

            Args:
                main_window (QWidget): The MainWindow QWidget.
            """
            super().__init__()
            self.main_window = main_window
            
            self._add_design()
            self._add_connections()
            
        def _add_design(self):
            """Function to add design to the button, colouring and sizing, ect."""
            self.setFixedSize(40, 40)
            self.setText("-")
        
        def _add_connections(self):
            """A function that will initialise all connections to the button with functions."""
            self.clicked.connect(self._on_click) # Minimise on click.
        
        def _on_click(self):
            """A function connected to the clicked function that will minimise the main window."""
            print("Minimise clicked!")
            
            self.main_window.showMinimized() # Minimises the MainWindow

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
                    background-color: red;
                    border-top-left-radius: 20px;
                    border-top-right-radius: 20px;    
                }
            """) # Set the colour and add a rounded edge to the top-left and top-right.
            
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