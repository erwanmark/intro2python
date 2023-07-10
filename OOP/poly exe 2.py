class Car:
    def __init__(self, make, model):
      self.make = make
      self.model = model

    def move (self):
        print("Driving around")

class plane:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def move(self):
            print("Flying Around")

class MotorBike:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def move(self):
            print("ride")

#instance of our classes

car = Car("Dodge", "Challenger")
plane = plane("Boeing","737")
bike = MotorBike("Kawasaki","Ninja650")

for i in (car, plane, bike):
    i.move()


