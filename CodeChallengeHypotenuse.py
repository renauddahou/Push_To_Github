#find the hypotenuse of a triangle:
import math
def getHypotenuse(a, b):
    hypotenuse = math.sqrt(pow(a,2) + pow(b,2))
    return hypotenuse
a = int(input("Enter one side of the trianlge: "))
b = int(input("Enter the other side of the triangle: "))
hypotenuse = getHypotenuse(a, b)
print(f'the value of the hypotenuse is: {hypotenuse}')