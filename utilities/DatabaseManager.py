from PySide6.QtSql import QSqlDatabase, QSqlQuery
from utilities.date_utilities import format_date
from utilities.face_utilities import embedding_to_string, get_face_embedding
from utilities.message_box_utils import show_message_box_on_error, show_message_box_on_success

class DatabaseManager():
    def __init__(self, name, host, user, password):
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setDatabaseName(name)
        self.db.setHostName(host)
        self.db.setUserName(user)
        self.db.setPassword(password)

        
    def openConnection(self):
        if not self.db.open():
            print("Cannot establish a database connection")
            print('Last error', self.db.lastError().text())
        else:
            print("Database connection established")
    

    def closeConnection(self):
        if self.db.isOpen():
            self.db.close()
            QSqlDatabase.removeDatabase('example.db')
            print("Database connection closed")
        else:
            print("Database connection already closed")
    
    def getPersonByFaceEmbedding(self, target_vector):
        target_vector = [str(x) for x in target_vector]
        query = QSqlQuery()
        query.prepare("SELECT * FROM find_closest_person(:target_vector)")
        query.bindValue(":target_vector", embedding_to_string(target_vector))
        person_data = {}
        if not query.exec():
            output = "Błąd przy wyszukiwaniu osoby\n"
            output += f'Powód: {query.lastError().text()}'
            show_message_box_on_error(output)
            return None
        
        while query.next():
            person_data["id"] = query.value(0)
            person_data["distance"] = query.value(1)

        query.finish()
        return person_data

    def addPerson(self, firstName, lastName, dateOfBirth, face_embedding):
        query = QSqlQuery()
        query.prepare("INSERT INTO person (first_name, last_name, date_of_birth, face_data) VALUES (:first_name, :last_name, :date_of_birth, :face_data)")
        query.bindValue(":first_name", firstName)
        query.bindValue(":last_name", lastName)
        query.bindValue(":date_of_birth", dateOfBirth)
        query.bindValue(":face_data", embedding_to_string(face_embedding))
        if not query.exec():
            output_text = "Błąd przy wstawianiu osoby do bazy danych.\n"
            output_text += f'Powód: {query.lastError().text()}'
            show_message_box_on_error(output_text)
        else:
            show_message_box_on_success("Poprawnie dodano osobę do bazy danych")
        query.finish()

    def updatePerson(self, id, firstName, lastName, dateOfBirth, face_embedding):
        query = QSqlQuery()
        query.prepare("UPDATE person SET first_name = :first_name, last_name = :last_name, date_of_birth = :date_of_birth, face_data = :face_data WHERE id = :id")
        query.bindValue(":first_name", firstName)
        query.bindValue(":last_name", lastName)
        query.bindValue(":date_of_birth", dateOfBirth)
        query.bindValue(":face_data", embedding_to_string(face_embedding))
        query.bindValue(":id", id)
        if not query.exec():
            output_text = "Błąd przy aktualizacji danych osoby.\n"
            output_text += f'Powód: {query.lastError().text()}'
            show_message_box_on_error(output_text)
        else:
            show_message_box_on_success("Poprawnie zaktualizowano dane osoby")
        query.finish()


    def getPersonById(self, id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM person WHERE id = :id")
        query.bindValue(":id", id)

        data = {}
        if not query.exec():
            output_text = "Błąd przy pobieraniu osoby z bazy danych.\n"
            output_text += f'Powód: {query.lastError().text()}'
            show_message_box_on_error(output_text)
        else:
            while query.next():
                data["id"] = query.value(0)
                data["first_name"] = query.value(1)
                data["last_name"] = query.value(2)
                data["date_of_birth"] = query.value(4)
                data["face_data"] = query.value(8)
        
        query.finish()
        return data