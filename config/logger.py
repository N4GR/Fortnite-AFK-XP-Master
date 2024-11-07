from datetime import datetime
import logging
import sys
import os

def GetArgs() -> bool:
    return "--debug" in sys.argv

class Logger:
    def __init__(self,
                 class_name: str) -> None:
        """Logger function used to initialise logging.

        Args:
            class_name (str): Name of the class / file that's currently being worked on.
        """
        now = datetime.now()
        current_datetime = now.strftime("%d-%m-%Y_%H-%M-%S")

        # Suppress debug logging from PIL
        logging.getLogger('PIL').setLevel(logging.WARNING)

        self.log = logging.getLogger(class_name)

        # If the --debug option isn't in the arguments, do not print to file.
        if GetArgs() is True:
            # Create the directory to place logs.
            os.makedirs("logs", exist_ok = True)

            handlers = [logging.FileHandler(f"logs\\{current_datetime}.log"),
                        logging.StreamHandler()]
        else:
            handlers = []

        logging.basicConfig(
            level = logging.DEBUG,
            format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers = handlers
        )
    
    def custom_excepthook(self,
                          exc_type,
                          exc_value,
                          exc_traceback):
        """Custom excepthook that captures excepts and passes it to the log."""
        if issubclass(exc_type,
                      KeyboardInterrupt):
            # Allow the program to terminate on a keyboard interrupt
            sys.__excepthook__(exc_type,
                               exc_value,
                               exc_traceback)
            return
        logging.error("Uncaught exception",
                      exc_info = (exc_type,
                                  exc_value,
                                  exc_traceback))