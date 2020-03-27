# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manage_Vulnerable_Programs.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManageVulnerablePrograms(object):

    # TODO function to get vulnerable programs from exploitDB or stored locally 
    def getItemsList(self):
        # dummy objects
        pr1 = {'name': "p0", "type": "WebApps", "platform": "PHP"}
        pr2 = {"name": "p1", "type": "Local", "platform": "Hardware"}
        pr3 = {"name": "Microsoft Word", "type": "WebApps", "platform": "Windows"}
        lst = [pr1, pr2, pr3]
        return lst

    def setupUi(self, ManageVulnerablePrograms):
        ManageVulnerablePrograms.setObjectName("ManageVulnerablePrograms")
        ManageVulnerablePrograms.resize(600, 320)
        self.layoutWidget = QtWidgets.QWidget(ManageVulnerablePrograms)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 551, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exploitTABLEWIDGET = QtWidgets.QTableWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exploitTABLEWIDGET.sizePolicy().hasHeightForWidth())
        self.exploitTABLEWIDGET.setSizePolicy(sizePolicy)
        self.exploitTABLEWIDGET.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.exploitTABLEWIDGET.setColumnCount(3) # column size always set to 3
        self.exploitTABLEWIDGET.setObjectName("exploitTABLEWIDGET")

        # set num of rows to the actual length of the vuln programs list
        self.exploitTABLEWIDGET.setRowCount(len(self.getItemsList())) # FIXME 

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exploitTABLEWIDGET.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exploitTABLEWIDGET.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exploitTABLEWIDGET.setHorizontalHeaderItem(2, item)
        self.exploitTABLEWIDGET.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout.addWidget(self.exploitTABLEWIDGET)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browseFilesBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.browseFilesBUTTON.setEnabled(True)
        self.browseFilesBUTTON.setObjectName("browseFilesBUTTON")
        self.horizontalLayout.addWidget(self.browseFilesBUTTON)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        self.openManagerBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.openManagerBUTTON.setObjectName("openManagerBUTTON")
        self.horizontalLayout.addWidget(self.openManagerBUTTON)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem5)
        self.selectBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.selectBUTTON.setObjectName("selectBUTTON")
        self.horizontalLayout.addWidget(self.selectBUTTON)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ManageVulnerablePrograms)
        QtCore.QMetaObject.connectSlotsByName(ManageVulnerablePrograms)

    def retranslateUi(self, ManageVulnerablePrograms):
        _translate = QtCore.QCoreApplication.translate
        ManageVulnerablePrograms.setWindowTitle(_translate("ManageVulnerablePrograms", "Manage Vulnerable Program"))
        item = self.exploitTABLEWIDGET.horizontalHeaderItem(0)
        item.setText(_translate("ManageVulnerablePrograms", "Vulnerable Program"))
        item = self.exploitTABLEWIDGET.horizontalHeaderItem(1)
        # corrected name of column below from 'New Column' to 'Type'
        item.setText(_translate("ManageVulnerablePrograms", "Type"))
        item = self.exploitTABLEWIDGET.horizontalHeaderItem(2)
        item.setText(_translate("ManageVulnerablePrograms", "Platform"))

        # Added this function call to fill table 
        self.fillTable()

        self.browseFilesBUTTON.setText(_translate("ManageVulnerablePrograms", "Browse Files"))
        self.openManagerBUTTON.setText(_translate("ManageVulnerablePrograms", "Open Manager"))
        self.selectBUTTON.setText(_translate("ManageVulnerablePrograms", "Select"))

    # function to fill table with content from exploitDB or locally saved vulnerable programs
    def fillTable(self):
        itemList = self.getItemsList()
        num_rows = len(itemList)
        for row in range(num_rows):
            self.exploitTABLEWIDGET.setItem(row, 0, QtWidgets.QTableWidgetItem(itemList[row]["name"]))
            self.exploitTABLEWIDGET.setItem(row, 1, QtWidgets.QTableWidgetItem(itemList[row]["type"]))
            self.exploitTABLEWIDGET.setItem(row, 2, QtWidgets.QTableWidgetItem(itemList[row]["platform"]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageVulnerablePrograms = QtWidgets.QWidget()
    ui = Ui_ManageVulnerablePrograms()
    ui.setupUi(ManageVulnerablePrograms)
    ManageVulnerablePrograms.show()
    sys.exit(app.exec_())