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

class Ui_ManageVulnerablePrograms(object):

    VulnerableProgramsList = {}

    # Opens a file browser window
    def importButtonStatus(self, path):
        try:
            client = MongoClient(Ui_DBConfiguration.dbConnection)
        except:
            client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["VulnerableProgramss"]
        if os.path.exists(path):
            self.importButton.setEnabled(True)

    def fileBrowser(self):
        options = QFileDialog.Options()
        self.dialog = QFileDialog()
        self.dialog.setOptions(options)
        self.path, __ = QFileDialog.getOpenFileName(self.dialog, "Select Directory")

        if self.path:
            #If Windows, change the separator
            if self.path == 'C:\\':
                self.path = self.path.replace('/', '\\')
                self.destinationDirectoryLINEEDIT.setText(self.path)
                #os.chdir(self.path)
                return self.path
            # if Linux-based
            else:
                self.destinationDirectoryLINEEDIT.setText(self.path)
                #os.chdir(self.path)
                return self.path
        else:
            self.destinationDirectoryLINEEDIT.setText(self.path)
            return ""

    def selectVulnerablePrograms(self):
        try:
            client = MongoClient(Ui_DBConfiguration.dbConnection)
        except:
            client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["VulnerableProgramss"]
        x=0
        for collection in data.find():
            if (self.tree["parent{0}".format(x)].checkState(0) == QtCore.Qt.Checked):
                self.VulnerableProgramsList[collection['name']] = collection
            x+=1
        self.translateVulnerablePrograms()

    def translateVulnerablePrograms(self):
        #print(self.VulnerableProgramsList['rubySlippers']['File'])
        for key in self.VulnerableProgramsList:
            self.VulnerableProgramsList[key]['File'] = base64.decodebytes(self.VulnerableProgramsList[key]['File'])

    def importVP(self):
        try:
            client = MongoClient(Ui_DBConfiguration.dbConnection)
        except:
            client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["VulnerablePrograms"]
        file = self.destinationDirectoryLINEEDIT.text()
        fileName = os.path.split(file)
        fileName = fileName[1]#.replace('.',';')
        scenario = {'name' : fileName}
        with open(file, 'rb') as eFile:
            encoded_img = base64.b64encode(eFile.read())
        scenario['File'] = encoded_img

        print("beginning push of " + fileName)
        data.insert_one(scenario)
        self.databseTREEWIDGET.clear()
        self.setupTree(self)
        self.retranslateUi(self)
        QMessageBox.about(self, "Success", fileName + " successfully uploaded!")

    def deleteVP(self):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.databseTREEWIDGET.isSortingEnabled()
        self.databseTREEWIDGET.setSortingEnabled(False)
        try:
            client = MongoClient(Ui_DBConfiguration.dbConnection)
        except:
            client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["VulnerablePrograms"]
        self.count = 0
        deletion = ""
        x=0
        y=0
        id=""
        for collection in data.find():
            for key in collection:
                if(key=="_id"):
                    id = collection[key]
                if(key!="_id" and key!="name"):
                    if(self.tree["parent{0}".format(x)].checkState(0)==QtCore.Qt.Checked):
                        data.delete_one({'_id': id})
                        print(key + " deleted from database.")
            x+=1
        self.databseTREEWIDGET.clear()
        self.setupTree(self)
        self.retranslateUi(self)
        QMessageBox.about(self, "Success", "Items Deleted Succesfully.")


    def setupUi(self, ManageVulnerablePrograms):


        x=0
        y=0
        self.tree={}

        ManageVulnerablePrograms.setObjectName("ManageVulnerablePrograms")
        ManageVulnerablePrograms.resize(622, 479)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManageVulnerablePrograms.sizePolicy().hasHeightForWidth())
        ManageVulnerablePrograms.setSizePolicy(sizePolicy)
        ManageVulnerablePrograms.setMinimumSize(QtCore.QSize(622, 479))
        ManageVulnerablePrograms.setMaximumSize(QtCore.QSize(622, 479))
        self.layoutWidget = QtWidgets.QWidget(ManageVulnerablePrograms)
        self.layoutWidget.setGeometry(QtCore.QRect(31, 34, 551, 411))
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
        self.destinationDirectoryLINEEDIT = QtWidgets.QLineEdit(self.layoutWidget)
        self.destinationDirectoryLINEEDIT.setObjectName("destinationDirectoryLINEEDIT")
        self.horizontalLayout.addWidget(self.destinationDirectoryLINEEDIT)

        self.browserBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.browserBUTTON.setEnabled(True)
        self.browserBUTTON.setObjectName("browserBUTTON")
        self.browserBUTTON.clicked.connect(self.fileBrowser)

        self.horizontalLayout.addWidget(self.browserBUTTON)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.databseTREEWIDGET = QtWidgets.QTreeWidget(self.layoutWidget)
        self.databseTREEWIDGET.setObjectName("databseTREEWIDGET")
        self.databseTREEWIDGET.headerItem().setText(0, "1")
        self.setupTree(ManageVulnerablePrograms)

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
        self.importButton = QtWidgets.QPushButton(self.layoutWidget)
        self.importButton.setObjectName("importButton")
        self.importButton.setEnabled(False)
        self.importButton.clicked.connect(self.importVP)
        self.horizontalLayout_2.addWidget(self.importButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.deleteButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.deleteVP)
        self.horizontalLayout_2.addWidget(self.deleteButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.nextButton = QtWidgets.QPushButton(self.layoutWidget)
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.selectVulnerablePrograms)
        self.destinationDirectoryLINEEDIT.textChanged.connect(self.importButtonStatus)
        #self.nextButton.clicked.connect(self.progress)
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ManageVulnerablePrograms)
        QtCore.QMetaObject.connectSlotsByName(ManageVulnerablePrograms)

    def retranslateUi(self, ManageVulnerablePrograms):
        j = 0
        i = 0
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["VulnerablePrograms"]
        _translate = QtCore.QCoreApplication.translate
        ManageVulnerablePrograms.setWindowTitle(_translate("ManageVulnerablePrograms", "Manage Vulnerable Programs"))
        self.destinationDirectoryLABEL.setText(_translate("ManageVulnerablePrograms", "Destination Directory:"))
        self.browserBUTTON.setText(_translate("ManageVulnerablePrograms", "Browse"))
        __sortingEnabled = self.databseTREEWIDGET.isSortingEnabled()
        self.databseTREEWIDGET.setSortingEnabled(False)
        for collection in data.find():
            j=0
            self.databseTREEWIDGET.topLevelItem(i).setText(0, _translate("Export", collection['name']))
            for key in collection:
                if(key!="_id" and key!="name" and key!='File'):
                    self.databseTREEWIDGET.topLevelItem(i).child(j).setText(0, _translate("Export", key + ' : ' + collection[key]))
                    j+=1
            i+=1
        self.databseTREEWIDGET.setSortingEnabled(__sortingEnabled)
        self.backBUTTON.setText(_translate("ManageVulnerablePrograms", "Back"))
        self.deleteButton.setText(_translate("ManageExploits", "Delete"))
        self.importButton.setText(_translate("ManageVulnerablePrograms", "Import"))
        self.nextButton.setText(_translate("ManageVulnerablePrograms", "Next"))

    def setupTree(self, ManageVulnerablePrograms):
        x=0
        y=0
        try:
            client = MongoClient(Ui_DBConfiguration.dbConnection)
        except:
            client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["VulnerablePrograms"]
        for collection in data.find():
            self.tree["parent{0}".format(x)] = QtWidgets.QTreeWidgetItem(self.databseTREEWIDGET)
            self.tree["parent{0}".format(x)].setCheckState(0, QtCore.Qt.Unchecked)
            #self.tree["parent{0}".format(x)].setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
            for key in collection:
                if(key!="_id" and key!="name" and key!='File'):
                    self.tree["child{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(x)])
                    #self.tree["child{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
                    y+=1
            x+=1
        return ManageVulnerablePrograms


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageVulnerablePrograms = QtWidgets.QWidget()
    ui = Ui_ManageVulnerablePrograms()
    ui.setupUi(ManageVulnerablePrograms)
    ManageVulnerablePrograms.show()
    sys.exit(app.exec_())
