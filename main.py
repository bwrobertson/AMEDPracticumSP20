from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
from ManageData import Ui_ManageData
from ManageScenarios import Ui_ManageScenarios
from NewScenario import Ui_NewScenario


# instantiation of UI (View) classes and controller class

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.manageDataBUTTON.clicked.connect(self.hide)
        self.manageScenarioBUTTON.clicked.connect(self.hide)
        self.runBUTTON.clicked.connect(self.hide)


class ManageDataWindow(QtWidgets.QDialog, Ui_ManageData):
    def __init__(self, parent):
        super(ManageDataWindow, self).__init__(parent)
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)


class ManageScenariosWindow(QtWidgets.QDialog, Ui_ManageScenarios):
    def __init__(self, parent=None):
        super(ManageScenariosWindow, self).__init__(parent)
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
        self.newBUTTON.clicked.connect(self.hide)


class NewScenariosWindow(QtWidgets.QDialog, Ui_NewScenario):
    def __init__(self, parent=None):
        super(NewScenariosWindow, self).__init__(parent)
        self.setupUi(self)
        self.cancelBUTTON.clicked.connect(self.close)


# shows window whenever an action is taken by the user via the GUI
class Controller:
    def __init__(self):
        self.main = MainWindow()
        self.manageData = ManageDataWindow(self.main)
        self.manageScenarios = ManageScenariosWindow()
        self.newScenario = NewScenariosWindow()
        self.main.manageDataBUTTON.clicked.connect(self.manageData.show)
        self.main.manageScenarioBUTTON.clicked.connect(self.manageScenarios.show)
        self.manageData.backBUTTON.clicked.connect(self.main.show)
        self.manageScenarios.backBUTTON.clicked.connect(self.main.show)
        self.manageScenarios.newBUTTON.clicked.connect(self.newScenario.show)
        self.newScenario.cancelBUTTON.clicked.connect(self.manageScenarios.show)
        self.main.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())
