# -*- coding: utf-8 -*-
############################################
#           Changes Start Here             #
############################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os, sys
import base64
from pymongo import MongoClient
from bson.objectid import ObjectId
from zipfile import ZipFile
from datetime import date
import time
from DBConfiguration import Ui_DBConfiguration

# MAY 3 #
import subprocess
import sys
############################################
#           Changes End   Here             #
############################################

class Ui_RunVM(object):
    ############################################
    #           Changes Start Here             #
    ############################################
    try:
        client = MongoClient(Ui_DBConfiguration.dbConnection)
    except:
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
    db = client.Test


    def setupUi(self, RunVM):
        ############################################
        #           Changes Start Here             #
        ############################################

        self.tree={}
        self.vms_start = []

        # MAY 3 #
        vbox_manage_path = 'C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe'
        try:
            proc = subprocess.Popen([vbox_manage_path, "list", "vms"], stdout=subprocess.PIPE)
            output = proc.stdout.read() # shows us a list of vms to run
            output=output.decode()
        except:
            QMessageBox.about(self, "Error", "VBoxManage.exe is not in the PATH environment variable. \
                Unable to find VBoxManage.exe.")
            self.close()

        # Convert raw (bytes) to string, makes data easier
        # to modify and run vms based on names/uuids
        b = output.split('\r\n') # turn VM string into list of VMs
        
        # Dictionary of VMs available by name 
        # and its uuid for VBoxManage startvm command
        self.name_uuid_vm = {}
        for e in b:
            if e == '':
                continue
            line = e.split('" ')
            self.name_uuid_vm[line[0][1:]] = line[1][1:-1]   
        ############################################
        #           Changes End   Here             #
        ############################################
        RunVM.setObjectName("RunVM")
        RunVM.resize(400, 479) # MAY 3 #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RunVM.sizePolicy().hasHeightForWidth())
        RunVM.setSizePolicy(sizePolicy)
        RunVM.setMinimumSize(QtCore.QSize(400, 479)) # MAY 3 #
        RunVM.setMaximumSize(QtCore.QSize(400, 479)) # MAY 3 #
        self.layoutWidget = QtWidgets.QWidget(RunVM)
        self.layoutWidget.setGeometry(QtCore.QRect(31, 34, 350, 411)) # MAY 3 #
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.destinationDirectoryLABEL = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.destinationDirectoryLABEL.setFont(font)
        self.destinationDirectoryLABEL.setObjectName("destinationDirectoryLABEL")
        self.verticalLayout.addWidget(self.destinationDirectoryLABEL)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        #Tree widget for database
        self.databseTREEWIDGET = QtWidgets.QTreeWidget(self.layoutWidget)
        self.databseTREEWIDGET.setObjectName("databseTREEWIDGET")
        self.databseTREEWIDGET.headerItem().setText(0, "1")
        ############################################
        #           Changes Start Here             #
        ############################################
        self.setupTree(RunVM)

        ############################################
        #           Changes End   Here             #
        ############################################
        self.databseTREEWIDGET.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.databseTREEWIDGET)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.backBUTTON.setObjectName("backBUTTON")
        self.horizontalLayout_2.addWidget(self.backBUTTON)
        spacerItem = QtWidgets.QSpacerItem(38, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.startBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.startBUTTON.setObjectName("startBUTTON")
        ############################################
        #           Changes Start Here             #
        ############################################
        self.startBUTTON.setEnabled(True)
        self.startBUTTON.clicked.connect(self.progress)
        ############################################
        #           Changes End   Here             #
        ############################################
        self.horizontalLayout_2.addWidget(self.startBUTTON)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        
        self.retranslateUi(RunVM)
        QtCore.QMetaObject.connectSlotsByName(RunVM)

    def retranslateUi(self, RunVM):
        i = 0
        _translate = QtCore.QCoreApplication.translate
        RunVM.setWindowTitle(_translate("RunVM", "Virtual Machine Selection"))
        self.destinationDirectoryLABEL.setText(_translate("RunVM", "Virtual Machines on System:"))
        __sortingEnabled = self.databseTREEWIDGET.isSortingEnabled()
        self.databseTREEWIDGET.setSortingEnabled(False)
        ############################################
        #           Changes Start Here             #
        ############################################
        for key in self.name_uuid_vm:
            try:
                self.databseTREEWIDGET.topLevelItem(i).setText(0, _translate("Export", key))
            except:
                print(key)
            i+=1
        ############################################
        #           Changes End   Here             #
        ############################################
        self.databseTREEWIDGET.setSortingEnabled(__sortingEnabled)
        self.backBUTTON.setText(_translate("RunVM", "Back"))
        self.startBUTTON.setText(_translate("RunVM", "Start Selected"))

    ############################################
    #           Changes Start Here             #
    ############################################

    def setupTree(self, RunVM):
        x=0
        for key in self.name_uuid_vm:

            self.tree["parent{0}".format(x)] = QtWidgets.QTreeWidgetItem(self.databseTREEWIDGET)
            self.tree["parent{0}".format(x)].setCheckState(0, QtCore.Qt.Unchecked)
            self.tree["parent{0}".format(x)].setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)

            x+=1

        return RunVM

    def progress(self):
        print('\nEntered Progress.')
        self.progressBar.setValue(0)
        self.count = 0
        numFiles = 0
        x=0
        for key in self.name_uuid_vm:
            if(self.tree["parent{0}".format(x)].checkState(0) == QtCore.Qt.Checked):
                print(key)
                self.vms_start.append(key)
            x+=1

        self.progressBar.setValue(100)
        # QMessageBox.about(self, "Success", "Virtual Machines were started.")
        self.progressBar.setValue(0)

        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RunVM = QtWidgets.QWidget()
    ui = Ui_RunVM()
    ui.setupUi(RunVM)
    RunVM.show()
    sys.exit(app.exec_())
