# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manage_Scenarios.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from NewScenario import Ui_NewScenario


class Ui_ManageScenarios(object):

    # Opens the scenarioRunningWindow on run button click############################3
    def openMainWindow(self):
        self.window = QtWidgets.QWidget()
        from MainWindow import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, ManageScenarios):
        ManageScenarios.setObjectName("ManageScenarios")
        ManageScenarios.resize(473, 322)
        ManageScenarios.setMinimumSize(QtCore.QSize(473, 322))
        ManageScenarios.setMaximumSize(QtCore.QSize(473, 322))
        self.scenariosTREEWIDGET = QtWidgets.QTreeWidget(ManageScenarios)
        self.scenariosTREEWIDGET.setGeometry(QtCore.QRect(30, 20, 411, 211))
        self.scenariosTREEWIDGET.setObjectName("scenariosTREEWIDGET")
        item_0 = QtWidgets.QTreeWidgetItem(self.scenariosTREEWIDGET)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        item_0.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        self.scenariosTREEWIDGET.header().setVisible(False)
        self.layoutWidget = QtWidgets.QWidget(ManageScenarios)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 250, 411, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.backBUTTON.setObjectName("backBUTTON")
        self.horizontalLayout.addWidget(self.backBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.deleteBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteBUTTON.setObjectName("deleteBUTTON")
        self.horizontalLayout.addWidget(self.deleteBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.newBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.newBUTTON.setObjectName("newBUTTON")
        self.horizontalLayout.addWidget(self.newBUTTON)
        self.retranslateUi(ManageScenarios)
        QtCore.QMetaObject.connectSlotsByName(ManageScenarios)

    def retranslateUi(self, ManageScenarios):
        _translate = QtCore.QCoreApplication.translate
        ManageScenarios.setWindowTitle(_translate("ManageScenarios", "Manage Scenarios"))
        __sortingEnabled = self.scenariosTREEWIDGET.isSortingEnabled()
        self.scenariosTREEWIDGET.setSortingEnabled(False)
        self.scenariosTREEWIDGET.topLevelItem(0).setText(0, _translate("ManageScenarios", "New Item"))
        self.scenariosTREEWIDGET.setSortingEnabled(__sortingEnabled)
        self.backBUTTON.setText(_translate("ManageScenarios", "Back"))
        self.deleteBUTTON.setText(_translate("ManageScenarios", "Delete"))
        self.newBUTTON.setText(_translate("ManageScenarios", "New"))


