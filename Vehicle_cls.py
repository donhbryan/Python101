
from pprint import pprint


class Vehicle:
    FuelType = ('Gas', 'Deisel', 'Electric', 'CNG')
    DriveType = ('FWD', 'RWD', 'AWD')

    def __init__(self, mfg, name):
        self.mfg = mfg
        self.name = name
        self.fueltype = None
        self.size = None
        self.horsepower = None
        self.drive = None

    def SetEngine(self, fueltype, size, horsepower, drive):
        if fueltype in Vehicle.FuelType:
            self.fueltype = fueltype
        else:
            self.fueltype = None
        self.size = size
        self.horsepower = horsepower
        if drive in Vehicle.DriveType:
            self.drive = drive
        else:
            self.drive = None


class Car(Vehicle):
    # super().__init__(self, mfg, name):
    pass


def main():
    etype = Car('Jaguar', 'XKE 2+2')
    # print(type(etype))
    # print(etype)
    etype.SetEngine("Gas", 4.2, 256, "RWD")
    temp = vars(etype)
    for item in temp:
        print(f"Item: {item} = {temp[item]}")
    print("%s %s" for item in temp.items())
    print(' -- '.join("%s: %s" % item for item in temp.items()))
    print(etype.__dict__)
    print(dir(etype))
    pprint(vars(etype))
    pprint(globals())
    pprint(locals())


main()
