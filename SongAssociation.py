import random 
import time
time.sleep(2)
def Intro():
    print("I will give you a word and you have 15 seconds to name a song that includes the word")
    time.sleep(2)
    print("The word can be in the song title or in the lyrics of the song")
    time.sleep(2)
    print("Ready! Lets Play!")
time.sleep(2)
def choose_word():
    Words = ["use", "come", "happy", "you", "somebody", "good", "clouds","love", "breathe", "think",
    "care","home", "baby", "time","cry","find","cool","me", "phone","lay"]
    random.shuffle(Words)
    for x in Words:
        print(f'the word is: {x}')
        time.sleep(15)
        print("Times Up!")
def play():
 Intro()
 choose_word()
play()