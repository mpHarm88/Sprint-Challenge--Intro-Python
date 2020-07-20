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

class Vehicle:
    # No base class
    def __init__(self):
        pass
    
class FlightVehicle(Vehicle):
    # Vehicle base class
    def __init__(self):
        pass

class Starship(FlightVehicle):
    # FlightVehicle base class
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    # Vehicle base class
    def __init__(self):
        pass

class Car(GroundVehicle):
    # Ground vehicle base class
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    # Ground Vehicle base class
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    # Flight vehicle base class
    def __init__(self):
        pass