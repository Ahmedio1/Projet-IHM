from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from View.GridView import GridView
from os import walk

class Grid():

    def __init__(self):
        self.__fichier=None
        self.__Taille=64
        self.__NbLigne=12
        self.__NbColone=12
        self.__grid=[]
        self.__view=None
        self.__controle=None
        #joueur
        self.__xJ=None
        self.__yJ=None
        self.positionJ=None

        #victoire
        self.__win=False

        #level
        self.__levelActu=None
        self.__level1=True
        self.__level2=False
        self.__level3=False
        self.choixLevel()
        self.chargeLevel()

        #nombre de pas
        self.__nbPas=0

    def getLevel(self):
        return [self.__level1, self.__level2, self.__level3]


    def getNbLigne(self):
        return self.__NbLigne

    def getNbColone(self):
        return self.__NbColone

    def setView(self,view):
        self.__view=view

    def getGrid(self):
        return self.__grid
    
    def getNbPas(self):
        return self.__nbPas

    def generateGrid(self):
        self.__grid=[]
        for i in range (self.__NbLigne):
            self.__grid.append([])
            for j in range (self.__NbColone):
                self.__grid[i].append(0)
    

    def getTaille(self):
        return self.__Taille

    def setControle(self,controle):
        self.__controle=controle
    
    def chargeLevel(self):
        if self.__level3:
            self.generateMap3()
        elif self.__level2:
            self.generateMap2()
        elif self.__level1:
            self.generateMap1()

    def generateMap1(self):
        self.generateGrid()
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        with open("Level/"+fileLevel[2][0], "r") as file: #ouvre le ficher et le ferme a la sortie
            for i in range (self.__NbLigne):
                line=file.readline()
                line=line.split("\n") #retire le \n
                line=line[0].split(",") #transform la chaine en tableau de charatere
                self.__grid[i]=line
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                self.__grid[i][j]=int(self.__grid[i][j]) #transformation des string en int
                if self.__grid[i][j]==1: #si il s'agit d'un joueur
                    self.__xJ=i #initialise les coo du joueurs
                    self.__yJ=j
                    self.positionJ=[self.__xJ,self.__yJ]

        
    def generateMap2(self):
        self.generateGrid()
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        with open("Level/"+fileLevel[2][1], "r") as file: #ouvre le ficher et le ferme a la sortie
            for i in range (self.__NbLigne):
                line=file.readline()
                line=line.split("\n")
                line=line[0].split(",")
                self.__grid[i]=line
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                self.__grid[i][j]=int(self.__grid[i][j]) #transformation des string en int
                if self.__grid[i][j]==1:
                    self.__xJ=i
                    self.__yJ=j
                    self.positionJ=[self.__xJ,self.__yJ]
    
    def generateMap3(self):
        self.generateGrid()
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        with open("Level/"+fileLevel[2][2], "r") as file: #ouvre le ficher et le ferme a la sortie
            for i in range (self.__NbLigne):
                line=file.readline()
                line=line.split("\n")
                line=line[0].split(",")
                self.__grid[i]=line
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                self.__grid[i][j]=int(self.__grid[i][j]) #transformation des string en int
                if self.__grid[i][j]==1:
                    self.__xJ=i
                    self.__yJ=j
                    self.positionJ=[self.__xJ,self.__yJ]
    
    def choixLevel(self):
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        with open("Level/"+fileLevel[2][3], "r") as file: #ouvre le ficher et le ferme a la sortie
            line=file.readline() #lie une ligne
            ligne=0
            while line!="": #tant qu'il ya a des lignes
                if line=='True\n':
                    if ligne==0:
                        self.__level1=True
                        self.__levelActu=1
                    elif ligne==1:
                        self.__level2=True
                        self.__levelActu=2
                    elif ligne==2:
                        self.__level3=True
                        self.__levelActu=3
                line=file.readline()
                ligne+=1

    

    def verifWin(self):
        for i in range (len(self.__grid)):
            for j in range (len(self.__grid[i])): #parcours chaque case
                if (self.__grid[i][j]==4):
                    return
        self.__win=True
        self.prochainLevel()

    def prochainLevel(self):
        self.__levelActu+=1
        if self.__levelActu==2:
            self.__level2=True
        elif self.__levelActu==3:
            self.__level3=True
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        file=open("Level/"+fileLevel[2][3],"w") #ouvre le ficher
        if self.__level1:
            file.write("True\n") #rentre true pour le level1 (celui ci doit tjr etre a True)
        file.close()
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        file=open("Level/"+fileLevel[2][3], "a") #ouvre le ficher
        if  self.__level2: #si on peut passer au level 2
            file.write("True\n") #le level 2 est accessible
        if  self.__level3: #si on peut passer au level 3
            file.write("True\n") #le level 3 est accessible
        file.close()
        if self.__levelActu>=4:
            self.reset()
        

    def reset(self):
        self.__level2=False
        self.__level3=False
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        file=open("Level/"+fileLevel[2][3],"w") #ouvre le ficher
        file.write("True\n"+"False\n"+"False\n") #reset le fichier mets tous les niveaux a false sauf le 1



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
                            self.verifWin()
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
                    elif (((i==self.positionJ[0]+x)and(j==self.positionJ[1]+y)) and (self.__grid[self.positionJ[0]+2*x][self.positionJ[1]+2*y]==3 or self.__grid[self.positionJ[0]+2*x][self.positionJ[1]+2*y]==5 or self.__grid[self.positionJ[0]+2*x][self.positionJ[1]+2*y]==2)):
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
            self.__nbPas+=1

        self.deplacerCai(x,y)
        lgnJ = self.positionJ[0] # ligne joueur
        colJ = self.positionJ[1] # colonne joueur
        self.__grid[lgnJ][colJ]=1
        self.__grid[lgnavt][colavt]=0
        self.__view.UpdateView()

