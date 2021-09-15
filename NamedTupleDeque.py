#namedtuple() is part of Collections module. assign name to each position in a tuple.
import collections
from collections import namedtuple
Date = namedtuple("Date", ['month', 'date', 'year'])
Today = Date(4, 13, 2021) 
print(Today)
print(Today.month)
print(Today.date)
print(Today.year)
color = namedtuple("Color", ('red', 'blue', 'green'))
first_color = color(123, 345, 456)
second_color = color( 234, 345, 567)
print(first_color)
print(second_color)
print(first_color.green)
print(second_color.red)

#Deque() is also part of collections. it appends elements to one side and remove from the other
from collections import deque
d = deque([1,2,3,4,5])
print(d)
d.append(6) #add a new entry to the right
d.appendleft(0) #add a new entry to the left
print(d)
d.pop() #return and remove the rightmost entry
d.popleft() #return and remove the leftmost entry
print(d)
d.extend([6,7,8,9]) #add entries to right
print(d)
d.extendleft([0,-1,-2]) #add entries to the left
print(d)
d.clear() #clears deque
print(d)