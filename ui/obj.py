from config.imports import *
from ui.imports import *
log = setup("UI.OBJ")

class InfoDialog(QDialog):
    def __init__(self, message: str, parent = None):
        super().__init__(parent)
        log.info("Launching information diolog.")
        self.setWindowTitle("Information")
        layout = QVBoxLayout(self)

        message_label = QLabel(message, self)
        layout.addWidget(message_label)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok, self)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)