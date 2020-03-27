# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Scenario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ManageVulnerablePrograms import Ui_ManageVulnerablePrograms
from ManageExploits import Ui_ManageExploits

class Ui_NewScenario(object):

    # function to open either manage vulnerable programs window
    # or exploits window
    # param windowName is passed via lambda expression to indicate which window to open
    def openWindow(self, windowName):
        self.window = QtWidgets.QWidget()
        if windowName == "VulnerableProgramsWindow":
            self.ui = Ui_ManageVulnerablePrograms()
        else:
            self.ui = Ui_ManageExploits()
        self.ui.setupUi(self.window)
        self.window.show()

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
        self.horizontalLayout.addWidget(self.exploitBrowseBUTTON)
        
        # added signal to display manage exploits window 
        self.exploitBrowseBUTTON.clicked.connect(lambda: self.openWindow("ExploitWindow"))

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
        self.horizontalLayout_2.addWidget(self.vulnerableProgramBrowseBUTTON)

        # added signal to display vulnerable programs window
        self.vulnerableProgramBrowseBUTTON.clicked.connect(lambda: self.openWindow("VulnerableProgramsWindow"))

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
    sys.exit(app.exec_())
