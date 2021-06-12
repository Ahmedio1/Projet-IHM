from PyQt5.QtWidgets import QApplication, QWidget, QLayout, QPushButton, QMainWindow, QLabel, QHBoxLayout
from Model.Grid import Grid

class ResetMessage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.message=QMainWindow()
        messageLayout=QWidget()
        self.message.setCentralWidget(messageLayout)
        messageLayout.setFixedSize(300,300)
        messageLabel=QLabel("oscour")
        messageLayout.setLayout(QHBoxLayout(messageLabel))
        yes=QPushButton("yes")
        no=QPushButton("no")
        messageLayout.layout().addWidget(yes)
        messageLayout.layout().addWidget(no)
        yes.clicked.connect(self.yesButton)
        no.clicked.connect(self.noButton)
        self.message.show()
        #pb la fenetre se femre toute seul
        
    
    def yesButton(self):
        Grid.reset()
        self.message.close()

    def noButton(self):
        self.message.close()
