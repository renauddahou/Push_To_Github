def func(x):
    return x ** 2
call = func(5)
print(call)
#this is a parameter

def g(x = 2):
    return x ** 3
options = g(4)
print (options)
#In optional paramaters you are assigning a default value. EX: x = 2.
def h(x, y = 6):
    return x + y 
puts = h(8)
print (puts)

#Static and Class methods
    #static methods are shared equally among all the instances of the class
    #class methods are accessible on the class and not on the instance of the class
class MyClass:
    def method(self):
        return "instance method called", self
    @classmethod
    def classmethod(cls):
        return "class method called", cls
    @staticmethod 
    def staticmethod():
        return "static method called"
obj = MyClass()
obj.method()
print(obj.method())
obj.classmethod()
print(obj.classmethod())
obj.staticmethod()
print(obj.staticmethod())