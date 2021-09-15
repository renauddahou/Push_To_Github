#map() function
Li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def func(x):
    return x ** x
NewList = []
for x in Li:
    NewList.append(func(x))
print(NewList)
print(list(map(func, Li))) #map() format includes the function name and the list/tuple name inside parenthesis

#filter() function
def add7(x):
    return x+7
def isOdd(x):
    return x%2 !=0
A = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
B = list(filter(isOdd, A)) #filter() format includes the function name and list/tuple name in parethensis
print(A)
print(B)
C = list(map(add7, B))
print(C)

#Reduce() function
import functools
Letters = ['H', 'E', 'L', 'L', 'O']
word = functools.reduce(lambda x , y , : x+y, Letters)
print(word)

#Lambda() function
def Rex(x):
    return x + 5
print(Rex(7))
Rex2 = lambda x : x + 5 #lambda function format is parameter colon(:) value to be returned
print(Rex2(8))

Play = [1, 2, 3, 4, 5, 6,7, 8, 9,10]
Next = list(map(lambda x : x + 5, Play)) #map() can be used with lambda
print(Next)
Skip = list(filter(lambda x : x%2 == 0, Play)) #filter() can be used with lambda
print(Skip)