# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manage_Vulnerable_Programs.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_ManageVulnerablePrograms(object):

    def vulnerableProgramBrowser(self):
        VPoptions = QFileDialog.Options()
        self.VPdialog = QFileDialog()
        self.VPdialog.setOptions(VPoptions)
        self.vulnerableProgramPath, __ = QFileDialog.getOpenFileName(self.VPdialog, "Select Vulnerable Program", '/home')

        if self.vulnerableProgramPath:
            #If Windows, change the separator
            if self.vulnerableProgramPath == 'C:\\':
                self.vulnerableProgramPath = self.vulnerableProgramPath.replace('/', '\\')
                #self.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
                #os.chdir(self.vulnerableProgramPath)
                self.parentDialog.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
                #return self.vulnerableProgramPath
                #self.parentDialog.show()
            # if Linux-based
            else:
                #self.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
                self.parentDialog.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
                #os.chdir(self.vulnerableProgramPath)
                #return self.vulnerableProgramPath
                #self.parentDialog.show()
        else:
            #self.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
            self.parentDialog.vulnerableProgramLINEEDIT.setText(self.vulnerableProgramPath)
            #return ""
            #self.parentDialog.show()

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
        self.exploitTABLEWIDGET.setColumnCount(3)
        self.exploitTABLEWIDGET.setObjectName("exploitTABLEWIDGET")
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
        #self.browseFilesBUTTON.clicked.connect(self.vulnerableProgramBrowser)
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
        item.setText(_translate("ManageVulnerablePrograms", "Type"))
        item = self.exploitTABLEWIDGET.horizontalHeaderItem(2)
        item.setText(_translate("ManageVulnerablePrograms", "Platform"))
        self.browseFilesBUTTON.setText(_translate("ManageVulnerablePrograms", "Browse Files"))
        self.openManagerBUTTON.setText(_translate("ManageVulnerablePrograms", "Open Manager"))
        self.selectBUTTON.setText(_translate("ManageVulnerablePrograms", "Select"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageVulnerablePrograms = QtWidgets.QWidget()
    ui = Ui_ManageVulnerablePrograms()
    ui.setupUi(ManageVulnerablePrograms)
    ManageVulnerablePrograms.show()
    sys.exit(app.exec_())
