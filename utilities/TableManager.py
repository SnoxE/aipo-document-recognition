from PySide6.QtWidgets import QPushButton
from PySide6.QtSql import QSqlQuery, QSqlTableModel
from PySide6.QtCore import Qt
from functools import partial

class TableManager():
    def __init__(self, table_name, table_view, db_manager):
        self.table_view = table_view
        self.model = QSqlTableModel()
        self.db_manager = db_manager
        self.model.setTable(table_name)
        self.model.select()
        self.table_view.setModel(self.model)
        self.draw()

    def insertDeleteButtons(self):
        for i in range(self.model.rowCount()):
            delete_button = QPushButton("Usuń")
            delete_button.clicked.connect(partial(self.deleteRecord, i))
            self.table_view.setIndexWidget(self.model.index(i, self.model.columnCount() - 1), delete_button)

    def draw(self):
        self.table_view.setColumnWidth(self.model.columnCount(), 100)
        self.model.select()
        self.model.insertColumn(self.model.columnCount())
        self.model.setHeaderData(self.model.columnCount() - 1, Qt.Orientation.Horizontal, "Akcje")
        self.insertDeleteButtons()
        self.table_view.hideColumn(0)
        self.table_view.hideColumn(3)
        self.table_view.hideColumn(5)
        self.table_view.hideColumn(6)
        self.table_view.hideColumn(7)
        self.table_view.hideColumn(8)

    def deleteRecord(self, index):
        record_id = self.model.data(self.model.index(index, 0))
        query = QSqlQuery(self.db_manager.db)
        query.exec(f"DELETE FROM person WHERE id = {record_id}")
        self.model.removeRow(index)
        self.draw()

    def destroy(self):
        self.model.clear()

    def addPersonToDatabase(self, firstName, lastName, dateOfBirth):
        self.db_manager.addPersonToDatabase(firstName, lastName, dateOfBirth)
        self.draw()