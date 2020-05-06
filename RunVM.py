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
import threading
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

    def create_vm(self):
        os.chdir(self.amed_home+os.sep+'vagrant')
        proc = subprocess.Popen(['vagrant','up'], stdout=subprocess.PIPE)
        output=proc.stdout.read().decode()
        print(output)

        proc_0 = subprocess.Popen(['vagrant','halt'], stdout=subprocess.PIPE)
        output=proc.stdout.read().decode()
        print(output)
        os.chdir(self.amed_home)



    def setupUi(self, RunVM):
        ############################################
        #           Changes Start Here             #
        ############################################
        print("Entered setupui.")
        self.tree={}
        self.vms_start = []

        self.amed_home=os.getcwd()
        self.action_provision_id=-1

        try:
            os.chdir(self.amed_home+os.sep+'vagrant'+os.sep+'.vagrant'+os.sep+'machines'+os.sep+'default'+os.sep+'virtualbox')
            f=open('action_provision','r') # Get the p_id from the vagrant file
            line=f.read()
            line=line.split(':')
            self.action_provision_id=line[1]
        except:
            os.chdir(self.amed_home)
            pass

        os.chdir(self.amed_home)
        # Path to running VBoxManage.exe to start up vms
        vbox_manage_path = os.environ['PATH']
        vbox_manage_path = vbox_manage_path.split(';')
        for ll in vbox_manage_path:
            if 'virtualbox' in ll.lower():
                vbox_manage_path = ll+os.sep+'VBoxManage.exe'

        try:
            proc = subprocess.Popen([vbox_manage_path, "list", "vms"], stdout=subprocess.PIPE)
            output = proc.stdout.read() # shows us a list of vms to run
            output=output.decode()
        except:
            pass


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
        self.rdpBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.rdpBUTTON.setObjectName("rdpBUTTON")
        self.horizontalLayout_2.addWidget(self.rdpBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.startBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.startBUTTON.setObjectName("startBUTTON")
        ############################################
        #           Changes Start Here             #
        ############################################
        self.startBUTTON.setEnabled(True)
        ############################################
        #           Changes End   Here             #
        ############################################
        self.horizontalLayout_2.addWidget(self.startBUTTON)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        
        self.retranslateUi(RunVM)
        QtCore.QMetaObject.connectSlotsByName(RunVM)
        print("Exited setupui")

    def retranslateUi(self, RunVM):
        i = 0
        x = 0
        _translate = QtCore.QCoreApplication.translate
        RunVM.setWindowTitle(_translate("RunVM", "Virtual Machine Selection"))
        self.destinationDirectoryLABEL.setText(_translate("RunVM", "Virtual Machines for Scenario:"))
        __sortingEnabled = self.databseTREEWIDGET.isSortingEnabled()
        self.databseTREEWIDGET.setSortingEnabled(False)
        ############################################
        #           Changes Start Here             #
        ############################################
        for key in self.name_uuid_vm:
            try:
                if self.name_uuid_vm[key] == self.action_provision_id:
                    self.databseTREEWIDGET.topLevelItem(i).setText(0, _translate("Export", key))
                    i+=1
            except:
                msg="Problem with retranslateUi in RunVM.py."
                QMessageBox.about(self, "Error", msg)
                pass
                

        ############################################
        #           Changes End   Here             #
        ############################################
        self.databseTREEWIDGET.setSortingEnabled(__sortingEnabled)
        self.backBUTTON.setText(_translate("RunVM", "Back"))
        self.rdpBUTTON.setText(_translate("RunVM", "Remote Desktop"))
        self.startBUTTON.setText(_translate("RunVM", "Start Selected"))

    ############################################
    #           Changes Start Here             #
    ############################################

    def setupTree(self, RunVM):
        x=0
        for key in self.name_uuid_vm:
            if self.name_uuid_vm[key] == self.action_provision_id:
                self.tree["parent{0}".format(x)] = QtWidgets.QTreeWidgetItem(self.databseTREEWIDGET)
                self.tree["parent{0}".format(x)].setCheckState(0, QtCore.Qt.Unchecked)
                self.tree["parent{0}".format(x)].setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
                x+=1

        return RunVM

    def progress(self):
        self.vms_start = []
        x=0
        for key in self.name_uuid_vm:
            if self.name_uuid_vm[key] == self.action_provision_id:
                if(self.tree["parent{0}".format(x)].checkState(0) == QtCore.Qt.Checked):
                    print(key)
                    self.vms_start.append(key)
                x+=1

        return self.vms_start


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RunVM = QtWidgets.QWidget()
    ui = Ui_RunVM()
    ui.setupUi(RunVM)
    RunVM.show()
    sys.exit(app.exec_())
    
