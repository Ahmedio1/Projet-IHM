import sys
from PyQt5.QtWidgets import QApplication
from Model.Grid import Grid
from View.GridView import GridView
from Controller.Controle import Controle


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.__model = Grid()
        self.__controller = Controle(self.__model)
        self.__view = GridView(self.__model, self.__controller)
        self.__controller.setView(self.__view)
        self.__model.setView(self.__view)
        self.__view.setWindowTitle("Sokoban")
        self.__view.show()


# Main
if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())