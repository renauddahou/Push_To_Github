apples = {
    'honeycrisp': 17, 
    'gala': 15, 
    'granny smith': 25, 
    'red delicious':  12
}

for apple in apples.keys():
    print(apple)
for apple in apples.values():
    print(apple)
for apple in apples.items():
    print(apple)

#len - if we want to see how many keys in dictionary 
# .keys - shows the keys
# .values - shows the values
# .items - shows keys and values 
#.update - use this to update a list
#.get - use this to bring up an item in list
#del or .pop - use this to delete an item from list