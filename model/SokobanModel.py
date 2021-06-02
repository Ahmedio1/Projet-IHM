import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import *

class SokobanModel:
    def __init__(self):
        self.__compteur=0
        self.__x=1
        self.__y=1
        self.__position=[x][y]
    
    def Compteur(self,event):
        if event.key()-16777234==0 or 1 or 2 or 3:
            self.__compteur+=1
    """
    compteur tout simple qui ne s'implémente seulement si une flèche directionel est pressé
    """
            
    def Position (self,event):
        if (event.key()-16777234==0):
            if y-1>1:                  """ ici remplacer les 1, on fera un tableau avec les cases qui représente le mur et il ne faut pas qu'il rentre dedans"""
                y-=1
                position=[x][y]
            print("gauche")
        elif (event.key()-16777234==1):
            if x-1>1:
                x-=1
                position=[x][y]
            print("haut")
        elif (event.key()-16777234==2):
            if y+1>9:
                y+=1
                position=[x][y]
            print("droite")
        elif (event.key()-16777234==3):
            if x+1>9:
                x+=1
                position=[x][y]
            print("bas")
        
        