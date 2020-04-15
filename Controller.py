from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QSplashScreen, QMenu

from ConfigureMongoDB import Ui_ConfigureMongoDB
from DBConfiguration import Ui_DBConfiguration
from ImportData import Ui_importData
from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ManageData import Ui_ManageData
from ManageDataOptions import Ui_ManageDataOptions
from ManageScenarios import Ui_ManageScenarios
from NetworkSetup import Ui_NetworkSetup
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
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.manageScenarioBUTTON.clicked.connect(self.hide)
        self.manageDataBUTTON.clicked.connect(self.hide)
        




class ManageDataWindow(QtWidgets.QDialog, Ui_ManageData):
    def __init__(self, parent=None):
        super(ManageDataWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
        self.deleteBUTTON.clicked.connect(self.deleteSelected)


class ManageScenariosWindow(QtWidgets.QDialog, Ui_ManageScenarios):
    def __init__(self, parent=None):
        super(ManageScenariosWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
        self.newBUTTON.clicked.connect(self.hide)


class NewScenariosWindow(QtWidgets.QDialog, Ui_NewScenario):
    def __init__(self, parent=None):
        super(NewScenariosWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.parentDialog = SuggestedSetupWindow(self)
        self.setupUi(self)
        self.exploitBrowseBUTTON.clicked.connect(self.hide)
        self.vulnerableProgramBrowseBUTTON.clicked.connect(self.hide)
        self.cancelBUTTON.clicked.connect(self.close)
        self.nextBUTTON.clicked.connect(self.close)

class ManageExploitsWindow(QtWidgets.QWidget, Ui_ManageExploits):
    def __init__(self, parent=None):
        super(ManageExploitsWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)

class ManageVulnerableProgramsWindow(QtWidgets.QWidget, 
                                Ui_ManageVulnerablePrograms):
    def __init__(self, parent=None):
        super(ManageVulnerableProgramsWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)

class SuggestedSetupWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, parent=None):
        self.editVmWindow = EditVmWindow("null")
        self.vMSystemsSettings=VmSystemSettings()
        super(SuggestedSetupWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backButton.clicked.connect(self.close)
        self.nextBUTTON.clicked.connect(self.close)
        self.listWidget_2.itemDoubleClicked.connect(self.handleDoubleClick)
        self.listWidget_3.itemDoubleClicked.connect(self.handleDoubleClick)

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        infoAct = cmenu.addAction("Info")
        removeAct = cmenu.addAction("Remove")

        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == removeAct:
            self.removeSelectedItem()
        if action == infoAct:
            print("launch info window")
            #Line where  VM Details Window will open with VM id being passed

#method responsible for removing an element from the PoV and Victim Lists
    def removeSelectedItem(self):
        listItems = self.listWidget_2.selectedItems() + self.listWidget_3.selectedItems()
        if not listItems: return
        for item in listItems:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget_3.takeItem(self.listWidget_3.row(item))

    def handleDoubleClick(self, item):
        item.setSelected(False)
        print(item.text())
        self.editVm = EditVmWindow(item.text())
        self.editVm.settingsBUTTON.clicked.connect(self.vMSystemsSettings.show)
        self.editVm.show()

            
class EditVmWindow(QtWidgets.QDialog, Ui_EditVM):
    def __init__(self, text,parent=None):
        super(EditVmWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.machineNameLINEEDIT.setText(text)
        self.discardBUTTON.clicked.connect(self.close)
        
class CreateNewVmWindow(QtWidgets.QDialog, Ui_CreateNewVm):
    def __init__(self, parent=None):
        super(CreateNewVmWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.discardBUTTON.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.vmFilesLISTWIDGET.clear()
        self.close()
        
class VmSystemSettings(QtWidgets.QDialog, Ui_VmSystemSettings):
    def __init__(self, parent=None):
        super(VmSystemSettings, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.cancelBUTTON.clicked.connect(self.close)

class ManageDataOptionsWindow(QtWidgets.QDialog, Ui_ManageDataOptions):
    def __init__(self, parent=None):
        super(ManageDataOptionsWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
        self.exportBUTTON.clicked.connect(self.close)
        self.importBUTTON.clicked.connect(self.close)

class ImportDataWindow(QtWidgets.QDialog, Ui_importData):
    def __init__(self, parent=None):
        super(ImportDataWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)
   
class ConfigureDatabaseWindow(QtWidgets.QDialog, Ui_ConfigureMongoDB):
    def __init__(self, parent=None):
        super(ConfigureDatabaseWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
       
class OpeningDBConfigurationWindow(QtWidgets.QDialog, Ui_DBConfiguration):
    def __init__(self, parent=None):
        super(OpeningDBConfigurationWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.closeBUTTON.clicked.connect(self.close)
        self.connectBUTTON.clicked.connect(self.close)

class NetworkSetupWindow(QtWidgets.QDialog, Ui_NetworkSetup):
    def __init__(self, parent=None):
        super(NetworkSetupWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backButton.clicked.connect(self.close)


        # shows window whenever an action is taken by the user via the GUI
class Controller:
    def __init__(self):
        self.showSplashScreen()
        self.main = MainWindow()
        self.openingDBConfiguration = OpeningDBConfigurationWindow()
        self.manageData = ManageDataWindow()
        self.configureDatabase = ConfigureDatabaseWindow()
        self.manageScenarios = ManageScenariosWindow()
        self.newScenario = NewScenariosWindow()
        self.manageExploits = ManageExploitsWindow()
        self.manageVulnerablePrograms = ManageVulnerableProgramsWindow()
        self.suggestedSetup=SuggestedSetupWindow()
        self.createNewVm = CreateNewVmWindow()
        self.vmSystemSettings = VmSystemSettings()
        self.editVm= EditVmWindow("null")
        self.manageDataOptions=ManageDataOptionsWindow()
        self.importData=ImportDataWindow()
        self.networkSetup=NetworkSetupWindow()
        self.splash.close()
        #
        self.openingDBConfiguration.connectBUTTON.clicked.connect(self.main.show)
        #
        self.main.manageDataBUTTON.clicked.connect(self.manageDataOptions.show)
        #
        self.main.setupBUTTON.clicked.connect(self.suggestedSetup.show)
        self.main.configureBUTTON.clicked.connect(self.networkSetup.show)
        #
        self.manageDataOptions.exportBUTTON.clicked.connect(self.manageData.show)
        self.manageDataOptions.importBUTTON.clicked.connect(self.importData.show)
        self.manageDataOptions.backBUTTON.clicked.connect(self.main.show)
        #
        self.main.configureDatabaseBUTTON.clicked.connect(self.configureDatabase.show)
        self.configureDatabase.backBUTTON.clicked.connect(self.main.show)
        #
        self.main.manageScenarioBUTTON.clicked.connect(self.manageScenarios.show)
        #
        self.manageData.backBUTTON.clicked.connect(self.main.show)
        #
        self.importData.pushButton_2.clicked.connect(self.main.show)
        #
        self.manageScenarios.backBUTTON.clicked.connect(self.main.show)
        self.manageScenarios.newBUTTON.clicked.connect(self.newScenario.show)
        #
        self.newScenario.exploitBrowseBUTTON.clicked.connect(self.manageExploits.show)
        self.newScenario.vulnerableProgramBrowseBUTTON.clicked.connect(self.manageVulnerablePrograms.show)
        self.newScenario.cancelBUTTON.clicked.connect(self.manageScenarios.show)
        self.newScenario.nextBUTTON.clicked.connect(self.suggestedSetup.show)
        #
        self.manageExploits.backBUTTON.clicked.connect(self.newScenario.show)
        #
        self.manageVulnerablePrograms.backBUTTON.clicked.connect(self.newScenario.show)
        #
        self.suggestedSetup.backButton.clicked.connect(self.newScenario.show)
        self.suggestedSetup.addVmBUTTON.clicked.connect(self.createNewVm.show)
        self.suggestedSetup.nextBUTTON.clicked.connect(self.networkSetup.show)
        #
        self.networkSetup.backButton.clicked.connect(self.suggestedSetup.show)
        #
        # Functionality for "Run" button (interval-based collection/
        # proof of concept)
        self.main.runBUTTON.clicked.connect(self.runCollectors)
        #

        #
        self.openingDBConfiguration.show()
        
        
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
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())


