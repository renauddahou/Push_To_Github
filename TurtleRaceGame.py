import turtle 
import random 
import time 
screen = turtle.Turtle()
turtle.bgcolor("#8FCEEB")
#creating players:
player_1 = turtle.Turtle()
player_1.color('red')
player_1.shape('turtle')
player_2 = player_1.clone()
player_2.color('blue')
player_1.penup()
player_1.goto(-300,200)
player_2.penup()
#draw finish line:
player_2.goto(-300,-200)
player_1.goto(300,-250)
player_1.left(90)
player_1.pendown()
player_1.color("black")
player_1.forward(500)
player_1.write("FINISH", font= 25)
player_1.penup()
#return player 1 to start position:
player_1.color("red")
player_1.goto(-300, 200)
player_1.right(90)
#players pens down:
player_1.pendown()
player_2.pendown()
#values for dice:
die = [1,2,3,4,5,6]
#Create the game:
for i in range(30):
    if player_1.pos() >= (300,250):
        print("Player 1 Wins the race!")
        break
    elif player_2.pos() >= (300, -250):
        print("Player 2 Wins the race!")
        break 
    else:
        die_roll = random.choice(die)
        player_1.forward(30*die_roll)
        time.sleep(1)
        die_roll = random.choice(die)
        player_2.forward(30*die_roll)
        time.sleep(1)
turtle.done()