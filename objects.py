# Imports to avoid circular importing.
from PIL.ImageQt import ImageQt, Image
from screeninfo import get_monitors, Monitor

import sys
import os

def GetAsset(name: str) -> str | bool:
    """A function to get a CleanPath asset from the asset directory.

    Args:
        name (str): Name of the asset to get.

    Returns:
        str: Path of the asset.
    """
    # Getting the directories.
    directory = Directory()

    # Getting a list of files in the assets directory.
    assets = os.listdir(directory.assets)

    # If the name given is in the assets directory, return the directory.
    if name in assets:
        return (directory.assets
                + f"\\{name}")
    else:
        # If it can't be found, return false.
        return False

def CleanPath(relative_path: str) -> str:
        """A function to give a relative path and a path compatible with PyInstaller be outputted.

        Args:
            relative_path (str): Relative path to be used.

        Returns:
            str: Path to be used in the code.
        """
        # If not running from PyInstaller, use original path.
        try:
            # Checking if PyInstall temp folder exists.
            base_path = sys._MEIPASS
        except AttributeError:
            # Use the original path.
            base_path = os.path.abspath(".")
        
        return os.path.join(base_path, relative_path)

class Directory:
    def __init__(self) -> None:
        """Directory object for relevant locations."""
        self.base = CleanPath("")
        self.assets = self.base + "assets"

class Window:
    def __init__(self) -> None:
        """Window object to contain data regarding the PyQt6 window."""
        self.title = "Fortnite AFK XP Master"
        self.app_id = "vamptek.fortnite.afkxpmaster.v1"

        self.icon = ImageQt(Image.open(GetAsset("icon.png")))
        self.background = ImageQt(Image.open(GetAsset("background.png")))

class Screen:
    def __init__(self) -> None:
        """Screen object with information regarding the displays of the user."""
        self.list = get_monitors()

        self.primary = self.GetPrimary()

    def GetPrimary(self) -> Monitor:
        """Function to return the main monitor object.

        Returns:
            Monitor: Monitor object from screeninfo.
        """
        for monitor in self.list:
            if monitor.is_primary is True:
                return monitor

    def ScaleSize(self, height: int, width: int) -> tuple[int]:
        """A function to correctly scale down or up a height and width from a 4K display.

        Args:
            height (int): Height of the object you want to scale.
            width (int): With of the object you want to scale.

        Returns:
            tuple[int]: A tuple of the newly made height and width. Example: (height, width)
        """
        height_scale_factor = self.primary.height / 2160
        width_scale_factor = self.primary.width / 3840

        new_height = int(height * height_scale_factor)
        new_width = int(width * width_scale_factor)

        return (new_height, new_width)