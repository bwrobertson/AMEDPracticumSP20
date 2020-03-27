from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
from ManageData import Ui_ManageData
from ManageScenarios import Ui_ManageScenarios
from NewScenario import Ui_NewScenario
from ManageExploits import Ui_ManageExploits
from ManageVulnerablePrograms import Ui_ManageVulnerablePrograms

# instantiation of UI (View) classes and controller class

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.manageDataBUTTON.clicked.connect(self.hide)
        self.manageScenarioBUTTON.clicked.connect(self.hide)
        self.runBUTTON.clicked.connect(self.hide)


class ManageDataWindow(QtWidgets.QDialog, Ui_ManageData):
    def __init__(self, parent=None):
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
        self.exploitBrowseBUTTON.clicked.connect(self.hide)
        self.vulnerableProgramBrowseBUTTON.clicked.connect(self.hide)
        self.cancelBUTTON.clicked.connect(self.close)

class ManageExploitsWindow(QtWidgets.QWidget, Ui_ManageExploits):
    def __init__(self, parent=None):
        super(ManageExploitsWindow, self).__init__(parent)
        self.setupUi(self)
        # set num of rows to the actual length of the vuln programs list
        self.exploitTABLEWIDGET.setRowCount(len(self.getExploitsList())) # FIXME 
        self.selectBUTTON.clicked.connect(self.close)
        self.fillTable()

    def getExploitsList(self):
        # dummy objects
        ex1 = {'name': "Cross-Site Request Forgery", "type": "WebApps", "platform": "PHP"}
        ex2 = {"name": "CSV Injection", "type": "WebApps", "platform": "Windows"}
        ex3 = {"name": "ex1", "type": "SQL Inj", "platform": ""}
        lst = [ex1, ex2, ex3]
        return lst

    def fillTable(self):
        itemsList = self.getExploitsList()
        num_rows = len(itemsList)
        for row in range(num_rows):
            self.exploitTABLEWIDGET.setItem(row, 0, QtWidgets.QTableWidgetItem(itemsList[row]["name"]))
            self.exploitTABLEWIDGET.setItem(row, 1, QtWidgets.QTableWidgetItem(itemsList[row]["type"]))
            self.exploitTABLEWIDGET.setItem(row, 2, QtWidgets.QTableWidgetItem(itemsList[row]["platform"]))

class ManageVulnerableProgramsWindow(QtWidgets.QWidget, 
                                Ui_ManageVulnerablePrograms):
    def __init__(self, parent=None):
        super(ManageVulnerableProgramsWindow, self).__init__(parent)
        self.setupUi(self)
        # set num of rows to the actual length of the vuln programs list
        self.exploitTABLEWIDGET.setRowCount(len(self.getItemsList())) # FIXME 
        self.selectBUTTON.clicked.connect(self.close)
        self.fillTable()

    # TODO function to get vulnerable programs from exploitDB or stored locally 
    def getItemsList(self):
        # dummy objects
        pr1 = {'name': "p0", "type": "WebApps", "platform": "PHP"}
        pr2 = {"name": "p1", "type": "Local", "platform": "Hardware"}
        pr3 = {"name": "Microsoft Word", "type": "WebApps", "platform": "Windows"}
        lst = [pr1, pr2, pr3]
        return lst

    # function to fill table with content from exploitDB or locally saved vulnerable programs
    def fillTable(self):
        itemList = self.getItemsList()
        num_rows = len(itemList)
        for row in range(num_rows):
            self.exploitTABLEWIDGET.setItem(row, 0, QtWidgets.QTableWidgetItem(itemList[row]["name"]))
            self.exploitTABLEWIDGET.setItem(row, 1, QtWidgets.QTableWidgetItem(itemList[row]["type"]))
            self.exploitTABLEWIDGET.setItem(row, 2, QtWidgets.QTableWidgetItem(itemList[row]["platform"]))

# shows window whenever an action is taken by the user via the GUI
class Controller:
    def __init__(self):
        self.main = MainWindow()
        self.manageData = ManageDataWindow()
        self.manageScenarios = ManageScenariosWindow()
        self.newScenario = NewScenariosWindow()
        self.manageExploits = ManageExploitsWindow()
        self.manageVulnerablePrograms = ManageVulnerableProgramsWindow()
        #
        self.main.manageDataBUTTON.clicked.connect(self.manageData.show)
        self.main.manageScenarioBUTTON.clicked.connect(self.manageScenarios.show)
        #
        self.manageData.backBUTTON.clicked.connect(self.main.show)
        #
        self.manageScenarios.backBUTTON.clicked.connect(self.main.show)
        self.manageScenarios.newBUTTON.clicked.connect(self.newScenario.show)
        #
        self.newScenario.exploitBrowseBUTTON.clicked.connect(self.manageExploits.show)
        self.newScenario.vulnerableProgramBrowseBUTTON.clicked.connect(self.manageVulnerablePrograms.show)
        self.newScenario.cancelBUTTON.clicked.connect(self.manageScenarios.show)
        #
        self.manageExploits.selectBUTTON.clicked.connect(self.newScenario.show)
        #
        self.manageVulnerablePrograms.selectBUTTON.clicked.connect(self.newScenario.show)
        #
        self.main.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())
