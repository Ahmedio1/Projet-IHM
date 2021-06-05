from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Model import *

class GridView(QMainWindow):

    def __init__(self,Model,Controle):
        super().__init__()
        self.__GridLayout=QGridLayout()
        self.__Grid=Model
        self.__Controller=Controle
        self.__GridLayout = QGridLayout(self.__Controller)
        self.__Controller.setLayout(self.__GridLayout)
        self.setCentralWidget(self.__Controller)
        self.UpdateView()
        self.__Controller.setFocus()

    def setGrid(self,Grid):
        self.__Grid=Grid

    def setControler(self,controle):
        self.__Controller=controle

    def UpdateView(self):
        grid=self.__Grid.getGrid()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                carre=QWidget()
                carre.setFixedSize(self.__Grid.getTaille(),self.__Grid.getTaille())
                if grid[i][j]==0:
                    carre.setStyleSheet("background-color: white; border:1px solid black")
                if grid[i][j]==1:
                    carre.setStyleSheet("background-color: black; border:1px solid black")
                if grid[i][j]==2:
                    carre.setStyleSheet("background-color: yellow; border:1px solid black")
                self.__GridLayout.addWidget(carre,i,j)


