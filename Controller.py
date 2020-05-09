from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QSplashScreen, QMenu, QApplication, QProgressBar
from qtpy import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets

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
from NetworkSetupAdvanced import Ui_NetworkSetupAdvanced
from NewScenario import Ui_NewScenario
from ManageExploits import Ui_ManageExploits
from ManageVulnerablePrograms import Ui_ManageVulnerablePrograms
from EditVm import Ui_EditVM
from CreateNewVm import Ui_CreateNewVm
from VmSystemSettings import Ui_VmSystemSettings
from SuggestedSetup import Ui_Form
from runWindow import Ui_runWindow
from RunVM import Ui_RunVM # MAY 3 #

import os, subprocess
import qtmodern.styles
import qtmodern.windows

import platform, threading

# instantiation of UI (View) classes and controller class

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.manageScenarioBUTTON.clicked.connect(self.hide)
       

        
class RunVMWindow(QtWidgets.QDialog, Ui_RunVM):
    def __init__(self, parent=None):
        super(RunVMWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.vms_checkmarked = []
        self.setupUi(self)
        self.runWindow = RunWindow() 
        self.startBUTTON.clicked.connect(self.send_vm_info)
        self.backBUTTON.clicked.connect(self.close)

    def send_vm_info(self):
        print("Here.")
        self.vms_checkmarked = self.progress()
        running_vms = self.get_running_vms() 

        # MAY 7
        self.vbox_manage_path = self.get_vbox_manage_path()
        for key in running_vms:
            for vm in self.vms_checkmarked:
                if key == vm:
                    QMessageBox.about(self, "Warning", str(key)+" is already running, powering down.")
                    subprocess.Popen([self.vbox_manage_path, 'controlvm', vm, 'poweroff'])
                    return

        if not self.vms_checkmarked:
            msg = "No VM's selected. Please select VM's."
            QMessageBox.about(self, "Warning", msg)
            return

        print(self.vms_checkmarked)
        self.runWindow.set_vm_info(self.vms_checkmarked)
        self.runWindow.show()


# Run collectors functionality
class RunWindow(QtWidgets.QWidget, Ui_runWindow): 
    def __init__(self, parent=None):
        super(RunWindow, self).__init__(parent)
        self.thread_scenarios = {}
        self.vms_proc_ids = {}
        self.t_id_counter = 0
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.okPushBUTTON.clicked.connect(self.okayClicked)
        self.cancelPushBUTTON.clicked.connect(self.close)


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
        self.nextBUTTON.clicked.connect(self.clearLineEdits)
        self.cancelBUTTON.clicked.connect(self.clearLineEdits)
        self.cancelBUTTON.clicked.connect(self.close)
        self.nextBUTTON.clicked.connect(self.close)

    def clearLineEdits(self):
        self.exploitLINEEDIT.setText("")
        self.vulnerableProgramLINEEDIT.setText("")
        self.scenarioLINEEDIT.setText("")
        
class ManageExploitsWindow(QtWidgets.QWidget, Ui_ManageExploits):
    def __init__(self, parent=None):
        super(ManageExploitsWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
        self.nextButton.clicked.connect(self.close)

class AlternateManageExploitsWindow(QtWidgets.QWidget, Ui_ManageExploits):
    def __init__(self, parent=None):
        super(AlternateManageExploitsWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.nextButton.setText(_translate("ManageExploits", "Add"))
        self.backBUTTON.clicked.connect(self.close)
        self.nextButton.clicked.connect(self.addMethod)

    def addMethod(self):
        for item in self.databseTREEWIDGET.findItems("", Qt.MatchContains | Qt.MatchRecursive):
            if (item.checkState(0)==QtCore.Qt.Checked):
                print (item.text(0))

                """lastIndex = CreateNewVmWindow.vmFilesTREEWIDGET.count()
                CreateNewVmWindow.vmFilesTREEWIDGET.addItem(QtWidgets.QListWidgetItem())
                newitem = CreateNewVmWindow.vmFilesTREEWIDGET.item(lastIndex)
                newitem.setText(item.text(0))"""


class ManageVulnerableProgramsWindow(QtWidgets.QWidget,
                                Ui_ManageVulnerablePrograms):
    def __init__(self, parent=None):
        super(ManageVulnerableProgramsWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
        self.nextButton.clicked.connect(self.close)

class SuggestedSetupWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, parent=None):
        self.nav=0
        super(SuggestedSetupWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backButton.clicked.connect(self.close)
        self.nextBUTTON.clicked.connect(self.close)

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
    def __init__(self,text, parent=None):
        super(EditVmWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.discardBUTTON.clicked.connect(self.close)
        self.vmSystemSettings = VmSystemSettings(self)
        self.suggestedSetup = SuggestedSetupWindow()
        self.settingsBUTTON.clicked.connect(self.vmSystemSettings.show)
        self.saveBUTTON.clicked.connect(self.suggestedSetup.refreshSetup)
        #self.manageExploitsBUTTON.clicked.connect(self.alternateManageExploits.show)

class CreateNewVmWindow(QtWidgets.QDialog, Ui_CreateNewVm):
    def __init__(self, parent=None):
        super(CreateNewVmWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.discardBUTTON.clicked.connect(self.close)

class VmSystemSettings(QtWidgets.QDialog, Ui_VmSystemSettings):
    def __init__(self, parent):
        super(VmSystemSettings, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.parentWindow = parent
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
        self.nav=0
        super(NetworkSetupWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backButton.clicked.connect(self.close)

class NetworkSetupAdvancedWindow(QtWidgets.QDialog, Ui_NetworkSetupAdvanced):
    def __init__(self, parent=None):
        super(NetworkSetupAdvancedWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
        self.enableNetworkAdapterCHECKBOX.stateChanged.connect(self.enableNetworkAdapterButtons)
        self.enableNetworkAdapterCHECKBOX_2.stateChanged.connect(self.enableNetworkAdapterButtons)
        self.enableNetworkAdapterCHECKBOX_3.stateChanged.connect(self.enableNetworkAdapterButtons)
        self.enableNetworkAdapterCHECKBOX_4.stateChanged.connect(self.enableNetworkAdapterButtons)
        self.enableAdvancedSettingsCHECK.stateChanged.connect(self.enableAdvancedSettings)
        self.enableAdvancedSettingsCHECK_2.stateChanged.connect(self.enableAdvancedSettings)
        self.enableAdvancedSettingsCHECK_3.stateChanged.connect(self.enableAdvancedSettings)
        self.enableAdvancedSettingsCHECK_4.stateChanged.connect(self.enableAdvancedSettings)

        # shows window whenever an action is taken by the user via the GUI
class Controller:
    def __init__(self):
        self.openingDBWindow = OpeningDBConfigurationWindow()
        self.openingDBWindow.show()
        self.openingDBWindow.connectBUTTON.clicked.connect(self.checkDBConnection)

    def launchAMED(self):
            self.showSplashScreen()
            self.main = MainWindow()
            #self.runVMWindow = RunVMWindow()
            self.progressBar.setValue(1)
            QApplication.processEvents()
            self.progressBar.setValue(2)
            QApplication.processEvents()
            self.manageData = ManageDataWindow()
            self.progressBar.setValue(3)
            QApplication.processEvents()
            self.configureDatabase = ConfigureDatabaseWindow()
            self.progressBar.setValue(4)
            QApplication.processEvents()
            self.manageScenarios = ManageScenariosWindow()
            self.progressBar.setValue(5)
            QApplication.processEvents()
            self.newScenario = NewScenariosWindow()
            self.progressBar.setValue(6)
            QApplication.processEvents()
            self.manageExploits = ManageExploitsWindow()
            self.progressBar.setValue(7)
            QApplication.processEvents()
            self.progressBar.setValue(8)
            QApplication.processEvents()
            self.manageVulnerablePrograms = ManageVulnerableProgramsWindow()
            self.progressBar.setValue(9)
            QApplication.processEvents()
            self.suggestedSetup=SuggestedSetupWindow()
            self.progressBar.setValue(10)
            QApplication.processEvents()
            self.createNewVm = CreateNewVmWindow()
            self.progressBar.setValue(11)
            QApplication.processEvents()
            self.editVm= EditVmWindow("null")
            self.progressBar.setValue(12)
            QApplication.processEvents()
            self.vmSystemSettings = VmSystemSettings(self.editVm)
            self.progressBar.setValue(13)
            QApplication.processEvents()
            self.manageDataOptions=ManageDataOptionsWindow()
            self.progressBar.setValue(14)
            QApplication.processEvents()
            self.importData=ImportDataWindow()
            self.progressBar.setValue(15)
            QApplication.processEvents()
            self.networkSetup=NetworkSetupWindow()
            self.progressBar.setValue(16)
            QApplication.processEvents()
            self.advancedNetworkSetup=NetworkSetupAdvancedWindow()
            self.progressBar.setValue(17)
            QApplication.processEvents()
            self.splash.close()
            #
            self.main.manageDataBUTTON.clicked.connect(self.manageDataOptions.show)
            #self.main.runBUTTON.clicked.connect(self.runVMWindow.show)
            #
            self.main.setupBUTTON.clicked.connect(self.setupButtonNav)
            self.main.configureBUTTON.clicked.connect(self.configureButtonNav)
            #
            self.manageDataOptions.exportBUTTON.clicked.connect(self.manageData.resetTree)
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
            self.manageScenarios.backBUTTON.clicked.connect(self.main.scenarioListCreation)
            #
            self.newScenario.exploitBrowseBUTTON.clicked.connect(self.manageExploits.show)
            self.newScenario.vulnerableProgramBrowseBUTTON.clicked.connect(self.manageVulnerablePrograms.show)
            self.newScenario.cancelBUTTON.clicked.connect(self.manageScenarios.show)
            self.newScenario.nextBUTTON.clicked.connect(self.suggestedSetup.show)
            self.newScenario.nextBUTTON.clicked.connect(self.suggestedSetup.refreshSetup)
            self.newScenario.cancelBUTTON.clicked.connect(self.manageScenarios.setupTree)
            #
            self.manageExploits.backBUTTON.clicked.connect(self.newScenario.show)
            self.manageExploits.nextButton.clicked.connect(self.newScenario.show)
            self.manageExploits.nextButton.clicked.connect(self.newScenario.refreshSetup)
            #
            self.manageVulnerablePrograms.backBUTTON.clicked.connect(self.newScenario.show)
            self.manageVulnerablePrograms.nextButton.clicked.connect(self.newScenario.show)
            self.manageVulnerablePrograms.nextButton.clicked.connect(self.newScenario.refreshSetup)
            #
            self.suggestedSetup.backButton.clicked.connect(self.alternateNavSuggestedSetup)
            self.suggestedSetup.addVmBUTTON.clicked.connect(self.createNewVm.show)
            self.suggestedSetup.nextBUTTON.clicked.connect(self.networkSetup.show)
            self.suggestedSetup.listWidget_2.itemDoubleClicked.connect(self.handleDoubleClick)
            self.suggestedSetup.listWidget_3.itemDoubleClicked.connect(self.handleDoubleClick)
            #
            #
            self.networkSetup.backButton.clicked.connect(self.alternateNavNetworkSetup)
            self.networkSetup.advancedSettingsBUTTON.clicked.connect(self.advancedNetworkSetup.show)
            #
            self.advancedNetworkSetup.backBUTTON.clicked.connect(self.networkSetup.show)
            #
            self.main.show()
            #

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
        # adding progress bar
        self.progressBar = QProgressBar(self.splash)
        self.progressBar.setMaximum(17)
        self.progressBar.setGeometry(0, self.pix.height() - 15, 834, 20)
        self.splash.show()

    def setupButtonNav(self):
        self.suggestedSetup.nav = 1
        self.suggestedSetup.refreshSetup()
        self.suggestedSetup.show()

    def configureButtonNav(self):
        self.networkSetup.nav = 1
        self.networkSetup.show()

    def alternateNavNetworkSetup(self):
        if self.networkSetup.nav == 1:
            self.networkSetup.nav = 0
            self.main.show()
        else:
            self.suggestedSetup.show()

    def alternateNavSuggestedSetup(self):
        if self.suggestedSetup.nav == 1:
            self.suggestedSetup.nav = 0
            self.main.show()
        else:
            self.newScenario.show()

    def handleDoubleClick(self, item):
        item.setSelected(False)
        print(item.text())
        self.editVm.machineNameLINEEDIT.setText(item.text())
        self.editVm.show()

    def checkDBConnection(self):
        self.launchAMED()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.light(app)
    controller = Controller()
    sys.exit(app.exec_())
