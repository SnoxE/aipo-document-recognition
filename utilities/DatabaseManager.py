from PySide6.QtSql import QSqlDatabase, QSqlQuery
from utilities.date_utilities import format_date

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

    def addPersonToDatabase(self, firstName, lastName, dateOfBirth):
        query = QSqlQuery()
        query.prepare("INSERT INTO person (first_name, last_name, date_of_birth) VALUES (:first_name, :last_name, :date_of_birth)")
        query.bindValue(":first_name", firstName)
        query.bindValue(":last_name", lastName)
        query.bindValue(":date_of_birth", format_date(dateOfBirth))
        if not query.exec():
            print("Error inserting person")
            print('Last error', query.lastError().text())
        else:
            print("Person inserted successfully")

    def readPeopleFromDatabase(self):
        query = QSqlQuery("SELECT id, first_name, last_name, date_of_birth FROM person")
        people = []
        while query.next():
            person = {
                "id": query.value(0),
                "first_name": query.value(1),
                "last_name": query.value(2),
                "date_of_birth": query.value(3)
            }
            people.append(person)
        return people