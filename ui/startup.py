from imports import *
log = SetupLogging("UI     ")

# Local imports
import ui.window
import ui.buttons

class UI:
    def __init__(self) -> None:
        # Creating main application.
        self.main_application = QtWidgets.QApplication(sys.argv)
        # Creating main window which will be displayed.
        self.main_window = ui.window.FNMainWindow()

        # Getting buttons for UI.
        buttons = ui.buttons.buttons(self.main_window)

        # Shows the constructed window.
        self.main_window.show()
        # Executes the application.
        log.success("Ready.")
        self.main_application.exec()