#abstract classes prevent user from creating an object from that class
#abstract class contains one or more abstract methods
#abstraact method- has a declaration but doesnt have an implementation
#to use abstract class and method, import 'ABC' and 'abstractmethod'

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("you drive the car")
    def stop(self):
        print("this car is stopped")
class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")
    def stop(self):
        print("this motorcyle has stopped")
#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()
#vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()