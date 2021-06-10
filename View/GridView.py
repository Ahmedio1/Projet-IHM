from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Model import *

class GridView(QMainWindow):

    def __init__(self,Model,Controle):
        super().__init__()
        self.__Grid=Model
        self.__Controller=Controle
        self.__GridLayout = QGridLayout(self.__Controller)
        self.__GridLayout.setContentsMargins(0,0,7,9)
        self.__Controller.setLayout(self.__GridLayout)
        self.setCentralWidget(self.__Controller)
        self.setFixedSize(640,640)
        self.UpdateView()
        self.__Controller.setFocus()

    def setGrid(self,Grid):
        self.__Grid=Grid

    def setControler(self,controle):
        self.__Controller=controle

    def UpdateView(self):
        for i in reversed(range(self.__GridLayout.count())):
            widget_to_remove = self.__GridLayout.itemAt(i).widget()
            # remove it from the layout list
            self.__GridLayout.removeWidget(widget_to_remove)
            # remove it from the gui
            widget_to_remove.setParent(None)
        grid=self.__Grid.getGrid()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                carre=QWidget()
                carre.setFixedSize(self.__Grid.getTaille(),self.__Grid.getTaille())
                if grid[i][j]==0:
                    carre.setStyleSheet("background-image: url(block/dirt.png)")
                if grid[i][j]==1:
                    carre.setStyleSheet("background-image: url(block/oxeye_daisy.png)")#mettre le sol derrière!
                if grid[i][j]==2:
                    carre.setStyleSheet("background-image: url(block/lime_wool.png)")
                if grid[i][j]==3:
                    carre.setStyleSheet("background-image: url(block/cobblestone.png) ")
                if grid[i][j]==4:
                    carre.setStyleSheet("background-image: url(block/black_stained_glass.png) ")
                if grid[i][j]==5:
                    carre.setStyleSheet("background-image: url(block/item_frame.png) ")
                self.__GridLayout.addWidget(carre,i,j)


