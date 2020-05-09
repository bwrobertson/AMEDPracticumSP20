# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vm_System_Settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from NewScenario import Ui_NewScenario
from pymongo import MongoClient
from DBConfiguration import Ui_DBConfiguration

class Ui_VmSystemSettings(object):

    def saveMachine(self):
        try:
            client = MongoClient(Ui_DBConfiguration.dbConnection)
        except:
            client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test")
        db = client.Test
        data = db["Scenario"]

        change = {}
        custom = {}

        change["memory"] = self.baseMemorySPINBOX.value()
        change["processors"] = self.processorsSPINBOX.value()
        # print(change)

        custom["--boot"] = self.getBootOrder()
        custom["--vrde"] = "on"         #rdp always on
        custom["--apis"] = "on" if self.enableIOApicCHECKBOX.isChecked() else "off"
        custom["--firmware"] = "on" if self.enableEfiCHECKBOX.isChecked() else "off"
        custom["--rtcuseutc"] = "on" if self.hardwareClockCHECKBOX.isChecked() else "off"
        custom["--cpuexecutioncap"] = self.executionCapSPINBOX.value()
        custom["--pae"] = "on" if self.enablePaeNxQCHECKBOX.isChecked() else "off"
        custom["--hwvirtex"] = "on" if self.enableVtxAmdv_CHECKBOX.isChecked() else "off"
        custom["--nestedpaging"] = "on" if self.enableNestedPagingCHECKBOX.isChecked() else "off"
        # print(custom)
        
        settings = {"regular": change,
                        "vbox": custom}
    
        self.parentWindow.get_settings(settings)
        self.close()

        # scen = data.find_one({'_id': ObjectId(Ui_NewScenario.id)})

    def getBootOrder(self):
        if(self.floppyCHECKBOX.isChecked()):
            return 1
        elif(self.opticalCHECKBOX.isChecked()):
            return 2
        elif(self.harddiskCHECKBOX.isChecked()):
            return 3
        elif(self.networkCHECKBOX.isChecked()):
            return 4
        return 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 659)
        Form.setMinimumSize(QtCore.QSize(451, 659))
        Form.setMaximumSize(QtCore.QSize(500, 660))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 471, 601))
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.motherboardLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.motherboardLABEL.setFont(font)
        self.motherboardLABEL.setObjectName("motherboardLABEL")
        self.verticalLayout_6.addWidget(self.motherboardLABEL)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.baseMemoryLABEL = QtWidgets.QLabel(self.widget)
        self.baseMemoryLABEL.setObjectName("baseMemoryLABEL")
        self.horizontalLayout.addWidget(self.baseMemoryLABEL)
        self.baseMemorySPINBOX = QtWidgets.QSpinBox(self.widget)
        self.baseMemorySPINBOX.setMaximum(999999999)
        self.baseMemorySPINBOX.setProperty("value", 2048)
        self.baseMemorySPINBOX.setObjectName("baseMemorySPINBOX")
        self.horizontalLayout.addWidget(self.baseMemorySPINBOX)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bootOrderLABEL = QtWidgets.QLabel(self.widget)
        self.bootOrderLABEL.setObjectName("bootOrderLABEL")
        self.horizontalLayout_2.addWidget(self.bootOrderLABEL)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.floppyCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.floppyCHECKBOX.setObjectName("floppyCHECKBOX")
        self.verticalLayout.addWidget(self.floppyCHECKBOX)
        self.opticalCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.opticalCHECKBOX.setObjectName("opticalCHECKBOX")
        self.verticalLayout.addWidget(self.opticalCHECKBOX)
        self.harddiskCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.harddiskCHECKBOX.setObjectName("harddiskCHECKBOX")
        self.verticalLayout.addWidget(self.harddiskCHECKBOX)
        self.networkCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.networkCHECKBOX.setObjectName("networkCHECKBOX")
        self.verticalLayout.addWidget(self.networkCHECKBOX)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chipsetLABEL = QtWidgets.QLabel(self.widget)
        self.chipsetLABEL.setObjectName("chipsetLABEL")
        self.horizontalLayout_3.addWidget(self.chipsetLABEL)
        self.chipsetCOMBOBOX = QtWidgets.QComboBox(self.widget)
        self.chipsetCOMBOBOX.setObjectName("chipsetCOMBOBOX")
        self.chipsetCOMBOBOX.addItem("")
        self.horizontalLayout_3.addWidget(self.chipsetCOMBOBOX)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pointingDeviceLABEL = QtWidgets.QLabel(self.widget)
        self.pointingDeviceLABEL.setObjectName("pointingDeviceLABEL")
        self.horizontalLayout_4.addWidget(self.pointingDeviceLABEL)
        self.pointingDeviceCOMBOBOX = QtWidgets.QComboBox(self.widget)
        self.pointingDeviceCOMBOBOX.setObjectName("pointingDeviceCOMBOBOX")
        self.pointingDeviceCOMBOBOX.addItem("")
        self.horizontalLayout_4.addWidget(self.pointingDeviceCOMBOBOX)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.extendedFeaturesLABEL = QtWidgets.QLabel(self.widget)
        self.extendedFeaturesLABEL.setObjectName("extendedFeaturesLABEL")
        self.horizontalLayout_5.addWidget(self.extendedFeaturesLABEL)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.enableIOApicCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.enableIOApicCHECKBOX.setObjectName("enableIOApicCHECKBOX")
        self.verticalLayout_2.addWidget(self.enableIOApicCHECKBOX)
        self.enableEfiCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.enableEfiCHECKBOX.setObjectName("enableEfiCHECKBOX")
        self.verticalLayout_2.addWidget(self.enableEfiCHECKBOX)
        self.hardwareClockCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.hardwareClockCHECKBOX.setObjectName("hardwareClockCHECKBOX")
        self.verticalLayout_2.addWidget(self.hardwareClockCHECKBOX)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.processorLABEL_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.processorLABEL_2.setFont(font)
        self.processorLABEL_2.setObjectName("processorLABEL_2")
        self.verticalLayout_5.addWidget(self.processorLABEL_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.processorLABEL = QtWidgets.QLabel(self.widget)
        self.processorLABEL.setObjectName("processorLABEL")
        self.horizontalLayout_6.addWidget(self.processorLABEL)
        self.processorsSPINBOX = QtWidgets.QSpinBox(self.widget)
        self.processorsSPINBOX.setMaximum(10)
        self.processorsSPINBOX.setProperty("value", 2)
        self.processorsSPINBOX.setObjectName("processorsSPINBOX")
        self.horizontalLayout_6.addWidget(self.processorsSPINBOX)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.executionCapLABEL = QtWidgets.QLabel(self.widget)
        self.executionCapLABEL.setObjectName("executionCapLABEL")
        self.horizontalLayout_7.addWidget(self.executionCapLABEL)
        self.executionCapSPINBOX = QtWidgets.QSpinBox(self.widget)
        self.executionCapSPINBOX.setSuffix("")
        self.executionCapSPINBOX.setMaximum(100)
        self.executionCapSPINBOX.setProperty("value", 100)
        self.executionCapSPINBOX.setObjectName("executionCapSPINBOX")
        self.horizontalLayout_7.addWidget(self.executionCapSPINBOX)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.extendedFeaturesEnablePaeNxLABEL = QtWidgets.QLabel(self.widget)
        self.extendedFeaturesEnablePaeNxLABEL.setObjectName("extendedFeaturesEnablePaeNxLABEL")
        self.horizontalLayout_8.addWidget(self.extendedFeaturesEnablePaeNxLABEL)
        self.enablePaeNxQCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.enablePaeNxQCHECKBOX.setObjectName("enablePaeNxQCHECKBOX")
        self.horizontalLayout_8.addWidget(self.enablePaeNxQCHECKBOX)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.accelerationLABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.accelerationLABEL.setFont(font)
        self.accelerationLABEL.setObjectName("accelerationLABEL")
        self.verticalLayout_4.addWidget(self.accelerationLABEL)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.paravirtualizationInterfaceLABEL = QtWidgets.QLabel(self.widget)
        self.paravirtualizationInterfaceLABEL.setObjectName("paravirtualizationInterfaceLABEL")
        self.horizontalLayout_9.addWidget(self.paravirtualizationInterfaceLABEL)
        self.paravirtualizationInterfaceCOMBOBOX = QtWidgets.QComboBox(self.widget)
        self.paravirtualizationInterfaceCOMBOBOX.setObjectName("paravirtualizationInterfaceCOMBOBOX")
        self.paravirtualizationInterfaceCOMBOBOX.addItem("")
        self.horizontalLayout_9.addWidget(self.paravirtualizationInterfaceCOMBOBOX)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.hardwareVirtualizationLABEL = QtWidgets.QLabel(self.widget)
        self.hardwareVirtualizationLABEL.setObjectName("hardwareVirtualizationLABEL")
        self.horizontalLayout_10.addWidget(self.hardwareVirtualizationLABEL)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.enableVtxAmdv_CHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.enableVtxAmdv_CHECKBOX.setObjectName("enableVtxAmdv_CHECKBOX")
        self.verticalLayout_3.addWidget(self.enableVtxAmdv_CHECKBOX)
        self.enableNestedPagingCHECKBOX = QtWidgets.QCheckBox(self.widget)
        self.enableNestedPagingCHECKBOX.setObjectName("enableNestedPagingCHECKBOX")
        self.verticalLayout_3.addWidget(self.enableNestedPagingCHECKBOX)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.okBUTTON = QtWidgets.QPushButton(self.widget)
        self.okBUTTON.setObjectName("okBUTTON")
        self.okBUTTON.clicked.connect(self.saveMachine)
        self.horizontalLayout_11.addWidget(self.okBUTTON)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.cancelBUTTON = QtWidgets.QPushButton(self.widget)
        self.cancelBUTTON.setObjectName("cancelBUTTON")
        self.horizontalLayout_11.addWidget(self.cancelBUTTON)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "VM System Settings"))
        self.motherboardLABEL.setText(_translate("Form", "Motherboard"))
        self.baseMemoryLABEL.setText(_translate("Form", "Base Memory"))
        self.bootOrderLABEL.setText(_translate("Form", "Boot Order"))
        self.floppyCHECKBOX.setText(_translate("Form", "Floppy"))
        self.opticalCHECKBOX.setText(_translate("Form", "Optical"))
        self.harddiskCHECKBOX.setText(_translate("Form", "Hard Disk"))
        self.networkCHECKBOX.setText(_translate("Form", "Network"))
        self.chipsetLABEL.setText(_translate("Form", "Chipset"))
        self.chipsetCOMBOBOX.setItemText(0, _translate("Form", "PIX3"))
        self.pointingDeviceLABEL.setText(_translate("Form", "Pointing Device"))
        self.pointingDeviceCOMBOBOX.setItemText(0, _translate("Form", "USB Tablet"))
        self.extendedFeaturesLABEL.setText(_translate("Form", "Extended Features"))
        self.enableIOApicCHECKBOX.setText(_translate("Form", "Enable I/O APIC"))
        self.enableEfiCHECKBOX.setText(_translate("Form", "Enable EFI (Special OSes Only)"))
        self.hardwareClockCHECKBOX.setText(_translate("Form", "Hardware Clock in UTC Time"))
        self.processorLABEL_2.setText(_translate("Form", "Processor"))
        self.processorLABEL.setText(_translate("Form", "Processor(s)"))
        self.executionCapLABEL.setText(_translate("Form", "Execution Cap"))
        self.extendedFeaturesEnablePaeNxLABEL.setText(_translate("Form", "Extended Features"))
        self.enablePaeNxQCHECKBOX.setText(_translate("Form", " Enable PAE/NX"))
        self.accelerationLABEL.setText(_translate("Form", "Acceleration"))
        self.paravirtualizationInterfaceLABEL.setText(_translate("Form", "Paravirtualization Interface"))
        self.paravirtualizationInterfaceCOMBOBOX.setItemText(0, _translate("Form", "Default"))
        self.hardwareVirtualizationLABEL.setText(_translate("Form", "Hardware Virtualization"))
        self.enableVtxAmdv_CHECKBOX.setText(_translate("Form", "Enable VT-x/AMD-v"))
        self.enableNestedPagingCHECKBOX.setText(_translate("Form", "Enable Nested Paging"))
        self.okBUTTON.setText(_translate("Form", "OK"))
        self.cancelBUTTON.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_VmSystemSettings()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

