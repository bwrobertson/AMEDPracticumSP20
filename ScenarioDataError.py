# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Scenario_Data_Error.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scenarioDataError(object):
    def setupUi(self, scenarioDataError):
        scenarioDataError.setObjectName("scenarioDataError")
        scenarioDataError.resize(469, 200)
        scenarioDataError.setMinimumSize(QtCore.QSize(469, 200))
        scenarioDataError.setMaximumSize(QtCore.QSize(469, 200))
        self.widget = QtWidgets.QWidget(scenarioDataError)
        self.widget.setGeometry(QtCore.QRect(140, 110, 198, 58))
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
        self.textLABEL.setObjectName("textLABEL")
        self.verticalLayout.addWidget(self.textLABEL)
        self.okayBUTTON = QtWidgets.QPushButton(self.widget)
        self.okayBUTTON.setObjectName("okayBUTTON")
        self.verticalLayout.addWidget(self.okayBUTTON)
        self.sadFaceLABEL = QtWidgets.QLabel(scenarioDataError)
        self.sadFaceLABEL.setGeometry(QtCore.QRect(190, 30, 91, 61))
        self.sadFaceLABEL.setText("")
        self.sadFaceLABEL.setPixmap(QtGui.QPixmap("sadface.png"))
        self.sadFaceLABEL.setScaledContents(True)
        self.sadFaceLABEL.setWordWrap(True)
        self.sadFaceLABEL.setObjectName("sadFaceLABEL")

        self.retranslateUi(scenarioDataError)
        QtCore.QMetaObject.connectSlotsByName(scenarioDataError)

    def retranslateUi(self, scenarioDataError):
        _translate = QtCore.QCoreApplication.translate
        scenarioDataError.setWindowTitle(_translate("scenarioDataError", "Scenario Data Error"))
        self.textLABEL.setText(_translate("scenarioDataError", "Scenario has no data to export!"))
        self.okayBUTTON.setText(_translate("scenarioDataError", "Okay"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scenarioDataError = QtWidgets.QDialog()
    ui = Ui_scenarioDataError()
    ui.setupUi(scenarioDataError)
    scenarioDataError.show()
    sys.exit(app.exec_())

