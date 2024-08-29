# Third-party imports
from PyQt6 import QtWidgets, QtGui, QtCore

# Python libraries
import ctypes
import sys
import logging

# Local imports
from util import logger

def SetupLogging(name: str) -> logging.Logger:
    """A function to initialise the logging of each file.

    Args:
        name (str): Name of the file being worked on.

    Returns:
        logging.Logger: Logger to use for logging.
    """
    logging = logger.Logger(name)
    log = logging.log

    sys.excepthook = logging.CustomExcepthook

    return log