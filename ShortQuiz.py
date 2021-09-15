def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
print("Helllo! Welcom to the quiz!")
print("All questions are worth 10 points each")
ans = input("Are you ready to play? (yes/no): ")
a = "Note: Write answers. do not write options!"
score = 0
total_questions = 4
correct_ans = ["spider", "red", "aang", "sacramento"]
if ans.lower() == "yes":
    print(a)
    print("Question - Peter Parler got bitten by a radocative _____")
    give_options("dog", "spider", "cat")
    ans = input("Answer: ")
    if ans.lower() == correct_ans[0]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What color is ketchup?")
    give_options("red", "blue", "white")
    ans = input("Answer: ")
    if ans.lower() == correct_ans[1]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- Who is the titular character of Avatar the Last Airbender?")
    give_options("aang", "katara", "zuko")
    ans = input("Answer: ")
    if ans.lower() == correct_ans[2]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is the capital of California?")
    give_options("sacramento", "compton", "los angeles")
    ans = input("Answer: ")
    if ans.lower() == correct_ans[3]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    i = score*10
    if i < 30:
        print(f"Oops! your score is {i}/40.")
    elif i == 30:
        print(f"Wow! Your score is {i}/40")
    else:
        print("Congratulations! A perfect score!")