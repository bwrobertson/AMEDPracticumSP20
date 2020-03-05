# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Establishing_Connection_Please_Wait.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_establishingConnectionDIALOG(object):
    def setupUi(self, establishingConnectionDIALOG):
        establishingConnectionDIALOG.setObjectName("establishingConnectionDIALOG")
        establishingConnectionDIALOG.resize(282, 196)
        establishingConnectionDIALOG.setMinimumSize(QtCore.QSize(282, 196))
        establishingConnectionDIALOG.setMaximumSize(QtCore.QSize(282, 196))
        self.establishingLABEL = QtWidgets.QLabel(establishingConnectionDIALOG)
        self.establishingLABEL.setGeometry(QtCore.QRect(60, 20, 161, 101))
        self.establishingLABEL.setScaledContents(False)
        self.establishingLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.establishingLABEL.setWordWrap(True)
        self.establishingLABEL.setObjectName("establishingLABEL")
        self.label = QtWidgets.QLabel(establishingConnectionDIALOG)
        self.label.setGeometry(QtCore.QRect(110, 100, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Picture1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(establishingConnectionDIALOG)
        QtCore.QMetaObject.connectSlotsByName(establishingConnectionDIALOG)

    def retranslateUi(self, establishingConnectionDIALOG):
        _translate = QtCore.QCoreApplication.translate
        establishingConnectionDIALOG.setWindowTitle(_translate("establishingConnectionDIALOG", "Dialog"))
        self.establishingLABEL.setText(_translate("establishingConnectionDIALOG", "Establishing Connections Please Wait"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    establishingConnectionDIALOG = QtWidgets.QDialog()
    ui = Ui_establishingConnectionDIALOG()
    ui.setupUi(establishingConnectionDIALOG)
    establishingConnectionDIALOG.show()
    sys.exit(app.exec_())

