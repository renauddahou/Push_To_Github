#Rock Paper Scissors Game. Tutorial with Junie Learning
import random
print("Welcome to Rock, Paper, Scissors")
user_score = 0
cpu_score = 0
while True:
    user_choice = input("Rock, Paper, or Scissors ").lower()
    while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        user_choice = input("Invalid input, please try again!").lower()
    random_number = random.randint(0,2)
    if random_number == 0:
        cpu_choice = "rock"
    elif random_number == 1:
        cpu_choice = "paper"
    elif random_number == 2:
        cpu_choice = "scissors"
    print("your choice: ", user_choice)
    print("computer choice: ", cpu_choice)
    if user_choice == "rock":
        if cpu_choice == "rock":
                print("Tie!")
        elif cpu_choice == "paper":
            print("computer won!")
            cpu_score += 1
        elif cpu_choice == "scissors":
            print("you won!")
            user_score += 1
    elif user_choice == "paper":
        if cpu_choice == "paper":
                print("Tie!")
        elif cpu_choice == "rock":
            print("you won!")
            user_score += 1
        elif cpu_choice == "scissors":
            print("computer won!")
            cpu_score += 1
    elif user_choice == "scissors":
        if cpu_choice == "scissors":
                print("Tie!")
        elif cpu_choice == "rock":
            print("computer won!")
            cpu_score += 1
        elif cpu_choice == "paper":
            print("you won!")
            user_score += 1
    print("You have: ", user_score,  "wins" )
    print("CPU has: ", cpu_score,  "wins")