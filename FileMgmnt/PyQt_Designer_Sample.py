import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
# from PyQt5.uic import loadUi

import MainWindows1

# "C:\Users\db\Anaconda3\Library\bin\pyuic5.bat" -x MainWindows1.ui -o "C:\Users\db\Python-Source\File Management\MainWindows1.py"


class Life2Coding(QtWidgets.QMainWindow, MainWindows1.Ui_MainWindow):
    '''
    Test dialog using PyQt5 Designer.
    '''

    def __init__(self,  *args, **kwargs):
        super(Life2Coding, self).__init__(*args, **kwargs)
        self.setupUi(self)
# '''
        self.btnOk.clicked.connect(self.ok_pushButton_clicked)
        self.btnQuit.clicked.connect(self.quit_pushButton_clicked)
        self.btnBrowse.clicked.connect(self.browse_folder)

    def ok_pushButton_clicked(self):
        self.textEdit.setText('Hello: ' + self.editName.text())

    def quit_pushButton_clicked(self):
        sys.exit()

    def browse_folder(self):
        self.listWidget.clear()  # In case there are any existing elements in the list
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Pick a folder")
        print(directory)
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory:  # if user didn't pick a directory don't continue
            # for all files, if any, in the directory
            for file_name in os.listdir(directory):
                # add file to the listWidget
                self.listWidget.addItem(file_name)
# '''

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Life2Coding()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

    # app = QtWidgets.QApplication(sys.argv)
    # MyWindow    = Life2Coding()
    # MyWindow.show()
    # sys.exit(app.exec_())
