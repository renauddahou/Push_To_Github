num= [1,2,3,4,5,6]
my_list = [n for n in num] #listcomprehension
print(my_list)
my_list2 = [n for n in num if n%2 == 0]
print(my_list2)
#list comprehension alllows for cleaner code compared to using map(),filter(),lambda()
names = ['clark', 'barry', 'bruce']
heroes = ['superman', 'flash', 'batman']
my_dict = {name:heroes for name, heroes in zip(names, heroes)} #zip function brings lists together
print(my_dict)
#zip function example below
X = [1, 2, 3, 4]
Y = [7, 6, 2, 1]
Z = ['a', 'b','c', 'd']
for a,b in zip(X,Y):
    print(a, b)
for a, b, c in zip(X,Y,Z):
    print(a,b,c)