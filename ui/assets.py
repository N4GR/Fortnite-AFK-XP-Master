from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance, ImageChops
from PIL.ImageQt import ImageQt

class panel(object):
    def __init__(self) -> None:
        """Panel object to open panel images."""
        self.ICON = self.openImage("icon")
    
    def openImage(self,
                  name: str) -> ImageQt:
        """openImage function for Panels, which opens images with a given name.

        Args:
            name (str): Name of the panel image to open.

        Returns:
            Image.Image: ImageQt object for PyQt6. 
        """
        return ImageQt(Image.open(f"assets/{name}.png"))