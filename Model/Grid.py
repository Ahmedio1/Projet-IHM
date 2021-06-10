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
        #du joueur
        self.__xJ=3
        self.__yJ=6
        self.positionJ=[self.__xJ,self.__yJ]
        self.generateMap1()


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

    def generateMap1(self):
        for i in range (len(self.__grid)): #entourage de la map avec des murs
            self.__grid[i][0]=3
            self.__grid[0][i]=3
            self.__grid[i][9]=3
            self.__grid[9][i]=3
        self.__grid[7][7]=4 #placement d'un trou
        self.__grid[5][4]=3
        self.__grid[2][2]=2 #placement d'une caisse
        self.__grid[7][2]=2



    def deplacerCai(self,x,y):
        #test que la caisse ne vas pas dans un mur
        for i in range (len(self.__grid)):
            for j in range (len(self.__grid[i])): #parcours chaque case
                if (self.__grid[i][j]==2): #si c'est une caisse
                    if (self.__grid[i+x][j+y]==2 or self.__grid[i+x][j+y]==3 or self.__grid[i+x][j+y]==5): #test la case vers laquelle on veut aller est un mur/autre caisse/trou rempli
                        return #ne se deplace pas

        #Caisse
        #test que la caisse ne sorte pas de la map
        for i in range (len(self.__grid)):
            for j in range (len(self.__grid[i])): #parcours chaque case
                if (self.__grid[i][j]==2): #si c'est une caisse
                    if not (0<=i+x<self.__NbLigne) and ((i==self.positionJ[0])and (j==self.positionJ[1])):
                        print("bloqué 1")
                        return
                    elif not (0<=j+y<self.__NbColone)and ((j==self.positionJ[1])and (i==self.positionJ[0])):
                        print("bloqué 2")
                        return
                    elif (self.positionJ[0]==i and self.positionJ[1]==j): #test que la caisse a le droit de se déplacer
                        if (self.__grid[i+x][j+y]==4): #test de deplacement dans le trou
                            self.__grid[i+x][j+y]=5  #la case prend l'etat 5 correspondant a une caisse dans un trou
                        else:
                            self.__grid[i+x][j+y]=2 #la nouvelle case devient une caisse



        
        



    def deplacerJo(self,x,y):
        
        # Mur
        for i in range (len(self.__grid)):
            for j in range (len(self.__grid[i])): 
                if (self.__grid[i][j]==3 or self.__grid[i][j]==4 or self.__grid[i][j]==5): #pour chaque case check si il s'agit d'un mur ou d'un trou (vide ou pas)
                    if (self.positionJ[0]+x == i) and (self.positionJ[1]==j):
                        return
                    if (self.positionJ[0] == i) and (self.positionJ[1]+y ==j):
                        return
        
        #Joueur
        for i in range (len(self.__grid)):
            for j in range (len(self.__grid[i])): #parcours chaque case
                if (self.__grid[i][j]==2): #si c'est une caisse
                    #test que qu'on n'essaye pas de faire sortir une caisse de la map
                    if ((i==0) and ((i==self.positionJ[0]+x)and(j==self.positionJ[1]))):
                        print("bloqué 1.5")
                        self.positionJ[0] = 1
                        return 
                    elif ((i==self.__NbLigne-1) and ((i==self.positionJ[0]+x)and(j==self.positionJ[1]))):
                        print("bloqué 1.6")
                        self.positionJ[0]=self.__NbLigne-2
                        return
                    elif ((j==0) and ((j==self.positionJ[1]+y)and(i==self.positionJ[0]))):
                        print("bloqué 1.3")
                        self.positionJ[1] = 1
                        return 
                    elif ((j==self.__NbColone-1) and ((j==self.positionJ[1]+y)and(i==self.positionJ[0]))):
                        print("bloqué 1.4")
                        self.positionJ[1]=self.__NbColone-2
                        return
                    #test si il y a une caisse puis un mur ou un trourempli  la ou le joueur se deplace
                    elif (((i==self.positionJ[0]+x)and(j==self.positionJ[1]+y)) and (self.__grid[self.positionJ[0]+2*x][self.positionJ[1]+2*y]==3 or self.__grid[self.positionJ[0]+2*x][self.positionJ[1]+2*y]==5)):
                        return

        if not (0<=self.positionJ[0]+x<self.__NbLigne):
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

        self.deplacerCai(x,y)
        lgnJ = self.positionJ[0] # ligne joueur
        colJ = self.positionJ[1] # colonne joueur
        self.__grid[lgnJ][colJ]=1
        self.__grid[lgnavt][colavt]=0
        self.__view.UpdateView()

