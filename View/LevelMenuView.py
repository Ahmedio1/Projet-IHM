from View.ResetMessage import ResetMessage
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QSound
import sys
from Model.Grid import Grid

class LevelMenuView(QMainWindow):
    def __init__(self, Model, View):
        super().__init__()
        self.__Grid=Model
        self.__GridView=View



        levelWidget=QWidget()
        self.setCentralWidget(levelWidget)
        levelWidget.setLayout(QVBoxLayout())
        levelWidget.setFixedSize(500,500)
        #button1
        self.__button1=QPushButton("level 1")
        self.__button1.setStyleSheet("background-image: url(block/end_stone.png)")
        self.__button1.clicked.connect(lambda x:self.choixLevel(1))
        levelWidget.layout().addWidget(self.__button1)
        #button2
        self.__button2=QPushButton("level 2")
        self.__button2.setStyleSheet("background-image: url(block/end_stone.png)")
        self.__button2.clicked.connect(lambda x:self.choixLevel(2))
        levelWidget.layout().addWidget(self.__button2)
        #button3
        self.__button3=QPushButton("level 3")
        self.__button3.setStyleSheet("background-image: url(block/end_stone.png)")
        self.__button3.clicked.connect(lambda x:self.choixLevel(3))
        levelWidget.layout().addWidget(self.__button3)

        #button reset
        self.__buttonReset=QPushButton("Reset")
        self.__buttonReset.setStyleSheet("background-image: url(block/mycelium_top.png)")
        self.__buttonReset.clicked.connect(ResetMessage)
        levelWidget.layout().addWidget(self.__buttonReset)

        
    def press(self):
        self.__press=True



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

        
    


