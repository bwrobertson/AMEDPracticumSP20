# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuggestedSetup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem
from pymongo import MongoClient
import json
from NewScenario import Ui_NewScenario
from bson.objectid import ObjectId
from DBConfiguration import Ui_DBConfiguration
from MainWindow import Ui_MainWindow
import os
import platform


class Ui_Form(object):

    id = "5e9801a1e6c7aa9190f814dc"
    thisPlat = platform.system()
    if(thisPlat=="Windows"):
        path = "C:/"
    elif(thisPlat=='Mac'):
        #need this verified by a mac buddy
        path= '/'
    elif(thisPlat=='Linux'):
        #need a linux buddy to fill this in with the base directory
        path = '/bin'
    try:
        for x in os.walk(path):
            if('\\VirtualBox VMs' in str(x)):
                thisPath = (x[0])
                break
        vmList = os.listdir(thisPath)
    except:
        vmList = []

    def runScen(self):

        db = Ui_Form.client.Test
        data = Ui_DBConfiguration.db["Scenario"]


        scen = data.find_one({'_id': ObjectId(Ui_NewScenario.id)})
        #scen = data.find_one({'_id': ObjectId("5e840e238a71b65203287a0a")})
        newScen = scen
        if(Ui_NewScenario.id!=0):
            Ui_Form.id = Ui_NewScenario.id
        else:
            Ui_Form.id = Ui_MainWindow.id

        #machines = dictScen['machines']

        itemVictims =  [str(self.listWidget_2.item(i).text()) for i in range(self.listWidget_2.count())]
        #print(itemVictims)

        itemAttackers =  [str(self.listWidget_3.item(i).text()) for i in range(self.listWidget_3.count())]
        #print(itemAttackers)
        victims = {}
        attackers = {}
        x = 1
        for item in itemVictims:
            victims['victim' + str(x)] = item
            x+=1

        x = 1
        for item in itemAttackers:
            attackers['attacker' + str(x)] = item
            x+=1

        machines = {'victim': victims}
        machines['attacker'] = attackers
        #print(machines)
        thisScen = newScen['scenario']
        thisScen['machines'] = machines
        #print(newScen)
        #data.delete_one({'_id': ObjectId("5e840e238a71b65203287a0a")})
        data.delete_one({'_id': ObjectId(Ui_NewScenario.id)})
        data.insert_one(newScen)



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(753, 480)
        Form.setMinimumSize(QtCore.QSize(753, 480))
        Form.setMaximumSize(QtCore.QSize(753, 480))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 721, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_2.setObjectName("listWidget_3")
        self.listWidget_2.setAcceptDrops(True)
        self.listWidget_2.setDragEnabled(False)
        self.gridLayout.addWidget(self.listWidget_2, 1, 3, 2, 1)
        self.addVmBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.addVmBUTTON.setObjectName("addVmBUTTON")
        self.gridLayout.addWidget(self.addVmBUTTON, 4, 6, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_3.setObjectName("listWidget_2")
        self.listWidget_3.setAcceptDrops(True)
        self.listWidget_3.setDragEnabled(False)
        self.gridLayout.addWidget(self.listWidget_3, 1, 0, 2, 2)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setAcceptDrops(False)
        self.listWidget.setDragEnabled(True)

        self.buildSetup()


        self.listWidget_2.setIconSize(QSize(40, 40))
        self.listWidget_3.setIconSize(QSize(40, 40))
        self.listWidget.setIconSize(QSize(40, 40))
        self.gridLayout.addWidget(self.listWidget, 1, 7, 1, 1)
        self.nextBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.nextBUTTON.setObjectName("nextBUTTON")
        #self.nextBUTTON.clicked.connect(runScen())
        self.gridLayout.addWidget(self.nextBUTTON, 4, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 5, 2, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 7, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.layoutWidget)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 4, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Suggested Setup", "Suggested Setup"))
        self.addVmBUTTON.setText(_translate("Form", "Add Machine"))
        self.label_2.setText(_translate("Form", "Victim"))
        self.nextBUTTON.setText(_translate("Form", "Next"))
        self.label.setText(_translate("Form", "Exploit"))
        self.label_3.setText(_translate("Form", "Available Machines"))
        self.backButton.setText(_translate("Form", "Back"))

    def refreshSetup(self):
        self.buildSetup()

    def buildSetup(self):
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        data = Ui_DBConfiguration.db["Scenario"]

        for x in Ui_Form.vmList:
            if('malware' in x):
                self.listWidget.insertItem(1, QListWidgetItem(QIcon("vmmalware.png"), x))
            else:
                self.listWidget.insertItem(1, QListWidgetItem(QIcon("vm.png"), x))        
        try:
            try:
                thisData = data.find_one({'_id': ObjectId(Ui_MainWindow.id)})
                print('using correct')
            except:
                thisData = data.find_one({'_id': ObjectId(Ui_Form.id)})
                print('using default')
            try:
                thisScen = thisData['scenario']
                thisMach = thisScen['machines']
                thisVic = thisMach['victim']
                thisAtt = thisMach['attacker']
                x=1
                temp = ""
                vms = []
                malware = []
                for item in thisVic:
                    if((thisVic.get(item) in vms)==False):
                        vms.append(thisVic.get(item))
                    #if((thisVic.get(item) in Ui_Form.vmList)==False):
                        #Ui_Form.vmList.append(thisVic.get(item))
                for item in thisAtt:
                    if((thisAtt.get(item) in malware)==False):
                        malware.append(thisAtt.get(item))
                    #if((thisAtt.get(item) in Ui_Form.vmList)==False):
                        #Ui_Form.vmList.append(thisAtt.get(item))

                #Ui_Form.vmList.sort()


                for x in vms:
                    self.listWidget_3.insertItem(1, QListWidgetItem(QIcon("vm.png"), x))

                for x in malware:
                    if('malware' in x):
                        self.listWidget_2.insertItem(1, QListWidgetItem(QIcon("vmmalware.png"), x))
                    else:
                        self.listWidget_2.insertItem(1, QListWidgetItem(QIcon("vm.png"), x))
            except:
                print('no machines found')
        except:
            print('starting up')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
