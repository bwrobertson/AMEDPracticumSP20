# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Export.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os, sys

class Ui_Export(object):
    # Opens file browser on browse button click
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
            return self.path
        else:
            self.destinationDirectoryLINEEDIT.setText(self.path)
            return ""
            
    def setupUi(self, Export):
        Export.setObjectName("Export")
        Export.resize(622, 479)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Export.sizePolicy().hasHeightForWidth())
        Export.setSizePolicy(sizePolicy)
        self.widget = QtWidgets.QWidget(Export)
        self.widget.setGeometry(QtCore.QRect(31, 34, 551, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.destinationDirectoryLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.destinationDirectoryLABEL.setFont(font)
        self.destinationDirectoryLABEL.setObjectName("destinationDirectoryLABEL")
        self.verticalLayout.addWidget(self.destinationDirectoryLABEL)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.destinationDirectoryLINEEDIT = QtWidgets.QLineEdit(self.widget)
        self.destinationDirectoryLINEEDIT.setObjectName("destinationDirectoryLINEEDIT")
        self.horizontalLayout.addWidget(self.destinationDirectoryLINEEDIT)
        #Browse Button
        self.browserBUTTON = QtWidgets.QPushButton(self.widget)
        self.browserBUTTON.setEnabled(True)
        self.browserBUTTON.setObjectName("browserBUTTON")
        self.browserBUTTON.clicked.connect(self.fileBrowser)
        self.horizontalLayout.addWidget(self.browserBUTTON)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        #Tree Widget for data from database
        self.databseTREEWIDGET = QtWidgets.QTreeWidget(self.widget)
        self.databseTREEWIDGET.setObjectName("databseTREEWIDGET")
        self.databseTREEWIDGET.headerItem().setText(0, "1")
        item_0 = QtWidgets.QTreeWidgetItem(self.databseTREEWIDGET)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        item_0.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        self.databseTREEWIDGET.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.databseTREEWIDGET)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backBUTTON = QtWidgets.QPushButton(self.widget)
        self.backBUTTON.setObjectName("backBUTTON")
        self.horizontalLayout_2.addWidget(self.backBUTTON)
        spacerItem = QtWidgets.QSpacerItem(38, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.exportBUTTON = QtWidgets.QPushButton(self.widget)
        self.exportBUTTON.setObjectName("exportBUTTON")
        self.horizontalLayout_2.addWidget(self.exportBUTTON)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Export)
        QtCore.QMetaObject.connectSlotsByName(Export)

    def retranslateUi(self, Export):
        _translate = QtCore.QCoreApplication.translate
        Export.setWindowTitle(_translate("Export", "Export"))
        self.destinationDirectoryLABEL.setText(_translate("Export", "Destination Directory:"))
        self.browserBUTTON.setText(_translate("Export", "Browse"))
        __sortingEnabled = self.databseTREEWIDGET.isSortingEnabled()
        self.databseTREEWIDGET.setSortingEnabled(False)
        self.databseTREEWIDGET.topLevelItem(0).setText(0, _translate("Export", "New Item"))
        self.databseTREEWIDGET.topLevelItem(0).child(0).setText(0, _translate("Export", "New Subitem"))
        self.databseTREEWIDGET.topLevelItem(0).child(1).setText(0, _translate("Export", "New Item"))
        self.databseTREEWIDGET.topLevelItem(0).child(2).setText(0, _translate("Export", "New Item"))
        self.databseTREEWIDGET.topLevelItem(0).child(3).setText(0, _translate("Export", "New Item"))
        self.databseTREEWIDGET.topLevelItem(0).child(4).setText(0, _translate("Export", "New Item"))
        self.databseTREEWIDGET.setSortingEnabled(__sortingEnabled)
        self.backBUTTON.setText(_translate("Export", "Back"))
        self.exportBUTTON.setText(_translate("Export", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Export = QtWidgets.QWidget()
    ui = Ui_Export()
    ui.setupUi(Export)
    Export.show()
    sys.exit(app.exec_())

