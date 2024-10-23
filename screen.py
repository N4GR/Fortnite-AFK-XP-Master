from imports import *

class Screen:
    def __init__(self):
        self.monitors = screeninfo.get_monitors()
    
    def GetPrimary(self) -> screeninfo.Monitor:
        for monitor in self.monitors:
            if monitor.is_primary is True:
                return monitor