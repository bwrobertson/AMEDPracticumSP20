from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QSplashScreen, QMenu

from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ManageData import Ui_ManageData
from ManageScenarios import Ui_ManageScenarios
from NewScenario import Ui_NewScenario
from ManageExploits import Ui_ManageExploits
from ManageVulnerablePrograms import Ui_ManageVulnerablePrograms
from EditVm import Ui_EditVM
from CreateNewVm import Ui_CreateNewVm
from VmSystemSettings import Ui_VmSystemSettings
from SuggestedSetup import Ui_Form

import os, subprocess

# instantiation of UI (View) classes and controller class

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.manageDataBUTTON.clicked.connect(self.hide)
        self.manageScenarioBUTTON.clicked.connect(self.hide)


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
        self.parentDialog = SuggestedSetupWindow(self)
        self.setupUi(self)
        self.exploitBrowseBUTTON.clicked.connect(self.hide)
        self.vulnerableProgramBrowseBUTTON.clicked.connect(self.hide)
        self.cancelBUTTON.clicked.connect(self.close)
        self.nextBUTTON.clicked.connect(self.close)

class ManageExploitsWindow(QtWidgets.QWidget, Ui_ManageExploits):
    def __init__(self, parent=None):
        super(ManageExploitsWindow, self).__init__(parent)
        self.setupUi(self)
        # set num of rows to the actual length of the vuln programs list
        self.exploitTABLEWIDGET.setRowCount(len(self.getExploitsList())) # FIXME 
        self.selectBUTTON.clicked.connect(self.close)
        self.fillTable()
        self.formatTable()
        self.exploitTABLEWIDGET.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.parentDialog = NewScenariosWindow(self)
        self.browseFilesBUTTON.clicked.connect(self.exploitBrowser)
    
    def formatTable(self):
        font = QFont()
        font.setPointSize(13)
        self.exploitTABLEWIDGET.setFont(font)
        self.exploitTABLEWIDGET.horizontalHeader().setStyleSheet("QHeaderView { font-size:  16pt};")
        header = self.exploitTABLEWIDGET.horizontalHeader()      
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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
        self.formatTable()
        self.exploitTABLEWIDGET.setSelectionBehavior(QtWidgets.QTableView.SelectRows)        
        self.parentDialog = NewScenariosWindow(self)
        self.browseFilesBUTTON.clicked.connect(self.vulnerableProgramBrowser)

    def formatTable(self):
        font = QFont()
        font.setPointSize(13)
        self.exploitTABLEWIDGET.setFont(font)
        self.exploitTABLEWIDGET.horizontalHeader().setStyleSheet("QHeaderView { font-size:  16pt};")
        header = self.exploitTABLEWIDGET.horizontalHeader()      
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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

class SuggestedSetupWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(SuggestedSetupWindow, self).__init__(parent)
        self.setupUi(self)
        self.backButton.clicked.connect(self.close)
        
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        removeAct = cmenu.addAction("Remove")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == removeAct:
          self.removeSelectedItem()

#method responsible for removing an element from the PoV and Victim Lists
    def removeSelectedItem(self):
        listItems = self.listWidget_2.selectedItems() + self.listWidget_3.selectedItems()
        if not listItems: return
        for item in listItems:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget_3.takeItem(self.listWidget_3.row(item))
        
class EditVmWindow(QtWidgets.QDialog, Ui_EditVM):
    def __init__(self, text,parent=None):
        super(EditVmWindow, self).__init__(parent)
        self.setupUi(self)
        self.machineNameLINEEDIT.setText(text)
        self.discardBUTTON.clicked.connect(self.close)
        
class CreateNewVmWindow(QtWidgets.QDialog, Ui_CreateNewVm):
    def __init__(self, parent=None):
        super(CreateNewVmWindow, self).__init__(parent)
        self.setupUi(self)
        self.discardBUTTON.clicked.connect(self.close)
        
class VmSystemSettings(QtWidgets.QDialog, Ui_VmSystemSettings):
    def __init__(self, parent=None):
        super(VmSystemSettings, self).__init__(parent)
        self.setupUi(self)
        self.cancelBUTTON.clicked.connect(self.close)


# shows window whenever an action is taken by the user via the GUI
class Controller:
    def __init__(self):
        self.showSplashScreen()
        self.main = MainWindow()
        self.manageData = ManageDataWindow()
        self.manageScenarios = ManageScenariosWindow()
        self.newScenario = NewScenariosWindow()
        self.manageExploits = ManageExploitsWindow()
        self.manageVulnerablePrograms = ManageVulnerableProgramsWindow()
        self.suggestedSetup=SuggestedSetupWindow()
        self.createNewVm = CreateNewVmWindow()
        self.vmSystemSettings = VmSystemSettings()
        self.editVm= EditVmWindow("null")
        self.splash.close()
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
        self.newScenario.nextBUTTON.clicked.connect(self.suggestedSetup.show)
        #
        self.manageExploits.selectBUTTON.clicked.connect(self.newScenario.show)
        #
        self.manageVulnerablePrograms.selectBUTTON.clicked.connect(self.newScenario.show)
        #
        self.suggestedSetup.backButton.clicked.connect(self.newScenario.show)
        self.suggestedSetup.createVmBUTTON.clicked.connect(self.createNewVm.show)
        self.suggestedSetup.listWidget_2.itemDoubleClicked.connect(self.handleDoubleClick)
        self.suggestedSetup.listWidget_3.itemDoubleClicked.connect(self.handleDoubleClick)
        
        # Functionality for "Run" button (interval-based collection/
        # proof of concept)
        self.main.runBUTTON.clicked.connect(self.runCollectors)
        
        #
        self.main.show()
        
        
     # Run collectors method for an interval of 5 seconds       
    def runCollectors(self):
        
        # Functionality on supported on Windows, need other collectors for that
        operating_system = os.getcwd()
        if "C:\\" in operating_system:
            msg = QMessageBox.about(self.main, "Warning", "Windows operating system not supported on collectors, yet.")
        else:
            
            # Controller.py must be ran in root (i.e. $ sudo su, on Linux)
            uid = os.getuid()
            if uid != 0:
                msg = QMessageBox.about(self.main, "Warning", "Collectors must be ran with root privileges.")
            else:
                proc = subprocess.Popen(["python", "ecel/start_stop_collectors.py"])
                msg = QMessageBox.about(self.main, "Notice", "Collectors have started!")
                # Need to add functionality to let Dr. Acosta 
                # know when collectors are done (signal w/ messagebox)   
        
    def showSplashScreen(self):
        self.pix = QPixmap("SplashPage.png")
        self.splash = QSplashScreen(self.pix, Qt.WindowStaysOnTopHint)
        self.splash.show()
        
    def handleDoubleClick(self, item):
        item.setSelected(False)
        print(item.text())
        self.editVm = EditVmWindow(item.text())
        self.editVm.settingsBUTTON.clicked.connect(self.vmSystemSettings.show)
        self.editVm.show()
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())

