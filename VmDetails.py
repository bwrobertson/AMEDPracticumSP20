# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vm_Details.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VmDetails(object):
    def setupUi(self, VmDetails):
        VmDetails.setObjectName("VmDetails")
        VmDetails.resize(562, 449)
        VmDetails.setMinimumSize(QtCore.QSize(562, 449))
        VmDetails.setMaximumSize(QtCore.QSize(562, 449))
        self.closeBUTTON = QtWidgets.QPushButton(VmDetails)
        self.closeBUTTON.setGeometry(QtCore.QRect(240, 400, 80, 30))
        self.closeBUTTON.setObjectName("closeBUTTON")
        self.detailsLISTWIDGET = QtWidgets.QListWidget(VmDetails)
        self.detailsLISTWIDGET.setGeometry(QtCore.QRect(20, 20, 521, 361))
        self.detailsLISTWIDGET.setObjectName("detailsLISTWIDGET")

        self.retranslateUi(VmDetails)
        QtCore.QMetaObject.connectSlotsByName(VmDetails)

    def retranslateUi(self, VmDetails):
        _translate = QtCore.QCoreApplication.translate
        VmDetails.setWindowTitle(_translate("VmDetails", "VM Details"))
        self.closeBUTTON.setText(_translate("VmDetails", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VmDetails = QtWidgets.QWidget()
    ui = Ui_VmDetails()
    ui.setupUi(VmDetails)
    VmDetails.show()
    sys.exit(app.exec_())

