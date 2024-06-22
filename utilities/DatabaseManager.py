from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class DatabaseManager():
    def __init__(self, name, host, user, password):
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setDatabaseName(name)
        self.db.setHostName(host)
        self.db.setUserName(user)
        self.db.setPassword(password)

        
    def open(self):
        if not self.db.open():
            print("Cannot establish a database connection")
            print('Last error', self.db.lastError().text())
        else:
            print("Database connection established")
    

    def close(self):
        if self.db.isOpen():
            self.db.close()
            QSqlDatabase.removeDatabase('example.db')
            print("Database connection closed")
        else:
            print("Database connection already closed")