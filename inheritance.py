class Vehicle:
    def general_usage(self):
        print("General Usage: Transportation")

class Car(Vehicle):
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        print("specific use: Commute to Work, vacation with family")

class Motor(Vehicle):
    def __init__(self):
        print("I am Motor")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        print("specific use: Racing")


c= Car()
c.general_usage()
c.specific_usage()

m=Motor()
m.general_usage()
m.specific_usage()
