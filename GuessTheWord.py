print("Hi! Welcome to Guess The Word!")
secret_word = "blast"
guess = "   "
guess_count = 0
guess_limit = 4
out_of_guesses = False
while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, You Lose!", "The Word was:", secret_word)
else:    
    print("You Win!")