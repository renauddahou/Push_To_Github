#class and object are fundamental to object oriented programming
class Laptop:
    def __init__(self,color,make,model):
        self.color = color
        self.make = make
        self.model = model
laptop = Laptop('tan', 'lenovo', 'ideaPad3')
print(laptop.color)
print(laptop.model)
print(laptop.make)

#objects as arguments
class Car:
    color = None
def change_color(car, color):
    car.color = color
car1 = Car()
car2 = Car()
car3 = Car()
change_color(car1, "red")
change_color(car2, 'blue')
change_color(car3, "white")
print(car1.color)
print(car2.color)
print(car3.color)

#duck typing is when the class of an object is less important than the method/attribute that the class has
class Duck:
    def walk(self):
        print("this duck is walking")
class Chicken:
    def walk(self):
        print("this chicken is walking")
class Person():
    def catch(self, duck):
        duck.walk()
        print("you caught the critter")
duck = Duck()
chicken = Chicken()
person = Person()
person.catch(duck)