from CreateNewVm import Ui_CreateNewVm
from VmSystemSettings import Ui_VmSystemSettings
from SuggestedSetup import Ui_Form
from runWindow import Ui_runWindow

import os, subprocess
import qtmodern.styles
@@ -36,20 +35,9 @@ def __init__(self, parent=None):
        self.setupUi(self)
        self.manageScenarioBUTTON.clicked.connect(self.hide)
        self.manageDataBUTTON.clicked.connect(self.hide)


class RunWindow(QtWidgets.QWidget, Ui_runWindow):
    def __init__(self, parent=None):
        super(RunWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.okPushBUTTON.clicked.connect(self.okayClicked)
        self.cancelPushBUTTON.clicked.connect(self.close)

    def okayClicked(self):
        ###### use the pollowing line  minus the print() to retrieve the value that is curerntly inside the spinbox
        print(self.intervalSPINBOX.value())
        print("Kevin method for Run")



class ManageDataWindow(QtWidgets.QDialog, Ui_ManageData):
@@ -87,7 +75,7 @@ def __init__(self, parent=None):
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backBUTTON.clicked.connect(self.close)
     

class AlternateManageExploitsWindow(QtWidgets.QWidget, Ui_ManageExploits):
    def __init__(self, parent=None):
        super(AlternateManageExploitsWindow, self).__init__(parent)
@@ -102,14 +90,14 @@ def addMethod(self):
        for item in self.databseTREEWIDGET.findItems("", Qt.MatchContains | Qt.MatchRecursive):
            if (item.checkState(0)==QtCore.Qt.Checked):
                print (item.text(0))
                

                """lastIndex = CreateNewVmWindow.vmFilesTREEWIDGET.count()
                CreateNewVmWindow.vmFilesTREEWIDGET.addItem(QtWidgets.QListWidgetItem())
                newitem = CreateNewVmWindow.vmFilesTREEWIDGET.item(lastIndex)
                newitem.setText(item.text(0))"""


class ManageVulnerableProgramsWindow(QtWidgets.QWidget, 
class ManageVulnerableProgramsWindow(QtWidgets.QWidget,
                                Ui_ManageVulnerablePrograms):
    def __init__(self, parent=None):
        super(ManageVulnerableProgramsWindow, self).__init__(parent)
@@ -127,7 +115,7 @@ def __init__(self, parent=None):
        self.setupUi(self)
        self.backButton.clicked.connect(self.close)
        self.nextBUTTON.clicked.connect(self.close)
 

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        infoAct = cmenu.addAction("Info")
@@ -148,7 +136,7 @@ def removeSelectedItem(self):
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget_3.takeItem(self.listWidget_3.row(item))

    

class EditVmWindow(QtWidgets.QDialog, Ui_EditVM):
    def __init__(self, text,parent=None):
        self.alternateManageExploits=AlternateManageExploitsWindow()
@@ -158,19 +146,19 @@ def __init__(self, text,parent=None):
        self.machineNameLINEEDIT.setText(text)
        self.discardBUTTON.clicked.connect(self.close)
        #self.manageExploitsBUTTON.clicked.connect(self.alternateManageExploits.show)
        

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
@@ -193,14 +181,14 @@ def __init__(self, parent=None):
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
@@ -216,7 +204,7 @@ def __init__(self, parent=None):
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backButton.clicked.connect(self.close)
        

class NetworkSetupAdvancedWindow(QtWidgets.QDialog, Ui_NetworkSetupAdvanced):
    def __init__(self, parent=None):
        super(NetworkSetupAdvancedWindow, self).__init__(parent)
@@ -237,7 +225,6 @@ class Controller:
    def __init__(self):
        self.showSplashScreen()
        self.main = MainWindow()
        self.runWindow =RunWindow()
        self.progressBar.setValue(1)
        QApplication.processEvents()
        self.openingDBConfiguration = OpeningDBConfigurationWindow()
@@ -293,7 +280,6 @@ def __init__(self):
        self.openingDBConfiguration.connectBUTTON.clicked.connect(self.main.show)
        #
        self.main.manageDataBUTTON.clicked.connect(self.manageDataOptions.show)
        self.main.runBUTTON.clicked.connect(self.runWindow.show)
        #
        self.main.setupBUTTON.clicked.connect(self.setupButtonNav)
        self.main.configureBUTTON.clicked.connect(self.configureButtonNav)
@@ -318,6 +304,7 @@ def __init__(self):
        self.newScenario.vulnerableProgramBrowseBUTTON.clicked.connect(self.manageVulnerablePrograms.show)
        self.newScenario.cancelBUTTON.clicked.connect(self.manageScenarios.show)
        self.newScenario.nextBUTTON.clicked.connect(self.suggestedSetup.show)
        self.newScenario.nextBUTTON.clicked.connect(self.suggestedSetup.refreshSetup)
        #
        self.manageExploits.backBUTTON.clicked.connect(self.newScenario.show)
        #
@@ -332,6 +319,7 @@ def __init__(self):
        #########---ALTERNATE MANAGE EXPLOITS---##################
        #self.createNewVm.manageExploitsBUTTON.clicked.connect(self.alternateManageExploits.show)
        self.editVm.settingsBUTTON.clicked.connect(self.vmSystemSettings.show)
        self.editVm.saveBUTTON.clicked.connect(self.suggestedSetup.refreshSetup)
        ################################################
        #
        self.networkSetup.backButton.clicked.connect(self.alternateNavNetworkSetup)
@@ -346,27 +334,27 @@ def __init__(self):

        #
        self.openingDBConfiguration.show()
        
        
     # Run collectors method for an interval of 5 seconds       


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
        
                # Need to add functionality to let Dr. Acosta
                # know when collectors are done (signal w/ messagebox)

    def showSplashScreen(self):
        self.pix = QPixmap("SplashPage.png")
        self.splash = QSplashScreen(self.pix, Qt.WindowStaysOnTopHint)
@@ -376,9 +364,10 @@ def showSplashScreen(self):
        self.progressBar.setGeometry(0, self.pix.height() - 15, 834, 20)
        self.splash.show()
        self.splash.show()
        

    def setupButtonNav(self):
        self.suggestedSetup.nav = 1
        self.suggestedSetup.refreshSetup()
        self.suggestedSetup.show()

    def configureButtonNav(self):
@@ -398,18 +387,16 @@ def alternateNavSuggestedSetup(self):
            self.main.show()
        else:
            self.newScenario.show()
            

    def handleDoubleClick(self, item):
        item.setSelected(False)
        print(item.text())
        self.editVm = EditVmWindow(item.text())
        self.editVm.show()
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.light(app)
    controller = Controller()
    sys.exit(app.exec_())
