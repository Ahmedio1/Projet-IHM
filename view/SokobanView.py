from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.Qt import Qt


class SnakeSokoban(QWidget):
    def __init__(self,width,height):
        super().__init__()

        self.setFixedSize(width,height)
        self.__model=None
        self.__controller=None
        self.show()

    def getModel(self):
        return self.__model
    
    def getController(self):
        return self.__controller
    
    def setModel(self,model):
        self.__model=model
    
    def setController(self,controller):
        self.__controller=controller
    
    def paintEvent(self,event):
        