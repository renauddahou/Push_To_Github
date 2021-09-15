#module is a file containing Python definitions and statements
#the word import allows you to pull modules from within Python
import random #random is a module
a = random.randint(0,100) #.randit picks random number of integers
print(a)
basket = ['apples', 'grapes', 'oranges', 'blueberries']
choose_fruit = random.choice(basket) #.choice picks an item from within a list
print(choose_fruit)
print("An even number within 50 is:" )
print(random.randrange(2,50, 2)) #.randrange picks an item within a range. only works with integers
print("random floating point number between 10 and 20 is:")
print(random.uniform(10, 20)) #.uniform returns a random floating number from a given range
Li= [1 ,2, 3, 4, 5, 6]
random.shuffle(Li) #.shuffle shuffles the items within a list
print(Li)