# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigureMongoDB.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigureMongoDB(object):
    def setupUi(self, ConfigureMongoDB):
        ConfigureMongoDB.setObjectName("ConfigureMongoDB")
        ConfigureMongoDB.resize(394, 307)
        ConfigureMongoDB.setMinimumSize(QtCore.QSize(394, 307))
        ConfigureMongoDB.setMaximumSize(QtCore.QSize(394, 307))
        self.widget = QtWidgets.QWidget(ConfigureMongoDB)
        self.widget.setGeometry(QtCore.QRect(10, 10, 371, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DBConnectionStringLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DBConnectionStringLABEL.setFont(font)
        self.DBConnectionStringLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.DBConnectionStringLABEL.setObjectName("DBConnectionStringLABEL")
        self.verticalLayout.addWidget(self.DBConnectionStringLABEL)
        self.DBConnectionStringLINEEDIT = QtWidgets.QLineEdit(self.widget)
        self.DBConnectionStringLINEEDIT.setObjectName("DBConnectionStringLINEEDIT")
        self.verticalLayout.addWidget(self.DBConnectionStringLINEEDIT)
        self.DBUserNameLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DBUserNameLABEL.setFont(font)
        self.DBUserNameLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.DBUserNameLABEL.setObjectName("DBUserNameLABEL")
        self.verticalLayout.addWidget(self.DBUserNameLABEL)
        self.DBUserNameLINEEDIT = QtWidgets.QLineEdit(self.widget)
        self.DBUserNameLINEEDIT.setObjectName("DBUserNameLINEEDIT")
        self.verticalLayout.addWidget(self.DBUserNameLINEEDIT)
        self.DBPasswordLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DBPasswordLABEL.setFont(font)
        self.DBPasswordLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.DBPasswordLABEL.setObjectName("DBPasswordLABEL")
        self.verticalLayout.addWidget(self.DBPasswordLABEL)
        self.DBPasswordLINEEDIT = QtWidgets.QLineEdit(self.widget)
        self.DBPasswordLINEEDIT.setObjectName("DBPasswordLINEEDIT")
        self.verticalLayout.addWidget(self.DBPasswordLINEEDIT)
        self.widget1 = QtWidgets.QWidget(ConfigureMongoDB)
        self.widget1.setGeometry(QtCore.QRect(10, 260, 371, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backBUTTON = QtWidgets.QPushButton(self.widget1)
        self.backBUTTON.setObjectName("backBUTTON")
        self.horizontalLayout.addWidget(self.backBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.connectBUTTON = QtWidgets.QPushButton(self.widget1)
        self.connectBUTTON.setObjectName("connectBUTTON")
        self.horizontalLayout.addWidget(self.connectBUTTON)

        self.retranslateUi(ConfigureMongoDB)
        QtCore.QMetaObject.connectSlotsByName(ConfigureMongoDB)

    def retranslateUi(self, ConfigureMongoDB):
        _translate = QtCore.QCoreApplication.translate
        ConfigureMongoDB.setWindowTitle(_translate("ConfigureMongoDB", "Configure MongoDB"))
        self.DBConnectionStringLABEL.setText(_translate("ConfigureMongoDB", "Database Connection String:"))
        self.DBUserNameLABEL.setText(_translate("ConfigureMongoDB", "Database User Name:"))
        self.DBPasswordLABEL.setText(_translate("ConfigureMongoDB", "Database Password:"))
        self.backBUTTON.setText(_translate("ConfigureMongoDB", "Back"))
        self.connectBUTTON.setText(_translate("ConfigureMongoDB", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigureMongoDB = QtWidgets.QWidget()
    ui = Ui_ConfigureMongoDB()
    ui.setupUi(ConfigureMongoDB)
    ConfigureMongoDB.show()
    sys.exit(app.exec_())

