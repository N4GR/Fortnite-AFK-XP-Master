from imports import *
log = SetupLogging("BUTTONS")

class buttons:
    def __init__(self, main_window: QtWidgets.QMainWindow) -> None:
        self.main_window = main_window

        # Initialising buttons.
        self.exit = self.Exit()
        self.minimise = self.Minimise()
    
    def LogDebug(self, name: str) -> None:
        log.debug(f"Creating {name} button...")

    def Exit(self):
        self.LogDebug("exit")

    def Minimise(self):
        self.LogDebug("minimise")