# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Export_Data_Progress.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExportDataProgress(object):
    def setupUi(self, ExportDataProgress):
        ExportDataProgress.setObjectName("ExportDataProgress")
        ExportDataProgress.resize(370, 167)
        ExportDataProgress.setMinimumSize(QtCore.QSize(370, 167))
        ExportDataProgress.setMaximumSize(QtCore.QSize(370, 167))
        self.widget = QtWidgets.QWidget(ExportDataProgress)
        self.widget.setGeometry(QtCore.QRect(80, 20, 221, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PROGRESSBAR = QtWidgets.QProgressBar(self.widget)
        self.PROGRESSBAR.setProperty("value", 24)
        self.PROGRESSBAR.setAlignment(QtCore.Qt.AlignCenter)
        self.PROGRESSBAR.setObjectName("PROGRESSBAR")
        self.verticalLayout.addWidget(self.PROGRESSBAR)
        self.cancelBUTTON = QtWidgets.QPushButton(self.widget)
        self.cancelBUTTON.setObjectName("cancelBUTTON")
        self.verticalLayout.addWidget(self.cancelBUTTON)

        self.retranslateUi(ExportDataProgress)
        QtCore.QMetaObject.connectSlotsByName(ExportDataProgress)

    def retranslateUi(self, ExportDataProgress):
        _translate = QtCore.QCoreApplication.translate
        ExportDataProgress.setWindowTitle(_translate("ExportDataProgress", "Export Data Progress"))
        self.cancelBUTTON.setText(_translate("ExportDataProgress", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExportDataProgress = QtWidgets.QDialog()
    ui = Ui_ExportDataProgress()
    ui.setupUi(ExportDataProgress)
    ExportDataProgress.show()
    sys.exit(app.exec_())

