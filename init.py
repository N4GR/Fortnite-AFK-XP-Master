from src.window.main_window import MainWindow
from src.window.imports import QApplication

if __name__ == "__main__":
    application = QApplication([])
    main_window = MainWindow()
    main_window.show()
    
    application.exec()