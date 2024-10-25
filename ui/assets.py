from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance, ImageChops
from PIL.ImageQt import ImageQt

class button(object):
    def __init__(self) -> None:
        """Button object containing ToggleButtons."""
        self.exit = self.ToggleButton("exit")
        self.minimise = self.ToggleButton("minimise")
        self.lego = self.ToggleButton("lego")
        self.jam = self.ToggleButton("jam")

    class ToggleButton(object):
        def __init__(self,
                     name: str) -> None:
            """Togglebutton.

            Args:
                name (str): Name of the button.
            """
            self.up = self.openImage(name, "up")
            self.down = self.openImage(name, "down")
        
        def openImage(self,
                      name: str,
                      type: str) -> ImageQt:
            """openImage function to create an ImageQt object for the button.

            Args:
                name (str): Name of the button to open.
                type (str): Type of button to open. up | down

            Returns:
                ImageQt: ImageQt object for PyQt6
            """
            return ImageQt(Image.open(f"assets/{name}_{type}.png"))

class panel(object):
    def __init__(self) -> None:
        """Panel object to open panel images."""
        self.ICON = self.openImage("icon")
        self.BACKGROUND = self.openImage("background")
    
    def openImage(self,
                  name: str) -> ImageQt:
        """openImage function for Panels, which opens images with a given name.

        Args:
            name (str): Name of the panel image to open.

        Returns:
            Image.Image: ImageQt object for PyQt6. 
        """
        return ImageQt(Image.open(f"assets/{name}.png"))