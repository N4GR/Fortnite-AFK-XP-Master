from src.window.main_window import MainWindow
from src.window.imports import QApplication

# Config imports.
from src.shared.config import WindowConfig

if __name__ == "__main__":
    window_configs = WindowConfig()
    
    application = QApplication([])
    main_window = MainWindow(window_configs)
    main_window.show()
    
    application.exec()