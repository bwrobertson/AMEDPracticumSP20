from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QSplashScreen, QMenu, QApplication, QProgressBar
from qtpy import QtCore

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

import os, subprocess
import qtmodern.styles
import qtmodern.windows

# instantiation of UI (View) classes and controller class

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.manageScenarioBUTTON.clicked.connect(self.hide)
        self.manageDataBUTTON.clicked.connect(self.hide)

# Run collectors functionality
class RunWindow(QtWidgets.QWidget, Ui_runWindow): # MAY 3 #
    def __init__(self, parent=None):
        super(RunWindow, self).__init__(parent)
        self.thread_scenarios = {}
        self.vms_proc_ids = {}
        self.t_id_counter = 0
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.okPushBUTTON.clicked.connect(self.okayClicked)
        self.cancelPushBUTTON.clicked.connect(self.close)

    def okayClicked(self):
        ###### use the following line  minus the print() to retrieve the value that is curerntly inside the spinbox
        interval_minute = self.intervalSPINBOX.value()
        print("Interval minute: ",interval_minute)
        print("Run Method. Starting scenario.")
        
        # start scenario on thread
        self.thread_scenarios[self.t_id_counter] = threading.Thread(target=self.runCollectors, args=(interval_minute,), daemon=True)
        self.thread_scenarios[self.t_id_counter].start()
        print("Started thread: ",self.thread_scenarios[self.t_id_counter])
        # self.thread_scenarios[self.t_id_counter].join()

        # to store ids of threads
        self.t_id_counter += 1
        self.hide()

    # Run collectors method for an interval of 5 seconds       
    def runCollectors(self, minute_interval):
        # identify OS
        operating_system = platform.system()
        try:
            interval_seconds = int(minute_interval)
        except:
            print("Not an integer.")
            return

        interval_seconds = interval_seconds * 60
        if interval_seconds == 0:
            interval_seconds = 20
            print("Defaulting to 20 seconds, because 0 minutes was given as an interval.")

        # Check if Virtualbox on server [would never run on local] has VM's,
        # If not prompt user to start a scenario
        # Common path: "C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe"
        if "windows" in operating_system.lower():
            # Needs a variable of the scenario info to find VM's to start
            # scenario_info = ''

            # Path to running VBoxManage.exe to start up vms
            vbox_manage_path = 'C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe'

            # Run VBoxManage to find the VM's to start
            try:
                proc = subprocess.Popen([vbox_manage_path, "list", "vms"], stdout=subprocess.PIPE)
                output = proc.stdout.read() # shows us a list of vms to run
                output=output.decode()

                proc_1 = subprocess.Popen([vbox_manage_path, "list", "runningvms"], stdout=subprocess.PIPE)
                output_1 = proc_1.stdout.read() # shows us a list of vms running
                output_1=output_1.decode()

            except:
                print("Need to add VBoxManage.exe to PATH environment variable.")
                print("Exiting from starting VM scenario.")
                return
            
            # Convert raw (bytes) to string, makes data easier
            # to modify and run vms based on names/uuids
            b = output.split('\r\n') # turn VM string into list of VMs
            
            # Dictionary of VMs available by name 
            # and its uuid for VBoxManage startvm command
            name_uuid_vm = {}
            print("b: ",b)
            print("\n\n")
            for e in b:
                if e == '':
                    continue
                line = e.split('" ')
                print(line)
                name_uuid_vm[line[0][1:]] = line[1][1:-1]            

            # Stub vm to start
            # Ideally, user should be able to enter the
            # exact vms from their scenario selected
            vms_to_start = []
            for key in name_uuid_vm:
                if "vagrant" in key.lower():        
                    vms_to_start.append(key)

            # Retrieve running vms to prevent issuing a command to
            # start an already running vm
            d = output_1.split('\r\n')
            running_vms = []
            for e in d:
                if e == '':
                    continue
                line = e.split('" ')
                running_vms.append(line[0][1:])

            print("List of vms to start: ", str(vms_to_start))
            print("Running vms: ", str(running_vms))   
            print('\n\n') 
            # Based on scenario find uuid for VMs to start
            # vms_to_start = [] # collection of strings to be used to find uuid later
            # ... perform collection from scenario file
            
            # Start VMs on their own threads (subprocess)
            # Could also use vagrant up!
            print("Proc ID dictionary (before): ",str(self.vms_proc_ids))
            print('\n\n')
            for v in vms_to_start:

                # Check if vm is running
                if v in running_vms:
                    print("VM is already running, powering off!")
                    print("ID: ", v)
                    proc_stop = subprocess.Popen([vbox_manage_path, 'controlvm', v, 'poweroff'], stdout=subprocess.PIPE)
                    output = proc_stop.stdout.read()
                    print(output.decode())
                    print('\n\n')
                else:
                    # Create a list to hold information of vm    
                    print("About to start vms...")
                    self.vms_proc_ids[v] = []
                    self.vms_proc_ids[v].append(subprocess.Popen([vbox_manage_path, 'startvm', v], stdout=subprocess.PIPE))
                    output = self.vms_proc_ids[v][0].stdout.read()
                    self.vms_proc_ids[v].append(output)
                    print("Added to vms_proc_ids...\n\n")

            print("Proc ID dictionary (after): ",str(self.vms_proc_ids))


            # how to power down vm safely
            # command must be executed in the folder where the Vagrantfile is
            # located (End of the day might be the AMED folder)
            # change into the vagrant folder where the Vagrantfile is located /path/to/AMEDPracticumSP20/vagrant
            current_directory = os.getcwd()
            if "vagrant" in current_directory:
                print("\nAlready in Vagrant folder.")
            elif "vagrant" in os.listdir(current_directory):
                os.chdir(current_directory + os.sep + "vagrant")
                print("\n"+str(os.getcwd()))
            else:
                print("\nVagrant folder not found.")
                print(os.getcwd())
                return
            try:
                # Need to verify the VM is up and running??

                # Sending vagrant command to start collectors
                vagrant_command_string = "sudo $ECEL_HOME/standalone.sh "+str(interval_seconds)
                proc = subprocess.Popen(['vagrant', 'ssh', '-c', vagrant_command_string], stdout=subprocess.PIPE)
                print("\nVagrant standalone command sent, output to follow ->")
                print('\n\n')
                output = proc.stdout.read()
                print(output)
                return
            except:
                print("\nEither the VM was not started, or")
                print("standalone.sh not found within Ubuntu guest or guest OS is Windows-based.\n")
                return


        # Stub windows (have it send a return value) 
        # verifying it received a signal from host
        # (Something present on all windows machines)
        else:
            # Ubuntu-based hosts that are running AMED

            # Controller.py must be ran in root (i.e. $ sudo su, on Linux)
            uid = os.getuid()
            if uid != 0:
                msg = QMessageBox.about(self.main, "Warning", "Collectors must be ran with root privileges.")
            else:
                proc = subprocess.Popen(["python", "ecel/start_stop_collectors.py"])
                msg = QMessageBox.about(self.main, "Notice", "Collectors have started!")
                # Need to add functionality to let Dr. Acosta 
                # know when collectors are done (signal w/ messagebox)



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

class SuggestedSetupWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, parent=None):
        self.nav=0
        self.editVmWindow = EditVmWindow("null")
        self.vMSystemsSettings=VmSystemSettings()
        super(SuggestedSetupWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
        self.backButton.clicked.connect(self.close)
        self.nextBUTTON.clicked.connect(self.close)

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


class EditVmWindow(QtWidgets.QDialog, Ui_EditVM):
    def __init__(self, text,parent=None):
        self.alternateManageExploits=AlternateManageExploitsWindow()
        super(EditVmWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setupUi(self)
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
        self.showSplashScreen()
        self.main = MainWindow()
        self.runWindow =RunWindow()
        self.progressBar.setValue(1)
        QApplication.processEvents()
        self.openingDBConfiguration = OpeningDBConfigurationWindow()
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
        self.alternateManageExploits = AlternateManageExploitsWindow()
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
        self.vmSystemSettings = VmSystemSettings()
        self.progressBar.setValue(12)
        QApplication.processEvents()
        self.editVm= EditVmWindow("null")
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
        self.openingDBConfiguration.connectBUTTON.clicked.connect(self.main.show)
        #
        self.main.manageDataBUTTON.clicked.connect(self.manageDataOptions.show)
        self.main.runBUTTON.clicked.connect(self.runWindow.show)
        #
        self.main.setupBUTTON.clicked.connect(self.setupButtonNav)
        self.main.configureBUTTON.clicked.connect(self.configureButtonNav)
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
        self.newScenario.nextBUTTON.clicked.connect(self.suggestedSetup.refreshSetup)
        #
        self.manageExploits.backBUTTON.clicked.connect(self.newScenario.show)
        #
        self.manageVulnerablePrograms.backBUTTON.clicked.connect(self.newScenario.show)
        #
        self.suggestedSetup.backButton.clicked.connect(self.alternateNavSuggestedSetup)
        self.suggestedSetup.addVmBUTTON.clicked.connect(self.createNewVm.show)
        self.suggestedSetup.nextBUTTON.clicked.connect(self.networkSetup.show)
        self.suggestedSetup.listWidget_2.itemDoubleClicked.connect(self.handleDoubleClick)
        self.suggestedSetup.listWidget_3.itemDoubleClicked.connect(self.handleDoubleClick)
        #
        #########---ALTERNATE MANAGE EXPLOITS---##################
        #self.createNewVm.manageExploitsBUTTON.clicked.connect(self.alternateManageExploits.show)
        self.editVm.settingsBUTTON.clicked.connect(self.vmSystemSettings.show)
        self.editVm.saveBUTTON.clicked.connect(self.suggestedSetup.refreshSetup)
        ################################################
        #
        self.networkSetup.backButton.clicked.connect(self.alternateNavNetworkSetup)
        self.networkSetup.advancedSettingsBUTTON.clicked.connect(self.advancedNetworkSetup.show)
        #
        self.advancedNetworkSetup.backBUTTON.clicked.connect(self.networkSetup.show)
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
        # adding progress bar
        self.progressBar = QProgressBar(self.splash)
        self.progressBar.setMaximum(17)
        self.progressBar.setGeometry(0, self.pix.height() - 15, 834, 20)
        self.splash.show()
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
        self.editVm = EditVmWindow(item.text())
        self.editVm.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.light(app)
    controller = Controller()
    sys.exit(app.exec_())
