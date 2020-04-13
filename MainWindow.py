# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from ManageData import Ui_ManageData
from PyQt5.QtWidgets import QFileDialog
import os, sys
import base64
from pymongo import MongoClient
from bson.objectid import ObjectId
from zipfile import ZipFile
from datetime import date
import time


class Ui_MainWindow(object):

    # Opens the scenarioRunningWindow on run button click############################3
    def openScenarioRunningWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ManageData()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(598, 459)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(598, 459))
        MainWindow.setMaximumSize(QtCore.QSize(598, 459))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(240, 20, 121, 51))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("med.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 80, 521, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        font = QtGui.QFont("Helvetica [Cronyx]", 16) # label
        self.qlabel = QtWidgets.QLabel("List of Scenarios")
        self.qlabel.setFont(font)
        self.verticalLayout.addWidget(self.qlabel) # label added 
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchLABEL = QtWidgets.QLabel(self.layoutWidget)
        self.searchLABEL.setObjectName("searchLABEL")
        self.horizontalLayout_3.addWidget(self.searchLABEL)
        self.searchEDITBOX = QtWidgets.QLineEdit(self.layoutWidget)
        self.searchEDITBOX.setText("")
        self.searchEDITBOX.setObjectName("searchEDITBOX")
        self.horizontalLayout_3.addWidget(self.searchEDITBOX)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.DATEEDIT = QtWidgets.QDateEdit(self.layoutWidget)
        self.DATEEDIT.setObjectName("DATEEDIT")
        self.horizontalLayout.addWidget(self.DATEEDIT)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ####################################scenariosLIST######################################
        self.scenariosLIST = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scenariosLIST.sizePolicy().hasHeightForWidth())
        self.scenariosLIST.setSizePolicy(sizePolicy)
        self.scenariosLIST.setIconSize(QtCore.QSize(0, 0))
        self.scenariosLIST.setResizeMode(QtWidgets.QListView.Fixed)
        self.scenariosLIST.setViewMode(QtWidgets.QListView.ListMode)
        self.scenariosLIST.setUniformItemSizes(False)
        self.scenariosLIST.setWordWrap(False)
        self.scenariosLIST.setSelectionRectVisible(False)
        self.scenariosLIST.setObjectName("scenariosLIST")
        self.verticalLayout.addWidget(self.scenariosLIST)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        #################################### END scenariosLIST######################################
        ####################################scenarioInfoLISTWIDGET######################################
        self.scenarioInfoLISTWIDGET = QtWidgets.QListWidget(self.layoutWidget)
        self.scenarioInfoLISTWIDGET.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.scenarioInfoLISTWIDGET.setObjectName("scenarioInfoLISTWIDGET")
        item = QtWidgets.QListWidgetItem() # item 0
        item.setTextAlignment(QtCore.Qt.AlignCenter) 
        font = QtGui.QFont("Helvetica [Cronyx]", 14) 
        item.setFont(font) 
        self.scenarioInfoLISTWIDGET.addItem(item) 
        item = QtWidgets.QListWidgetItem() # item 1
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.scenarioInfoLISTWIDGET.addItem(item) 
        item = QtWidgets.QListWidgetItem() # item 2
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.scenarioInfoLISTWIDGET.addItem(item) 
        item = QtWidgets.QListWidgetItem() # item 3
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.scenarioInfoLISTWIDGET.addItem(item)
        item = QtWidgets.QListWidgetItem() # item 4
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.scenarioInfoLISTWIDGET.addItem(item)
        self.horizontalLayout_2.addWidget(self.scenarioInfoLISTWIDGET)
        ####################################END scenarioInfoLISTWIDGET######################################
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.runBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBUTTON.sizePolicy().hasHeightForWidth())
        self.runBUTTON.setSizePolicy(sizePolicy)
        self.runBUTTON.setObjectName("runBUTTON")
        self.horizontalLayout_8.addWidget(self.runBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.configureBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configureBUTTON.sizePolicy().hasHeightForWidth())
        self.configureBUTTON.setSizePolicy(sizePolicy)
        self.configureBUTTON.setObjectName("configureBUTTON")
        self.horizontalLayout_8.addWidget(self.configureBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.setupBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setupBUTTON.sizePolicy().hasHeightForWidth())
        self.setupBUTTON.setSizePolicy(sizePolicy)
        self.setupBUTTON.setObjectName("setupBUTTON")
        self.horizontalLayout_8.addWidget(self.setupBUTTON)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # Manage data button##############################
        self.manageDataBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.manageDataBUTTON.setObjectName("manageDataBUTTON")
        self.horizontalLayout_6.addWidget(self.manageDataBUTTON)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.configureDatabaseBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.configureDatabaseBUTTON.setObjectName("configureDatabaseBUTTON")
        self.horizontalLayout_6.addWidget(self.configureDatabaseBUTTON)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.manageScenarioBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manageScenarioBUTTON.sizePolicy().hasHeightForWidth())
        self.manageScenarioBUTTON.setSizePolicy(sizePolicy)
        self.manageScenarioBUTTON.setObjectName("manageScenarioBUTTON")
        self.horizontalLayout_6.addWidget(self.manageScenarioBUTTON)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.scenariosLIST.clicked.connect(self.listViewClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def listViewClicked(self, MainWindow):
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["Scenario"]
        _translate = QtCore.QCoreApplication.translate
        scen = ""
        type = ""
        type2 = ''
        item = self.scenariosLIST.currentItem()
        collections = data.find_one({"scenario.name":item.text()})
        scen = collections['scenario']
        type = scen['exploit']
        type2 = scen['pov']
        item = self.scenarioInfoLISTWIDGET.item(0) # added a new item
        item.setText(_translate("MainWindow", "Scenario Details"))
        item = self.scenarioInfoLISTWIDGET.item(1)
        item.setText(_translate("MainWindow", "Date Created: " + scen["date_created"]))
        item = self.scenarioInfoLISTWIDGET.item(2)
        item.setText(_translate("MainWindow", "Date Modified: " + scen['date_modified']))
        item = self.scenarioInfoLISTWIDGET.item(3)
        item.setText(_translate("MainWindow", "Exploit: " + type['file']))
        item = self.scenarioInfoLISTWIDGET.item(4)
        item.setText(_translate("MainWindow", "Vulnerable Program: " + type2['file']))

    def retranslateUi(self, MainWindow):
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["Scenario"]
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchLABEL.setText(_translate("MainWindow", "Search"))
        self.scenariosLIST.setSortingEnabled(False)
        __sortingEnabled = self.scenariosLIST.isSortingEnabled()
        self.scenariosLIST.setSortingEnabled(False)
        x = 0
        scen = ""
        type = ""
        type2 = ''
        for collection in data.find():
            self.scenariosLIST.addItem(QtWidgets.QListWidgetItem())
            item = self.scenariosLIST.item(x)
            scen = collection['scenario']
            type = scen['exploit']
            type2 = scen['pov']
            
            # Prevents NoneType Error
            if not item:
                continue
            item.setText(_translate("MainWindow", scen['name'])) #SCENARIO NAME IS CHANGED HERE
            x+=1
        self.scenariosLIST.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.scenarioInfoLISTWIDGET.isSortingEnabled()
        self.scenarioInfoLISTWIDGET.setSortingEnabled(False)
        item = self.scenarioInfoLISTWIDGET.item(0)  # added a new item
        item.setText(_translate("MainWindow", "Scenario Details"))
        self.scenarioInfoLISTWIDGET.setSortingEnabled(__sortingEnabled)
        self.runBUTTON.setText(_translate("MainWindow", "Run"))
        self.configureBUTTON.setText(_translate("MainWindow", "Configure"))
        self.setupBUTTON.setText(_translate("MainWindow", "Setup"))
        self.manageDataBUTTON.setText(_translate("MainWindow", "Manage Data"))
        self.configureDatabaseBUTTON.setText(_translate("MainWindow", "Configure Database"))
        self.manageScenarioBUTTON.setText(_translate("MainWindow", "Manage Scenario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
