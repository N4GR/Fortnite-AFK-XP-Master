# Imports to avoid circular importing.
from PIL.ImageQt import ImageQt, Image
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
        self.height = 0
        self.width = 0

        self.title = "Fortnite AFK XP Master"
        self.app_id = "vamptek.fortnite.afkxpmaster.v1"

        self.icon = ImageQt(Image.open(GetAsset("icon.png")))
        self.background = ImageQt(Image.open(GetAsset("background.png")))