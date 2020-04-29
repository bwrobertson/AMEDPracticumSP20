# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Edit_Vm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import VagrantFileTemplate as temp
import os
from pymongo import MongoClient
from DBConfiguration import Ui_DBConfiguration
from bson.objectid import ObjectId
import threading
import subprocess

class Ui_EditVM(object):
    def setupUi(self, EditVM):
        EditVM.setObjectName("EditVM")
        EditVM.resize(560, 679)
        EditVM.setMinimumSize(QtCore.QSize(560, 679))
        EditVM.setMaximumSize(QtCore.QSize(560, 679))
        self.widget = QtWidgets.QWidget(EditVM)
        self.widget.setGeometry(QtCore.QRect(30, 20, 522, 651))
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.machineNameLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.machineNameLABEL.setFont(font)
        self.machineNameLABEL.setObjectName("machineNameLABEL")
        self.verticalLayout.addWidget(self.machineNameLABEL)
        self.machineNameLINEEDIT = QtWidgets.QLineEdit(self.widget)
        self.machineNameLINEEDIT.setObjectName("machineNameLINEEDIT")
        self.verticalLayout.addWidget(self.machineNameLINEEDIT)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.typeLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.typeLABEL.setFont(font)
        self.typeLABEL.setObjectName("typeLABEL")
        self.horizontalLayout.addWidget(self.typeLABEL)
        self.vmFilesLABEL = QtWidgets.QLabel(self.widget)
        self.vmFilesLABEL.setFont(font)
        self.vmFilesLABEL.setObjectName("vmFilesLABEL")
        self.typeCOMBOBOX = QtWidgets.QComboBox(self.widget)
        self.typeCOMBOBOX.setObjectName("typeCOMBOBOX")
        self.typeCOMBOBOX.addItem("")
        self.typeCOMBOBOX.addItem("")
        self.horizontalLayout.addWidget(self.typeCOMBOBOX)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        ####CHANGES START: Added a new horizontal Layout####
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        ####CHANGES END####
        self.createVmLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.createVmLABEL.setFont(font)
        self.createVmLABEL.setObjectName("createVmLABEL")
        self.horizontalLayout_2.addWidget(self.createVmLABEL)
        self.openExistingBUTTON = QtWidgets.QPushButton(self.widget)
        self.openExistingBUTTON.setObjectName("openExistingBUTTON")
        self.horizontalLayout_2.addWidget(self.openExistingBUTTON)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vmOsLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.vmOsLABEL.setFont(font)
        self.vmOsLABEL.setObjectName("vmOsLABEL")

        self.verticalLayout_2.addWidget(self.vmOsLABEL)
        self.vmOsCOMBOBOX = QtWidgets.QComboBox(self.widget)
        self.vmOsCOMBOBOX.setObjectName("vmOsCOMBOBOX")
        self.vmOsCOMBOBOX.addItem("")
        self.vmOsCOMBOBOX.addItem("")
        self.vmOsCOMBOBOX.addItem("")
        self.verticalLayout_2.addWidget(self.vmOsCOMBOBOX)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        #self.malwareLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.malwareLABEL.setFont(font)
        #self.malwareLABEL.setObjectName("malwareLABEL")
        #self.verticalLayout_4.addWidget(self.malwareLABEL)
        self.verticalLayout_4.addWidget(self.vmFilesLABEL)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        #self.metasploitLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.metasploitLABEL.setFont(font)
        #self.metasploitLABEL.setObjectName("metasploitLABEL")
        #self.verticalLayout_5.addWidget(self.metasploitLABEL)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        #self.metasploitLINEEDIT = QtWidgets.QLineEdit(self.widget)
        #self.metasploitLINEEDIT.setObjectName("metasploitLINEEDIT")
        #self.horizontalLayout_5.addWidget(self.metasploitLINEEDIT)
        #self.metasploitBrowseBUTTON = QtWidgets.QPushButton(self.widget)
        #self.metasploitBrowseBUTTON.setObjectName("metasploitBrowseBUTTON")
        #self.horizontalLayout_5.addWidget(self.metasploitBrowseBUTTON)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        #self.scriptLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.scriptLABEL.setFont(font)
        #self.scriptLABEL.setObjectName("scriptLABEL")
        #self.verticalLayout_6.addWidget(self.scriptLABEL)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        #self.scriptLINEEDIT = QtWidgets.QLineEdit(self.widget)
        #self.scriptLINEEDIT.setObjectName("scriptLINEEDIT")
        #self.horizontalLayout_9.addWidget(self.scriptLINEEDIT)
        #self.scriptBrowseBUTTON = QtWidgets.QPushButton(self.widget)
        #self.scriptBrowseBUTTON.setObjectName("scriptBrowseBUTTON")
        #self.horizontalLayout_9.addWidget(self.scriptBrowseBUTTON)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
         ####VM FILES QTREE WIDGET START####
        self.vmFilesTREEWIDGET = QtWidgets.QTreeWidget(self.widget)
        self.vmFilesTREEWIDGET.setObjectName("vmFilesTREEWIDGET")
        self.vmFilesTREEWIDGET.headerItem().setText(0, "1")

        self.vmFilesTREEWIDGET.header().setVisible(False)
        self.horizontalLayout_10.addWidget(self.vmFilesTREEWIDGET)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        ####VM FILES QTREE WIDGET END####
        self.softwareLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.softwareLABEL.setFont(font)
        self.softwareLABEL.setObjectName("softwareLABEL")
        self.verticalLayout_3.addWidget(self.softwareLABEL)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.softwareTREEWIDGET = QtWidgets.QTreeWidget(self.widget)
        self.softwareTREEWIDGET.setObjectName("softwareTREEWIDGET")
        #item_0 = QtWidgets.QTreeWidgetItem(self.softwareTREEWIDGET)
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        #item_0 = QtWidgets.QTreeWidgetItem(self.softwareTREEWIDGET)
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        #item_0 = QtWidgets.QTreeWidgetItem(self.softwareTREEWIDGET)
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.softwareTREEWIDGET.header().setVisible(False)
        self.setupVMFiles(EditVM)
        self.horizontalLayout_8.addWidget(self.softwareTREEWIDGET)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.discardBUTTON = QtWidgets.QPushButton(self.widget)
        self.discardBUTTON.setObjectName("discardBUTTON")
        self.horizontalLayout_6.addWidget(self.discardBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.settingsBUTTON = QtWidgets.QPushButton(self.widget)
        self.settingsBUTTON.setObjectName("settingsBUTTON")
        self.horizontalLayout_6.addWidget(self.settingsBUTTON)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.saveBUTTON = QtWidgets.QPushButton(self.widget)
        self.saveBUTTON.setObjectName("saveBUTTON")
        self.saveBUTTON.clicked.connect(self.runVagrant)
        self.horizontalLayout_6.addWidget(self.saveBUTTON)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.retranslateUi(EditVM)
        QtCore.QMetaObject.connectSlotsByName(EditVM)

    def createJson(self):
        data = temp.VagrantFileTemplate.createJson(self)

        os = ""
        if self.vmOsCOMBOBOX.currentIndex == 0:
            os = "kali linux"
        elif self.vmOsCOMBOBOX.currentIndex == 1:
            os = "ubuntu/trusty64"
        elif self.vmOsCOMBOBOX.currentIndex == 2:
            os = "windows"
        data['source_path'] = os

        return data


    def runVagrant(self):
        data = self.createJson()
        # data = json.dumps(data)
        # loaded_data = json.loads(data)
        # with open('packer_test_vagrant.json', 'w') as f:
        #     json.dump(data, f)
        # t = threading.Thread(os.system("packer build packer_test_vagrant.json"))
        subprocess.Popen("packer build packer_test_vagrant.json")
        # os.system("packer build packer_test_vagrant.json")
       # os.system("vagrant up --provision")
        self.hide()

    def retranslateUi(self, EditVM):
        _translate = QtCore.QCoreApplication.translate
        EditVM.setWindowTitle(_translate("EditVM", "Edit VM"))
        self.machineNameLABEL.setText(_translate("EditVM", "Machine Name:"))
        self.typeLABEL.setText(_translate("EditVM", "Type:"))
        self.typeCOMBOBOX.setItemText(0, _translate("EditVM", "POV Entity"))
        self.typeCOMBOBOX.setItemText(1, _translate("EditVM", "Victim Entity"))
        self.createVmLABEL.setText(_translate("EditVM", "Create From Existing VM:"))
        self.openExistingBUTTON.setText(_translate("EditVM", "Open Existing"))
        self.vmOsLABEL.setText(_translate("EditVM", "VM OS:"))
        self.vmOsCOMBOBOX.setItemText(0, _translate("EditVM", "Kali Linux"))
        self.vmOsCOMBOBOX.setItemText(1, _translate("EditVM", "Ubuntu"))
        self.vmOsCOMBOBOX.setItemText(2, _translate("EditVM", "Windows"))
        self.vmFilesLABEL.setText(_translate("CreateNewVm", "VM Files:"))
        self.softwareLABEL.setText(_translate("EditVM", "Software:"))
        j=0
        i=0
        try:
            client = MongoClient(Ui_DBConfiguration.dbConnection)
        except:
            client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["Scenario"]
        EXPLOITS = db['Exploits']
        POVS = db['VulnerablePrograms']
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.softwareTREEWIDGET.isSortingEnabled()
        """for collection in data.find({'_id': ObjectId('5e89003d2da10a05adcbf77a')}):
            scen = collection['scenario']
            j=0
            for key in scen:
                exploit = scen['exploit']
                pov = scen['pov']
                if (key == 'exploit'):
                    for item in exploit:
                        self.vmFilesTREEWIDGET.topLevelItem(j).setText(0, _translate("Export", exploit['file']))
                        #print(exploit['file'])
                        try:
                            temp = EXPLOITS.find_one({'name': exploit['file']})
                            self.vmFilesTREEWIDGET.topLevelItem(j).child(0).setText(0, _translate("Export", 'Lauguage : ' + temp['Language']))
                            self.vmFilesTREEWIDGET.topLevelItem(j).child(1).setText(0, _translate("Export", 'Platform : ' + temp['Platform']))
                            self.vmFilesTREEWIDGET.topLevelItem(j).child(2).setText(0, _translate("Export", 'Type : ' + temp['Type']))
                        except:
                            self.vmFilesTREEWIDGET.topLevelItem(j).child(0).setText(0, _translate("Export", 'Lauguage : UNK'))
                            self.vmFilesTREEWIDGET.topLevelItem(j).child(1).setText(0, _translate("Export", 'Platform : UNK'))
                            self.vmFilesTREEWIDGET.topLevelItem(j).child(2).setText(0, _translate("Export", 'Type : UNK'))
                        j+=1
                if (key == 'pov'):
                    for item in pov:
                        self.vmFilesTREEWIDGET.topLevelItem(j).setText(0, _translate("Export", pov['file']))
                        try:
                            temp = POVS.find_one({'name': pov['file']})
                            self.vmFilesTREEWIDGET.topLevelItem(j).child(0).setText(0, _translate("Export", 'Information : ' + temp['Information']))
                        except:
                            self.vmFilesTREEWIDGET.topLevelItem(j).child(0).setText(0, _translate("Export", 'Information : UNK'))
                        j+=1
            i+=1
        """
        self.softwareTREEWIDGET.setSortingEnabled(False)
        i=0
        for collection in EXPLOITS.find():
            self.vmFilesTREEWIDGET.topLevelItem(i).setText(0, _translate("EditVM", collection['name']))
            self.vmFilesTREEWIDGET.topLevelItem(i).child(0).setText(0, _translate("EditVM", 'Language : ' + collection['Language']))
            self.vmFilesTREEWIDGET.topLevelItem(i).child(1).setText(0, _translate("EditVM", 'Platform : ' + collection['Platform']))
            self.vmFilesTREEWIDGET.topLevelItem(i).child(2).setText(0, _translate("EditVM", 'Type : ' + collection['Type']))
            i+=1
        for collection in POVS.find():
            self.vmFilesTREEWIDGET.topLevelItem(i).setText(0, _translate("EditVM", collection['name']))
            self.vmFilesTREEWIDGET.topLevelItem(i).child(0).setText(0, _translate("EditVM", 'Information : ' + collection['Information']))
            i+=1

        self.vmFilesTREEWIDGET.setSortingEnabled(__sortingEnabled)
        self.discardBUTTON.setText(_translate("EditVM", "Discard"))
        self.settingsBUTTON.setText(_translate("EditVM", "System Settings"))
        self.saveBUTTON.setText(_translate("EditVM", "Save"))

    def setupVMFiles(self, EditVM):
        x=0
        y=0
        self.tree={}
        try:
            client = MongoClient(Ui_DBConfiguration.dbConnection)
        except:
            client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["Scenario"]
        thisVM = data.find_one({'_id': ObjectId('5e89003d2da10a05adcbf77a')})
        thisScen = thisVM['scenario']
        print(thisVM)
        thisExploit = thisScen['exploit']
        thisPOV = thisScen['pov']
        EXPLOITS = db['Exploits']
        POVS = db['VulnerablePrograms']
        for collection in EXPLOITS.find():
            self.tree["parent{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.vmFilesTREEWIDGET)
            #print(collection['name'])
            if(collection['name'] in thisExploit.values()):
                self.tree["parent{0}".format(y)].setCheckState(0, QtCore.Qt.Checked)
            else:
                self.tree["parent{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
            self.tree["child{0}".format(0)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
            self.tree["child{0}".format(1)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
            self.tree["child{0}".format(2)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
            y+=1
        for collection in POVS.find():
            self.tree["parent{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.vmFilesTREEWIDGET)
            if(collection['name'] in thisPOV.values()):
                self.tree["parent{0}".format(y)].setCheckState(0, QtCore.Qt.Checked)
            else:
                self.tree["parent{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
            self.tree["child{0}".format(0)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
            y+=1

        return EditVM

    def setupTree(self, EditVM):
            x=0
            y=0
            self.tree={}
            try:
                client = MongoClient(Ui_DBConfiguration.dbConnection)
            except:
                client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
            db = client.Test
            data = db["Scenario"]
            EXPLOITS = db['Exploits']
            POVS = db['VulnerablePrograms']
            for collection in data.find({'_id': ObjectId('5e89003d2da10a05adcbf77a')}):
                scen = collection['scenario']
                #self.tree["parent{0}".format(x)].setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
                for key in scen:
                    exploit = scen['exploit']
                    pov = scen['pov']
                    if (key == 'exploit'):
                        for item in exploit:
                            self.tree["parent{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.vmFilesTREEWIDGET)
                            self.tree["parent{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
                            self.tree["child{0}".format(0)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
                            self.tree["child{0}".format(1)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
                            self.tree["child{0}".format(2)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
                            y+=1
                    if(key=='pov'):
                        for item in pov:
                            self.tree["parent{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.vmFilesTREEWIDGET)
                            self.tree["parent{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
                            self.tree["child{0}".format(0)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
                            y+=1
                x+=1
            return EditVM

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditVM = QtWidgets.QWidget()
    ui = Ui_EditVM()
    ui.setupUi(EditVM)
    EditVM.show()
    sys.exit(app.exec_())
