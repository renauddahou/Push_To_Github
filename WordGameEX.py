import random
# library that we use in order to choose random words from a list of words
name = input("What is your name? ")
# Here the user is asked to enter the name first
print("Good Luck ! ", name)
words = ["sleep", "aardvark", "deck", "floor", "musical", "helping"]
word = random.choice(words) #function will choose one random word from this list
print("Guess the characters")
guesses = "  "
# any number of turns can be used here
turns = 6
while turns > 0:
	failed = 0 #counts the number of times a user fails
	for char in word: #all characters from the input word taking one at a time
		if char in guesses: #comparing that character with the character in guesses
			print(char)
		else:
			print("_")
			failed += 1 #for every failure 1 will be incremented in failure
	if failed == 0:
		# user will win the game if failure is 0 and 'You Win' will be given as output
		print("You Win")
		# this print the correct word
		print("The word is: ", word)
		break	
	# if user has input the wrong alphabet then it will ask user to enter another alphabet
	guess = input("guess a character:")
	
	# every input character will be stored in guesses
	guesses += guess	
	# check input with the character in word
	if guess not in word:	
		turns -= 1
		# if the character doesn’t match the word then “Wrong” will be given as output
		print("Wrong")
		# this will print the number of turns left for the user
		print("You have", + turns, 'more guesses')
		if turns == 0:
			print("You Loose")
			print("The word is: ", word)
