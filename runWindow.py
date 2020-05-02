# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_runWindow(object):
    def setupUi(self, runWindow):
        runWindow.setObjectName("runWindow")
        runWindow.resize(360, 200)
        runWindow.setMinimumSize(QtCore.QSize(360, 200))
        runWindow.setMaximumSize(QtCore.QSize(360, 200))
        self.widget = QtWidgets.QWidget(runWindow)
        self.widget.setGeometry(QtCore.QRect(40, 20, 282, 153))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.intervalLABEL = QtWidgets.QLabel(self.widget)
        self.intervalLABEL.setObjectName("intervalLABEL")
        self.horizontalLayout.addWidget(self.intervalLABEL)
        self.intervalSPINBOX = QtWidgets.QSpinBox(self.widget)
        self.intervalSPINBOX.setMinimumSize(QtCore.QSize(71, 21))
        self.intervalSPINBOX.setMaximumSize(QtCore.QSize(71, 21))
        self.intervalSPINBOX.setObjectName("intervalSPINBOX")
        self.horizontalLayout.addWidget(self.intervalSPINBOX)
        spacerItem2 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.buttonsHorizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.buttonsHorizontalLayout_2.setObjectName("buttonsHorizontalLayout_2")
        self.cancelPushBUTTON = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelPushBUTTON.sizePolicy().hasHeightForWidth())
        self.cancelPushBUTTON.setSizePolicy(sizePolicy)
        self.cancelPushBUTTON.setMinimumSize(QtCore.QSize(112, 32))
        self.cancelPushBUTTON.setMaximumSize(QtCore.QSize(112, 32))
        self.cancelPushBUTTON.setObjectName("cancelPushBUTTON")
        self.buttonsHorizontalLayout_2.addWidget(self.cancelPushBUTTON)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsHorizontalLayout_2.addItem(spacerItem4)
        self.okPushBUTTON = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okPushBUTTON.sizePolicy().hasHeightForWidth())
        self.okPushBUTTON.setSizePolicy(sizePolicy)
        self.okPushBUTTON.setMinimumSize(QtCore.QSize(112, 32))
        self.okPushBUTTON.setMaximumSize(QtCore.QSize(112, 32))
        self.okPushBUTTON.setObjectName("okPushBUTTON")
        self.buttonsHorizontalLayout_2.addWidget(self.okPushBUTTON)
        self.verticalLayout.addLayout(self.buttonsHorizontalLayout_2)

        self.retranslateUi(runWindow)
        QtCore.QMetaObject.connectSlotsByName(runWindow)

    def retranslateUi(self, runWindow):
        _translate = QtCore.QCoreApplication.translate
        runWindow.setWindowTitle(_translate("runWindow", "Run"))
        self.label_2.setText(_translate("runWindow", "Enter an interval of time for data capture:"))
        self.intervalLABEL.setText(_translate("runWindow", "Interval (minutes):"))
        self.cancelPushBUTTON.setText(_translate("runWindow", "Cancel"))
        self.okPushBUTTON.setText(_translate("runWindow", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    runWindow = QtWidgets.QWidget()
    ui = Ui_runWindow()
    ui.setupUi(runWindow)
    runWindow.show()
    sys.exit(app.exec_())
