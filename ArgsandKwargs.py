#*args = parameter that will pack all arguments into a tuple. 
# useful so a function can accept varying arguments
def add (*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6))

#**kwargs parameter that will pack all arguments into a dictionary
# useful so that a function can accept varying amount of keyword arguments
def hello(**kwargs):
    #print("Hello" + kwargs['first'] + " " + kwargs['last'])
    print("Hello" , end=" ")
    for key , value  in kwargs.items():
        print(value, end=" ")
hello(title="Mr", first="Bro", mmiddle="Dude", last="Code")