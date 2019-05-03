import unicodedata
import emoji
from pprint import pprint


class Vehicle:
    FuelType = ('Gas', 'Deisel', 'Electric', 'CNG')
    DriveType = ('FWD', 'RWD', 'AWD')

    def __init__(self, mfg, name):
        self.mfg = mfg
        self.name = name
        # self.modelyear = None
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


# 🏍🏎🛥🛶🚲🚒🚗
class Car(Vehicle):
    Vehicle_Type = {"car": emoji.emojize(
        "🚗"), "truck": "🚙", "taxi": "🚕"}
    Vehicle_Type = {"car": emoji.emojize(
        ':automobile:'), "truck":  emoji.emojize(":truck:"), "lorry":  emoji.emojize(":articulated_lorry:"), "bike":  emoji.emojize(":motorcycle:")}

    def __init__(self, mfg, name, modelyear, doors, bodystyle, vehicletype=Vehicle_Type["car"]):
        super().__init__(mfg, name)
        self.modelyear = modelyear
        self.doors = doors
        self.bodystyle = bodystyle
        self.type = vehicletype
        # pass


def main():
    etype = Car('Jaguar', 'XKE 2+2', 1968, 2, 'Coupe')
    etypeconv = Car('Jaguar', 'XKE', 1968, 2, 'Convertible')
    # print(type(etype))
    # print(etype)
    etype.SetEngine("Gas", 4.2, 256, "RWD")
    etypeconv.SetEngine("Gas", 308, 256, "RWD")
    temp = vars(etype)
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
    print(etype.type)


main()
'''
s = u'\u0627'
# import unicodedata
s = u"\U0001F697"
x = s.encode('utf-32')  
print(x.decode('unicode-escape'))

print(u"\U0001F697".encode('utf-8'))
print("\N{SNAKE}")
'''
print(emoji.emojize("Python is fun :thumbsup:", use_aliases=True))
