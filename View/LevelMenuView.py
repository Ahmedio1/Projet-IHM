from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Model import *
from Model.Grid import Grid

class LevelMenuView(QMainWindow):
    def __init__(self, Model, View):
        super().__init__()
        self.__Grid=Model
        self.__GridView=View

        levelWidget=QWidget()
        self.setCentralWidget(levelWidget)
        levelWidget.setLayout(QVBoxLayout())
        #button1
        self.__button1=QPushButton()
        self.__button1.clicked.connect(lambda x:self.choixLevel(1))
        levelWidget.layout().addWidget(self.__button1)
        #button2
        self.__button2=QPushButton()
        self.__button2.clicked.connect(lambda x:self.choixLevel(2))
        levelWidget.layout().addWidget(self.__button2)
        #button3
        self.__button3=QPushButton()
        self.__button3.clicked.connect(lambda x:self.choixLevel(3))
        levelWidget.layout().addWidget(self.__button3)

    def choixLevel(self,numLevel):
        if numLevel==1:
            if self.__Grid.getLevel()[0]:
                self.close()
                self.__GridView.show()
        elif numLevel==2:
            if self.__Grid.getLevel()[1]:
                self.close()
                self.__GridView.show()
        elif numLevel==3:
            if self.__Grid.getLevel()[2]:
                self.close()
                self.__GridView.show()
        
    


