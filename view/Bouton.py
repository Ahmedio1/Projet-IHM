from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class NumHorloge(QLabel):
    def __init__(self):
        """
        TODO
        """

        super().__init__()

        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setFont(QFont('Coups', 40))

        self.setStyleSheet(
            "border: 3px solid black;color: blue; background-color: white")
        self.setText("0")

        self.__model = None

    def setModel(self, model):
        self.__model = model

    def maj(self):
        """
        TODO
        """
        currentTime = 0
        if self.__model is not None:
            currentTime = self.__model.elapsed()

        dixieme = str((currentTime // 10) % 100)
        seconds = str((currentTime // 1000) % 60)
        minutes = str((currentTime // 1000 // 60) % 60)

        self.setText(minutes.zfill(2) + ":" +
                     seconds.zfill(2) + ":" +
                     dixieme.zfill(2))

    def paintEvent(self, event):
        """
        TODO
        """
        self.maj()
        super().paintEvent(event)

