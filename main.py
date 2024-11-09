from config.imports import *
log = setup("MAIN")

# Local imports.
from config.obj import PROCESS
import ui.init

if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(PROCESS.ID)

    log.info("Launching...")

    ui.init.ui()