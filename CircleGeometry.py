#Write a function to find the circumference of a circle
import math 
def getCircumference(radius):
    circumference = 2 * math.pi * radius
    return circumference
radius = float(input("Enter your radius: "))
circumference = getCircumference(radius)
print(f'the circumference of this circle is: {circumference}')