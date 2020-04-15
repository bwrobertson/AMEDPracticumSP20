# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'networkSetup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(753, 480)
        Form.setMinimumSize(QtCore.QSize(753, 480))
        Form.setMaximumSize(QtCore.QSize(753, 480))
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(495, 11, 16, 424))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(21, 11, 471, 461))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.povLIST = QtWidgets.QListWidget(self.widget)
        self.povLIST.setObjectName("povLIST")
        self.verticalLayout.addWidget(self.povLIST)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.victimLIST = QtWidgets.QListWidget(self.widget)
        self.victimLIST.setObjectName("victimLIST")
        self.verticalLayout_2.addWidget(self.victimLIST)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.widget)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.advancedSettingsBUTTON = QtWidgets.QPushButton(self.widget)
        self.advancedSettingsBUTTON.setObjectName("advancedSettingsBUTTON")
        self.horizontalLayout.addWidget(self.advancedSettingsBUTTON)
        self.testBUTTON = QtWidgets.QPushButton(self.widget)
        self.testBUTTON.setObjectName("testBUTTON")
        self.horizontalLayout.addWidget(self.testBUTTON)
        self.runBUTTON = QtWidgets.QPushButton(self.widget)
        self.runBUTTON.setObjectName("runBUTTON")
        self.horizontalLayout.addWidget(self.runBUTTON)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(510, 10, 231, 461))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.machineLIST = QtWidgets.QListWidget(self.widget1)
        self.machineLIST.setObjectName("machineLIST")
        self.verticalLayout_4.addWidget(self.machineLIST)
        self.addVmBUTTON = QtWidgets.QPushButton(self.widget1)
        self.addVmBUTTON.setObjectName("addVmBUTTON")
        self.verticalLayout_4.addWidget(self.addVmBUTTON)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PoV"))
        self.label_2.setText(_translate("Form", "Victim"))
        self.backButton.setText(_translate("Form", "Back"))
        self.advancedSettingsBUTTON.setText(_translate("Form", "Advanced Sett."))
        self.testBUTTON.setText(_translate("Form", "Test Connection"))
        self.runBUTTON.setText(_translate("Form", "Run Scenario"))
        self.label_3.setText(_translate("Form", "Available Machines"))
        self.addVmBUTTON.setText(_translate("Form", "Add Victim || PoV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
