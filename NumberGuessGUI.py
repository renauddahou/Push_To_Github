#source code from Code Academy
import tkinter
import random
from random import randint
from tkinter import font
root = tkinter.Tk()
root.title('Guess The Number!')
root.geometry("500x500")
num_label = tkinter.Label(root, text="Pick A Number\nBetween 1 and 10!", font=("Times New Roman", 28))
num_label.pack(pady=20)
def guesser():
	if guess_box.get().isdigit():
		# Reset our label
		num_label.config(text="Pick A Number\nBetween 1 and 10!")
		# Find out how far away our pick was from the actual number
		dif = abs(num - int(guess_box.get()))
		# Check to see if correct
		if int(guess_box.get()) == num:
			bc = "SystemButtonFace"
			num_label.config(text="Correct!!")
		elif dif == 5:
			# Set background color to white
			bc = "white"
		elif dif < 5:
			bc = f'#ff{dif}{dif}{dif}{dif}'
		else: 
			bc = f'#{dif}{dif}{dif}{dif}ff'
		# Change the background of the app
		root.config(bg=bc)
		# Change bg of label
		num_label.config(bg=bc)
	else:
		# Delete entry and throw error message
		guess_box.delete(0)
		num_label.config(text="Hey! That's Not A Number!")
def rando():
	global num
	num = randint(1,10)
	# Clear the guess box
	guess_box.delete(0)
	# Change the colors back to normal
	num_label.config(bg="SystemButtonFace", text="Pick A Number\nBetween 1 and 10!")
	root.config(bg="SystemButtonFace")
guess_box = tkinter.Entry(root, font=("Times New Roman", 100), width=2)
guess_box.pack(pady=20)
guess_button = tkinter.Button(root, text="Submit", command=guesser)
guess_button.pack(pady=20)
rand_button = tkinter.Button(root, text="New Number", command=rando)
rand_button.pack(pady=20)
# Generate a random number on start
rando()
root.mainloop()