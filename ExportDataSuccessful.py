# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Export_Data_Successful.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExportDataSuccessful(object):
    def setupUi(self, ExportDataSuccessful):
        ExportDataSuccessful.setObjectName("ExportDataSuccessful")
        ExportDataSuccessful.resize(378, 147)
        ExportDataSuccessful.setMinimumSize(QtCore.QSize(378, 147))
        ExportDataSuccessful.setMaximumSize(QtCore.QSize(378, 147))
        self.widget = QtWidgets.QWidget(ExportDataSuccessful)
        self.widget.setGeometry(QtCore.QRect(30, 20, 322, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textLABEL.setFont(font)
        self.textLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.textLABEL.setObjectName("textLABEL")
        self.verticalLayout.addWidget(self.textLABEL)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.showInFolderBUTTON = QtWidgets.QPushButton(self.widget)
        self.showInFolderBUTTON.setObjectName("showInFolderBUTTON")
        self.horizontalLayout.addWidget(self.showInFolderBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.doneBUTTON = QtWidgets.QPushButton(self.widget)
        self.doneBUTTON.setObjectName("doneBUTTON")
        self.horizontalLayout.addWidget(self.doneBUTTON)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ExportDataSuccessful)
        QtCore.QMetaObject.connectSlotsByName(ExportDataSuccessful)

    def retranslateUi(self, ExportDataSuccessful):
        _translate = QtCore.QCoreApplication.translate
        ExportDataSuccessful.setWindowTitle(_translate("ExportDataSuccessful", "Export Data Succesful"))
        self.textLABEL.setText(_translate("ExportDataSuccessful", "Export Successful!"))
        self.showInFolderBUTTON.setText(_translate("ExportDataSuccessful", "Show in Folder"))
        self.doneBUTTON.setText(_translate("ExportDataSuccessful", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExportDataSuccessful = QtWidgets.QDialog()
    ui = Ui_ExportDataSuccessful()
    ui.setupUi(ExportDataSuccessful)
    ExportDataSuccessful.show()
    sys.exit(app.exec_())

