# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pymongo import MongoClient
from DBConfiguration import Ui_DBConfiguration

class Ui_CreateNewVm(object):
    def setupUi(self, CreateNewVm):
        CreateNewVm.setObjectName("CreateNewVm")
        CreateNewVm.resize(567, 686)
        CreateNewVm.setMinimumSize(QtCore.QSize(567, 607))
        CreateNewVm.setMaximumSize(QtCore.QSize(567, 686))
        self.layoutWidget = QtWidgets.QWidget(CreateNewVm)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 522, 651))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.machineNameLABEL = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.machineNameLABEL.setFont(font)
        self.machineNameLABEL.setObjectName("machineNameLABEL")
        self.verticalLayout.addWidget(self.machineNameLABEL)
        self.machineNameLINEEDIT = QtWidgets.QLineEdit(self.layoutWidget)
        self.machineNameLINEEDIT.setObjectName("machineNameLINEEDIT")
        self.verticalLayout.addWidget(self.machineNameLINEEDIT)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.typeLABEL = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.typeLABEL.setFont(font)
        self.typeLABEL.setObjectName("typeLABEL")
        self.horizontalLayout.addWidget(self.typeLABEL)
        self.typeCOMBOBOX = QtWidgets.QComboBox(self.layoutWidget)
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
        self.createVmLABEL = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.createVmLABEL.setFont(font)
        self.createVmLABEL.setObjectName("createVmLABEL")
        self.horizontalLayout_2.addWidget(self.createVmLABEL)
        self.openExistingBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.openExistingBUTTON.setObjectName("openExistingBUTTON")
        self.horizontalLayout_2.addWidget(self.openExistingBUTTON)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vmOsLABEL = QtWidgets.QLabel(self.layoutWidget)
        ####CHANGE START####
        self.vmFilesLABEL = QtWidgets.QLabel(self.layoutWidget)
         ####CHANGE END####
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.vmOsLABEL.setFont(font)
        self.vmOsLABEL.setObjectName("vmOsLABEL")
        self.verticalLayout_2.addWidget(self.vmOsLABEL)
        self.vmOsCOMBOBOX = QtWidgets.QComboBox(self.layoutWidget)
        self.vmOsCOMBOBOX.setObjectName("vmOsCOMBOBOX")
        self.vmOsCOMBOBOX.addItem("")
        self.vmOsCOMBOBOX.addItem("")
        self.vmOsCOMBOBOX.addItem("")
        self.verticalLayout_2.addWidget(self.vmOsCOMBOBOX)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ####CHANGE START: Added Label####
        self.vmFilesLABEL.setFont(font)
        self.vmFilesLABEL.setObjectName("vmFilesLABEL")
        ####CHANGED END####
        self.vmFilesAddToVMBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.vmFilesAddToVMBUTTON.setObjectName("vmFilesAddToVMBUTTON")
        self.manageExploitsBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.manageExploitsBUTTON.setObjectName("manageExploitsBUTTON")
        self.verticalLayout_4.addWidget(self.vmFilesLABEL)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.softwareLABEL = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.softwareLABEL.setFont(font)
        self.softwareLABEL.setObjectName("softwareLABEL")
        self.verticalLayout_6.addWidget(self.softwareLABEL)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.softwareTREEWIDGET = QtWidgets.QTreeWidget(self.layoutWidget)
        self.softwareTREEWIDGET.setObjectName("softwareTREEWIDGET")
        self.softwareTREEWIDGET.header().setVisible(False)
        self.setupSoftware(CreateNewVm)
        self.horizontalLayout_8.addWidget(self.softwareTREEWIDGET)

        ####VM FILES QTREE WIDGET START####
        self.vmFilesTREEWIDGET = QtWidgets.QTreeWidget(self.layoutWidget)
        self.vmFilesTREEWIDGET.setObjectName("vmFilesTREEWIDGET")
        self.vmFilesTREEWIDGET.headerItem().setText(0, "1")
        #self.setupTree(CreateNewVm) ###Method Call

        self.vmFilesTREEWIDGET.header().setVisible(False)
        self.verticalLayout_10.addWidget(self.manageExploitsBUTTON)
        self.verticalLayout_10.addWidget(self.vmFilesAddToVMBUTTON)
        self.horizontalLayout_10.addWidget(self.vmFilesTREEWIDGET)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        ####VM FILES QTREE WIDGET END####

        self.softwareAddBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.softwareAddBUTTON.setObjectName("softwareAddBUTTON")
        self.horizontalLayout_8.addWidget(self.softwareAddBUTTON)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.discardBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.discardBUTTON.setObjectName("discardBUTTON")
        self.horizontalLayout_6.addWidget(self.discardBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(298, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.saveBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.saveBUTTON.setObjectName("saveBUTTON")
        self.horizontalLayout_6.addWidget(self.saveBUTTON)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.retranslateUi(CreateNewVm)
        QtCore.QMetaObject.connectSlotsByName(CreateNewVm)

    ####Add file to the list####
    def addVmFiles(self):
        lastIndex = self.vmFilesLISTWIDGET.count()
        if len(self.malwareLINEEDIT.text())>0:
            self.vmFilesLISTWIDGET.addItem(QtWidgets.QListWidgetItem())
            item = self.vmFilesLISTWIDGET.item(lastIndex)
            filename = self.malwareLINEEDIT.text()
            stringList = filename.split('/')
            item.setText(stringList[-1])
            ##TODO fix the clear to make it clear right away
            self.malwareLINEEDIT.clear()

    ####Remove file from the list####
    def removeVmFiles(self):
        item = self.vmFilesLISTWIDGET.currentItem()
        self.vmFilesLISTWIDGET.takeItem(self.vmFilesLISTWIDGET.row(item))

    ####Browse button functionality####
    def exploitBrowser(self):
        exploitOptions = QFileDialog.Options()
        self.exploitDialog = QFileDialog()
        self.exploitDialog.setOptions(exploitOptions)
        self.exploitPath, __ = QFileDialog.getOpenFileName(self.exploitDialog, "Select Exploit", '/home')

        if self.exploitPath:
            #If Windows, change the separator
            if self.exploitPath == 'C:\\':
                self.exploitPath = self.exploitPath.replace('/', '\\')
                self.malwareLINEEDIT.setText(self.exploitPath)
            # if Linux-based
            else:
                self.malwareLINEEDIT.setText(self.exploitPath)
        else:
            self.malwareLINEEDIT.setText(self.exploitPath)

    def retranslateUi(self, CreateNewVm):
        _translate = QtCore.QCoreApplication.translate
        CreateNewVm.setWindowTitle(_translate("CreateNewVm", "Create New VM"))
        self.machineNameLABEL.setText(_translate("CreateNewVm", "Machine Name:"))
        self.typeLABEL.setText(_translate("CreateNewVm", "Type:"))
        self.typeCOMBOBOX.setItemText(0, _translate("CreateNewVm", "POV Entity"))
        self.typeCOMBOBOX.setItemText(1, _translate("CreateNewVm", "Victim Entity"))
        self.createVmLABEL.setText(_translate("CreateNewVm", "Create From Existing VM:"))
        self.openExistingBUTTON.setText(_translate("CreateNewVm", "Open Existing"))
        self.vmOsLABEL.setText(_translate("CreateNewVm", "VM OS:"))
        #####CHANGES START####
        self.vmFilesLABEL.setText(_translate("CreateNewVm", "VM Files:"))
        j = 0
        i = 0
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["Exploits"]
        POVS = db['VulnerablePrograms']
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.vmFilesTREEWIDGET.isSortingEnabled()
        self.vmFilesTREEWIDGET.setSortingEnabled(False)
        """for collection in data.find():
            j=0
            self.vmFilesTREEWIDGET.topLevelItem(i).setText(0, _translate("Export", collection['name']))
            for key in collection:
                if(key!="_id" and key!="name" and key!='File'):
                    self.vmFilesTREEWIDGET.topLevelItem(i).child(j).setText(0, _translate("Export", key + ' : ' + collection[key]))
                    j+=1
            i+=1"""
        i=0
        for collection in data.find():
            self.softwareTREEWIDGET.topLevelItem(i).setText(0, _translate("EditVM", collection['name']))
            self.softwareTREEWIDGET.topLevelItem(i).child(0).setText(0, _translate("EditVM", 'Language : ' + collection['Language']))
            self.softwareTREEWIDGET.topLevelItem(i).child(1).setText(0, _translate("EditVM", 'Platform : ' + collection['Platform']))
            self.softwareTREEWIDGET.topLevelItem(i).child(2).setText(0, _translate("EditVM", 'Type : ' + collection['Type']))
            i+=1
        for collection in POVS.find():
            self.softwareTREEWIDGET.topLevelItem(i).setText(0, _translate("EditVM", collection['name']))
            self.softwareTREEWIDGET.topLevelItem(i).child(0).setText(0, _translate("EditVM", 'Information : ' + collection['Information']))
            i+=1
        self.vmFilesTREEWIDGET.setSortingEnabled(__sortingEnabled)

        #####CHANGES END####

        self.vmOsCOMBOBOX.setItemText(0, _translate("CreateNewVm", "Kali Linux"))
        self.vmOsCOMBOBOX.setItemText(1, _translate("CreateNewVm", "Ubuntu"))
        self.vmOsCOMBOBOX.setItemText(2, _translate("CreateNewVm", "Windows"))
        self.vmFilesAddToVMBUTTON.setText(_translate("CreateNewVm", "Add to VM"))
        self.manageExploitsBUTTON.setText(_translate("CreateNewVm", "Manage Exploits"))
        self.softwareLABEL.setText(_translate("CreateNewVm", "Software:"))
        __sortingEnabled = self.softwareTREEWIDGET.isSortingEnabled()
        self.softwareTREEWIDGET.setSortingEnabled(False)
        self.softwareTREEWIDGET.topLevelItem(0).setText(0, _translate("CreateNewVm", "All"))
        self.softwareTREEWIDGET.topLevelItem(0).child(0).setText(0, _translate("CreateNewVm", "example"))
        self.softwareTREEWIDGET.topLevelItem(1).setText(0, _translate("CreateNewVm", "Linux Specific"))
        self.softwareTREEWIDGET.topLevelItem(1).child(0).setText(0, _translate("CreateNewVm", "example"))
        self.softwareTREEWIDGET.topLevelItem(2).setText(0, _translate("CreateNewVm", "Windows Specific"))
        self.softwareTREEWIDGET.topLevelItem(2).child(0).setText(0, _translate("CreateNewVm", "example"))
        self.softwareTREEWIDGET.setSortingEnabled(__sortingEnabled)
        self.softwareAddBUTTON.setText(_translate("CreateNewVm", "Add to VM"))
        self.discardBUTTON.setText(_translate("CreateNewVm", "Discard"))
        self.saveBUTTON.setText(_translate("CreateNewVm", "Save"))


    def setupSoftware(self, CreateNewVm):
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
        for collection in EXPLOITS.find():
            self.tree["parent{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.softwareTREEWIDGET)
            self.tree["parent{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
            self.tree["child{0}".format(0)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
            self.tree["child{0}".format(1)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
            self.tree["child{0}".format(2)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
            y+=1
        for collection in POVS.find():
            self.tree["parent{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.softwareTREEWIDGET)
            self.tree["parent{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
            self.tree["child{0}".format(0)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(y)])
            y+=1
        return CreateNewVm

    def setupTree(self, CreateNewVm):
            x=0
            y=0
            self.tree={}
            try:
                client = MongoClient(Ui_DBConfiguration.dbConnection)
            except:
                client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
            db = client.Test
            data = db["Exploits"]
            for collection in data.find():
                self.tree["parent{0}".format(x)] = QtWidgets.QTreeWidgetItem(self.vmFilesTREEWIDGET)
                self.tree["parent{0}".format(x)].setCheckState(0, QtCore.Qt.Unchecked)
                #self.tree["parent{0}".format(x)].setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
                for key in collection:
                    if(key!="_id" and key!="name" and key!='File'):
                        self.tree["child{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(x)])
                        #self.tree["child{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
                        y+=1
                x+=1
            return CreateNewVm


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateNewVm = QtWidgets.QWidget()
    ui = Ui_CreateNewVm()
    ui.setupUi(CreateNewVm)
    CreateNewVm.show()
    sys.exit(app.exec_())
