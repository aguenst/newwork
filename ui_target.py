# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'target.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 110, 311, 451))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 110, 321, 451))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u6977\u4f53"])
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(93, 165, 201, 71))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_3.setFont(font1)
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 270, 161, 20))
        self.lineEdit.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgba(0, 0, 0,100);\n"
"background-color: rgba(0, 0, 0,0);\n"
"")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 350, 161, 20))
        self.lineEdit_2.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgba(0, 0, 0,100);\n"
"background-color: rgba(0, 0, 0,0);\n"
"\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText(u"\u5bc6\u7801\uff1a")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 440, 81, 41))
        font2 = QFont()
        font2.setFamilies([u"\u6977\u4f53"])
        font2.setPointSize(12)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(39, 110, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 250, 171, 61))
        font3 = QFont()
        font3.setPointSize(17)
        self.label_4.setFont(font3)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(618, 120, 71, 41))
        self.frame.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	padding-top:3px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(MainWindow.showMinimized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"img", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u767b\u5f55", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"wechat:nihao\n"
"\u4e00\u4ef6\u4e09\u8054", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"x", None))
    # retranslateUi

