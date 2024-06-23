from PySide6.QtWidgets import QMessageBox


def show_message_box_on_success(message: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setWindowTitle("Sukces")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
    
def show_message_box_on_error(message: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle("Błąd")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
    
def show_message_box_on_warning(message: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle("Ostrzeżenie")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

