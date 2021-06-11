from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Model import *

class LevelMenuView(QMainWindow):
    def __init__(self):
        super().__init__()
        levelWidget=QWidget()
        self.setCentralWidget(levelWidget)
        levelWidget.setLayout(QVBoxLayout)
        button1=QPushButton()
        button1.clicked.connect(self.choixLevel1)
        levelWidget.layout().addWidget(button1)

    def choixLevel1(self):
        print("level1")


