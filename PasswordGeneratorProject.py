import random
print("Password Generator")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&"
number = int(input("amount of passwords to generate"))
length = int(input("Password length"))
print("Here Are Your Passwords")
for p in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)