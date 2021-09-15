#Counter() function 
import collections
from collections import Counter
word = 'mississippi'
counter = {}
for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] +=1
print(counter)