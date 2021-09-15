email = "pythonprogrammer@gmail.com"
password = "123345"
count = 0
while count < 3:
    email_input = input("Enter your email:  ")
    password_input = input("Enter your password:  ")
    if email_input == email:
        print("Email is correct")
    else:
        print("Email is not coorect")
    if password_input == password:
        print("Password is correct")
    else:
        print("Password is not correct")
    if email_input == email and password_input == password:
        break
    else:
        count += 1
else:
    print("You have made too many invalid attempts. For security, you are locked out of your account.")
if count < 3:
    print("You are now logged in")