# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from NewScenario import Ui_NewScenario
from pymongo import MongoClient
from DBConfiguration import Ui_DBConfiguration

class Ui_ManageScenarios(object):
    def setupUi(self, ManageScenarios):
        ManageScenarios.setObjectName("ManageScenarios")
        ManageScenarios.resize(483, 330)
        ManageScenarios.setMinimumSize(QtCore.QSize(483, 330))
        ManageScenarios.setMaximumSize(QtCore.QSize(483, 330))
        self.layoutWidget = QtWidgets.QWidget(ManageScenarios)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 461, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        ####Select all checkbox
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        ###
        self.scenariosLISTWIDGET = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scenariosLISTWIDGET.sizePolicy().hasHeightForWidth())
        self.scenariosLISTWIDGET.setSizePolicy(sizePolicy)
        self.scenariosLISTWIDGET.setSelectionRectVisible(False)
        self.scenariosLISTWIDGET.setObjectName("scenariosLISTWIDGET")
        self.verticalLayout_2.addWidget(self.scenariosLISTWIDGET)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBUTTON.sizePolicy().hasHeightForWidth())
        self.backBUTTON.setSizePolicy(sizePolicy)
        self.backBUTTON.setObjectName("backBUTTON")
        self.horizontalLayout_2.addWidget(self.backBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.newBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.newBUTTON.setObjectName("newBUTTON")
        self.horizontalLayout_2.addWidget(self.newBUTTON)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.deleteBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteBUTTON.setObjectName("deleteBUTTON")
        self.deleteBUTTON.clicked.connect(self.deleteSelected)
        self.verticalLayout.addWidget(self.deleteBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(20, 138, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ManageScenarios)
        QtCore.QMetaObject.connectSlotsByName(ManageScenarios)

    ###Method to check all box or uncheck all boxes###
    def selectAll(self):
        if self.checkBox.isChecked():
            for i in range(self.scenariosLISTWIDGET.count()):
                item = self.scenariosLISTWIDGET.item(i)
                item.setCheckState(QtCore.Qt.Checked)
        else:
            for i in range(self.scenariosLISTWIDGET.count()):
                item = self.scenariosLISTWIDGET.item(i)
                item.setCheckState(QtCore.Qt.Unchecked)

    def retranslateUi(self, ManageScenarios):
        ###Changed###
        _translate = QtCore.QCoreApplication.translate
        self.setupTree()
        ###End Changed###

        _translate = QtCore.QCoreApplication.translate
        ManageScenarios.setWindowTitle(_translate("ManageScenarios", "Manage Scenarios"))
        ###More select all stuff
        self.checkBox.setText(_translate("ManageScenarios", "Select All"))
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.selectAll)
        #########
        self.scenariosLISTWIDGET.setSortingEnabled(False)
        __sortingEnabled = self.scenariosLISTWIDGET.isSortingEnabled()
        self.scenariosLISTWIDGET.setSortingEnabled(False)
        self.scenariosLISTWIDGET.setSortingEnabled(__sortingEnabled)
        self.backBUTTON.setText(_translate("ManageScenarios", "Back"))
        self.newBUTTON.setText(_translate("ManageScenarios", "New"))
        self.deleteBUTTON.setText(_translate("ManageScenarios", "Delete"))

    def setupTree(self):
        data = Ui_DBConfiguration.db['Scenario']
        _translate = QtCore.QCoreApplication.translate
        x = 0
        for collection in data.find():
            self.scenariosLISTWIDGET.addItem(QtWidgets.QListWidgetItem())
            item = self.scenariosLISTWIDGET.item(x)
            item.setCheckState(QtCore.Qt.Unchecked)
            scen = collection['scenario']
            # Prevents NoneType Error
            if not item:
                continue
            item.setText(_translate("ManageScenarios", scen['name']))
            x+=1

    def deleteSelected(self):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.scenariosLISTWIDGET.isSortingEnabled()
        self.scenariosLISTWIDGET.setSortingEnabled(False)
        data = Ui_DBConfiguration.db["Scenario"]
        i = 0
        id = 0
        for collection in data.find():
            id = collection['_id']
            if(self.scenariosLISTWIDGET.item(i).checkState()==QtCore.Qt.Checked):
                data.delete_one({'_id': id})
            i+=1
        self.scenariosLISTWIDGET.clear()
        self.setupTree()
        #QMessageBox.about(self, "Success", "Items Deleted Succesfully.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageScenarios = QtWidgets.QWidget()
    ui = Ui_ManageScenarios()
    ui.setupUi(ManageScenarios)
    ManageScenarios.show()
    sys.exit(app.exec_())
