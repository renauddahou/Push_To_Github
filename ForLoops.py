#for loops allow you to loop content without having to rewrite the line of codde
for number in range(3):
    print("Hello")

#nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})") #f' string is used here


for even in range(1,10):
    if even % 2 == 0:
        print(even)
print("we have four even numbers")