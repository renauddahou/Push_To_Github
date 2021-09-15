#f' strings
first_name = 'Cory'
last_name = 'Schafer'
sentence1 = 'My name is {}{}'.format(first_name,  last_name) #format method
print(sentence1)
sentence2 = f'My name is {first_name} {last_name}' #f' string method
print(sentence2)
person = {'name': "Jen", 'age': 23}
sentence3 = f"My name is {person['name']} and I am {person['age']} years old" #run functions within f' string
print(sentence3)
name = "Sam"
print(f'Hey, {name}')
print(f'{1}, {2}, {3}, {"a"}, {"this is a tip"}')