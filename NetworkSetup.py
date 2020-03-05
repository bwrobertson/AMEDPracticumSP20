# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'networkSetup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NetworkSetup(object):
    def setupUi(self, NetworkSetup):
        NetworkSetup.setObjectName("NetworkSetup")
        NetworkSetup.resize(753, 480)
        NetworkSetup.setMinimumSize(QtCore.QSize(753, 480))
        NetworkSetup.setMaximumSize(QtCore.QSize(753, 480))
        self.layoutWidget = QtWidgets.QWidget(NetworkSetup)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 711, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.advancedSettinggsBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.advancedSettinggsBUTTON.setObjectName("advancedSettinggsBUTTON")
        self.horizontalLayout.addWidget(self.advancedSettinggsBUTTON)
        self.finalizeConnectionBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.finalizeConnectionBUTTON.setObjectName("finalizeConnectionBUTTON")
        self.horizontalLayout.addWidget(self.finalizeConnectionBUTTON)
        self.runScenarioBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.runScenarioBUTTON.setObjectName("runScenarioBUTTON")
        self.horizontalLayout.addWidget(self.runScenarioBUTTON)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout.addWidget(self.graphicsView_2)
        self.createVmBUTTON = QtWidgets.QPushButton(self.layoutWidget)
        self.createVmBUTTON.setObjectName("createVmBUTTON")
        self.verticalLayout.addWidget(self.createVmBUTTON)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(NetworkSetup)
        QtCore.QMetaObject.connectSlotsByName(NetworkSetup)

    def retranslateUi(self, NetworkSetup):
        _translate = QtCore.QCoreApplication.translate
        NetworkSetup.setWindowTitle(_translate("NetworkSetup", "Network Setup"))
        self.advancedSettinggsBUTTON.setText(_translate("NetworkSetup", "Advanced Settings"))
        self.finalizeConnectionBUTTON.setText(_translate("NetworkSetup", "Finalize Connection"))
        self.runScenarioBUTTON.setText(_translate("NetworkSetup", "Run Scenario"))
        self.createVmBUTTON.setText(_translate("NetworkSetup", "Create VM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NetworkSetup = QtWidgets.QWidget()
    ui = Ui_NetworkSetup()
    ui.setupUi(NetworkSetup)
    NetworkSetup.show()
    sys.exit(app.exec_())

