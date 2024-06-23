# This Python file uses the following encoding: utf-8
import sys
import pytesseract
import os
import cv2

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from dotenv import load_dotenv

from utilities.TableManager import TableManager
from utilities.date_utilities import format_date
from utilities.face_utilities import cosine_similarity, detect_faces, get_face_embedding
from utilities.message_box_utils import show_message_box_on_error
from utilities.read_utilities import generateData
from utilities.text_utilities import format_person_output
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
        self.ui.addPersonData.setEnabled(False)
        self.ui.changeUserDataButton.setEnabled(False)
        self.ui.changeUserDataButton.clicked.connect(self.update_person_in_database)
        self.ui.addPersonData.clicked.connect(self.add_person_to_database)
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
        self.closest_person = None
        self.face_embedding = None

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
            self.file_name = fileName

    def load_data_from_image(self):
        self.ui.addPersonData.setEnabled(self.uploaded_image is not None)
        if self.uploaded_image is None:
            show_message_box_on_error("Nie wybrano zdjęcia")
            return
        
        height, width, _ = self.uploaded_image.shape
        firstName, lastName, dateOfBirth, document_type = generateData(self.uploaded_image, height, width)
        self.ui.firstName.setText(firstName)
        self.ui.lastName.setText(lastName)
        self.ui.dateOfBirth.setText(dateOfBirth) 
        self.document_type = document_type
        self.ui.detectedDocumentType.setText(document_type)

        self.face_embedding = get_face_embedding(detect_faces(self.file_name))
        self.closest_person = self.usersTable.db_manager.getPersonByFaceEmbedding(self.face_embedding)
        self.ui.changeUserDataButton.setEnabled(False)
        self.ui.detectedPersonData.setText("")
        
        print(f"Closest person: {self.closest_person}")
        
        if 'id' not in self.closest_person.keys():
            self.ui.detectedPersonData.setText("Nie znaleziono osoby w bazie danych")
            return
        
        self.update_detected_person_data()

    def add_person_to_database(self):
        firstName = self.ui.firstName.toPlainText()
        lastName = self.ui.lastName.toPlainText()
        dateOfBirth = format_date(self.ui.dateOfBirth.toPlainText(), self.document_type)
        print(self.closest_person)
        self.usersTable.addPersonToDatabase(
            firstName, 
            lastName, 
            dateOfBirth, 
            self.face_embedding,
        )
        
        self.update_detected_person_data()
        
        
    def update_person_in_database(self):
        firstName = self.ui.firstName.toPlainText()
        lastName = self.ui.lastName.toPlainText()
        dateOfBirth = format_date(self.ui.dateOfBirth.toPlainText(), self.document_type)
        self.usersTable.updatePersonInDatabase(
            firstName, 
            lastName, 
            dateOfBirth, 
            self.face_embedding,
            self.closest_person
        )
        
        self.update_detected_person_data()
        
    def update_detected_person_data(self):
        closest_person_data = self.usersTable.db_manager.getPersonById(self.closest_person['id'])
        # zamień embedding zapisany w bazie danych jako string na listę floatów
        closest_person_face_embedding =  list(map(lambda x: float(x), closest_person_data['face_data'].replace('{', '').replace('}','').strip().split(',')))
        similarity = cosine_similarity(self.face_embedding, closest_person_face_embedding)  
        
        found_similar_person = self.closest_person is not None and similarity > 0.85
        print(f"Similarity: {similarity}, Distance: {self.closest_person['distance']}, Found similar person: {found_similar_person}")
        
        self.ui.changeUserDataButton.setEnabled(found_similar_person)
        
        if found_similar_person:
            self.ui.detectedPersonData.setText(format_person_output(closest_person_data, ['id', 'face_data']))
        else:
            self.ui.detectedPersonData.setText("Nie znaleziono osoby w bazie danych")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.setWindowTitle("AiPO Document Recognition")
    widget.show()
    sys.exit(app.exec())
