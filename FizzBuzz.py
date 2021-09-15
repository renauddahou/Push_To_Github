#FizzBuzz is a common interview question. Print "fizz"/"buzz"/"fizzbuzz" for multiples of 3 and 5
for i in range(1, 101):
    if i%15 == 0:
        print("Fizzbuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)