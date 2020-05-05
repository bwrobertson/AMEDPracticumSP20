# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import threading, platform
import os, sys, subprocess

class Ui_runWindow(object):
    def setupUi(self, runWindow):
        runWindow.setObjectName("runWindow")
        runWindow.resize(360, 200)
        runWindow.setMinimumSize(QtCore.QSize(360, 200))
        runWindow.setMaximumSize(QtCore.QSize(360, 200))
        self.widget = QtWidgets.QWidget(runWindow)
        self.widget.setGeometry(QtCore.QRect(40, 20, 282, 153))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.intervalLABEL = QtWidgets.QLabel(self.widget)
        self.intervalLABEL.setObjectName("intervalLABEL")
        self.horizontalLayout.addWidget(self.intervalLABEL)
        self.intervalSPINBOX = QtWidgets.QSpinBox(self.widget)
        self.intervalSPINBOX.setMinimumSize(QtCore.QSize(71, 21))
        self.intervalSPINBOX.setMaximumSize(QtCore.QSize(71, 21))
        self.intervalSPINBOX.setObjectName("intervalSPINBOX")
        self.horizontalLayout.addWidget(self.intervalSPINBOX)
        spacerItem2 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.buttonsHorizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.buttonsHorizontalLayout_2.setObjectName("buttonsHorizontalLayout_2")
        self.cancelPushBUTTON = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelPushBUTTON.sizePolicy().hasHeightForWidth())
        self.cancelPushBUTTON.setSizePolicy(sizePolicy)
        self.cancelPushBUTTON.setMinimumSize(QtCore.QSize(112, 32))
        self.cancelPushBUTTON.setMaximumSize(QtCore.QSize(112, 32))
        self.cancelPushBUTTON.setObjectName("cancelPushBUTTON")
        self.buttonsHorizontalLayout_2.addWidget(self.cancelPushBUTTON)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsHorizontalLayout_2.addItem(spacerItem4)
        self.okPushBUTTON = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okPushBUTTON.sizePolicy().hasHeightForWidth())
        self.okPushBUTTON.setSizePolicy(sizePolicy)
        self.okPushBUTTON.setMinimumSize(QtCore.QSize(112, 32))
        self.okPushBUTTON.setMaximumSize(QtCore.QSize(112, 32))
        self.okPushBUTTON.setObjectName("okPushBUTTON")
        self.buttonsHorizontalLayout_2.addWidget(self.okPushBUTTON)
        self.verticalLayout.addLayout(self.buttonsHorizontalLayout_2)

        self.retranslateUi(runWindow)
        QtCore.QMetaObject.connectSlotsByName(runWindow)

    def retranslateUi(self, runWindow):
        _translate = QtCore.QCoreApplication.translate
        runWindow.setWindowTitle(_translate("runWindow", "Run"))
        self.label_2.setText(_translate("runWindow", "Enter an interval of time for data capture:"))
        self.intervalLABEL.setText(_translate("runWindow", "Interval (minutes):"))
        self.cancelPushBUTTON.setText(_translate("runWindow", "Cancel"))
        self.okPushBUTTON.setText(_translate("runWindow", "Ok"))

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
            vbox_manage_path = os.environ['PATH']
            vbox_manage_path = vbox_manage_path.split(';')
            for ll in vbox_manage_path:
                if 'Oracle' in ll:
                    vbox_manage_path = ll+os.sep+'VBoxManage.exe'

            vagrant_folder = os.getcwd()+os.sep+'\\vagrant'
            if not 'AMEDPracticumSP20' in vagrant_folder:
                QMessageBox.about(self, "Warning", "No vagrant folder present. Creating one!")
                os.mkdir(os.getcwd()+os.sep+'\\vagrant')
                return

            amed_home = os.getcwd()
            # Run VBoxManage to find the VM's to start
            try:

                proc = subprocess.Popen([vbox_manage_path, 'list', 'vms'], stdout=subprocess.PIPE)
                output = proc.stdout.read() # shows us a list of vms to run
                output=output.decode()

                proc_1 = subprocess.Popen([vbox_manage_path, "list", "runningvms"], stdout=subprocess.PIPE)
                output_1 = proc_1.stdout.read() # shows us a list of vms running
                output_1=output_1.decode()

            except:
                QMessageBox.about(self, "Warning", "Need to add VBoxManage.exe to PATH environment variable.")
                print(vbox_manage_path)
                print("Need to add VBoxManage.exe to PATH environment variable.")
                print("Exiting from starting VM scenario.")
                return
            
            os.chdir(amed_home)
            # Convert raw (bytes) to string, makes data easier
            # to modify and run vms based on names/uuids
            b = output.split('\r\n') # turn VM string into list of VMs
            
            # # Dictionary of VMs available by name 
            # # and its uuid for VBoxManage startvm command
            name_uuid_vm = {}
            print("b: ",b)
            print("\n\n")
            for e in b:
                if e == '':
                    continue
                line = e.split('" ')
                print(line)
                name_uuid_vm[line[0][1:]] = line[1][1:-1]            

            # # Stub vm to start
            # # Ideally, user should be able to enter the
            # # exact vms from their scenario selected
            vms_to_start = []
            for key in name_uuid_vm:
                if "vagrant" in key.lower():        
                    vms_to_start.append(key)

            # # Retrieve running vms to prevent issuing a command to
            # # start an already running vm
            d = output_1.split('\r\n')
            running_vms = []
            for e in d:
                if e == '':
                    continue
                line = e.split('" ')
                running_vms.append(line[0][1:])
            
            # # Start VMs on their own threads (subprocess)
            # # Could also use vagrant up!
            for v in vms_to_start:

                # Check if vm is running
                if v in running_vms:
                    print("VM is already running, powering off!")
                    print("ID: ", v)
                    proc_stop = subprocess.Popen([vbox_manage_path, 'controlvm', v, 'poweroff'], stdout=subprocess.PIPE)
                    output = proc_stop.stdout.read()
                    print(output.decode())
                    print('\n\n')


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
                os.chdir(vagrant_folder)
                vagrant_command_string = "sudo $ECEL_HOME/standalone.sh "+str(interval_seconds)
                proc_1 = subprocess.Popen(['vagrant', 'up'], stdout=subprocess.PIPE)
                print("\nVagrant standalone command sent, output to follow ->")
                print('\n\n')
                output = proc_1.stdout.read()
                print(output)          

                proc = subprocess.Popen(['vagrant', 'ssh', '-c', vagrant_command_string], stdout=subprocess.PIPE)
                print("\nVagrant standalone command sent, output to follow ->")
                print('\n\n')
                output = proc.stdout.read()
                print(output)
                os.chdir(amed_home)
                return
            except:
                print("\nEither the VM was not started, or")
                print("standalone.sh not found within Ubuntu guest or guest OS is Windows-based.\n")
                return

            
            os.chdir(amed_home)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    runWindow = QtWidgets.QWidget()
    ui = Ui_runWindow()
    ui.setupUi(runWindow)
    runWindow.show()
    sys.exit(app.exec_())
