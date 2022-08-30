class Vehicle(object):

    def __init__(self, fuel, range):
        self.fuel = fuel
        self.range = range

    def drive(self, distance):
        self.range = self.range - distance
        return f"brrrrr brrrrrrrrr brrr brrrrrrr sqeeek, you have {self.range} miles remaining"

class Car(Vehicle):

    def __init__(self, fuel, range):
        super().__init__(fuel, range)
        self.type = "car"
    
    def explain(self):
        return f"i'm a {self.type} with {self.fuel} fuel and i have a range of {self.range} miles"

class Bike(Vehicle):

    def __init__(self, fuel, range):
        super().__init__(fuel, range)
        self.type = "Bike"
    
    def explain(self):
        return f"i'm a {self.type} with {self.fuel} fuel and i have a range of {self.range} miles"
