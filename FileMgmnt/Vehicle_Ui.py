# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\db\Documents\GitHub\Python101\FileMgmnt\Vehicle_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(443, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 60, 211, 245))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vmanufacturer = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vmanufacturer.setFont(font)
        self.vmanufacturer.setObjectName("vmanufacturer")
        self.verticalLayout_2.addWidget(self.vmanufacturer)
        self.vname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vname.setFont(font)
        self.vname.setObjectName("vname")
        self.verticalLayout_2.addWidget(self.vname)
        self.vmodelyear = QtWidgets.QLabel(self.layoutWidget)
        self.vmodelyear.setObjectName("vmodelyear")
        self.verticalLayout_2.addWidget(self.vmodelyear)
        self.vdoors = QtWidgets.QLabel(self.layoutWidget)
        self.vdoors.setObjectName("vdoors")
        self.verticalLayout_2.addWidget(self.vdoors)
        self.vbodystyle = QtWidgets.QLabel(self.layoutWidget)
        self.vbodystyle.setObjectName("vbodystyle")
        self.verticalLayout_2.addWidget(self.vbodystyle)
        self.venginesize = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.venginesize.setFont(font)
        self.venginesize.setObjectName("venginesize")
        self.verticalLayout_2.addWidget(self.venginesize)
        self.vhorsepower = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vhorsepower.setFont(font)
        self.vhorsepower.setObjectName("vhorsepower")
        self.verticalLayout_2.addWidget(self.vhorsepower)
        self.vfueltype = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vfueltype.setFont(font)
        self.vfueltype.setObjectName("vfueltype")
        self.verticalLayout_2.addWidget(self.vfueltype)
        self.vdrivenwheels = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vdrivenwheels.setFont(font)
        self.vdrivenwheels.setObjectName("vdrivenwheels")
        self.verticalLayout_2.addWidget(self.vdrivenwheels)
        self.vtype = QtWidgets.QLabel(self.centralwidget)
        self.vtype.setGeometry(QtCore.QRect(120, 10, 71, 41))
        self.vtype.setScaledContents(True)
        self.vtype.setObjectName("vtype")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 60, 103, 245))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_0 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.verticalLayout.addWidget(self.label_0)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.picturelabel = QtWidgets.QLabel(self.centralwidget)
        self.picturelabel.setGeometry(QtCore.QRect(20, 330, 311, 261))
        self.picturelabel.setObjectName("picturelabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vehicle Display"))
        self.vmanufacturer.setText(_translate("MainWindow", "Manufacturer"))
        self.vname.setText(_translate("MainWindow", "Name"))
        self.vmodelyear.setText(_translate("MainWindow", "Model Year"))
        self.vdoors.setText(_translate("MainWindow", "Doors"))
        self.vbodystyle.setText(_translate("MainWindow", "Body Style"))
        self.venginesize.setText(_translate("MainWindow", "Engine Size"))
        self.vhorsepower.setText(_translate("MainWindow", "Horsepower"))
        self.vfueltype.setText(_translate("MainWindow", "Fuel Type"))
        self.vdrivenwheels.setText(_translate("MainWindow", "Driven Wheels"))
        self.vtype.setText(_translate("MainWindow", "🚒"))
        self.label_2.setText(_translate("MainWindow", "Manufacturer"))
        self.label_0.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Model Year"))
        self.label_8.setText(_translate("MainWindow", "Doors"))
        self.label_7.setText(_translate("MainWindow", "Body Style"))
        self.label_4.setText(_translate("MainWindow", "Engine Size"))
        self.label_5.setText(_translate("MainWindow", "Horsepower"))
        self.label_3.setText(_translate("MainWindow", "Fuel Type"))
        self.label_1.setText(_translate("MainWindow", "Driven Wheels"))
        self.picturelabel.setText(_translate("MainWindow", "picture"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
