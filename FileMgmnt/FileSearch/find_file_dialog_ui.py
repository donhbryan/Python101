# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\db\Documents\GitHub\Python101\FileMgmnt\FileSearch\find_file_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(1111, 888)
        self.quitBtn = QtWidgets.QPushButton(WizardPage)
        self.quitBtn.setGeometry(QtCore.QRect(1020, 850, 75, 23))
        self.quitBtn.setObjectName("quitBtn")
        self.okBtn = QtWidgets.QPushButton(WizardPage)
        self.okBtn.setGeometry(QtCore.QRect(920, 850, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.status_lable = QtWidgets.QLabel(WizardPage)
        self.status_lable.setGeometry(QtCore.QRect(10, 855, 900, 10))
        self.status_lable.setObjectName("status_lable")
        self.textBrowser = QtWidgets.QTextBrowser(WizardPage)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 1071, 811))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        _translate = QtCore.QCoreApplication.translate
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage"))
        self.quitBtn.setText(_translate("WizardPage", "Quit"))
        self.okBtn.setText(_translate("WizardPage", "OK"))
        self.status_lable.setText(_translate("WizardPage", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WizardPage = QtWidgets.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

