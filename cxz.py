import sys

import PySide6
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import Qt, QPoint, QRect


class Drawing(QGraphicsView):
    def __init__(self):
        super(Drawing, self).__init__()
        self.scene = MyGraphicsScene(self)
        self.addPoint(0, 0)
        self.setSceneRect(QRect(-150,-150,400,400))
        self.setScene(self.scene)
        # self.frame = None
        # self.pianLabel = None
        # self.previous_pos = None
        # # self.initUI()
      
    def addPoint(self,x,y):
        self.scene.addLine(x,y,100,100,QPen(QColor(Qt.red)))
        
    def initUI(self):
        # self.setGeometry(200,200,800,600)
        # self.setWindowTitle("钢笔例子")
        self.scene = QGraphicsScene(0, 0, 711, 601)
        self.setSceneRect(0, 0, 800, 600)
        self.view = QGraphicsView(self.scene)
        
        # self.graphics = QGraphicsScene()
        
        
    # def paintEvent(self,event):
    #     # self.graphics.clear()
    #     qp=QPainter()
    #     qp.begin(self)
    #     self.drawlines(qp)
    #     qp.end()
    #
    #
    # def drawlines(self,qp):
    #     pen=QPen(Qt.red,2,Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(QPoint(0,0),QPoint(200,300),QBrush(Qt.red))
        
        

        # pen.setStyle(Qt.DashLine)
        # qp.setPen(pen)
        # qp.drawLine(20,80,250,80)
        #
        # pen.setStyle(Qt.DashDotLine)
        # qp.setPen(pen)
        # qp.drawLine(20,120,250,120)
        #
        # pen.setStyle(Qt.DotLine)
        # qp.setPen(pen)
        # qp.drawLine(20,160,240,160)
        #
        # pen.setStyle(Qt.DashDotDotLine)
        # qp.setPen(pen)
        # qp.drawLine(20,200,250,200)
#自定义线条样式
        # pen.setStyle(Qt.CustomDashLine)#创建线条样式
        # pen.setDashPattern([1,4,5,4])#定义线条样式
        # '''数字列表的个数必须是偶数，奇数位（1，3，5，7，9等）代表一端横线，
        # 偶数位（2，4，6，8，10等）代表两端横线之间的空余距离，数字越大，
        # 横线和控与激励就越大，本例中含义为，1像素宽度的横线，4像素宽度的空余距离，
        # 5像素宽度的横线，4像素宽度的空余距离'''
        # qp.setPen(pen)
        # qp.drawLine(20,240,250,240)


class MyGraphicsScene(QGraphicsScene):
    def __int__(self):
        super(MyGraphicsScene, self).__int__()
        
    def dragEnterEvent(self, event: PySide6.QtWidgets.QGraphicsSceneDragDropEvent) -> None:
        pass
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Drawing()
    win.show()
    sys.exit(app.exec())
