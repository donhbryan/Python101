
from PyQt5 import QtCore, QtGui, QtWidgets
import testunicode
import sys


class MyUnicodeTest(QtWidgets.QMainWindow,  testunicode.Ui_MainWindow):
    '''
    Test red car
    '''

    def __init__(self,  *args, **kwargs):
        super(MyUnicodeTest, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.marbles.text = "french"
        u = chr(233) + chr(0x0bf2) + \
            chr(3972) + chr(6000) + chr(13231)+chr(797)


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MyUnicodeTest()
    win.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


'''
print("Fichier non trouvé")
répertoire = 'funky'
# print(répertoire.decode('1252'))
# print(emoji.emojize(':red_car:', use_aliases=True))

u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)+chr(797)

for i, c in enumerate(u):
    print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
    print(unicodedata.name(c))

# Get numeric value of second character
print(unicodedata.numeric(u[1]))
'''
