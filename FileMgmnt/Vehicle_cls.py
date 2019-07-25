import unicodedata
import Vehicle_Ui
from PyQt5 import QtCore, QtGui, QtWidgets
import emoji 
from pprint import pprint
import sys

# Vehicle_Type = {"car": "🚗", "truck": "🚙", "taxi": "🚕"}

Vehicle_Type = {"car": emoji.emojize(
    ':automobile:'), "truck":  emoji.emojize(":truck:"), "lorry":  emoji.emojize(":articulated_lorry:"), "bike":  emoji.emojize(":motorcycle:")}


class Vehicle:
    FuelType = ('Gas', 'Deisel', 'Electric', 'CNG')
    DriveType = ('FWD', 'RWD', 'AWD')


    def __init__(self, mfg, name):
        self.mfg = mfg
        self.name = name
        self.modelyear = None
        self.fueltype = None
        self.enginesize = None
        self.horsepower = None
        self.drive = None

    def SetEngine(self, fueltype, enginesize, horsepower, drive):
        if fueltype in Vehicle.FuelType:
            self.fueltype = fueltype
        else:
            self.fueltype = None
        self.enginesize = enginesize
        self.horsepower = horsepower
        if drive in Vehicle.DriveType:
            self.drive = drive
        else:
            self.drive = None

    def get_name(self):
        if self.name is None:
            return None
        else:
            return self.name

    def get_manufacturer(self):
        if self.mfg is None:
            return None
        else:
            return self.mfg

    def get_modelyear(self):
        if self.modelyear is None:
            return None
        else:
            return self.modelyear

    def get_doors(self):
        if self.doors is None:
            return None
        else:
            return self.doors

    def get_bodystyle(self):
        if self.bodystyle is None:
            return None
        else:
            return self.bodystyle

    def get_type(self):
        if self.type is None:
            return None
        else:
            return self.type

    def get_enginesize(self):
        if self.enginesize is None:
            return None
        else:
            return self.enginesize

    def get_horsepower(self):
        if self.horsepower is None:
            return None
        else:
            return self.horsepower

    def get_fueltype(self):
        if self.fueltype is None:
            return None
        else:
            return self.fueltype

    def get_drivenwheels(self):
        if self.drive is None:
            return None
        else:
            return self.drive


# 🏍🏎🛥🛶🚲🚒🚗
class Car(Vehicle):



    def __init__(self, mfg, name, modelyear, doors, bodystyle, vehicletype=Vehicle_Type["car"]):
        super().__init__(mfg, name)
        self.modelyear = modelyear
        self.doors = doors
        self.bodystyle = bodystyle
        self.type = vehicletype
        # pass


class VehicleUI(QtWidgets.QMainWindow, Vehicle_Ui.Ui_MainWindow):
    def __init__(self,  *args, **kwargs):
        super(VehicleUI, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.loadpage()

    def loadpage(self):
        etype = Car('Jaguar', 'XKE 2+2', 1968, 2, 'Coupe')
        etypeconv = Car('Jaguar', 'XKE', 1968, 2, 'Convertible')
        # print(type(etype))
        # print(etype)
        etype.SetEngine("Gas", 4.2, 256, "RWD")
        etypeconv.SetEngine("Gas", 308, 256, "RWD")
        temp = vars(etype)

        self.vmanufacturer.setText(etype.get_manufacturer())
        self.vname.setText(etype.get_name())
        self.vmodelyear.setText(str(etype.get_modelyear()))
        self.vdoors.setText(str(etype.get_doors()))
        self.vbodystyle.setText(etype.get_bodystyle())
        self.venginesize.setText(str(etype.get_enginesize()))
        self.vhorsepower.setText(str(etype.get_horsepower()))
        self.vfueltype.setText(etype.get_fueltype())
        self.vdrivenwheels.setText(etype.get_drivenwheels())
        self.vtype.setText(etype.get_type())

# for item in temp:
#     print(f"Item: {item} = {temp[item]}")
# print("%s %s /n" for item in temp.items())
# pprint(' -- '.join("%s: %s" % item for item in temp.items()))
# print(etype.__dict__)
# print(dir(etype))

# pprint(vars(etype))
# pprint(vars(etypeconv))

# pprint(globals())
# pprint(locals())
# print(etype.type)


def main():
    # prime()
    app = QtWidgets.QApplication(sys.argv)
    win = VehicleUI()
    win.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

'''
s = u'\u0627'   
# import unicodedata
s = u"\U0001F697"
x = s.encode('utf-32')  
print(x.decode('unicode-escape'))

print(u"\U0001F697".encode('utf-8'))
print("\N{SNAKE}")

print(emoji.emojize("Python is fun :thumbsup:", use_aliases=True))
'''
