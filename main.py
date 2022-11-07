<<<<<<< HEAD

import sys

import PySide6
=======
import sys

>>>>>>> 75a5aef (fix:command)
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_main_menu import *
from ui_color_change import *
from PySide6.QtUiTools import QUiLoader


class LoginWindow(QMainWindow):
<<<<<<< HEAD
  
  def __init__(self):  # 主界面初始化
    # super().__init__()
    # self.ui = Ui_MainWindow()
    # self.ui.setupUi(self)
    super(LoginWindow, self).__init__()
    self.ui = QUiLoader().load("main_menu.ui")
    self.ui.mainButton.clicked.connect(self.go_to_change)
    
    self.widget = QWidget()
    self.view = QGraphicsView()
    self.layout = QGridLayout()
    self.scene = QGraphicsScene()
    
    self.layout.addWidget(self.view)
    self.scene.setSceneRect(0,0,400,400)
    self.scene.addLine(0,0,300,300)
    self.view.show()
    self.setCentralWidget(self.view)
    
    # self.view = QGraphicsView()
    #
    # self.scene = MyGraphicsScene()
    # self.view.setSceneRect(QRect(-150, -150, 400, 400))
    #
    # self.addline(0, 0, 20, 29)
    #
    # self.view.setScene(self.scene)
    #
    #
    #
    #
    # layout = QHBoxLayout()
    # layout.addWidget(self.view)
    # self.setLayout(layout)
    #
    # self.initUI()
    # self.paintEvent()
    self.ui.show()
  
  def go_to_change(self):  # 界面跳转
    
    try:
      self.win = ChangeColor()
      self.ui.close()
    except:
      print("又整错了")

  def addline(self, x, y, z, n):
    self.scene.addLine(x, y, z, n, QPen(QColor(Qt.red),5,Qt.SolidLine))
    # 推拽
    # def mousePressEvent(self,event):
    #   if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
    #     self.m_flag = True
    #     self.m_Position = event.globalPos() - self.pos()
    #     event.accept()
    #     self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
    #
    # def mouserMoveEvent(self,mouse_event):
    #   if QtCore.Qt.LeftButton and self.m_flag:
    #     self.move(mouse_event.globalPos() - self.m_Position)
    #     mouse_event.accept()
    #
    # def mouseReleaseEvent(self,mouse_event):
    #   self.m_flag = False
    #   self.setCurser(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    # def pantagram(self):
    #   pass
    #   paiter = QPainter(self)

class Drawing(QGraphicsView):
  
  def __int__(self):
    super(Drawing, self).__int__()
    self.scene = MyGraphicsScene()
    self.addline(0,0,20,29)
    self.setSceneRect(QRect(-150,-150,400,400))
    self.setScene(self.scene)
  
  def addline(self,x,y,z,n):
    self.scene.addLine(x,y,z,n,QPen(QColor(Qt.red)))
    
class MyGraphicsScene(QGraphicsScene):
  
  def __int__(self):
    super(MyGraphicsScene, self).__int__()
    
  def drawBackground(self, painter, rect) -> None:
    pass

class ChangeColor(QWidget):
  
  def __init__(self):  # 副界面初始化
    # super().__init__()
    # self.ui = Ui_Form()
    # self.ui.setupUi(self)
    super(ChangeColor, self).__init__()
    self.ui = QUiLoader().load("color_change.ui")
    self.ui.BlackCButton.clicked.connect(self.BlackChange)
    self.ui.RedCButton.clicked.connect(self.RedChange)
    self.ui.GreenCButton.clicked.connect(self.GreenChange)
    self.ui.BlueCButton.clicked.connect(self.BlueChange)
    
    # self.ui.BlackCButton.mousemove.connect(lambda :self.ui.stackedWidget.setCurrentIndex(1))
    self.ui.show()
  
  def BlackChange(self):  # 颜色改变触发
    
    self.ui.FrameColor.setStyleSheet("#FrameColor{background:#000000;}")
    self.ui.stackedWidget.setCurrentIndex(1)
  
  def RedChange(self):
    self.ui.stackedWidget.setCurrentIndex(0)
    self.ui.FrameColor.setStyleSheet("#FrameColor{background:#aa0000;}")
  
  def GreenChange(self):
    self.ui.stackedWidget.setCurrentIndex(0)
    self.ui.FrameColor.setStyleSheet("#FrameColor{background:#00aa00;}")
  
  def BlueChange(self):
    self.ui.stackedWidget.setCurrentIndex(0)
    self.ui.FrameColor.setStyleSheet("#FrameColor{background:#0000ff;}")


if __name__ == '__main__':
  app = QApplication(sys.argv)
  
  win = LoginWindow()
  # win.show()
  
  sys.exit(app.exec())
=======
    
    def __init__(self):  # 主界面初始化
        # super().__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        super(LoginWindow, self).__init__()
        self.win = None
        self.ui = QUiLoader().load("main_menu.ui")
        self.ui.mainButton.clicked.connect(self.go_to_change)
        
        self.widget = QWidget()
        self.view = QGraphicsView()
        self.layout = QGridLayout()
        self.scene = QGraphicsScene()
        
        self.layout.addWidget(self.view)
        self.scene.setSceneRect(0, 0, 400, 400)
        self.scene.addLine(0, 0, 300, 300)
        self.view.show()
        self.setCentralWidget(self.view)
        self.ui.show()
    
    def go_to_change(self):  # 界面跳转
        
        try:
            self.win = ChangeColor()
            self.ui.close()
        
        except:
            print("又整错了")
    
    def addline(self, x, y, z, n):
        self.scene.addLine(x, y, z, n, QPen(QColor(Qt.red), 5, Qt.SolidLine))


class Drawing(QGraphicsView):
    
    def __int__(self):
        super(Drawing, self).__int__()
        self.scene = MyGraphicsScene()
        self.addline(0, 0, 20, 29)
        self.setSceneRect(QRect(-150, -150, 400, 400))
        self.setScene(self.scene)
    
    def addline(self, x, y, z, n):
        self.scene.addLine(x, y, z, n, QPen(QColor(Qt.red)))


class MyGraphicsScene(QGraphicsScene):
    
    def __int__(self):
        super(MyGraphicsScene, self).__int__()
    
    def drawBackground(self, painter, rect) -> None:
        pass


class ChangeColor(QWidget):
    
    def __init__(self):  # 副界面初始化
        # super().__init__()
        # self.ui = Ui_Form()
        # self.ui.setupUi(self)
        super(ChangeColor, self).__init__()
        self.ui = QUiLoader().load("color_change.ui")
        self.ui.BlackCButton.clicked.connect(self.BlackChange)
        self.ui.RedCButton.clicked.connect(self.RedChange)
        self.ui.GreenCButton.clicked.connect(self.GreenChange)
        self.ui.BlueCButton.clicked.connect(self.BlueChange)
        
        # self.ui.BlackCButton.mousemove.connect(lambda :self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.show()
    
    def BlackChange(self):  # 颜色改变触发
        
        self.ui.FrameColor.setStyleSheet("#FrameColor{background:#000000;}")
        self.ui.stackedWidget.setCurrentIndex(1)
        main()
    
    def RedChange(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.FrameColor.setStyleSheet("#FrameColor{background:#aa0000;}")
    
    def GreenChange(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.FrameColor.setStyleSheet("#FrameColor{background:#00aa00;}")
    
    def BlueChange(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.FrameColor.setStyleSheet("#FrameColor{background:#0000ff;}")


class undo_command(QUndoCommand):
    
    def __init__(self):
        super(undo_command, self).__init__()
    
    def redo(self) -> None:
        print('就这')
    
    def undo(self) -> None:
        print('没了？')


def main():
    Undo_stack = QUndoStack()
    Undo_stack.beginMacro("Add For Multiple Times")
    Undo_stack.push(undo_command())
    Undo_stack.endMacro()
    Undo_stack.undo()
    print('哪呢')
    Undo_stack.redo()
    print('牛啊牛啊')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    win = LoginWindow()
    # win.show()
    
    sys.exit(app.exec())
>>>>>>> 75a5aef (fix:command)
