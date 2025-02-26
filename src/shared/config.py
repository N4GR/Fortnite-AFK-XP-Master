from src.shared.imports import *

# Windowing imports.
from src.window.imports import QColor

def get_yaml_data(yaml_directory: str) -> dict:
    """A function to extract the data pertaining to a YAML directory.

    Args:
        yaml_directory (str): Directory path string to the YAML file.

    Returns:
        dict: Dictionary of data extracted from the YAML file.
    """
    with open(yaml_directory, "r", encoding = "utf-8") as file:
        return yaml.safe_load(file)

class WindowConfig:
    def __init__(self):
        config_directory = "data/window/config.yaml"
        yaml_data = get_yaml_data(config_directory)
        
        self.main_window = self.MainWindow(yaml_data["MainWindow"])
        self.top_bar = self.TopBar(yaml_data["TopBar"])
    
    class MainWindow:
        def __init__(
                self,
                main_window_data: dict
        ) -> None:
            self.main_window_data = main_window_data
            
            self.background = self.Background(self.main_window_data["Background"])
            
        class Background:
            def __init__(
                    self,
                    gradient_data: dict
            ) -> None:
                self.gradient_data = gradient_data
                
                self.inner_colour = self._get_qcolor(self.gradient_data["InnerColour"])
                self.outer_colour = self._get_qcolor(self.gradient_data["OuterColour"])
            
            def _get_qcolor(
                    self,
                    colour_list: list[str]
            ) -> QColor:
                colour = QColor(
                    colour_list[0],
                    colour_list[1],
                    colour_list[2]
                )
                
                return colour
    
    class TopBar:
        def __init__(
                self,
                top_bar_data: dict
        ) -> None:
            self.top_bar_data = top_bar_data
            
            self.background = self.Background(self.top_bar_data["Background"])
        
        class Background:
            def __init__(
                    self,
                    background_data: dict
            ) -> None:
                self.background_data = background_data
                
                self.colour = self.background_data["Colour"]
        
