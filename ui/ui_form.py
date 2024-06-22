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
    QPushButton, QSizePolicy, QTabWidget, QTableView,
    QTextEdit, QVBoxLayout, QWidget)

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
        self.verticalLayoutWidget.setGeometry(QRect(130, 370, 281, 82))
        self.uploadedDocumentActions = QVBoxLayout(self.verticalLayoutWidget)
        self.uploadedDocumentActions.setObjectName(u"uploadedDocumentActions")
        self.uploadedDocumentActions.setContentsMargins(0, 0, 0, 0)
        self.uploadButton = QPushButton(self.verticalLayoutWidget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.uploadedDocumentActions.addWidget(self.uploadButton)

        self.loadDataFromDocument = QPushButton(self.verticalLayoutWidget)
        self.loadDataFromDocument.setObjectName(u"loadDataFromDocument")

        self.uploadedDocumentActions.addWidget(self.loadDataFromDocument)

        self.verticalLayoutWidget_2 = QWidget(self.tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(630, 150, 291, 328))
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

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.personDataForm.addWidget(self.label_4)

        self.dateOfBirth = QTextEdit(self.verticalLayoutWidget_2)
        self.dateOfBirth.setObjectName(u"dateOfBirth")

        self.personDataForm.addWidget(self.dateOfBirth)

        self.addOrUpdatePersonData = QPushButton(self.verticalLayoutWidget_2)
        self.addOrUpdatePersonData.setObjectName(u"addOrUpdatePersonData")

        self.personDataForm.addWidget(self.addOrUpdatePersonData)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.usersTable = QTableView(self.tab_2)
        self.usersTable.setObjectName(u"usersTable")
        self.usersTable.setGeometry(QRect(60, 80, 911, 241))
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
        self.loadDataFromDocument.setText(QCoreApplication.translate("Widget", u"Pobierz dane ze zdj\u0119cia", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Otrzymane dane", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Imi\u0119", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Nazwisko", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Data urodzenia", None))
        self.addOrUpdatePersonData.setText(QCoreApplication.translate("Widget", u"Zapisz w bazie danych", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Wczytywanie dokument\u00f3w", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Baza u\u017cytkownik\u00f3w", None))
    # retranslateUi

