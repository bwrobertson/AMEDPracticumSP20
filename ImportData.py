# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importData.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import time
from datetime import date
from pymongo import MongoClient
import json
from DBConfiguration import Ui_DBConfiguration
import base64
import os
import magic

class Ui_importData(object):

    def scenarioBrowser(self):
        scenarioOptions = QFileDialog.Options()
        self.scenarioDialog = QFileDialog()
        self.scenarioDialog.setOptions(scenarioOptions)
        self.scenarioPath, __ = QFileDialog.getOpenFileName(self.scenarioDialog, "Select scenario")

        if self.scenarioPath:
            #If Windows, change the separator
            if self.scenarioPath == 'C:\\':
                self.scenarioPath = self.scenarioPath.replace('/', '\\')
                self.lineEdit_2.setText(self.scenarioPath)
                #os.chdir(self.scenarioPath)
                return self.scenarioPath
            # if Linux-based
            else:
                self.lineEdit_2.setText(self.scenarioPath)
                #os.chdir(self.scenarioPath)
                return self.scenarioPath
        else:
            self.lineEdit_2.setText(self.scenarioPath)
            return ""



    def setupUi(self, importData):
        importData.setObjectName("importData")
        importData.resize(523, 390)
        importData.setMinimumSize(QtCore.QSize(523, 390))
        importData.setMaximumSize(QtCore.QSize(523, 390))
        self.layoutWidget = QtWidgets.QWidget(importData)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 481, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.scenarioBrowser)
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.layoutWidget_2 = QtWidgets.QWidget(importData)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 330, 271, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pushScenario)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(importData)
        QtCore.QMetaObject.connectSlotsByName(importData)

    def retranslateUi(self, importData):
        _translate = QtCore.QCoreApplication.translate
        importData.setWindowTitle(_translate("importData", "Import Data"))
        self.label.setText(_translate("importData", "File type:"))
        self.comboBox.setItemText(0, _translate("importData", "Vulnerable Program"))
        self.comboBox.setItemText(1, _translate("importData", "Scenario"))
        self.comboBox.setItemText(2, _translate("importData", "Exploit"))
        self.comboBox.setItemText(3, _translate("importData", "VM"))
        self.comboBox.setItemText(4, _translate("importData", "Other"))
        self.label_2.setText(_translate("importData", "Name:"))
        self.label_3.setText(_translate("importData", "File Path:"))
        self.pushButton.setText(_translate("importData", "Browse"))
        self.pushButton_3.setText(_translate("importData", "Import"))
        self.pushButton_2.setText(_translate("importData", "Back"))

    def pushScenario(self):
        folder = str(self.comboBox.currentText())
        if(folder=='Exploit'):
            self.importExploit()
        elif(folder == 'Vulnerable Program'):
            self.importVP()

        """data = Ui_DBConfiguration.db[folder]
        today = date.today()
        today = today.strftime("%d%b%Y")

        absolutePath = self.scenarioPath

        # try:
        with open(absolutePath, "rb") as image_file:
            encoded_img = base64.b64encode(image_file.read())

        #m = hashlib.sha256(encoded_content) # Hashed encoded data
        file_name = self.lineEdit.text()
        d = {'name' : file_name}
        d['file'] = encoded_img # to recover base64.b64decode(encoded_content.encode()).decode()
        #d['hash'] = m.hexdigest()

        data.insert_one(d)
        #QMessage.about(self, "Select Folder", "File uploaded.")
        # except:
        #     print("ImportData.py -- pushScenario.")

        return"""

    def importExploit(self):
        data = Ui_DBConfiguration.db["Exploits"]
        file = self.lineEdit.text()
        fileName = os.path.split(file)
        fileName = fileName[1]#.replace('.',';')
        absolutePath = self.scenarioPath
        scenario = {'name' : fileName}
        with open(absolutePath, 'rb') as eFile:
            encoded_img = base64.b64encode(eFile.read())
        scenario['File'] = encoded_img

        scenario['Language'] = magic.from_file(absolutePath)

        Platform = ['Windows', 'Mac', 'Linux', 'Unix']
        netCon = ['Local', 'Remote']

        scenario['Platform'] = ''
        scenario['Type'] = ''
        with open(absolutePath) as f:
            try:
                scenario['Type'] = next((x for x in netCon if x in f.read()), False)
            except:
                scenario['Type']='Unknown'
        f.close()

        with open(absolutePath) as f:
            try:
                scenario['Platform'] = next((x for x in Platform if x in f.read()), False)
            except:
                scenario['Platform']='Multiple'
        f.close()

        if(scenario['Platform']==False):
            scenario['Platform']='Multiple'

        if(scenario['Type']==False):
            scenario['Type']='Unknown'

        print("beginning push of " + fileName)
        data.insert_one(scenario)
        QMessageBox.about(self, "Success", fileName + " successfully uploaded!")

    def importVP(self):
        data = Ui_DBConfiguration.db["VulnerablePrograms"]
        file = self.lineEdit.text()
        fileName = os.path.split(file)
        fileName = fileName[1]#.replace('.',';')
        absolutePath = self.scenarioPath
        scenario = {'name' : fileName}
        with open(absolutePath, 'rb') as eFile:
            encoded_img = base64.b64encode(eFile.read())
        scenario['File'] = encoded_img

        #print(magic.from_file(file, mime=True))
        scenario['Information'] = magic.from_file(absolutePath)
        print("beginning push of " + fileName)
        data.insert_one(scenario)
        QMessageBox.about(self, "Success", fileName + " successfully uploaded!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    importData = QtWidgets.QWidget()
    ui = Ui_importData()
    ui.setupUi(importData)
    importData.show()
    sys.exit(app.exec_())
