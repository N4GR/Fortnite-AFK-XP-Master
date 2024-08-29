from imports import *
log = SetupLogging("MAIN   ")

# Local imports
import ui.startup
import objects
from util.update import Update

if __name__ == "__main__":
    # Initialising required objects.
    window = objects.Window()

    # Setting window app ID.
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(window.app_id)

    # Check for updates.
    update = Update()

    # Initialising Main window.
    log.debug("Creating UI...")
    ui.startup.UI()