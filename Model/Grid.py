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
        self.__xM=4
        self.__yM=6
        self.positionJ=[self.__xJ,self.__yJ]
        self.positionC=[self.__xC,self.__yC]
        self.positionM1=[self.__xM,self.__yM]

    def getNbLigne(self):
        return self.__NbLigne

    def getNbColone(self):
        return self.__NbColone

    def setView(self,view):
        self.__view=view

    def getGrid(self):
        return self.__grid

    def generateGrid(self):
        for i in range (self.__NbLigne):
            self.__grid.append([])
            for j in range (self.__NbColone):
                self.__grid[i].append(0)

    def getTaille(self):
        return self.__Taille

    def setControle(self,controle):
        self.__controle=controle


    def deplacerJo(self,x,y):
        # Mur
        if ((self.positionJ[0]==self.positionM1[0])and(self.positionJ[1]==self.positionM1[1])):
            self.positionJ[0]=self.positionJ[0]
            self.positionJ[1]=self.positionJ[1]

        #Joueur
        if ((self.positionC[0]==0) and ((self.positionC[0]==self.positionJ[0]+x)and(self.positionC[1]==self.positionJ[1]))):
            print("bloqué 1.3")
            self.positionJ[0] = 1
            return 
        elif ((self.positionC[0]==self.__NbLigne-1) and ((self.positionC[0]==self.positionJ[0]+x)and(self.positionC[1]==self.positionJ[1]))):
            print("bloqué 1.4")
            self.positionJ[0]=self.__NbLigne-2
            return
        elif ((self.positionC[1]==0) and ((self.positionC[1]==self.positionJ[1]+y)and(self.positionC[0]==self.positionJ[0]))):
            print("bloqué 1.3")
            self.positionJ[1] = 1
            return 
        elif ((self.positionC[1]==self.__NbColone-1) and ((self.positionC[1]==self.positionJ[1]+y)and(self.positionC[0]==self.positionJ[0]))):
            print("bloqué 1.4")
            self.positionJ[1]=self.__NbColone-2
            return
        elif not (0<=self.positionJ[0]+x<self.__NbLigne):
            print("bloqué 1.1")
            return
        elif not (0<=self.positionJ[1]+y<self.__NbColone):
            print("bloqué 1.2")
            return
        
        else:
            lgnavt=self.positionJ[0]
            colavt = self.positionJ[1]
            self.positionJ[0] = self.positionJ[0] + x
            self.positionJ[1] = self.positionJ[1] + y

        #Caisse
        if not (0<=self.positionC[0]+x<self.__NbLigne) and ((self.positionC[0]==self.positionJ[0])and (self.positionC[1]==self.positionJ[1])):
            print("bloqué 1")
            return
        elif not (0<=self.positionC[1]+y<self.__NbColone)and ((self.positionC[1]==self.positionJ[1])and (self.positionC[0]==self.positionJ[0])):
            print("bloqué 2")
            return 
        elif ((self.positionJ[0]==self.positionC[0] and self.positionJ[1]==self.positionC[1])or(self.positionJ[1]==self.positionC[1] and self.positionJ[0]==self.positionC[0])):
            self.positionC[0]=self.positionC[0]+x
            self.positionC[1] = self.positionC[1]+y



        lgnC =self.positionC[0] # ligne case
        colC =self.positionC[1] # colonne case
        lgnJ = self.positionJ[0] # ligne joueur
        colJ = self.positionJ[1] # colonne joueur
        lgnM = self.positionM1[0] # ligne mur
        colM = self.positionM1[1] # colonne mur

        print(lgnJ,colJ)
        print(lgnC,colC)
        self.__grid[lgnJ][colJ]=1
        self.__grid[lgnavt][colavt]=0
        self.__grid[lgnC][colC]=2
        self.__grid[lgnM][colM]=3
        self.__view.UpdateView()


