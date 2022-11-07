# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QToolBar, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionlook = QAction(MainWindow)
        self.actionlook.setObjectName(u"actionlook")
        icon = QIcon()
        icon.addFile(u":/images/img/game.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionlook.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(170, 60, 511, 391))
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 12, 12, 12)
        self.mainButton = QPushButton(self.layoutWidget)
        self.mainButton.setObjectName(u"mainButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainButton.sizePolicy().hasHeightForWidth())
        self.mainButton.setSizePolicy(sizePolicy)
        self.mainButton.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.mainButton)

        self.outButton = QPushButton(self.layoutWidget)
        self.outButton.setObjectName(u"outButton")
        sizePolicy.setHeightForWidth(self.outButton.sizePolicy().hasHeightForWidth())
        self.outButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(12)
        self.outButton.setFont(font)
        self.outButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(233, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border:none;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}")

        self.horizontalLayout.addWidget(self.outButton)

        self.splitter.addWidget(self.layoutWidget)
        self.DrawFrame = QFrame(self.splitter)
        self.DrawFrame.setObjectName(u"DrawFrame")
        sizePolicy.setHeightForWidth(self.DrawFrame.sizePolicy().hasHeightForWidth())
        self.DrawFrame.setSizePolicy(sizePolicy)
        self.DrawFrame.setFrameShape(QFrame.StyledPanel)
        self.DrawFrame.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.DrawFrame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 11, 521, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.splitter.addWidget(self.DrawFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.MainMenu = QMenu(self.menubar)
        self.MainMenu.setObjectName(u"MainMenu")
        font1 = QFont()
        font1.setFamilies([u"\u534e\u6587\u96b6\u4e66"])
        self.MainMenu.setFont(font1)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.MainMenu.menuAction())
        self.MainMenu.addAction(self.actionlook)
        self.toolBar.addAction(self.actionlook)

        self.retranslateUi(MainWindow)
        self.outButton.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionlook.setText(QCoreApplication.translate("MainWindow", u"\u4f60\u7785\u5565", None))
        self.mainButton.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u83dc\u5355", None))
        self.outButton.setText(QCoreApplication.translate("MainWindow", u"\u522b\u70b9\u6211x", None))
        self.MainMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u83dc\u5355", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

