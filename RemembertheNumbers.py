import random 
import time
digits = int(input("How many digits do you want to guess: "))
sequence = []
for i in range(0,digits):
    sequence.append(random.randint(0,9))
    print(sequence)
    time.sleep(3)
for i in range(0,35):
    print("-")
for i in range(0,digits):
    print("enter number at index" + str(i))
    num = int(input())
    if num == sequence[i]:
        print("correct")
    else:
        print("wrong")
        break
print(sequence)