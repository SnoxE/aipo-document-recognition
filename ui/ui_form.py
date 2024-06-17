# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1092, 593)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.photoField = QLabel(self.tab)
        self.photoField.setObjectName(u"photoField")
        self.photoField.setGeometry(QRect(60, 50, 421, 271))
        self.photoField.setAutoFillBackground(False)
        self.photoField.setScaledContents(True)
        self.photoField.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(140, 380, 281, 80))
        self.uploadedDocumentActions = QVBoxLayout(self.verticalLayoutWidget)
        self.uploadedDocumentActions.setObjectName(u"uploadedDocumentActions")
        self.uploadedDocumentActions.setContentsMargins(0, 0, 0, 0)
        self.uploadButton = QPushButton(self.verticalLayoutWidget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.uploadedDocumentActions.addWidget(self.uploadButton)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.uploadedDocumentActions.addWidget(self.pushButton_3)

        self.verticalLayoutWidget_2 = QWidget(self.tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(620, 100, 291, 291))
        self.personDataForm = QVBoxLayout(self.verticalLayoutWidget_2)
        self.personDataForm.setObjectName(u"personDataForm")
        self.personDataForm.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.personDataForm.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.personDataForm.addWidget(self.label_2)

        self.firstName = QTextEdit(self.verticalLayoutWidget_2)
        self.firstName.setObjectName(u"firstName")

        self.personDataForm.addWidget(self.firstName)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.personDataForm.addWidget(self.label_3)

        self.lastName = QTextEdit(self.verticalLayoutWidget_2)
        self.lastName.setObjectName(u"lastName")

        self.personDataForm.addWidget(self.lastName)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.personDataForm.addWidget(self.label_5)

        self.dateOfBirth = QTextEdit(self.verticalLayoutWidget_2)
        self.dateOfBirth.setObjectName(u"dateOfBirth")

        self.personDataForm.addWidget(self.dateOfBirth)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.personDataForm.addWidget(self.label_4)

        self.sex = QTextEdit(self.verticalLayoutWidget_2)
        self.sex.setObjectName(u"sex")

        self.personDataForm.addWidget(self.sex)

        self.addOrUpdatePersonData = QPushButton(self.verticalLayoutWidget_2)
        self.addOrUpdatePersonData.setObjectName(u"addOrUpdatePersonData")

        self.personDataForm.addWidget(self.addOrUpdatePersonData)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.usersTable = QTableWidget(self.tab_2)
        if (self.usersTable.columnCount() < 4):
            self.usersTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.usersTable.rowCount() < 2):
            self.usersTable.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.usersTable.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.usersTable.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.usersTable.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.usersTable.setItem(0, 3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.usersTable.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.usersTable.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.usersTable.setItem(1, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.usersTable.setItem(1, 3, __qtablewidgetitem11)
        self.usersTable.setObjectName(u"usersTable")
        self.usersTable.setGeometry(QRect(60, 80, 931, 251))
        self.usersTable.setBaseSize(QSize(0, 0))
        self.usersTable.setSortingEnabled(False)
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.photoField.setText(QCoreApplication.translate("Widget", u"Tutaj pojawi si\u0119 zdj\u0119cie dokumentu", None))
        self.uploadButton.setText(QCoreApplication.translate("Widget", u"Wczytaj zdj\u0119cie", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Wprowad\u017a dane r\u0119cznie", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Otrzymane dane", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Imi\u0119", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Nazwisko", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"P\u0142e\u0107", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Data urodzenia", None))
        self.addOrUpdatePersonData.setText(QCoreApplication.translate("Widget", u"Zapisz w bazie danych", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Wczytywanie dokument\u00f3w", None))
        ___qtablewidgetitem = self.usersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Imi\u0119", None));
        ___qtablewidgetitem1 = self.usersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Nazwisko", None));
        ___qtablewidgetitem2 = self.usersTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"P\u0142e\u0107", None));
        ___qtablewidgetitem3 = self.usersTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Data urodzenia", None));

        __sortingEnabled = self.usersTable.isSortingEnabled()
        self.usersTable.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.usersTable.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"Adam", None));
        ___qtablewidgetitem5 = self.usersTable.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"Abacki", None));
        ___qtablewidgetitem6 = self.usersTable.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget", u"M", None));
        ___qtablewidgetitem7 = self.usersTable.item(0, 3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Widget", u"01.01.1990", None));
        ___qtablewidgetitem8 = self.usersTable.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Widget", u"Bogdan", None));
        ___qtablewidgetitem9 = self.usersTable.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Widget", u"Babacki", None));
        ___qtablewidgetitem10 = self.usersTable.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Widget", u"M", None));
        ___qtablewidgetitem11 = self.usersTable.item(1, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Widget", u"01.01.1990", None));
        self.usersTable.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Baza u\u017cytkownik\u00f3w", None))
    # retranslateUi

