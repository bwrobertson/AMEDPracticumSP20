# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuggestedSetup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(753, 480)
        Form.setMinimumSize(QtCore.QSize(753, 480))
        Form.setMaximumSize(QtCore.QSize(753, 480))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 10, 681, 461))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget1)
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setAcceptDrops(True)
        self.listWidget_2.setDragEnabled(True)
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.listWidget_3 = QtWidgets.QListWidget(self.widget1)
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.setAcceptDrops(True)
        self.listWidget_3.setDragEnabled(True)
        self.horizontalLayout_2.addWidget(self.listWidget_3)
        self.widget2 = QtWidgets.QWidget(self.splitter)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runScenarioBUTTON = QtWidgets.QPushButton(self.widget2)
        self.runScenarioBUTTON.setObjectName("runScenarioBUTTON")
        self.horizontalLayout.addWidget(self.runScenarioBUTTON)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setAcceptDrops(False)
        self.listWidget.setDragEnabled(True)
        ######Dummy data to fill table with drag and drop PoV and Victim machines

        vms = ["vm 1", "vm 2", "vm 3", "vm 4"]
        malware = ["malware 1", "malware 2"]

        for x in vms:
            self.listWidget.insertItem(1, QListWidgetItem(QIcon("vm.png"), x))

        for x in malware:
            self.listWidget.insertItem(1, QListWidgetItem(QIcon("vmmalware.png"), x))

        self.listWidget_2.setIconSize(QSize(40, 40))
        self.listWidget_3.setIconSize(QSize(40, 40))
        self.listWidget.setIconSize(QSize(40, 40))
        self.verticalLayout.addWidget(self.listWidget)
        self.createVmBUTTON = QtWidgets.QPushButton(self.widget)
        self.createVmBUTTON.setObjectName("createVmBUTTON")
        self.verticalLayout.addWidget(self.createVmBUTTON)
        self.gridLayout.addLayout(self.verticalLayout, 0, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Suggested Setup", "Suggested Setup"))
        self.runScenarioBUTTON.setText(_translate("Form", "Next"))
        self.createVmBUTTON.setText(_translate("Form", "Add Victim || PoV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
