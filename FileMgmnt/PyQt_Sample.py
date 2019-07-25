# import PyQt5
# from PyQt5.QtCore import Slot
# from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton,
#                              QVBoxLayout, QWidget)

# from PyQt5.QtGui import *
# (QApplication, QLabel, QPushButton,
#  QVBoxLayout, QWidget, QMainWindow)
# from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#(QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QMainWindow)

from PyQt5 import (QtGui)
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QSizePolicy,
                             QDoubleSpinBox, QLabel, QCheckBox, QMainWindow,
                             QGridLayout)
from PyQt5.QtCore import QCoreApplication
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)  # boilerplate
        self.setWindowTitle("The Title")
        label = QLabel("this is a label")
        # label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        # btn.resize(25,50)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(80, 70)


class SubWindows2(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SubWindows2, self).__init__(*args, **kwargs)  # boilerplate
        self.setWindowTitle("The Title2")
        label = QLabel("this is a label2")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


class SubWindow1(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SubWindow1, self).__init__(*args, **kwargs)  # boilerplate
        self.setWindowTitle("Subwindow 1")
        self.setGeometry(100, 100, 500, 500)
        self.setWindowIcon(QtGui.QIcon('pyc.png'))
        now = QDateTime.currentDateTime()
        print(now.toString())
        label = QLabel(f"date: {now.toString()}")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

#
# print(now.toString(Qt.ISODateWithMs))
# print(now.toString(Qt.DefaultLocaleLongDate))


def run():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sw1 = SubWindow1()
    sw1.show()
    # sys.exit(app.exec_())
    app.exec_()


run()
'''


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
                      "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
'''
