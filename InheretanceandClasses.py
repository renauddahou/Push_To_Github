#inheratence within classes and objects
#the class labeled Pet is a Parent class
#the classes labeled Dog is the Child class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'I am  {self.name} and i am  {self.age}')
class Dog(Pet):
    def speak(self):
        print('Woof')
p = Pet('tim', 19)
p.show()
d = Dog('jim' , 23)
d.show()
d.speak()

#multiple inheretance is when a Child class is derived from a Parent class
class Prey:
    def flee(self):
        print("this animal flees")
class Predator:
    def hunt(self):
        print("this animal hunts")
class Rabbit(Prey):
    pass
class Fish(Prey, Predator):
    pass
class Hawk(Predator):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()