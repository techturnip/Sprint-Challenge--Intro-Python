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
    pass

# Flying vehicles
class FlightVehicle(Vehicle):
    # BASE -> Vehicle
            
    pass

class Airplane(FlightVehicle):
    # BASE -> FlightVehicle
        
    pass

class Starship(FlightVehicle):
    # BASE -> FlightVehicle
         
    pass

# Ground vehicles
class GroundVehicle(Vehicle):
    # BASE -> Vehicle
    
    pass

class Car(GroundVehicle):
    # Base -> GroundVehicle
    
    pass

class Motorcycle(GroundVehicle):
    # Base -> GroundVehicle
    
    pass