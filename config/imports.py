# Python imports.
import time
from random import (
    uniform, randint,
    choice
)
import ctypes
import sys
import threading
import os

# Third-Party imports.
import vgamepad
import screeninfo
import keyboard

# Logging setup
from config import logger
import logging

def setup(name: str) -> logging.Logger:
    logging = logger.Logger(name)
    log = logging.log

    sys.excepthook = logging.custom_excepthook

    return log