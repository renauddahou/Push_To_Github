import time
from time import sleep
name = input("Enter Your Name: ")
print("Hi" + "  " +  name)
time.sleep(1)
print("Let's Play")
time.sleep(0.5)
word = 'outside'
wrd = "  "
chance = 10
while chance > 0:
    failed = 0 
    for char in word:
        if char in wrd:
            print(char)
        else:
            print(" ")
            failed += 1
    if failed == 0:
        print("Congratulations! YOU WON!")
        break 
    guess = input("Guess a letter:  ")
    wrd = wrd + guess
    if guess not in word:
        chance -= 1
        print("Wrong guess. Try Again")
        print("You have" + " " + str(chance) + " " + "more turns")
        if chance == 0:
            print("Sorry! You are out of turns")