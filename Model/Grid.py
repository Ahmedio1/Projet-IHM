from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from View.GridView import GridView

class Grid():

    def __init__(self):
        self.__Taille=64
        self.__NbLigne=10
        self.__NbColone=10
        self.__grid=[]
        self.generateGrid()
        self.__view=None
        self.__controle=None
        self.__xJ=5
        self.__yJ=5
        self.positionJ=[self.__xJ,self.__yJ]

    def getNbLigne(self):
        return self.__NbLigne

    def getNbColone(self):
        return self.__NbColone

    def setView(self,view):
        self.__view=view

    def getGrid(self):
        return self.__grid

    def generateGrid(self):
        for i in range (self.__NbColone):
            self.__grid.append([])
            for j in range (self.__NbLigne):
                self.__grid[i].append(0)

    def getTaille(self):
        return self.__Taille

    def setControle(self,controle):
        self.__controle=controle


    def deplacerJo(self,x,y):
        if not (1<self.positionJ[0]+x<9) and (9>self.positionJ[1]+y>1):
            return
        else:
            self.positionJ[0] = self.positionJ[0] + x
            self.positionJ[1] = self.positionJ[1] + y
            lgn = self.positionJ[0]
            col = self.positionJ[1]
            print(lgn,col)
            self.__grid[lgn][col]=1
            self.__view.UpdateView()




