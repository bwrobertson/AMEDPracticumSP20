# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Scenario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os, sys
import base64
from pymongo import MongoClient
from bson.objectid import ObjectId
from zipfile import ZipFile
from datetime import date
import time
import ScenarioJsonTemplate as template

class Ui_NewScenario(object):

    # def exploitBrowser(self):
    #     exploitOptions = QFileDialog.Options()
    #     self.exploitDialog = QFileDialog()
    #     self.exploitDialog.setOptions(exploitOptions)
    #     self.exploitPath, __ = QFileDialog.getOpenFileName(self.exploitDialog, "Select Exploit", '/home')

    #     if self.exploitPath:
    #         #If Windows, change the separator
    #         if self.exploitPath == 'C:\\':
    #             self.exploitPath = self.exploitPath.replace('/', '\\')
    #             self.exploitLINEEDIT.setText(self.exploitPath)
    #             #os.chdir(self.exploitPath)
    #             return self.exploitPath
    #         # if Linux-based
    #         else:
    #             self.exploitLINEEDIT.setText(self.exploitPath)
    #             #os.chdir(self.exploitPath)
    #             return self.exploitPath
    #     else:
    #         self.exploitLINEEDIT.setText(self.exploitPath)
    #         return ""

    # def vulnerableProgramBrowser(self):
    #     VPoptions = QFileDialog.Options()
    #     self.VPdialog = QFileDialog()
    #     self.VPdialog.setOptions(VPoptions)
    #     self.vulnerableProgramPath, __ = QFileDialog.getOpenFileName(self.VPdialog, "Select Vulnerable Program", '/home')

    #     if self.vulnerableProgramPath:
    #         #If Windows, change the separator
    #         if self.vulnerableProgramPath == 'C:\\':
    #             self.vulnerableProgramPath = self.vulnerableProgramPath.replace('/', '\\')
    #             self.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
    #             #os.chdir(self.vulnerableProgramPath)
    #             return self.vulnerableProgramPath
    #         # if Linux-based
    #         else:
    #             self.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
    #             #os.chdir(self.vulnerableProgramPath)
    #             return self.vulnerableProgramPath
    #     else:
    #         self.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
    #         return ""

    def storeScenario(self, jd):
        client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["Scenario"]

        today = date.today()
        today = today.strftime("%d%b%Y")
        scenName = str(today) + self.scenarioLINEEDIT.text()
        encodedFile = ""
        #exploitName = self.exploitLINEEDIT.text()
        exploitName = self.exploitPath
        #VPname = self.vulnerableProgramLINEEDIT.text()
        VPname = self.vulnerableProgramPath

        jd["name"] = scenName
        jd["date_created"] = today
        jd["date_modified"] = today
        jd["exploit"] = {"file" : exploitName}
        jd["pov"] = {"file" : VPname}

        # scenarioStore = {"name": scenName}
        # scenarioStore['Date'] = today
        # scenarioStore["Exploit"] = exploitName
        # scenarioStore["VulnerableProgram"] = VPname

        jsondata = {"scenario" : jd}
        print("beginning push")
        data.insert_one(jsondata)
        print("end push")
        # self.manageExploits = ct.ManageExploitsWindow()
        # self.manageExploits.show

    def createScenario(self):
        data = template.ScenarioJsonTemplate.createJson(self)
        print(data)

        self.storeScenario(data)

    def setupUi(self, NewScenario):
        NewScenario.setObjectName("NewScenario")
        NewScenario.resize(512, 313)
        NewScenario.setMinimumSize(QtCore.QSize(512, 313))
        NewScenario.setMaximumSize(QtCore.QSize(512, 313))
        self.widget = QtWidgets.QWidget(NewScenario)
        self.widget.setGeometry(QtCore.QRect(10, 20, 491, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scenarioNameLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.scenarioNameLABEL.setFont(font)
        self.scenarioNameLABEL.setObjectName("scenarioNameLABEL")
        self.verticalLayout.addWidget(self.scenarioNameLABEL)
        self.scenarioLINEEDIT = QtWidgets.QLineEdit(self.widget)
        self.scenarioLINEEDIT.setObjectName("scenarioLINEEDIT")
        self.verticalLayout.addWidget(self.scenarioLINEEDIT)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.exploitLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exploitLABEL.setFont(font)
        self.exploitLABEL.setObjectName("exploitLABEL")
        self.verticalLayout_2.addWidget(self.exploitLABEL)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exploitLINEEDIT = QtWidgets.QLineEdit(self.widget)
        self.exploitLINEEDIT.setObjectName("exploitLINEEDIT")
        self.horizontalLayout.addWidget(self.exploitLINEEDIT)
        self.exploitBrowseBUTTON = QtWidgets.QPushButton(self.widget)
        self.exploitBrowseBUTTON.setObjectName("exploitBrowseBUTTON")
        #self.exploitBrowseBUTTON.clicked.connect(self.exploitBrowser)
        self.horizontalLayout.addWidget(self.exploitBrowseBUTTON)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vulnerableProgramLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vulnerableProgramLABEL.setFont(font)
        self.vulnerableProgramLABEL.setObjectName("vulnerableProgramLABEL")
        self.verticalLayout_3.addWidget(self.vulnerableProgramLABEL)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vulnerableProgramLINEEDIT = QtWidgets.QLineEdit(self.widget)
        self.vulnerableProgramLINEEDIT.setObjectName("vulnerableProgramLINEEDIT")
        self.horizontalLayout_2.addWidget(self.vulnerableProgramLINEEDIT)
        self.vulnerableProgramBrowseBUTTON = QtWidgets.QPushButton(self.widget)
        self.vulnerableProgramBrowseBUTTON.setObjectName("vulnerableProgramBrowseBUTTON")
        #self.vulnerableProgramBrowseBUTTON.clicked.connect(self.vulnerableProgramBrowser)
        self.horizontalLayout_2.addWidget(self.vulnerableProgramBrowseBUTTON)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancelBUTTON = QtWidgets.QPushButton(self.widget)
        self.cancelBUTTON.setObjectName("cancelBUTTON")
        self.horizontalLayout_3.addWidget(self.cancelBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.addBUTTON = QtWidgets.QPushButton(self.widget)
        self.addBUTTON.setObjectName("addBUTTON")
        self.horizontalLayout_3.addWidget(self.addBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.nextBUTTON = QtWidgets.QPushButton(self.widget)
        self.nextBUTTON.setObjectName("nextBUTTON")
        self.nextBUTTON.clicked.connect(self.createScenario)
        self.horizontalLayout_3.addWidget(self.nextBUTTON)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.retranslateUi(NewScenario)
        QtCore.QMetaObject.connectSlotsByName(NewScenario)

    def retranslateUi(self, NewScenario):
        _translate = QtCore.QCoreApplication.translate
        NewScenario.setWindowTitle(_translate("NewScenario", "New Scenario"))
        self.scenarioNameLABEL.setText(_translate("NewScenario", "Scenario Name:"))
        self.exploitLABEL.setText(_translate("NewScenario", "Exploit:"))
        self.exploitBrowseBUTTON.setText(_translate("NewScenario", "Browse"))
        self.vulnerableProgramLABEL.setText(_translate("NewScenario", "Vulnerable Program:"))
        self.vulnerableProgramBrowseBUTTON.setText(_translate("NewScenario", "Browse"))
        self.cancelBUTTON.setText(_translate("NewScenario", "Cancel"))
        self.addBUTTON.setText(_translate("NewScenario", "Add"))
        self.nextBUTTON.setText(_translate("NewScenario", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewScenario = QtWidgets.QWidget()
    ui = Ui_NewScenario()
    ui.setupUi(NewScenario)
    NewScenario.show()
    #sys.exit(app.exec_())
