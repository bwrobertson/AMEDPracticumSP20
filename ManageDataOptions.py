# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageDataOptions.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManageDataOptions(object):
    def setupUi(self, ManageDataOptions):
        ManageDataOptions.setObjectName("ManageDataOptions")
        ManageDataOptions.resize(400, 200)
        ManageDataOptions.setMinimumSize(QtCore.QSize(400, 200))
        ManageDataOptions.setMaximumSize(QtCore.QSize(400, 200))
        self.backBUTTON = QtWidgets.QPushButton(ManageDataOptions)
        self.backBUTTON.setGeometry(QtCore.QRect(310, 160, 75, 23))
        self.backBUTTON.setObjectName("backBUTTON")
        self.widget = QtWidgets.QWidget(ManageDataOptions)
        self.widget.setGeometry(QtCore.QRect(22, 21, 361, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.selectLABEL.setFont(font)
        self.selectLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.selectLABEL.setObjectName("selectLABEL")
        self.verticalLayout.addWidget(self.selectLABEL)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importBUTTON = QtWidgets.QPushButton(self.widget)
        self.importBUTTON.setObjectName("importBUTTON")
        self.horizontalLayout.addWidget(self.importBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exportBUTTON = QtWidgets.QPushButton(self.widget)
        self.exportBUTTON.setObjectName("exportBUTTON")
        self.horizontalLayout.addWidget(self.exportBUTTON)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ManageDataOptions)
        QtCore.QMetaObject.connectSlotsByName(ManageDataOptions)

    def retranslateUi(self, ManageDataOptions):
        _translate = QtCore.QCoreApplication.translate
        ManageDataOptions.setWindowTitle(_translate("ManageDataOptions", "Manage Data Options"))
        self.backBUTTON.setText(_translate("ManageDataOptions", "Back"))
        self.selectLABEL.setText(_translate("ManageDataOptions", "Please select to either import or export data."))
        self.importBUTTON.setText(_translate("ManageDataOptions", "Import"))
        self.exportBUTTON.setText(_translate("ManageDataOptions", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageDataOptions = QtWidgets.QWidget()
    ui = Ui_ManageDataOptions()
    ui.setupUi(ManageDataOptions)
    ManageDataOptions.show()
    sys.exit(app.exec_())

