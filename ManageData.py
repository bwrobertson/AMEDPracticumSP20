# -*- coding: utf-8 -*-
############################################
#           Changes Start Here             #
############################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os, sys
import base64
from pymongo import MongoClient 
from bson.objectid import ObjectId
from zipfile import ZipFile
############################################
#           Changes End   Here             #
############################################

class Ui_ManageData(object):
    ############################################
    #           Changes Start Here             #
    ############################################
    # Opens a file browser window
    def exportButtonStatus(self, path):
        if os.path.exists(path):
            self.exportBUTTON.setEnabled(True)

    def fileBrowser(self):
        options = QFileDialog.Options()
        self.dialog = QFileDialog()
        self.dialog.setOptions(options)
        self.path = str(QFileDialog.getExistingDirectory(self.dialog, "Select Directory"))
        
        if self.path:
        #If Windows, change the separator
            if os.sep == '\\':
                self.path = self.path.replace('/', '\\')
                self.destinationDirectoryLINEEDIT.setText(self.path)
                os.chdir(self.path)
            return self.path
        else:
            self.destinationDirectoryLINEEDIT.setText(self.path)
            return ""
    ############################################
    #           Changes End   Here             #
    ############################################

    def setupUi(self, ManageData):
        ############################################
        #           Changes Start Here             #
        ############################################
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test") 
        db = client.Test
        data = db["Demo"]
        x=0
        y=0
        self.tree={}
        ############################################
        #           Changes End   Here             #
        ############################################
        ManageData.setObjectName("ManageData")
        ManageData.resize(622, 479)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManageData.sizePolicy().hasHeightForWidth())
        ManageData.setSizePolicy(sizePolicy)
        ManageData.setMinimumSize(QtCore.QSize(622, 479))
        ManageData.setMaximumSize(QtCore.QSize(622, 479))
        self.layoutWidget = QtWidgets.QWidget(ManageData)
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

        #Browse button##########################################
        self.browserBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.browserBUTTON.setEnabled(True)
        self.browserBUTTON.setObjectName("browserBUTTON")
        ####clicked function################
        self.browserBUTTON.clicked.connect(self.fileBrowser)
        ####################################################

        self.horizontalLayout.addWidget(self.browserBUTTON)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        #Tree widget for database
        self.databseTREEWIDGET = QtWidgets.QTreeWidget(self.layoutWidget)
        self.databseTREEWIDGET.setObjectName("databseTREEWIDGET")
        self.databseTREEWIDGET.headerItem().setText(0, "1")
        ############################################
        #           Changes Start Here             #
        ############################################
        for collection in data.find():
            self.tree["parent{0}".format(x)] = QtWidgets.QTreeWidgetItem(self.databseTREEWIDGET)
            self.tree["parent{0}".format(x)].setCheckState(0, QtCore.Qt.Unchecked)
            self.tree["parent{0}".format(x)].setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
            for key in collection:
                if(key!="_id" and key!="name"):
                    self.tree["child{0}".format(y)] = QtWidgets.QTreeWidgetItem(self.tree["parent{0}".format(x)])
                    self.tree["child{0}".format(y)].setCheckState(0, QtCore.Qt.Unchecked)
                    y+=1
            x+=1    
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
        self.deleteBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteBUTTON.setObjectName("deleteBUTTON")
        self.deleteBUTTON.clicked.connect(self.deleteSelected)
        self.horizontalLayout_2.addWidget(self.deleteBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.exportBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.exportBUTTON.setObjectName("exportBUTTON")
        ############################################
        #           Changes Start Here             #
        ############################################     
        self.exportBUTTON.setEnabled(False)
        self.destinationDirectoryLINEEDIT.textChanged.connect(self.exportButtonStatus)   
        self.exportBUTTON.clicked.connect(self.progress)
        ############################################
        #           Changes End   Here             #
        ############################################
        self.horizontalLayout_2.addWidget(self.exportBUTTON)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)

        self.retranslateUi(ManageData)
        QtCore.QMetaObject.connectSlotsByName(ManageData)

    def retranslateUi(self, ManageData):
        ############################################
        #           Changes Start Here             #
        ############################################
        j = 0
        i = 0
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test") 
        db = client.Test
        data = db["Demo"]
        ############################################
        #           Changes End   Here             #
        ############################################
        _translate = QtCore.QCoreApplication.translate
        ManageData.setWindowTitle(_translate("ManageData", "Manage Data"))
        self.destinationDirectoryLABEL.setText(_translate("ManageData", "Destination Directory:"))
        self.browserBUTTON.setText(_translate("ManageData", "Browse"))
        __sortingEnabled = self.databseTREEWIDGET.isSortingEnabled()
        self.databseTREEWIDGET.setSortingEnabled(False)
        ############################################
        #           Changes Start Here             #
        ############################################
        for collection in data.find():
            j=0
            self.databseTREEWIDGET.topLevelItem(i).setText(0, _translate("Export", collection['name']))
            for key in collection:
                if(key!="_id" and key!="name"):
                    self.databseTREEWIDGET.topLevelItem(i).child(j).setText(0, _translate("Export", key))
                    j+=1
            i+=1
        ############################################
        #           Changes End   Here             #
        ############################################
        self.databseTREEWIDGET.setSortingEnabled(__sortingEnabled)
        self.backBUTTON.setText(_translate("ManageData", "Back"))
        self.deleteBUTTON.setText(_translate("ManageData", "Delete Selected"))
        self.exportBUTTON.setText(_translate("ManageData", "Export Selected"))

    ############################################
    #           Changes Start Here             #
    ############################################

    def progress(self):
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test") 
        db = client.Test
        data = db["Demo"]
        self.count = 0
        numFiles = 0
        x=0
        y=0
        for collection in data.find():
                #if (self.tree["parent{0}".format(x)] == QtCore.Qt.Checked):
                for key in collection:
                    if(key!="_id" and key!="name"):
                        if(self.tree["child{0}".format(y)].checkState(0)== QtCore.Qt.Checked):
                            numFiles+=1
                        y+=1
           
        tickSize = int(100/numFiles)
        print(tickSize)
        x=0
        y=0
        fileName = ""
        fileContent = ""
        with ZipFile('test.zip', 'w') as newzip:
            for collection in data.find():
                #if (self.tree["parent{0}".format(x)] == QtCore.Qt.Checked):
                for key in collection:
                    if(key!="_id" and key!="name"):
                        if(self.tree["child{0}".format(y)].checkState(0)== QtCore.Qt.Checked):
                            fileName = collection["name"] + key
                            fileContent = collection[key]
                            if(key == "PCAP"):
                                fileName = fileName + ".pcap"
                            elif(key == "log"):
                                fileName = fileName + ".log"
                            else:
                                fileName = fileName + ".jpg"
                            with open(fileName, "wb") as decoded_image:
                                decoded_image.write(base64.decodebytes(fileContent))
                                print(fileName + " written to " + self.path)
                                newzip.write(fileName)
                            os.remove(fileName)
                            self.count+=tickSize
                            print(self.count)
                            self.progressBar.setValue(self.count)
                        y+=1
                x+=1          


        return


    def deleteSelected(self):
        #Not yet completed
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test") 
        db = client.Test
        data = db["Demo"]
        self.count = 0
        numFiles = 0
        y=0
        for collection in data.find():
            for key in collection:
                if(key!="_id" and key!="name"):
                    if(self.tree["child{0}".format(y)].checkState(0)== QtCore.Qt.Checked):
                        data.delete_one(key)
                    y+=1
    
    ############################################
    #           Changes End   Here             #
    ############################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageData = QtWidgets.QWidget()
    ui = Ui_ManageData()
    ui.setupUi(ManageData)
    ManageData.show()
    sys.exit(app.exec_())

