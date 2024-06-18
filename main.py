# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from utilities.read_utilities import imieDowodOsobisty, wygenerujDane, wygenerujDaneDowodOsobisty
import numpy as np
import cv2
import pytesseract


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.ui_form import Ui_Widget

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.uploadButton.clicked.connect(self.upload_photo)
        self.ui.loadDataFromDocument.clicked.connect(self.load_data_from_image)
        self.uploaded_image = None

    def upload_photo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                  "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if fileName:
            pixmap = QPixmap(fileName)
            self.ui.photoField.setPixmap(pixmap)
            self.ui.photoField.setScaledContents(True)
            self.uploaded_image = cv2.imread(fileName)

    def load_data_from_image(self):
        if self.uploaded_image is None:
            print("No image uploaded")
            return
        
        height, width, _ = self.uploaded_image.shape
        firstName, lastName, dateOfBirth = wygenerujDane(self.uploaded_image, height, width)
        self.ui.firstName.setText(firstName)
        self.ui.lastName.setText(lastName)
        self.ui.dateOfBirth.setText(dateOfBirth)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
