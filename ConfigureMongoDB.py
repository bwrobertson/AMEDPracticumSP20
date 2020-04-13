# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigureMongoDB.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient
import pymongo
import re
import base64

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
        self.connectBUTTON.clicked.connect(self.pingDB)
        self.horizontalLayout.addWidget(self.connectBUTTON)

        self.retranslateUi(ConfigureMongoDB)
        QtCore.QMetaObject.connectSlotsByName(ConfigureMongoDB)

    def retranslateUi(self, ConfigureMongoDB):

        try:
            file = open('mongodbconnectioninfo.txt', 'rb')
            dbConnection = file.read()
            dbConnection = base64.decodebytes(dbConnection)
            dbConnection = dbConnection.decode()
            self.DBConnectionStringLINEEDIT.setText(dbConnection)
            user = re.search('://(.*):', dbConnection)
            password = re.search(user.group(1) + ':(.*)@', dbConnection)
            self.DBUserNameLINEEDIT.setText(user.group(1))
            self.DBPasswordLINEEDIT.setText(password.group(1))
            file.close()
        except IOError:
            print('file not found')

        _translate = QtCore.QCoreApplication.translate
        ConfigureMongoDB.setWindowTitle(_translate("ConfigureMongoDB", "Configure MongoDB"))
        self.DBConnectionStringLABEL.setText(_translate("ConfigureMongoDB", "Database Connection String:"))
        self.DBUserNameLABEL.setText(_translate("ConfigureMongoDB", "Database User Name:"))
        self.DBPasswordLABEL.setText(_translate("ConfigureMongoDB", "Database Password:"))
        self.backBUTTON.setText(_translate("ConfigureMongoDB", "Back"))
        self.connectBUTTON.setText(_translate("ConfigureMongoDB", "Connect"))


    def pingDB(self):
        dbConnection = self.DBConnectionStringLINEEDIT.text()
        dbUser = self.DBUserNameLINEEDIT.text()
        dbPass = self.DBPasswordLINEEDIT.text()

        user = re.search('://(.*):', dbConnection)
        password = re.search(user.group(1) + ':(.*)@', dbConnection)
        if(dbUser != ""):
            dbConnection = dbConnection.replace(user.group(1), dbUser)
        if(dbPass != ""):
            dbConnection = dbConnection.replace(password.group(1), dbPass)
        print(dbConnection)

        try:
            client = MongoClient(dbConnection, 1)
            client.server_info() # force connection on a request as the
                                     # connect=True parameter of MongoClient seems
                                     # to be useless here
            print('yes')
            file = open('mongodbconnectioninfo.txt', 'wb')
            file.write(base64.b64encode(str.encode(dbConnection)))
            file.close()
        except pymongo.errors.ServerSelectionTimeoutError as err:
            # do whatever you need
            print(err)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigureMongoDB = QtWidgets.QWidget()
    ui = Ui_ConfigureMongoDB()
    ui.setupUi(ConfigureMongoDB)
    ConfigureMongoDB.show()
    sys.exit(app.exec_())
