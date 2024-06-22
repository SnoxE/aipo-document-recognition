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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1065, 615)
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 50, 471, 399))
        self.uploadedDocumentActions = QVBoxLayout(self.verticalLayoutWidget)
        self.uploadedDocumentActions.setObjectName(u"uploadedDocumentActions")
        self.uploadedDocumentActions.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.uploadedDocumentActions.addItem(self.verticalSpacer_2)

        self.photoField = QLabel(self.verticalLayoutWidget)
        self.photoField.setObjectName(u"photoField")
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

        self.verticalLayoutWidget_3 = QWidget(self.tab)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(650, 90, 298, 331))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.personDataForm = QVBoxLayout()
        self.personDataForm.setObjectName(u"personDataForm")
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.personDataForm.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.personDataForm.addWidget(self.label_2)

        self.firstName = QTextEdit(self.verticalLayoutWidget_3)
        self.firstName.setObjectName(u"firstName")

        self.personDataForm.addWidget(self.firstName)

        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.personDataForm.addWidget(self.label_3)

        self.lastName = QTextEdit(self.verticalLayoutWidget_3)
        self.lastName.setObjectName(u"lastName")

        self.personDataForm.addWidget(self.lastName)

        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.personDataForm.addWidget(self.label_4)

        self.dateOfBirth = QTextEdit(self.verticalLayoutWidget_3)
        self.dateOfBirth.setObjectName(u"dateOfBirth")

        self.personDataForm.addWidget(self.dateOfBirth)

        self.addOrUpdatePersonData = QPushButton(self.verticalLayoutWidget_3)
        self.addOrUpdatePersonData.setObjectName(u"addOrUpdatePersonData")

        self.personDataForm.addWidget(self.addOrUpdatePersonData)

        self.verticalSpacer_3 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.personDataForm.addItem(self.verticalSpacer_3)


        self.verticalLayout_2.addLayout(self.personDataForm)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.detectedDocumentType = QLabel(self.verticalLayoutWidget_3)
        self.detectedDocumentType.setObjectName(u"detectedDocumentType")

        self.horizontalLayout_2.addWidget(self.detectedDocumentType)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.usersTable = QTableView(self.tab_2)
        self.usersTable.setObjectName(u"usersTable")
        self.usersTable.setGeometry(QRect(60, 80, 911, 391))
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


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
        self.label_5.setText(QCoreApplication.translate("Widget", u"Wykryty rodzaj dokumentu:", None))
        self.detectedDocumentType.setText(QCoreApplication.translate("Widget", u"Brak", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Wczytywanie dokument\u00f3w", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Baza u\u017cytkownik\u00f3w", None))
    # retranslateUi

