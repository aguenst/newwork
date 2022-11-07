# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_change.ui'
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
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(758, 477)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 761, 441))
        self.frame.setStyleSheet(u"background-color: rgb(240, 250, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.RedCButton = QPushButton(self.frame_4)
        self.RedCButton.setObjectName(u"RedCButton")
        self.RedCButton.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(200, 13, 0);\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"c")

        self.verticalLayout_2.addWidget(self.RedCButton)

        self.GreenCButton = QPushButton(self.frame_4)
        self.GreenCButton.setObjectName(u"GreenCButton")
        self.GreenCButton.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 170, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.GreenCButton)

        self.BlueCButton = QPushButton(self.frame_4)
        self.BlueCButton.setObjectName(u"BlueCButton")
        self.BlueCButton.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 85, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.BlueCButton)

        self.BlackCButton = QPushButton(self.frame_4)
        self.BlackCButton.setObjectName(u"BlackCButton")
        self.BlackCButton.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.BlackCButton)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(150)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.FrameColor = QWidget()
        self.FrameColor.setObjectName(u"FrameColor")
        self.FrameColor.setStyleSheet(u"background-color: rgb(255, 253, 230);")
        self.stackedWidget.addWidget(self.FrameColor)
        self.Frame = QWidget()
        self.Frame.setObjectName(u"Frame")
        self.Frame.setStyleSheet(u"")
        self.PianLabel = QLabel(self.Frame)
        self.PianLabel.setObjectName(u"PianLabel")
        self.PianLabel.setGeometry(QRect(50, 40, 321, 321))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u7425\u73c0"])
        font.setPointSize(27)
        self.PianLabel.setFont(font)
        self.PianLabel.setStyleSheet(u"background-image: url(:/images/img/fanzha.jpg);\n"
"color: rgb(255, 255, 255);")
        self.PianLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.PianLabel.setMargin(15)
        self.PianLabel.setIndent(4)
        self.stackedWidget.addWidget(self.Frame)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.RedCButton.setText(QCoreApplication.translate("Form", u"\u70b9\u6211", None))
        self.GreenCButton.setText(QCoreApplication.translate("Form", u"\u522b\u9009\u4ed6\uff0c\u9009\u6211", None))
        self.BlueCButton.setText(QCoreApplication.translate("Form", u"\u4e0b\u53cd\u8bc8app\u6ca1", None))
        self.BlackCButton.setText(QCoreApplication.translate("Form", u"\u8bf4\u7684", None))
        self.PianLabel.setText(QCoreApplication.translate("Form", u"\u5c31\u4f60\n"
"\u4e0b\u8f7d\u53cd\u6e23", None))
    # retranslateUi

