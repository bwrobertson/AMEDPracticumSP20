# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time 
from tqdm import tqdm
import requests



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 183)
        self.exportPUSHBUTTON = QtWidgets.QPushButton(Dialog)
        self.exportPUSHBUTTON.setGeometry(QtCore.QRect(30, 140, 112, 32))
        self.exportPUSHBUTTON.setObjectName("exportPUSHBUTTON")    
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(80, 30, 261, 61))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.exportPUSHBUTTON.clicked.connect(self.progress) 
        #self.exportPUSHBUTTON.clicked.connect(self.download)
    
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Progress  "))
        self.exportPUSHBUTTON.setText(_translate("Dialog", "Export"))
        self.label.setText(_translate("Dialog", "Running"))

    def progress(self):
        url = "http://localhost/practicum/TEST2.pdf"
        file_name = "TEST2.pdf"
        r = requests.get(url, stream = True) #get url request
        f = open(file_name, 'wb')
        file_size = int(r.headers['Content-Length'])

        chunk_size = int(file_size / 100)

        self.count = 0
        for chunk in r.iter_content(chunk_size = chunk_size): #loop# = file_size/chunk_size
            f.write(chunk)
            self.count+=1
            print(self.count)
            self.progressBar.setValue(self.count)
           
        f.close
        print("Dowload Complete!")
        print(file_size)
        return
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
