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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1092, 593)
        self.uploadButton = QPushButton(Widget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(140, 420, 301, 31))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(680, 420, 301, 31))
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(680, 360, 301, 31))
        self.photoField = QLabel(Widget)
        self.photoField.setObjectName(u"photoField")
        self.photoField.setGeometry(QRect(70, 70, 441, 301))
        self.photoField.setAutoFillBackground(True)
        self.photoField.setScaledContents(True)
        self.photoField.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(670, 60, 181, 16))
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.label_2)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.uploadButton.setText(QCoreApplication.translate("Widget", u"Wczytaj zdj\u0119cie", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Baza U\u017cytkownik\u00f3w", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Pozosta\u0142e dokumenty", None))
        self.photoField.setText(QCoreApplication.translate("Widget", u"Tutaj pojawi si\u0119 zdj\u0119cie dokumentu", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Menu", None))
    # retranslateUi

