print("Hi") 
name = input("What Is Your Name?") 
print(f"Lets get to know each other {name}") 
would_you_answer_questions = input("Do you want to answer some questions?") 
if would_you_answer_questions == "yes" : 
        print("Great!") 
        age = int(input("What Is Your Age?")) 
        favorite_Show = input("What is your favorite TV Show?") 
        favorite_Movie = input("what is your favorite movie?")
        favorite_music_genre = input("what is your favorite music genre?")
else:
        print("OK Goodbye")
more_questions = input("do you want to answer more questions?") 
if more_questions == "yes": 
    print("Awesome!")
    social_media = input("Do You Have Social Media?") 
    if social_media == "yes": 
        what_platform = input("what platforms?") 
        which_platform = input("which platform do you use the most?") 
        how_platform = input("do you prefer the app or desktop version of your perferred platform?") 
    else:
        print("Wow! Not being on social media is rare. Cool") 
else:
    print("Ok. Goodbye") 
print(f"So, you said your favorite music genre was {favorite_music_genre}" ) 
print(input("what artists do you listen to?")) 
print("Wow!I will check those artists out")
print("Thanks so much for participating!") 
print("Goodbye. Have a great day!") 