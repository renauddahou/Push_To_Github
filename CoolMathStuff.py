#Fibonacci using Recursion:
def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-2)+fib(n-1)
n = int(input("Enter a number for the sequence: "))
for i in range(n):
    print(fib(i))
print(20*"-")
#multiplication table:
number = int(input("Enter a number to see multiplication table: "))
for i in range(0, 13):
    print(number, 'x', i, '=', number*i)
print(20*"-")
#Find the factorial:
import math
m = int(input("Enter a numbeer to find the factorial: "))
print(math.factorial(m))
print(20*"-")
#Find LCM:
b = int(input("Enter a number to find the least common multiple: "))
c = int(input("Enter another number to find the least common multiple: "))
print(math.lcm(b,c))
print(20*"-")
#Find the Power of two numbers:
g = int(input("Enter a number to find the power: "))
h = int(input("Enter another number to find the power: "))
print(math.pow(g,h))
print(20*"-")
#find combinations
import math
n = 7
k = 5
print(math.comb(7,5))
print(20*"-")
#find permutation:
import math 
h = 6
j = 3
print(math.perm(6,3))