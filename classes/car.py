class Car:

    def __init__(self, doors, color):
        self.doors = doors
        self.color = color
        self.wheels = 4
        self.range = 400
    
    def drive(self, distance):
        self.range = self.range - distance
        return f"brrrrr brrrrrrrrr brrr brrrrrrr sqeeek, you have {self.range} miles remaining"

    def explain(self):
        return f"i'm a car with {self.doors} doors and i'm colored {self.color}"
