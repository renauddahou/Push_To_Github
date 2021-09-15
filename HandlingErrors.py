#try and except function handles erros so the program doesnt crash
text = input("username: ")
try:
    number = int(text)
    print(number)
except:
    print("Invalid Username")