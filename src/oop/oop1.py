# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# THIS IS THE BASE CLASS
class Vehicle:
    def __init__(self, name):
        self.name = name
    pass

# Flying vehicles
class FlightVehicle(Vehicle):
    # BASE -> Vehicle
    def __init__(self, name):
        super().__init__(name)
        
    pass

class Airplane(FlightVehicle):
    # BASE -> FlightVehicle
    def __init__(self, name):
        super().__init__(name)
    
    pass

class Starship(FlightVehicle):
    # BASE -> FlightVehicle
    def __init__(self, name):
        super().__init__(name)
     
    pass

# Ground vehicles
class GroundVehicle(Vehicle):
    # BASE -> Vehicle
    def __init__(self, name):
        super().__init__(name)

    pass

class Car(GroundVehicle):
    # Base -> GroundVehicle
    def __init__(self, name):
        super().__init__(name)

    pass

class Motorcycle(GroundVehicle):
    # Base -> GroundVehicle
    def __init__(self, name):
        super().__init__(name)
        
    pass