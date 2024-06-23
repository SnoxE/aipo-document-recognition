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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1065, 641)
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget_2 = QWidget(self.tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(570, 20, 431, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 120))
        self.detectedPersonData = QTextBrowser(self.groupBox)
        self.detectedPersonData.setObjectName(u"detectedPersonData")
        self.detectedPersonData.setGeometry(QRect(10, 30, 411, 81))

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 40, 391, 353))
        self.personDataForm = QVBoxLayout(self.widget)
        self.personDataForm.setObjectName(u"personDataForm")
        self.personDataForm.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.personDataForm.addWidget(self.label_2)

        self.firstName = QTextEdit(self.widget)
        self.firstName.setObjectName(u"firstName")
        self.firstName.setMaximumSize(QSize(16777215, 40))

        self.personDataForm.addWidget(self.firstName)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.personDataForm.addWidget(self.label_3)

        self.lastName = QTextEdit(self.widget)
        self.lastName.setObjectName(u"lastName")
        self.lastName.setMaximumSize(QSize(16777215, 40))

        self.personDataForm.addWidget(self.lastName)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.personDataForm.addWidget(self.label_4)

        self.dateOfBirth = QTextEdit(self.widget)
        self.dateOfBirth.setObjectName(u"dateOfBirth")
        self.dateOfBirth.setMaximumSize(QSize(16777215, 40))

        self.personDataForm.addWidget(self.dateOfBirth)

        self.changeUserDataButton = QPushButton(self.widget)
        self.changeUserDataButton.setObjectName(u"changeUserDataButton")

        self.personDataForm.addWidget(self.changeUserDataButton)

        self.addPersonData = QPushButton(self.widget)
        self.addPersonData.setObjectName(u"addPersonData")

        self.personDataForm.addWidget(self.addPersonData)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.detectedDocumentType = QLabel(self.widget)
        self.detectedDocumentType.setObjectName(u"detectedDocumentType")

        self.horizontalLayout_2.addWidget(self.detectedDocumentType)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.personDataForm.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 521, 551))
        self.verticalLayoutWidget = QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 90, 471, 399))
        self.uploadedDocumentActions = QVBoxLayout(self.verticalLayoutWidget)
        self.uploadedDocumentActions.setObjectName(u"uploadedDocumentActions")
        self.uploadedDocumentActions.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.uploadedDocumentActions.addItem(self.verticalSpacer_2)

        self.photoField = QLabel(self.verticalLayoutWidget)
        self.photoField.setObjectName(u"photoField")
        self.photoField.setMaximumSize(QSize(16777215, 400))
        self.photoField.setSizeIncrement(QSize(0, 0))
        self.photoField.setBaseSize(QSize(0, 0))
        self.photoField.setAutoFillBackground(False)
        self.photoField.setScaledContents(True)
        self.photoField.setAlignment(Qt.AlignCenter)

        self.uploadedDocumentActions.addWidget(self.photoField)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.uploadedDocumentActions.addItem(self.verticalSpacer)

        self.uploadButton = QPushButton(self.verticalLayoutWidget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.uploadedDocumentActions.addWidget(self.uploadButton)

        self.loadDataFromDocument = QPushButton(self.verticalLayoutWidget)
        self.loadDataFromDocument.setObjectName(u"loadDataFromDocument")

        self.uploadedDocumentActions.addWidget(self.loadDataFromDocument)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 30, 981, 541))
        self.usersTable = QTableView(self.groupBox_4)
        self.usersTable.setObjectName(u"usersTable")
        self.usersTable.setGeometry(QRect(30, 50, 911, 461))
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Otrzymane dane z bazy danych", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Otrzymane dane ze zdj\u0119cia", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Imi\u0119", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Nazwisko", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Data urodzenia/PESEL", None))
        self.changeUserDataButton.setText(QCoreApplication.translate("Widget", u"Zmie\u0144 dane", None))
        self.addPersonData.setText(QCoreApplication.translate("Widget", u"Dodaj do bazy danych", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Wykryty rodzaj dokumentu:", None))
        self.detectedDocumentType.setText(QCoreApplication.translate("Widget", u"Brak", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Wczytywanie zdj\u0119cia", None))
        self.photoField.setText(QCoreApplication.translate("Widget", u"Tutaj pojawi si\u0119 zdj\u0119cie dokumentu", None))
        self.uploadButton.setText(QCoreApplication.translate("Widget", u"Wczytaj zdj\u0119cie", None))
        self.loadDataFromDocument.setText(QCoreApplication.translate("Widget", u"Pobierz dane ze zdj\u0119cia", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Wczytywanie dokument\u00f3w", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"Dane u\u017cytkownik\u00f3w", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Baza u\u017cytkownik\u00f3w", None))
    # retranslateUi

