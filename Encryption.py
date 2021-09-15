import hashlib #this is a module
crypt = hashlib.md5() #'.md5()' is an algorithm in hashlib
crypt.update(b"hello") #'.update' function is where you put the word/'b' character before the word allows for encryption
print(crypt.hexdigest()) #'.hexdigest'gets the encrypted string
#print(hashlib.algorithms_available) algorithms available shows how many algorithms in your system

#Ceasar encryption example:
import string
plain_text = "good morning"
shift = 7
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
encrypted = plain_text.translate(table)
print(encrypted)
#cryptography package:
from cryptography.fernet import Fernet 
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"check out this secret message")
print(f.decrypt(token))