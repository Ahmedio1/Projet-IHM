from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Model.Grid import Grid
from View.GridView import GridView

class Controle(QWidget):
    def __init__(self,model):
        super().__init__()
        self.__model=model
        self.__view=None

    def setView(self,view):
        self.__view=view

    def keyPressEvent(self,event):
        if event.key()==16777234:
            print("gauche")
            self.__model.deplacerJo(0,-1)
        if event.key()==16777235:
            print("haut")
            self.__model.deplacerJo(-1,0)
        if event.key()==16777236:
            print("droite")
            self.__model.deplacerJo(0,1)
        if event.key()==16777237:
            print("bas")
            self.__model.deplacerJo(1,0)