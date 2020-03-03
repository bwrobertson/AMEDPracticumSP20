# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Export import Ui_Export

class Ui_MainWindow(object):
    #Opens the export widow on data button click
    def openExportWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Export()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(240, 20, 121, 51))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("med.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 80, 521, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchLABEL = QtWidgets.QLabel(self.widget)
        self.searchLABEL.setObjectName("searchLABEL")
        self.horizontalLayout_3.addWidget(self.searchLABEL)
        self.searchEDITBOX = QtWidgets.QLineEdit(self.widget)
        self.searchEDITBOX.setText("")
        self.searchEDITBOX.setObjectName("searchEDITBOX")
        self.horizontalLayout_3.addWidget(self.searchEDITBOX)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.DATEEDIT = QtWidgets.QDateEdit(self.widget)
        self.DATEEDIT.setObjectName("DATEEDIT")
        self.horizontalLayout.addWidget(self.DATEEDIT)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scenariosLIST = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scenariosLIST.sizePolicy().hasHeightForWidth())
        self.scenariosLIST.setSizePolicy(sizePolicy)
        self.scenariosLIST.setIconSize(QtCore.QSize(0, 0))
        self.scenariosLIST.setResizeMode(QtWidgets.QListView.Fixed)
        self.scenariosLIST.setViewMode(QtWidgets.QListView.ListMode)
        self.scenariosLIST.setUniformItemSizes(False)
        self.scenariosLIST.setWordWrap(False)
        self.scenariosLIST.setSelectionRectVisible(False)
        self.scenariosLIST.setObjectName("scenariosLIST")
        item = QtWidgets.QListWidgetItem()
        self.scenariosLIST.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.scenariosLIST.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.scenariosLIST.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.scenariosLIST.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.scenariosLIST.addItem(item)
        self.verticalLayout.addWidget(self.scenariosLIST)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.plainTEXTEDIT = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTEXTEDIT.setObjectName("plainTEXTEDIT")
        self.horizontalLayout_2.addWidget(self.plainTEXTEDIT)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.runBUTTON = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBUTTON.sizePolicy().hasHeightForWidth())
        self.runBUTTON.setSizePolicy(sizePolicy)
        self.runBUTTON.setObjectName("runBUTTON")
        self.horizontalLayout_8.addWidget(self.runBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.configureBUTTON = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configureBUTTON.sizePolicy().hasHeightForWidth())
        self.configureBUTTON.setSizePolicy(sizePolicy)
        self.configureBUTTON.setObjectName("configureBUTTON")
        self.horizontalLayout_8.addWidget(self.configureBUTTON)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.setupBUTTON = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setupBUTTON.sizePolicy().hasHeightForWidth())
        self.setupBUTTON.setSizePolicy(sizePolicy)
        self.setupBUTTON.setObjectName("setupBUTTON")
        self.horizontalLayout_8.addWidget(self.setupBUTTON)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.newScenarioBUTTON = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newScenarioBUTTON.sizePolicy().hasHeightForWidth())
        self.newScenarioBUTTON.setSizePolicy(sizePolicy)
        self.newScenarioBUTTON.setObjectName("newScenarioBUTTON")
        self.horizontalLayout_6.addWidget(self.newScenarioBUTTON)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        #Export data button
        self.exportDataBUTTON = QtWidgets.QPushButton(self.widget)
        self.exportDataBUTTON.setObjectName("exportDataBUTTON")
        self.exportDataBUTTON.clicked.connect(self.openExportWindow)
        self.horizontalLayout_6.addWidget(self.exportDataBUTTON)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchLABEL.setText(_translate("MainWindow", "Search"))
        self.scenariosLIST.setSortingEnabled(False)
        __sortingEnabled = self.scenariosLIST.isSortingEnabled()
        self.scenariosLIST.setSortingEnabled(False)
        item = self.scenariosLIST.item(0)
        item.setText(_translate("MainWindow", "Test_e0"))
        item = self.scenariosLIST.item(1)
        item.setText(_translate("MainWindow", "Test_e01"))
        item = self.scenariosLIST.item(2)
        item.setText(_translate("MainWindow", "Test_e02"))
        item = self.scenariosLIST.item(3)
        item.setText(_translate("MainWindow", "Test_e03"))
        item = self.scenariosLIST.item(4)
        item.setText(_translate("MainWindow", "Test_e04"))
        self.scenariosLIST.setSortingEnabled(__sortingEnabled)
        self.plainTEXTEDIT.setPlainText(_translate("MainWindow", "Date Created: \n"
"Date Modified:\n"
"Exploit:\n"
"Vulnerable Program:\n"
""))
        self.runBUTTON.setText(_translate("MainWindow", "Run"))
        self.configureBUTTON.setText(_translate("MainWindow", "Configure"))
        self.setupBUTTON.setText(_translate("MainWindow", "Setup"))
        self.newScenarioBUTTON.setText(_translate("MainWindow", "New Scenario"))
        self.exportDataBUTTON.setText(_translate("MainWindow", "Export Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
