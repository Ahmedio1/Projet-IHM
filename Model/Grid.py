from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from View.GridView import GridView

class Grid():

    def __init__(self):
        self.__Taille=64
        self.__NbLigne=9
        self.__NbColone=8
        self.__grid=[]
        self.generateGrid()
        self.__view=None
        self.__controle=None
        self.__xJ=5
        self.__yJ=5
        self.__xC=2
        self.__yC=2
        self.positionJ=[self.__xJ,self.__yJ]
        self.positionC=[self.__xC,self.__yC]

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
        if not (0<=self.positionJ[0]+x<self.__NbColone):
            return
        elif not (0<=self.positionJ[1]+y<self.__NbLigne):
            return
        else:
            lgnavt=self.positionJ[0]
            colavt = self.positionJ[1]
            self.positionJ[0] = self.positionJ[0] + x
            self.positionJ[1] = self.positionJ[1] + y
            print(self.positionJ[1])


        if (self.positionJ[0]==self.positionC[0] and self.positionJ[1]==self.positionC[1] ):
            self.positionC[0]=self.positionC[0]+x
            self.positionC[1] = self.positionC[1]+y

        lgnC =self.positionC[0] # ligne case
        colC =self.positionC[1] # colonne case
        lgnJ = self.positionJ[0] # ligne joueur
        colJ = self.positionJ[1] # colonne joueur

        print(lgnJ,colJ)
        self.__grid[lgnJ][colJ]=1
        self.__grid[lgnavt][colavt]=0
        self.__grid[lgnC][colC]=2
        self.__view.UpdateView()




