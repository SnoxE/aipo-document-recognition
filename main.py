# This Python file uses the following encoding: utf-8
import sys
import pytesseract
import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton
from PySide6.QtGui import QPixmap
from dotenv import load_dotenv


from utilities.TableManager import TableManager
from utilities.date_utilities import format_date
from utilities.read_utilities import generateData
from utilities.DatabaseManager import DatabaseManager
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.ui_form import Ui_Widget


load_dotenv(verbose=True, override=True)
pytesseract.pytesseract.tesseract_cmd = os.getenv("PYTESSERACT_PATH")


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.uploadButton.clicked.connect(self.upload_photo)
        self.ui.loadDataFromDocument.clicked.connect(self.load_data_from_image)
        self.ui.addOrUpdatePersonData.clicked.connect(self.add_person_to_database)
        self.uploaded_image = None
        self.document_type = None
        self.db_manager = DatabaseManager(
            os.getenv("DB_USERNAME"),
            os.getenv("DB_HOSTNAME"),
            os.getenv("DB_USERNAME"),
            os.getenv("DB_PASSWORD")
        )
        self.db_manager.openConnection()
        self.usersTable = TableManager("person", self.ui.usersTable, self.db_manager)

    def closeEvent(self, event):
        self.usersTable.destroy()
        self.db_manager.closeConnection()
        event.accept()

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
        firstName, lastName, dateOfBirth, document_type = generateData(self.uploaded_image, height, width)
        self.ui.firstName.setText(firstName)
        self.ui.lastName.setText(lastName)
        self.ui.dateOfBirth.setText(dateOfBirth) 
        self.document_type = document_type
        self.ui.detectedDocumentType.setText(document_type)

    def add_person_to_database(self):
        firstName = self.ui.firstName.toPlainText()
        lastName = self.ui.lastName.toPlainText()
        dateOfBirth = format_date(self.ui.dateOfBirth.toPlainText(), self.document_type)
        self.usersTable.addPersonToDatabase(firstName, lastName, dateOfBirth)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
