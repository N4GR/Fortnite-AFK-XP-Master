from datetime import datetime
import logging
import sys
import os

# Setting log level for success.
SUCCESS_NUM = 25
# Adding to logging.
logging.addLevelName(SUCCESS_NUM, "SUCCESS")

def success(self, message,
            *args, **kwargs):
    if self.isEnabledFor(SUCCESS_NUM):
        self._log(SUCCESS_NUM, message,
                  args, **kwargs)

# Adding function to logging success.
logging.Logger.success = success

class Logger:
    def __init__(self, class_name: str) -> None:
        """Logger function used to initialise logging.

        Args:
            class_name (str): Name of the class / file that's currently being worked on.
        """
        now = datetime.now()
        current_datetime = now.strftime("%d-%m-%Y_%H-%M-%S")

        # Suppress debug logging from PIL
        logging.getLogger('PIL').setLevel(logging.WARNING)

        self.log = logging.getLogger(class_name)
        self.log.setLevel(logging.DEBUG)

        # If the --debug option isn't in the arguments, do not print to file.
        if self.GetArgs() is True:
            # Create the directory to place logs.
            os.makedirs("logs", exist_ok = True)

            # Plain formatting for file.
            plain_format = "%(asctime)s %(levelname)s     %(name)s %(message)s"
            plain_formatter = logging.Formatter(plain_format, datefmt = "%Y-%m-%d %H:%M:%S")

            # File handler without colored output
            file_handler = logging.FileHandler(f"logs\\{current_datetime}.log")
            file_handler.setFormatter(plain_formatter)
            self.log.addHandler(file_handler)
            
        # Console handler with colored output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.CustomFormatter())
        self.log.addHandler(console_handler)
    
    class CustomFormatter(logging.Formatter):
        grey = "\x1b[90m"
        bright_blue = "\x1b[94m"
        bright_green = "\x1b[92m"
        bright_purple = "\x1b[95m"
        bright_yellow = "\x1b[93m"
        bright_red = "\x1b[91m"
        white = "\x1b[37m"

        end = "\x1b[0m"

        FORMATS = {
            logging.DEBUG:
            "{time} {level}    {name} {message}".format(
                time = grey + "%(asctime)s" + end,
                name = bright_blue + "%(name)s" + end,
                level = grey + "%(levelname)s" + end,
                message = white + "%(message)s" + end
            ),

            logging.INFO:
            "{time} {level}     {name} {message}".format(
                time = grey + "%(asctime)s" + end,
                name = bright_blue + "%(name)s" + end,
                level = bright_purple + "%(levelname)s" + end,
                message = white + "%(message)s" + end
            ),

            25:
            "{time} {level}  {name} {message}".format(
                time = grey + "%(asctime)s" + end,
                name = bright_blue + "%(name)s" + end,
                level = bright_green + "%(levelname)s" + end,
                message = white + "%(message)s" + end  # Bright green for SUCCESS
            ),

            logging.WARNING:
            "{time} {level}  {name} {message}".format(
                time = grey + "%(asctime)s" + end,
                name = bright_blue + "%(name)s" + end,
                level = bright_yellow + "%(levelname)s" + end,
                message = white + "%(message)s" + end
            ),

            logging.ERROR:
            "{time} {level}    {name} {message}".format(
                time = grey + "%(asctime)s" + end,
                name = bright_blue + "%(name)s" + end,
                level = bright_red + "%(levelname)s" + end,
                message = white + "%(message)s" + end
            ),

            logging.CRITICAL:
            "{time} {level} {name} {message}".format(
                time = grey + "%(asctime)s" + end,
                name = bright_blue + "%(name)s" + end,
                level = bright_red + "%(levelname)s" + end,
                message = white + "%(message)s" + end
            )
        }

        def format(self, record):
            # Retrieve the format string based on the log level
            log_fmt = self.FORMATS.get(record.levelno, self.format)
            formatter = logging.Formatter(log_fmt, datefmt = "%Y-%m-%d %H:%M:%S")
            return formatter.format(record)

    def CustomExcepthook(self, exc_type,
                         exc_value, exc_traceback):
        """Custom excepthook that captures excepts and passes it to the log."""
        if issubclass(exc_type,
                      KeyboardInterrupt):
            # Allow the program to terminate on a keyboard interrupt
            sys.__excepthook__(exc_type, exc_value,
                               exc_traceback)
            return
        logging.error("Uncaught exception",
                      exc_info = (exc_type, exc_value,
                                  exc_traceback))

    def GetArgs(self) -> bool:
        return "--debug" in sys.argv